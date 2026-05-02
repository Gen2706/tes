#!/usr/bin/env python3
"""
MikroTik NOC Monitor - SNMP Backend
Ubuntu 22.04 | Flask + pysnmp
"""

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from pysnmp.hlapi import *
from pysnmp.hlapi import SnmpEngine, CommunityData, UdpTransportTarget, ContextData
from pysnmp.hlapi import getCmd, nextCmd, bulkCmd
import threading
import time
import json
import ipaddress
from datetime import datetime, timedelta
from collections import defaultdict, deque
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# ─── KONFIGURASI ────────────────────────────────────────────────────────────
CONFIG = {
    "host": "192.168.1.1",        # ← Ganti IP MikroTik kamu
    "port": 161,
    "community": "public",        # ← Ganti SNMP community string
    "version": "2c",
    "poll_interval": 10,          # detik
    "history_size": 360,          # jumlah titik histori (360 × 10s = 1 jam)
    "bgp_enabled": True,
}

# ─── OID MikroTik ───────────────────────────────────────────────────────────
OID = {
    # System
    "sysDescr":         "1.3.6.1.2.1.1.1.0",
    "sysUpTime":        "1.3.6.1.2.1.1.3.0",
    "sysName":          "1.3.6.1.2.1.1.5.0",

    # CPU & Memory (MikroTik specific)
    "cpuLoad":          "1.3.6.1.2.1.25.3.3.1.2.1",
    "memTotal":         "1.3.6.1.2.1.25.2.3.1.5",
    "memUsed":          "1.3.6.1.2.1.25.2.3.1.6",

    # Interfaces (IF-MIB)
    "ifDescr":          "1.3.6.1.2.1.2.2.1.2",
    "ifOperStatus":     "1.3.6.1.2.1.2.2.1.8",
    "ifInOctets":       "1.3.6.1.2.1.2.2.1.10",
    "ifOutOctets":      "1.3.6.1.2.1.2.2.1.16",
    "ifSpeed":          "1.3.6.1.2.1.2.2.1.5",
    "ifInErrors":       "1.3.6.1.2.1.2.2.1.14",
    "ifOutErrors":      "1.3.6.1.2.1.2.2.1.20",

    # 64-bit counters (ifXTable)
    "ifHCInOctets":     "1.3.6.1.2.1.31.1.1.1.6",
    "ifHCOutOctets":    "1.3.6.1.2.1.31.1.1.1.10",
    "ifAlias":          "1.3.6.1.2.1.31.1.1.1.18",

    # DHCP Leases (MikroTik)
    "dhcpLeaseAddr":    "1.3.6.1.4.1.14988.1.1.6.1.1.3",
    "dhcpLeaseHost":    "1.3.6.1.4.1.14988.1.1.6.1.1.5",
    "dhcpLeaseMAC":     "1.3.6.1.4.1.14988.1.1.6.1.1.2",

    # Firewall connections
    "fwConnCount":      "1.3.6.1.4.1.14988.1.1.9.1.0",

    # BGP (BGP4-MIB)
    "bgpPeerState":     "1.3.6.1.2.1.15.3.1.2",
    "bgpPeerRemoteAs":  "1.3.6.1.2.1.15.3.1.9",
    "bgpPeerInUpdates": "1.3.6.1.2.1.15.3.1.10",
    "bgpPeerOutUpdates":"1.3.6.1.2.1.15.3.1.11",
    "bgpPeerPrefixRcv": "1.3.6.1.2.1.15.3.1.24",  # (non-standard, some mikrotik)

    # Queues (MikroTik Simple Queue)
    "queueName":        "1.3.6.1.4.1.14988.1.1.2.1.1.2",
    "queueBytesIn":     "1.3.6.1.4.1.14988.1.1.2.1.1.8",
    "queueBytesOut":    "1.3.6.1.4.1.14988.1.1.2.1.1.9",
    "queueMaxLimit":    "1.3.6.1.4.1.14988.1.1.2.1.1.13",

    # VPN / PPP active
    "pppActiveName":    "1.3.6.1.4.1.14988.1.1.2.2.1.2",
    "pppActiveAddr":    "1.3.6.1.4.1.14988.1.1.2.2.1.4",
    "pppActiveUptime":  "1.3.6.1.4.1.14988.1.1.2.2.1.7",
}

BGP_PEER_STATES = {
    1:"idle", 2:"connect", 3:"active",
    4:"opensent", 5:"openconfirm", 6:"established"
}

