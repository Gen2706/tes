<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MikroTik NOC Monitor</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Barlow:wght@400;500;600&family=Barlow+Condensed:wght@500;600&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#080d14;--panel:#0c1422;--panel2:#101b2e;
  --border:#1a3050;--border2:#1e3a5f;
  --green:#00e87a;--green-dim:#009950;
  --red:#ff2d55;--amber:#ffb300;--blue:#0af;--cyan:#00e5ff;
  --purple:#bf5fff;--teal:#00cfbe;
  --text:#b8cce0;--muted:#4a6a8a;--bright:#ddeeff;
  --mono:'Share Tech Mono',monospace;
  --sans:'Barlow',sans-serif;
  --cond:'Barlow Condensed',sans-serif;
}
body{background:var(--bg);font-family:var(--sans);color:var(--text);font-size:13px;min-height:100vh}

/* TOPBAR */
.topbar{
  background:var(--panel);border-bottom:1px solid var(--border);
  padding:0 16px;height:48px;
  display:flex;align-items:center;justify-content:space-between;
  position:sticky;top:0;z-index:200;
}
.logo{font-family:var(--mono);font-size:15px;color:var(--cyan);letter-spacing:3px;display:flex;align-items:center;gap:10px}
.logo-icon{width:24px;height:24px;display:flex;align-items:center;justify-content:center}
.logo-icon svg{fill:none;stroke:var(--cyan);stroke-width:1.5}
.poll-dot{width:7px;height:7px;border-radius:50%;background:var(--green);animation:blink 2s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
.poll-dot.err{background:var(--red);animation:none}
.topbar-mid{display:flex;gap:0}
.nav-btn{
  padding:0 14px;height:48px;border:none;background:transparent;
  color:var(--muted);font-family:var(--sans);font-size:13px;
  cursor:pointer;border-bottom:2px solid transparent;transition:.2s;
  display:flex;align-items:center;gap:6px;
}
.nav-btn:hover{color:var(--text)}
.nav-btn.active{color:var(--cyan);border-bottom-color:var(--cyan)}
.topbar-right{display:flex;align-items:center;gap:12px;font-family:var(--mono);font-size:11px}
.host-badge{background:var(--panel2);border:1px solid var(--border2);padding:3px 10px;border-radius:3px;color:var(--blue)}
.clock{color:var(--cyan)}

/* TICKER */
.ticker{background:#0a1520;border-bottom:1px solid var(--border);padding:5px 16px;display:flex;align-items:center;gap:10px;overflow:hidden}
.ticker-label{font-family:var(--mono);font-size:10px;background:var(--blue);color:#000;padding:1px 6px;border-radius:2px;white-space:nowrap}
.ticker-scroll{font-family:var(--mono);font-size:10px;color:var(--muted);white-space:nowrap;animation:ticker 40s linear infinite}
@keyframes ticker{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}

/* PAGES */
.page{display:none;padding:12px;flex-direction:column;gap:10px}
.page.active{display:flex}

/* GRID HELPERS */
.g2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.gcol{display:flex;flex-direction:column;gap:10px}

/* PANEL */
.pnl{background:var(--panel);border:1px solid var(--border);border-radius:4px;overflow:hidden}
.pnl-hdr{
  background:var(--panel2);border-bottom:1px solid var(--border);
  padding:7px 14px;display:flex;align-items:center;justify-content:space-between;
}
.pnl-title{font-family:var(--mono);font-size:10px;color:var(--cyan);letter-spacing:1.5px}
.pnl-body{padding:10px 14px}
.badge{font-family:var(--mono);font-size:9px;padding:2px 7px;border-radius:2px;border:1px solid}
.b-green{color:var(--green);border-color:rgba(0,232,122,.3);background:rgba(0,232,122,.1)}
.b-red{color:var(--red);border-color:rgba(255,45,85,.3);background:rgba(255,45,85,.1)}
.b-amber{color:var(--amber);border-color:rgba(255,179,0,.3);background:rgba(255,179,0,.1)}
.b-blue{color:var(--blue);border-color:rgba(0,170,255,.3);background:rgba(0,170,255,.1)}
.b-muted{color:var(--muted);border-color:var(--border);background:transparent}

/* STAT CARDS */
.stat-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:8px}
.stat{background:var(--panel2);border:1px solid var(--border);border-radius:4px;padding:10px 12px}
.stat-lbl{font-family:var(--mono);font-size:9px;color:var(--muted);margin-bottom:5px;letter-spacing:1px}
.stat-val{font-family:var(--mono);font-size:22px;line-height:1;font-weight:400}
.stat-sub{font-size:10px;color:var(--muted);margin-top:3px}
.c-green{color:var(--green)}.c-red{color:var(--red)}.c-amber{color:var(--amber)}.c-blue{color:var(--blue)}.c-cyan{color:var(--cyan)}.c-purple{color:var(--purple)}

/* CHART */
.chart-wrap{position:relative;width:100%}

/* TABLE */
.tbl{width:100%;border-collapse:collapse}
.tbl th{font-family:var(--mono);font-size:9px;color:var(--muted);padding:6px 10px;border-bottom:1px solid var(--border);text-align:left;letter-spacing:1px;white-space:nowrap}
.tbl td{padding:6px 10px;border-bottom:1px solid rgba(26,48,80,.5);font-size:12px;white-space:nowrap}
.tbl tr:last-child td{border-bottom:none}
.tbl tr:hover td{background:rgba(255,255,255,.03)}
.tbl .mono{font-family:var(--mono);font-size:11px}

/* IFACE ROW */
.iface-card{border:1px solid var(--border);border-radius:4px;padding:10px 12px;background:var(--panel2);cursor:pointer;transition:.2s}
.iface-card:hover{border-color:var(--border2)}
.iface-card.active{border-color:var(--cyan)}
.iface-top{display:flex;align-items:center;gap:8px;margin-bottom:8px}
.iface-name{font-family:var(--cond);font-size:14px;font-weight:600;flex:1}
.iface-alias{font-size:10px;color:var(--muted);font-family:var(--mono)}
.bw-row{display:flex;justify-content:space-between;font-family:var(--mono);font-size:11px;margin-bottom:4px}
.bw-in{color:var(--green)}.bw-out{color:var(--red)}
.util-bar{height:3px;background:rgba(255,255,255,.08);border-radius:2px;overflow:hidden}
.util-fill{height:100%;border-radius:2px;transition:width .8s ease}

/* SEARCH */
.search-box{
  background:var(--panel2);border:1px solid var(--border);border-radius:3px;
  padding:6px 10px;color:var(--text);font-family:var(--mono);font-size:12px;
  width:100%;outline:none;
}
.search-box:focus{border-color:var(--border2)}
.search-box::placeholder{color:var(--muted)}

/* BGP */
.bgp-peer{display:flex;align-items:center;gap:10px;padding:7px 0;border-bottom:1px solid rgba(26,48,80,.5)}
.bgp-peer:last-child{border-bottom:none}
.bgp-state{padding:2px 8px;border-radius:2px;font-family:var(--mono);font-size:10px;font-weight:600}
.bs-established{background:rgba(0,232,122,.15);color:var(--green)}
.bs-other{background:rgba(255,45,85,.15);color:var(--red)}
.as-block{
  background:var(--panel2);border:1px solid var(--border);border-radius:3px;
  padding:8px 12px;display:flex;align-items:center;gap:10px;
}
.as-num{font-family:var(--mono);font-size:13px;color:var(--blue);min-width:80px}
.pfx-bar-bg{flex:1;height:6px;background:rgba(255,255,255,.07);border-radius:3px;overflow:hidden}
.pfx-bar{height:100%;background:var(--blue);border-radius:3px;transition:width .5s}
.pfx-count{font-family:var(--mono);font-size:11px;color:var(--muted);min-width:60px;text-align:right}

/* VPN */
.vpn-row{display:flex;align-items:center;gap:10px;padding:6px 0;border-bottom:1px solid rgba(26,48,80,.5)}
.vpn-row:last-child{border-bottom:none}
.vpn-name{font-family:var(--mono);font-size:12px;flex:0 0 160px;overflow:hidden;text-overflow:ellipsis}
.vpn-addr{font-family:var(--mono);font-size:11px;color:var(--blue);flex:0 0 120px}
.vpn-up{font-family:var(--mono);font-size:11px;color:var(--muted);flex:1}

/* QUEUE */
.q-row{padding:8px 0;border-bottom:1px solid rgba(26,48,80,.5)}
.q-row:last-child{border-bottom:none}
.q-top{display:flex;justify-content:space-between;margin-bottom:4px}
.q-name{font-family:var(--mono);font-size:11px}
.q-limit{font-family:var(--mono);font-size:10px;color:var(--muted)}
.q-bars{display:flex;flex-direction:column;gap:3px}
.q-bar-row{display:flex;align-items:center;gap:6px}
.q-label{font-size:9px;color:var(--muted);font-family:var(--mono);width:25px}
.q-bar-bg{flex:1;height:4px;background:rgba(255,255,255,.07);border-radius:2px;overflow:hidden}
.q-bar{height:100%;border-radius:2px}

/* ALERTS */
.alert-item{display:flex;gap:8px;align-items:flex-start;padding:6px 10px;border-radius:3px;margin-bottom:4px}
.al-crit{background:rgba(255,45,85,.1);border:1px solid rgba(255,45,85,.2)}
.al-warn{background:rgba(255,179,0,.1);border:1px solid rgba(255,179,0,.2)}
.al-info{background:rgba(0,170,255,.1);border:1px solid rgba(0,170,255,.2)}
.al-dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;margin-top:3px}
.al-crit .al-dot{background:var(--red)}
.al-warn .al-dot{background:var(--amber)}
.al-info .al-dot{background:var(--blue)}
.al-text{flex:1;font-size:11px}
.al-source{font-family:var(--mono);font-size:10px;color:var(--muted)}
.al-time{font-family:var(--mono);font-size:10px;color:var(--muted);white-space:nowrap}

/* GAUGE SVG */
.gauge-svg{width:100%;max-width:180px}
.gauge-section{display:flex;flex-direction:column;align-items:center;padding:8px}

/* CONFIG PANEL */
.cfg-row{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.cfg-lbl{font-family:var(--mono);font-size:10px;color:var(--muted);width:130px}
.cfg-input{
  background:var(--panel2);border:1px solid var(--border);border-radius:3px;
  padding:5px 10px;color:var(--text);font-family:var(--mono);font-size:12px;
  flex:1;outline:none;
}
.cfg-input:focus{border-color:var(--border2)}
.btn{
  background:transparent;border:1px solid var(--border2);color:var(--text);
  padding:6px 14px;border-radius:3px;cursor:pointer;font-family:var(--mono);font-size:11px;
  transition:.2s;
}
.btn:hover{background:var(--panel2);border-color:var(--cyan);color:var(--cyan)}
.btn-save{border-color:var(--green);color:var(--green)}
.btn-save:hover{background:rgba(0,232,122,.1)}

/* EMPTY STATE */
.empty{text-align:center;padding:40px;color:var(--muted);font-family:var(--mono);font-size:11px}

/* SCROLLBAR */
::-webkit-scrollbar{width:3px;height:3px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--border2);border-radius:2px}

/* RESPONSIVE */
@media(max-width:900px){
  .stat-grid{grid-template-columns:repeat(3,1fr)}
  .g4{grid-template-columns:1fr 1fr}
  .topbar-mid{display:none}
}
</style>
</head>
<body>

<div class="topbar">
  <div class="logo">
    <div class="logo-icon">
      <svg viewBox="0 0 24 24" width="22" height="22">
        <rect x="2" y="6" width="20" height="12" rx="1"/>
        <circle cx="18" cy="12" r="1.5" fill="var(--cyan)"/>
        <circle cx="14" cy="12" r="1.5" fill="var(--green)"/>
        <line x1="2" y1="9" x2="22" y2="9"/>
      </svg>
    </div>
    MIKROTIK·NOC
    <div class="poll-dot" id="poll-dot"></div>
  </div>

  <div class="topbar-mid">
    <button class="nav-btn active" onclick="showPage('dashboard',this)">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
      Dashboard
    </button>
    <button class="nav-btn" onclick="showPage('interfaces',this)">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      Interfaces
    </button>
    <button class="nav-btn" onclick="showPage('dhcp',this)">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M8 12h8M12 8v8"/></svg>
      DHCP
    </button>
    <button class="nav-btn" onclick="showPage('bgp',this)">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="5" cy="12" r="2"/><circle cx="19" cy="5" r="2"/><circle cx="19" cy="19" r="2"/><path d="M7 12h5m2-5l2 3m0 4l-2 3"/></svg>
      BGP
    </button>
    <button class="nav-btn" onclick="showPage('vpn',this)">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 118 0v4"/></svg>
      VPN
    </button>
    <button class="nav-btn" onclick="showPage('queues',this)">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
      Queues
    </button>
    <button class="nav-btn" onclick="showPage('alerts',this)">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9M13.73 21a2 2 0 01-3.46 0"/></svg>
      Alerts
    </button>
    <button class="nav-btn" onclick="showPage('config',this)">⚙ Config</button>
  </div>

  <div class="topbar-right">
    <span class="host-badge" id="top-host">192.168.1.1</span>
    <span class="clock" id="clk">--:--:--</span>
  </div>
</div>

<div class="ticker">
  <span class="ticker-label">LIVE</span>
  <div style="overflow:hidden;flex:1">
    <div class="ticker-scroll" id="ticker-text">
      Memuat data dari MikroTik... &nbsp;&nbsp;&nbsp;
      Memuat data dari MikroTik... &nbsp;&nbsp;&nbsp;
    </div>
  </div>
</div>

<!-- ═══ DASHBOARD PAGE ═══ -->
<div id="page-dashboard" class="page active">
  <div class="stat-grid">
    <div class="stat"><div class="stat-lbl">// CPU</div><div class="stat-val c-green" id="s-cpu">--%</div><div class="stat-sub" id="s-cpu-sub">RouterOS</div></div>
    <div class="stat"><div class="stat-lbl">// MEMORY</div><div class="stat-val c-blue" id="s-mem">--%</div><div class="stat-sub" id="s-mem-sub">-- / -- MB</div></div>
    <div class="stat"><div class="stat-lbl">// FW CONN</div><div class="stat-val c-amber" id="s-fw">--</div><div class="stat-sub">active connections</div></div>
    <div class="stat"><div class="stat-lbl">// UPTIME</div><div class="stat-val c-cyan" id="s-uptime" style="font-size:14px;padding-top:4px">--</div><div class="stat-sub">router uptime</div></div>
    <div class="stat"><div class="stat-lbl">// DHCP</div><div class="stat-val c-purple" id="s-dhcp">--</div><div class="stat-sub">leases aktif</div></div>
  </div>

  <div class="g2">
    <div class="pnl">
      <div class="pnl-hdr"><span class="pnl-title">CPU — REAL TIME</span><span class="badge b-green" id="cpu-badge">--</span></div>
      <div class="pnl-body">
        <div class="chart-wrap" style="height:120px"><canvas id="cpuChart" role="img" aria-label="CPU usage over time"></canvas></div>
      </div>
    </div>
    <div class="pnl">
      <div class="pnl-hdr"><span class="pnl-title">MEMORY — REAL TIME</span><span class="badge b-blue" id="mem-badge">--</span></div>
      <div class="pnl-body">
        <div class="chart-wrap" style="height:120px"><canvas id="memChart" role="img" aria-label="Memory usage over time"></canvas></div>
      </div>
    </div>
  </div>

  <div class="g2">
    <div class="pnl">
      <div class="pnl-hdr"><span class="pnl-title">TOP INTERFACES — BANDWIDTH</span></div>
      <div class="pnl-body" id="dash-ifaces"></div>
    </div>
    <div class="pnl">
      <div class="pnl-hdr"><span class="pnl-title">RECENT ALERTS</span><span class="badge b-red" id="alert-count-badge">0</span></div>
      <div class="pnl-body" id="dash-alerts"></div>
    </div>
  </div>

  <div class="g2">
    <div class="pnl">
      <div class="pnl-hdr"><span class="pnl-title">BGP PEERS</span></div>
      <div class="pnl-body" id="dash-bgp"></div>
    </div>
    <div class="pnl">
      <div class="pnl-hdr"><span class="pnl-title">VPN / PPP SESSIONS</span><span class="badge b-green" id="vpn-count-badge">0</span></div>
      <div class="pnl-body" id="dash-vpn"></div>
    </div>
  </div>
</div>

<!-- ═══ INTERFACES PAGE ═══ -->
<div id="page-interfaces" class="page">
  <div id="iface-grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:8px"></div>
  <div class="pnl">
    <div class="pnl-hdr"><span class="pnl-title">BANDWIDTH HISTORY — <span id="iface-sel-name">pilih interface di atas</span></span></div>
    <div class="pnl-body">
      <div class="chart-wrap" style="height:150px"><canvas id="ifaceHistChart" role="img" aria-label="Interface bandwidth history"></canvas></div>
    </div>
  </div>
  <div class="pnl">
    <div class="pnl-hdr"><span class="pnl-title">DETAIL SEMUA INTERFACE</span></div>
    <div class="pnl-body" style="padding:0;overflow-x:auto">
      <table class="tbl">
        <thead><tr>
          <th>INTERFACE</th><th>ALIAS</th><th>STATUS</th><th>SPEED</th>
          <th>IN (Mbps)</th><th>OUT (Mbps)</th><th>UTIL%</th><th>ERR IN</th><th>ERR OUT</th>
        </tr></thead>
        <tbody id="iface-tbl"></tbody>
      </table>
    </div>
  </div>
</div>

<!-- ═══ DHCP PAGE ═══ -->
<div id="page-dhcp" class="page">
  <div class="pnl">
    <div class="pnl-hdr">
      <span class="pnl-title">DHCP LEASES</span>
      <span class="badge b-blue" id="dhcp-total-badge">0 leases</span>
    </div>
    <div class="pnl-body">
      <input class="search-box" id="dhcp-search" placeholder="Cari IP / hostname / MAC..." oninput="filterDHCP()">
    </div>
    <div style="overflow-x:auto">
      <table class="tbl">
        <thead><tr><th>#</th><th>IP ADDRESS</th><th>HOSTNAME</th><th>MAC ADDRESS</th></tr></thead>
        <tbody id="dhcp-tbl"></tbody>
      </table>
    </div>
  </div>
</div>

<!-- ═══ BGP PAGE ═══ -->
<div id="page-bgp" class="page">
  <div class="g2">
    <div class="pnl">
      <div class="pnl-hdr"><span class="pnl-title">BGP PEERS</span></div>
      <div class="pnl-body" style="padding:0;overflow-x:auto">
        <table class="tbl">
          <thead><tr><th>PEER IP</th><th>REMOTE AS</th><th>STATE</th><th>PREFIXES</th><th>IN UPD</th><th>OUT UPD</th></tr></thead>
          <tbody id="bgp-peer-tbl"></tbody>
        </table>
      </div>
    </div>
    <div class="pnl">
      <div class="pnl-hdr"><span class="pnl-title">PREFIXES PER AS NUMBER</span></div>
      <div class="pnl-body" id="bgp-as-list"></div>
    </div>
  </div>
  <div class="pnl">
    <div class="pnl-hdr"><span class="pnl-title">DISTRIBUSI PREFIX RECEIVED</span></div>
    <div class="pnl-body">
      <div class="chart-wrap" style="height:200px"><canvas id="bgpChart" role="img" aria-label="BGP prefix distribution by AS"></canvas></div>
    </div>
  </div>
</div>

<!-- ═══ VPN PAGE ═══ -->
<div id="page-vpn" class="page">
  <div class="pnl">
    <div class="pnl-hdr"><span class="pnl-title">VPN / PPP ACTIVE SESSIONS</span><span class="badge b-green" id="vpn-total"></span></div>
    <div style="overflow-x:auto">
      <table class="tbl">
        <thead><tr><th>NAME</th><th>ADDRESS</th><th>UPTIME</th></tr></thead>
        <tbody id="vpn-tbl"></tbody>
      </table>
    </div>
  </div>
</div>

<!-- ═══ QUEUES PAGE ═══ -->
<div id="page-queues" class="page">
  <div class="pnl">
    <div class="pnl-hdr"><span class="pnl-title">SIMPLE QUEUES</span><span class="badge b-blue" id="q-total"></span></div>
    <div class="pnl-body" id="q-list"></div>
  </div>
</div>

<!-- ═══ ALERTS PAGE ═══ -->
<div id="page-alerts" class="page">
  <div class="pnl">
    <div class="pnl-hdr"><span class="pnl-title">ALERT LOG</span><span class="badge b-red" id="alert-total"></span></div>
    <div class="pnl-body" id="alert-list"></div>
  </div>
</div>

<!-- ═══ CONFIG PAGE ═══ -->
<div id="page-config" class="page">
  <div class="pnl" style="max-width:500px">
    <div class="pnl-hdr"><span class="pnl-title">KONFIGURASI SNMP</span></div>
    <div class="pnl-body">
      <div class="cfg-row"><div class="cfg-lbl">IP MikroTik</div><input class="cfg-input" id="cfg-host" placeholder="192.168.1.1"></div>
      <div class="cfg-row"><div class="cfg-lbl">SNMP Community</div><input class="cfg-input" id="cfg-comm" placeholder="public"></div>
      <div class="cfg-row"><div class="cfg-lbl">Poll Interval (s)</div><input class="cfg-input" id="cfg-poll" type="number" min="5" max="300" value="10"></div>
      <button class="btn btn-save" onclick="saveConfig()">SIMPAN & TERAPKAN</button>
      <div id="cfg-msg" style="margin-top:8px;font-family:var(--mono);font-size:11px;color:var(--green)"></div>
    </div>
  </div>
  <div class="pnl" style="max-width:500px">
    <div class="pnl-hdr"><span class="pnl-title">SETUP MIKROTIK (SNMP)</span></div>
    <div class="pnl-body">
      <p style="font-family:var(--mono);font-size:11px;color:var(--muted);line-height:1.8">
        Aktifkan SNMP di MikroTik via Winbox atau terminal:<br><br>
        <span style="color:var(--cyan)">/snmp set enabled=yes</span><br>
        <span style="color:var(--cyan)">/snmp community set name=public read-access=yes</span><br>
        <span style="color:var(--cyan)">/ip firewall filter add chain=input protocol=udp dst-port=161 action=accept comment="SNMP"</span><br><br>
        Untuk BGP prefix tracking, aktifkan juga:<br>
        <span style="color:var(--cyan)">/routing bgp instance set default redistribute-other-bgp=yes</span>
      </p>
    </div>
  </div>
</div>

<script>
// ── STATE ─────────────────────────────────────────────────────────────────
const API = '';  // kosong = same origin; ganti 'http://IP:5000' jika beda server
let selectedIface = null;
let ifaceHistChart = null;
let cpuChart = null;
let memChart = null;
let bgpChart = null;
let dhcpAll = [];

// ── NAVIGATION ────────────────────────────────────────────────────────────
function showPage(name, btn) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('page-' + name).classList.add('active');
  if (btn) btn.classList.add('active');
}

// ── CLOCK ─────────────────────────────────────────────────────────────────
function updateClock() {
  document.getElementById('clk').textContent = new Date().toLocaleTimeString('id-ID', {hour12:false});
}
updateClock();
setInterval(updateClock, 1000);

// ── CHART INIT ────────────────────────────────────────────────────────────
function initCharts() {
  const baseOpts = (yMax, yLabel) => ({
    responsive: true, maintainAspectRatio: false,
    animation: {duration: 300},
    plugins: {legend: {display: false}},
    scales: {
      x: {display: false},
      y: {
        min: 0, max: yMax,
        grid: {color: 'rgba(26,48,80,.5)', drawBorder: false},
        ticks: {color: '#4a6a8a', font: {family: 'Share Tech Mono', size: 9},
                maxTicksLimit: 5, callback: v => v + yLabel}
      }
    }
  });

  cpuChart = new Chart(document.getElementById('cpuChart'), {
    type: 'line',
    data: {labels: [], datasets: [{
      data: [], borderColor: '#00e87a', borderWidth: 1.5, fill: true,
      backgroundColor: 'rgba(0,232,122,.08)', tension: .4, pointRadius: 0
    }]},
    options: baseOpts(100, '%')
  });

  memChart = new Chart(document.getElementById('memChart'), {
    type: 'line',
    data: {labels: [], datasets: [{
      data: [], borderColor: '#00aaff', borderWidth: 1.5, fill: true,
      backgroundColor: 'rgba(0,170,255,.08)', tension: .4, pointRadius: 0
    }]},
    options: baseOpts(100, '%')
  });

  ifaceHistChart = new Chart(document.getElementById('ifaceHistChart'), {
    type: 'line',
    data: {labels: [], datasets: [
      {label:'IN', data:[], borderColor:'#00e87a', borderWidth:1.5, fill:true,
       backgroundColor:'rgba(0,232,122,.08)', tension:.4, pointRadius:0},
      {label:'OUT', data:[], borderColor:'#ff2d55', borderWidth:1.5, fill:true,
       backgroundColor:'rgba(255,45,85,.08)', tension:.4, pointRadius:0},
    ]},
    options: {
      responsive: true, maintainAspectRatio: false,
      animation: {duration: 200},
      plugins: {legend: {display: false}},
      scales: {
        x: {display: false},
        y: {
          min: 0,
          grid: {color: 'rgba(26,48,80,.5)'},
          ticks: {color: '#4a6a8a', font: {family:'Share Tech Mono',size:9},
                  maxTicksLimit: 5, callback: v => v + ' Mbps'}
        }
      }
    }
  });

  bgpChart = new Chart(document.getElementById('bgpChart'), {
    type: 'bar',
    data: {labels: [], datasets: [{
      data: [], backgroundColor: 'rgba(0,170,255,.5)',
      borderColor: '#0af', borderWidth: 1
    }]},
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: {legend: {display: false}},
      scales: {
        x: {ticks: {color:'#4a6a8a', font:{family:'Share Tech Mono',size:9}}},
        y: {grid:{color:'rgba(26,48,80,.5)'}, ticks:{color:'#4a6a8a',font:{size:9}}}
      }
    }
  });
}