# ─── DATA STORE ─────────────────────────────────────────────────────────────
store = {
    "system": {},
    "cpu_history": deque(maxlen=CONFIG["history_size"]),
    "mem_history": deque(maxlen=CONFIG["history_size"]),
    "interfaces": {},
    "iface_history": defaultdict(lambda: {"in": deque(maxlen=CONFIG["history_size"]),
                                           "out": deque(maxlen=CONFIG["history_size"])}),
    "dhcp_leases": [],
    "firewall": {"conn_count": 0},
    "bgp_peers": [],
    "queues": [],
    "vpn_sessions": [],
    "bgp_prefix_by_as": {},
    "alerts": deque(maxlen=100),
    "last_poll": None,
    "poll_ok": False,
    "_prev_iface_octets": {},
    "_prev_time": None,
}

# ─── SNMP HELPERS ───────────────────────────────────────────────────────────
def snmp_get(oid_list):
    """Get multiple scalar OIDs at once."""
    results = {}
    engine = SnmpEngine()
    community = CommunityData(CONFIG["community"], mpModel=1)
    transport = UdpTransportTarget((CONFIG["host"], CONFIG["port"]), timeout=3, retries=1)
    ctx = ContextData()

    for oid in oid_list:
        for (errInd, errSt, errIdx, varBinds) in getCmd(
            engine, community, transport, ctx, ObjectType(ObjectIdentity(oid))
        ):
            if errInd or errSt:
                results[oid] = None
            else:
                for vb in varBinds:
                    results[oid] = vb[1].prettyPrint()
    return results


def snmp_walk(base_oid):
    """Walk a subtree, return {suffix: value}."""
    results = {}
    engine = SnmpEngine()
    community = CommunityData(CONFIG["community"], mpModel=1)
    transport = UdpTransportTarget((CONFIG["host"], CONFIG["port"]), timeout=3, retries=1)
    ctx = ContextData()

    for (errInd, errSt, errIdx, varBinds) in nextCmd(
        engine, community, transport, ctx,
        ObjectType(ObjectIdentity(base_oid)),
        lexicographicMode=False
    ):
        if errInd or errSt:
            break
        for vb in varBinds:
            oid_str = str(vb[0])
            suffix = oid_str[len(base_oid)+1:] if oid_str.startswith(base_oid) else oid_str
            results[suffix] = vb[1].prettyPrint()
    return results


def snmp_walk_int(base_oid):
    raw = snmp_walk(base_oid)
    out = {}
    for k, v in raw.items():
        try:
            out[k] = int(v)
        except:
            out[k] = 0
    return out