// ── FETCH HELPERS ─────────────────────────────────────────────────────────
async function fetchJSON(url) {
  const r = await fetch(API + url);
  return r.json();
}

// ── POLL SUMMARY ──────────────────────────────────────────────────────────
async function pollSummary() {
  try {
    const d = await fetchJSON('/api/summary');
    const dot = document.getElementById('poll-dot');
    dot.className = 'poll-dot' + (d.poll_ok ? '' : ' err');

    document.getElementById('top-host').textContent = d.system.host || CONFIG.host;
    document.getElementById('s-cpu').textContent = (d.system.cpu ?? '--') + '%';
    document.getElementById('s-cpu').className = 'stat-val ' + cpuColor(d.system.cpu);
    document.getElementById('s-cpu-sub').textContent = d.system.name || 'MikroTik';
    document.getElementById('s-mem').textContent = (d.system.mem_pct ?? '--') + '%';
    document.getElementById('s-mem-sub').textContent =
      d.system.mem_used_mb ? `${d.system.mem_used_mb} / ${d.system.mem_total_mb} MB` : '-- / -- MB';
    document.getElementById('s-fw').textContent = (d.firewall.conn_count ?? '--').toLocaleString();
    document.getElementById('s-uptime').textContent = d.system.uptime || '--';
    document.getElementById('s-dhcp').textContent = d.dhcp_count ?? '--';
    document.getElementById('cpu-badge').textContent = (d.system.cpu ?? '--') + '%';
    document.getElementById('mem-badge').textContent = (d.system.mem_pct ?? '--') + '%';
    document.getElementById('alert-count-badge').textContent = d.alert_count || '0';
    document.getElementById('vpn-count-badge').textContent = d.vpn_count || '0';
  } catch(e) {
    document.getElementById('poll-dot').className = 'poll-dot err';
  }
}

function cpuColor(v) {
  if (v > 80) return 'stat-val c-red';
  if (v > 60) return 'stat-val c-amber';
  return 'stat-val c-green';
}
function memColor(v) {
  if (v > 85) return 'c-red';
  if (v > 70) return 'c-amber';
  return 'c-blue';
}
function utilColor(v) {
  if (v > 80) return '#ff2d55';
  if (v > 60) return '#ffb300';
  return '#00e87a';
}
function fmtBps(bps) {
  if (bps >= 1e9) return (bps/1e9).toFixed(2) + ' Gbps';
  if (bps >= 1e6) return (bps/1e6).toFixed(2) + ' Mbps';
  if (bps >= 1e3) return (bps/1e3).toFixed(1) + ' Kbps';
  return bps + ' bps';
}

// ── CPU / MEM CHARTS ──────────────────────────────────────────────────────
async function updateCpuChart() {
  const data = await fetchJSON('/api/cpu_history');
  const labels = data.map(() => '');
  const vals = data.map(d => d.v);
  cpuChart.data.labels = labels;
  cpuChart.data.datasets[0].data = vals;
  cpuChart.update('none');
}
async function updateMemChart() {
  const data = await fetchJSON('/api/mem_history');
  memChart.data.labels = data.map(() => '');
  memChart.data.datasets[0].data = data.map(d => d.v);
  memChart.update('none');
}