# ─── POLLER ─────────────────────────────────────────────────────────────────
def poll():
    """Main polling function — runs every poll_interval seconds."""
    global store
    now = time.time()

    try:
        # ── System Info ──────────────────────────────────────────────────
        sys_vals = snmp_get([OID["sysDescr"], OID["sysUpTime"], OID["sysName"],
                             OID["cpuLoad"], OID["fwConnCount"]])

        cpu = None
        try:
            cpu = int(sys_vals.get(OID["cpuLoad"], 0))
        except:
            cpu = 0

        uptime_ticks = 0
        try:
            uptime_ticks = int(sys_vals.get(OID["sysUpTime"], 0))
        except:
            pass

        uptime_sec = uptime_ticks // 100
        uptime_str = str(timedelta(seconds=uptime_sec))

        fw_conn = 0
        try:
            fw_conn = int(sys_vals.get(OID["fwConnCount"], 0))
        except:
            pass

        store["system"] = {
            "name": sys_vals.get(OID["sysName"], CONFIG["host"]),
            "descr": sys_vals.get(OID["sysDescr"], "MikroTik"),
            "uptime": uptime_str,
            "uptime_sec": uptime_sec,
            "cpu": cpu,
            "host": CONFIG["host"],
            "timestamp": datetime.now().isoformat(),
        }
        store["cpu_history"].append({"t": int(now), "v": cpu})
        store["firewall"]["conn_count"] = fw_conn

        # CPU alert
        if cpu > 85:
            _add_alert("CRIT", f"CPU tinggi: {cpu}%", "system")
        elif cpu > 70:
            _add_alert("WARN", f"CPU elevated: {cpu}%", "system")

        # ── Memory ───────────────────────────────────────────────────────
        mem_total_raw = snmp_walk_int(OID["memTotal"])
        mem_used_raw  = snmp_walk_int(OID["memUsed"])

        # MikroTik HR memory index usually .1 = RAM
        mem_total = 0
        mem_used  = 0
        for idx in mem_total_raw:
            if idx in mem_used_raw:
                t = mem_total_raw[idx]
                u = mem_used_raw[idx]
                if t > mem_total:
                    mem_total = t
                    mem_used  = u

        mem_pct = round(mem_used / mem_total * 100, 1) if mem_total else 0
        store["system"]["mem_total_mb"] = round(mem_total / 1024 / 1024, 1)
        store["system"]["mem_used_mb"]  = round(mem_used  / 1024 / 1024, 1)
        store["system"]["mem_pct"]      = mem_pct
        store["mem_history"].append({"t": int(now), "v": mem_pct})

        # ── Interfaces ───────────────────────────────────────────────────
        iface_names   = snmp_walk(OID["ifDescr"])
        iface_status  = snmp_walk_int(OID["ifOperStatus"])
        iface_speed   = snmp_walk_int(OID["ifSpeed"])
        iface_alias   = snmp_walk(OID["ifAlias"])
        iface_in64    = snmp_walk_int(OID["ifHCInOctets"])
        iface_out64   = snmp_walk_int(OID["ifHCOutOctets"])
        iface_inerr   = snmp_walk_int(OID["ifInErrors"])
        iface_outerr  = snmp_walk_int(OID["ifOutErrors"])

        dt = now - store["_prev_time"] if store["_prev_time"] else 1
        new_ifaces = {}
        for idx, name in iface_names.items():
            status = iface_status.get(idx, 2)
            in_oct  = iface_in64.get(idx, 0)
            out_oct = iface_out64.get(idx, 0)
            speed   = iface_speed.get(idx, 0)
            alias   = iface_alias.get(idx, "")

            # Bps calculation
            prev = store["_prev_iface_octets"].get(idx, {})
            in_bps  = max(0, (in_oct  - prev.get("in",  in_oct))  * 8 / dt) if prev else 0
            out_bps = max(0, (out_oct - prev.get("out", out_oct)) * 8 / dt) if prev else 0
            store["_prev_iface_octets"][idx] = {"in": in_oct, "out": out_oct}

            # Utilization %
            util = 0
            if speed > 0:
                util = round(max(in_bps, out_bps) / speed * 100, 1)

            new_ifaces[idx] = {
                "name": name, "alias": alias,
                "status": "up" if status == 1 else "down",
                "speed_mbps": round(speed / 1_000_000, 1),
                "in_bps": round(in_bps),
                "out_bps": round(out_bps),
                "in_mbps": round(in_bps / 1_000_000, 2),
                "out_mbps": round(out_bps / 1_000_000, 2),
                "util_pct": min(util, 100),
                "in_errors": iface_inerr.get(idx, 0),
                "out_errors": iface_outerr.get(idx, 0),
            }
            store["iface_history"][idx]["in"].append({"t": int(now), "v": round(in_bps/1e6, 2)})
            store["iface_history"][idx]["out"].append({"t": int(now), "v": round(out_bps/1e6, 2)})

            # Interface down alert
            prev_iface = store["interfaces"].get(idx, {})
            if prev_iface.get("status") == "up" and status != 1:
                _add_alert("CRIT", f"Interface DOWN: {name}", "interface")

        store["interfaces"] = new_ifaces
        store["_prev_time"] = now

        # ── DHCP Leases ──────────────────────────────────────────────────
        dhcp_addr = snmp_walk(OID["dhcpLeaseAddr"])
        dhcp_host = snmp_walk(OID["dhcpLeaseHost"])
        dhcp_mac  = snmp_walk(OID["dhcpLeaseMAC"])
        leases = []
        for idx in dhcp_addr:
            leases.append({
                "idx": idx,
                "ip":  dhcp_addr.get(idx, ""),
                "host": dhcp_host.get(idx, "unknown"),
                "mac":  dhcp_mac.get(idx, ""),
            })
        store["dhcp_leases"] = leases

        # ── BGP Peers ─────────────────────────────────────────────────────
        if CONFIG["bgp_enabled"]:
            bgp_state   = snmp_walk_int(OID["bgpPeerState"])
            bgp_as      = snmp_walk_int(OID["bgpPeerRemoteAs"])
            bgp_in_upd  = snmp_walk_int(OID["bgpPeerInUpdates"])
            bgp_out_upd = snmp_walk_int(OID["bgpPeerOutUpdates"])
            bgp_pfx     = snmp_walk_int(OID["bgpPeerPrefixRcv"])

            peers = []
            as_prefix_map = defaultdict(list)
            for peer_ip in bgp_state:
                state_num = bgp_state[peer_ip]
                remote_as = bgp_as.get(peer_ip, 0)
                pfx_count = bgp_pfx.get(peer_ip, 0)
                state_str = BGP_PEER_STATES.get(state_num, "unknown")
                peers.append({
                    "peer_ip":   peer_ip,
                    "remote_as": remote_as,
                    "state":     state_str,
                    "in_updates":  bgp_in_upd.get(peer_ip, 0),
                    "out_updates": bgp_out_upd.get(peer_ip, 0),
                    "prefix_count": pfx_count,
                })
                if pfx_count > 0:
                    as_prefix_map[str(remote_as)].append({
                        "peer": peer_ip,
                        "prefixes": pfx_count
                    })
                if state_str != "established":
                    _add_alert("WARN", f"BGP peer {peer_ip} AS{remote_as} state: {state_str}", "bgp")

            store["bgp_peers"] = peers
            store["bgp_prefix_by_as"] = dict(as_prefix_map)

        # ── Simple Queues ────────────────────────────────────────────────
        q_names   = snmp_walk(OID["queueName"])
        q_bytes_in  = snmp_walk_int(OID["queueBytesIn"])
        q_bytes_out = snmp_walk_int(OID["queueBytesOut"])
        q_max     = snmp_walk(OID["queueMaxLimit"])

        queues = []
        for idx, name in q_names.items():
            max_raw = q_max.get(idx, "0/0")
            queues.append({
                "name": name,
                "bytes_in":  q_bytes_in.get(idx, 0),
                "bytes_out": q_bytes_out.get(idx, 0),
                "max_limit": max_raw,
            })
        store["queues"] = queues

        # ── VPN / PPP Sessions ───────────────────────────────────────────
        vpn_names   = snmp_walk(OID["pppActiveName"])
        vpn_addrs   = snmp_walk(OID["pppActiveAddr"])
        vpn_uptimes = snmp_walk_int(OID["pppActiveUptime"])

        sessions = []
        for idx, name in vpn_names.items():
            sessions.append({
                "name":    name,
                "address": vpn_addrs.get(idx, ""),
                "uptime_sec": vpn_uptimes.get(idx, 0),
                "uptime_str": str(timedelta(seconds=vpn_uptimes.get(idx, 0))),
            })
        store["vpn_sessions"] = sessions

        store["last_poll"] = datetime.now().isoformat()
        store["poll_ok"] = True
        log.info(f"Poll OK — CPU:{cpu}% MEM:{mem_pct}% Ifaces:{len(new_ifaces)} DHCP:{len(leases)} BGP:{len(store['bgp_peers'])} VPN:{len(sessions)}")

    except Exception as e:
        store["poll_ok"] = False
        log.error(f"Poll error: {e}")
        _add_alert("CRIT", f"SNMP poll gagal: {str(e)[:80]}", "system")