// ── INTERFACES ────────────────────────────────────────────────────────────
let ifaceData = [];
async function updateInterfaces() {
  ifaceData = await fetchJSON('/api/interfaces');

  // Dashboard top ifaces
  const top = [...ifaceData].sort((a,b) => (b.in_bps+b.out_bps)-(a.in_bps+a.out_bps)).slice(0,5);
  const di = document.getElementById('dash-ifaces');
  di.innerHTML = top.map(f => `
    <div style="display:flex;align-items:center;gap:8px;padding:5px 0;border-bottom:1px solid rgba(26,48,80,.4)">
      <div style="width:8px;height:8px;border-radius:50%;background:${f.status==='up'?'var(--green)':'var(--red)'};flex-shrink:0"></div>
      <div style="font-family:var(--mono);font-size:11px;min-width:100px;overflow:hidden;text-overflow:ellipsis">${f.name}</div>
      <div style="flex:1;height:3px;background:rgba(255,255,255,.07);border-radius:2px;overflow:hidden">
        <div style="height:100%;width:${Math.min(f.util_pct,100)}%;background:${utilColor(f.util_pct)};border-radius:2px;transition:width .8s"></div>
      </div>
      <div style="font-family:var(--mono);font-size:10px;color:var(--green);min-width:70px;text-align:right">↑${f.out_mbps}M</div>
      <div style="font-family:var(--mono);font-size:10px;color:var(--red);min-width:70px;text-align:right">↓${f.in_mbps}M</div>
    </div>`).join('');

  // Iface grid
  const grid = document.getElementById('iface-grid');
  grid.innerHTML = ifaceData.map((f, i) => `
    <div class="iface-card ${selectedIface===i?'active':''}" onclick="selectIface(${i})">
      <div class="iface-top">
        <div style="width:8px;height:8px;border-radius:50%;background:${f.status==='up'?'var(--green)':'var(--red)'}"></div>
        <div class="iface-name" style="color:${f.status==='up'?'var(--bright)':'var(--muted)'}">${f.name}</div>
        <div class="badge ${f.status==='up'?'b-green':'b-red'}">${f.status.toUpperCase()}</div>
      </div>
      ${f.alias ? `<div class="iface-alias">${f.alias}</div>` : ''}
      <div class="bw-row">
        <span class="bw-in">↓ ${fmtBps(f.in_bps)}</span>
        <span class="bw-out">↑ ${fmtBps(f.out_bps)}</span>
      </div>
      <div class="util-bar"><div class="util-fill" style="width:${Math.min(f.util_pct,100)}%;background:${utilColor(f.util_pct)}"></div></div>
      <div style="font-family:var(--mono);font-size:9px;color:var(--muted);margin-top:4px">${f.speed_mbps ? f.speed_mbps+'Mbps · ' : ''}util ${f.util_pct}%</div>
    </div>`).join('');

  // Table
  const tbl = document.getElementById('iface-tbl');
  tbl.innerHTML = ifaceData.map(f => `
    <tr>
      <td class="mono">${f.name}</td>
      <td style="color:var(--muted);font-size:11px">${f.alias||'-'}</td>
      <td><span class="badge ${f.status==='up'?'b-green':'b-red'}">${f.status}</span></td>
      <td class="mono">${f.speed_mbps}M</td>
      <td class="mono c-green">${f.in_mbps}</td>
      <td class="mono c-red">${f.out_mbps}</td>
      <td class="mono" style="color:${utilColor(f.util_pct)}">${f.util_pct}%</td>
      <td class="mono ${f.in_errors>0?'c-red':''}">${f.in_errors}</td>
      <td class="mono ${f.out_errors>0?'c-red':''}">${f.out_errors}</td>
    </tr>`).join('');
}