def _add_alert(level, msg, source):
    store["alerts"].appendleft({
        "level": level,
        "msg": msg,
        "source": source,
        "time": datetime.now().strftime("%H:%M:%S"),
    })


def poller_loop():
    while True:
        poll()
        time.sleep(CONFIG["poll_interval"])

# ─── API ROUTES ─────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/summary")
def api_summary():
    return jsonify({
        "system":   store["system"],
        "poll_ok":  store["poll_ok"],
        "last_poll": store["last_poll"],
        "firewall": store["firewall"],
        "alert_count": len(store["alerts"]),
        "iface_count": len(store["interfaces"]),
        "dhcp_count":  len(store["dhcp_leases"]),
        "vpn_count":   len(store["vpn_sessions"]),
        "bgp_count":   len(store["bgp_peers"]),
    })

@app.route("/api/interfaces")
def api_interfaces():
    return jsonify(list(store["interfaces"].values()))

@app.route("/api/iface_history/<idx>")
def api_iface_history(idx):
    h = store["iface_history"].get(idx, {"in":[],"out":[]})
    return jsonify({"in": list(h["in"]), "out": list(h["out"])})

@app.route("/api/cpu_history")
def api_cpu_history():
    return jsonify(list(store["cpu_history"]))

@app.route("/api/mem_history")
def api_mem_history():
    return jsonify(list(store["mem_history"]))

@app.route("/api/dhcp")
def api_dhcp():
    q = request.args.get("q", "").lower()
    leases = store["dhcp_leases"]
    if q:
        leases = [l for l in leases if q in l["ip"].lower() or q in l["host"].lower() or q in l["mac"].lower()]
    return jsonify(leases)

@app.route("/api/bgp")
def api_bgp():
    return jsonify({
        "peers": store["bgp_peers"],
        "prefix_by_as": store["bgp_prefix_by_as"],
    })

@app.route("/api/queues")
def api_queues():
    return jsonify(store["queues"])

@app.route("/api/vpn")
def api_vpn():
    return jsonify(store["vpn_sessions"])

@app.route("/api/alerts")
def api_alerts():
    return jsonify(list(store["alerts"]))

@app.route("/api/firewall")
def api_firewall():
    return jsonify(store["firewall"])

@app.route("/api/config", methods=["GET", "POST"])
def api_config():
    if request.method == "POST":
        data = request.json or {}
        for k in ["host", "community", "poll_interval"]:
            if k in data:
                CONFIG[k] = data[k]
        return jsonify({"ok": True, "config": CONFIG})
    return jsonify(CONFIG)

# ─── MAIN ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Start poller in background
    t = threading.Thread(target=poller_loop, daemon=True)
    t.start()
    log.info(f"MikroTik NOC Monitor — polling {CONFIG['host']} every {CONFIG['poll_interval']}s")
    app.run(host="0.0.0.0", port=5000, debug=False)