function selectIface(idx) {
  selectedIface = idx;
  const f = ifaceData[idx];
  document.getElementById('iface-sel-name').textContent = f.name + (f.alias ? ` (${f.alias})` : '');
  document.querySelectorAll('.iface-card').forEach((c,i) => c.classList.toggle('active', i===idx));
  loadIfaceHistory(idx);
}

async function loadIfaceHistory(idx) {
  const idxKey = Object.keys(ifaceData)[idx] || idx;
  // Use array index since backend keys by interface index
  const allIfaces = await fetchJSON('/api/interfaces');
  const ifaceIdx = Object.keys(allIfaces)[idx] || (idx+1);
  try {
    const data = await fetchJSON('/api/iface_history/' + (idx+1));
    ifaceHistChart.data.labels = data.in.map(()=>'');
    ifaceHistChart.data.datasets[0].data = data.in.map(d=>d.v);
    ifaceHistChart.data.datasets[1].data = data.out.map(d=>d.v);
    ifaceHistChart.update('none');
  } catch(e) {}
}

// ── DHCP ──────────────────────────────────────────────────────────────────
async function updateDHCP() {
  dhcpAll = await fetchJSON('/api/dhcp');
  document.getElementById('dhcp-total-badge').textContent = dhcpAll.length + ' leases';
  renderDHCP(dhcpAll);
}
function renderDHCP(leases) {
  document.getElementById('dhcp-tbl').innerHTML = leases.map((l,i) => `
    <tr>
      <td class="mono" style="color:var(--muted)">${i+1}</td>
      <td class="mono c-cyan">${l.ip}</td>
      <td style="color:var(--text)">${l.host||'unknown'}</td>
      <td class="mono" style="color:var(--muted)">${l.mac}</td>
    </tr>`).join('') || '<tr><td colspan="4" class="empty">Tidak ada data DHCP</td></tr>';
}
function filterDHCP() {
  const q = document.getElementById('dhcp-search').value.toLowerCase();
  renderDHCP(q ? dhcpAll.filter(l =>
    l.ip.includes(q) || (l.host||'').toLowerCase().includes(q) || l.mac.includes(q)
  ) : dhcpAll);
}

// ── BGP ───────────────────────────────────────────────────────────────────
async function updateBGP() {
  const d = await fetchJSON('/api/bgp');
  const peers = d.peers || [];
  const byAS = d.prefix_by_as || {};

  // Dashboard mini
  document.getElementById('dash-bgp').innerHTML = peers.map(p => `
    <div class="bgp-peer">
      <span class="bgp-state ${p.state==='established'?'bs-established':'bs-other'}">${p.state}</span>
      <span style="font-family:var(--mono);font-size:11px;flex:1">${p.peer_ip}</span>
      <span style="font-family:var(--mono);font-size:10px;color:var(--blue)">AS${p.remote_as}</span>
      <span style="font-family:var(--mono);font-size:10px;color:var(--muted)">${p.prefix_count} pfx</span>
    </div>`).join('') || '<div class="empty">Tidak ada BGP peer</div>';

  // BGP page table
  document.getElementById('bgp-peer-tbl').innerHTML = peers.map(p => `
    <tr>
      <td class="mono c-cyan">${p.peer_ip}</td>
      <td class="mono c-blue">AS${p.remote_as}</td>
      <td><span class="bgp-state ${p.state==='established'?'bs-established':'bs-other'}">${p.state}</span></td>
      <td class="mono">${p.prefix_count.toLocaleString()}</td>
      <td class="mono" style="color:var(--muted)">${p.in_updates.toLocaleString()}</td>
      <td class="mono" style="color:var(--muted)">${p.out_updates.toLocaleString()}</td>
    </tr>`).join('') || '<tr><td colspan="6" class="empty">Tidak ada BGP peer</td></tr>';

  // AS prefix list
  const asList = document.getElementById('bgp-as-list');
  const asEntries = Object.entries(byAS).sort((a,b) => {
    const ta = a[1].reduce((s,p)=>s+p.prefixes,0);
    const tb = b[1].reduce((s,p)=>s+p.prefixes,0);
    return tb-ta;
  });
  const maxPfx = asEntries.reduce((m,[,v])=>Math.max(m,v.reduce((s,p)=>s+p.prefixes,0)),0)||1;
  asList.innerHTML = asEntries.map(([as, peers]) => {
    const total = peers.reduce((s,p)=>s+p.prefixes,0);
    return `<div class="as-block" style="margin-bottom:4px">
      <div class="as-num">AS${as}</div>
      <div class="pfx-bar-bg"><div class="pfx-bar" style="width:${total/maxPfx*100}%"></div></div>
      <div class="pfx-count">${total.toLocaleString()} pfx</div>
    </div>`;
  }).join('') || '<div class="empty">Tidak ada prefix data</div>';

  // BGP chart
  bgpChart.data.labels = asEntries.map(([as]) => 'AS'+as);
  bgpChart.data.datasets[0].data = asEntries.map(([,v]) => v.reduce((s,p)=>s+p.prefixes,0));
  bgpChart.update();
}

// ── VPN ───────────────────────────────────────────────────────────────────
async function updateVPN() {
  const sessions = await fetchJSON('/api/vpn');
  document.getElementById('vpn-total').textContent = sessions.length + ' sesi';

  // Dashboard
  document.getElementById('dash-vpn').innerHTML = sessions.slice(0,6).map(s => `
    <div class="vpn-row">
      <div class="vpn-name">${s.name}</div>
      <div class="vpn-addr">${s.address||'-'}</div>
      <div class="vpn-up">${s.uptime_str||'-'}</div>
    </div>`).join('') || '<div class="empty">Tidak ada sesi VPN aktif</div>';

  // VPN page
  document.getElementById('vpn-tbl').innerHTML = sessions.map(s => `
    <tr>
      <td class="mono c-green">${s.name}</td>
      <td class="mono c-blue">${s.address||'-'}</td>
      <td class="mono" style="color:var(--muted)">${s.uptime_str||'-'}</td>
    </tr>`).join('') || '<tr><td colspan="3" class="empty">Tidak ada sesi VPN aktif</td></tr>';
}

// ── QUEUES ────────────────────────────────────────────────────────────────
async function updateQueues() {
  const queues = await fetchJSON('/api/queues');
  document.getElementById('q-total').textContent = queues.length + ' queues';
  const maxB = queues.reduce((m,q)=>Math.max(m,q.bytes_in+q.bytes_out),0)||1;

  document.getElementById('q-list').innerHTML = queues.map(q => `
    <div class="q-row">
      <div class="q-top">
        <div class="q-name">${q.name}</div>
        <div class="q-limit">${q.max_limit||'-'}</div>
      </div>
      <div class="q-bars">
        <div class="q-bar-row">
          <span class="q-label">IN</span>
          <div class="q-bar-bg"><div class="q-bar" style="width:${q.bytes_in/maxB*100}%;background:var(--green)"></div></div>
          <span style="font-family:var(--mono);font-size:10px;color:var(--muted);min-width:70px;text-align:right">${(q.bytes_in/1e6).toFixed(2)} MB</span>
        </div>
        <div class="q-bar-row">
          <span class="q-label">OUT</span>
          <div class="q-bar-bg"><div class="q-bar" style="width:${q.bytes_out/maxB*100}%;background:var(--red)"></div></div>
          <span style="font-family:var(--mono);font-size:10px;color:var(--muted);min-width:70px;text-align:right">${(q.bytes_out/1e6).toFixed(2)} MB</span>
        </div>
      </div>
    </div>`).join('') || '<div class="empty">Tidak ada simple queue</div>';
}

// ── ALERTS ────────────────────────────────────────────────────────────────
async function updateAlerts() {
  const alerts = await fetchJSON('/api/alerts');
  document.getElementById('alert-total').textContent = alerts.length;
  const klsMap = {CRIT:'al-crit',WARN:'al-warn',INFO:'al-info'};

  const html = alerts.map(a => `
    <div class="alert-item ${klsMap[a.level]||'al-info'}">
      <div class="al-dot"></div>
      <div class="al-text">${a.msg}</div>
      <div class="al-source">${a.source}</div>
      <div class="al-time">${a.time}</div>
    </div>`).join('');
  document.getElementById('alert-list').innerHTML = html || '<div class="empty">Tidak ada alert</div>';

  // Dashboard
  document.getElementById('dash-alerts').innerHTML = alerts.slice(0,5).map(a => `
    <div class="alert-item ${klsMap[a.level]||'al-info'}" style="margin-bottom:3px">
      <div class="al-dot"></div>
      <div class="al-text" style="font-size:11px">${a.msg}</div>
      <div class="al-time">${a.time}</div>
    </div>`).join('') || '<div class="empty">Tidak ada alert</div>';
}

// ── TICKER ────────────────────────────────────────────────────────────────
function updateTicker(summary, ifaces) {
  const sys = summary.system || {};
  const parts = [
    `📡 ${sys.name||'MikroTik'} · CPU:${sys.cpu||'--'}% · RAM:${sys.mem_pct||'--'}%`,
    `⏱ Uptime: ${sys.uptime||'--'}`,
    `🔗 FW Conn: ${(summary.firewall?.conn_count||0).toLocaleString()}`,
    `👥 DHCP: ${summary.dhcp_count||0} leases`,
    `🔐 VPN: ${summary.vpn_count||0} sesi`,
    `🌐 BGP: ${summary.bgp_count||0} peers`,
  ];
  if (ifaces) {
    const top = ifaces.sort((a,b)=>(b.in_bps+b.out_bps)-(a.in_bps+a.out_bps)).slice(0,3);
    top.forEach(f => parts.push(`📶 ${f.name}: ↓${f.in_mbps}M ↑${f.out_mbps}M`));
  }
  const t = parts.join('  ·  ');
  document.getElementById('ticker-text').textContent = t + '   ' + t;
}

// ── CONFIG ────────────────────────────────────────────────────────────────
let CONFIG = {};
async function loadConfig() {
  try {
    CONFIG = await fetchJSON('/api/config');
    document.getElementById('cfg-host').value = CONFIG.host || '';
    document.getElementById('cfg-comm').value = CONFIG.community || '';
    document.getElementById('cfg-poll').value = CONFIG.poll_interval || 10;
  } catch(e) {}
}
async function saveConfig() {
  const body = {
    host: document.getElementById('cfg-host').value,
    community: document.getElementById('cfg-comm').value,
    poll_interval: parseInt(document.getElementById('cfg-poll').value),
  };
  try {
    await fetch(API + '/api/config', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(body)});
    document.getElementById('cfg-msg').textContent = '✓ Konfigurasi disimpan!';
    setTimeout(() => document.getElementById('cfg-msg').textContent = '', 3000);
    CONFIG = body;
  } catch(e) {
    document.getElementById('cfg-msg').style.color = 'var(--red)';
    document.getElementById('cfg-msg').textContent = '✗ Gagal menyimpan';
  }
}

// ── MAIN LOOP ─────────────────────────────────────────────────────────────
async function refreshAll() {
  try {
    const [summary] = await Promise.all([
      pollSummary(),
      updateCpuChart(),
      updateMemChart(),
      updateInterfaces(),
      updateDHCP(),
      updateBGP(),
      updateVPN(),
      updateQueues(),
      updateAlerts(),
    ]);
    const ifaces = await fetchJSON('/api/interfaces');
    const sum = await fetchJSON('/api/summary');
    updateTicker(sum, Object.values(ifaces));
  } catch(e) {
    console.error('Refresh error:', e);
  }
}

// ── BOOT ──────────────────────────────────────────────────────────────────
initCharts();
loadConfig();
refreshAll();
setInterval(refreshAll, 10000);
</script>
</body>
</html>
