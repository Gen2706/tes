#!/bin/bash
# ─────────────────────────────────────────────────────────────────
#  MikroTik NOC Monitor — Setup Script untuk Ubuntu 22.04
# ─────────────────────────────────────────────────────────────────
set -e

RED='\033[0;31m'; GREEN='\033[0;32m'; CYAN='\033[0;36m'; NC='\033[0m'
info()    { echo -e "${CYAN}[INFO]${NC} $1"; }
success() { echo -e "${GREEN}[OK]${NC} $1"; }
error()   { echo -e "${RED}[ERR]${NC} $1"; exit 1; }

echo ""
echo "  ███╗   ███╗██╗██╗  ██╗██████╗  ██████╗ ████████╗██╗██╗  ██╗"
echo "  ████╗ ████║██║██║ ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝██║██║ ██╔╝"
echo "  ██╔████╔██║██║█████╔╝ ██████╔╝██║   ██║   ██║   ██║█████╔╝ "
echo "  ██║╚██╔╝██║██║██╔═██╗ ██╔══██╗██║   ██║   ██║   ██║██╔═██╗ "
echo "  ██║ ╚═╝ ██║██║██║  ██╗██║  ██║╚██████╔╝   ██║   ██║██║  ██╗"
echo "  NOC Monitor for MikroTik — Ubuntu 22.04"
echo ""

# ── Cek Python ──────────────────────────────────────────────────
info "Cek Python 3..."
python3 --version || error "Python3 tidak ditemukan. Install dengan: sudo apt install python3"
success "Python3 OK"

# ── Buat virtual environment ────────────────────────────────────
info "Membuat virtual environment..."
python3 -m venv venv
source venv/bin/activate
success "venv aktif"

# ── Install dependencies ─────────────────────────────────────────
info "Install dependencies Python..."
pip install --upgrade pip -q
pip install -r requirements.txt -q
success "Dependencies terinstall"

# ── Test SNMP ────────────────────────────────────────────────────
echo ""
read -p "Masukkan IP MikroTik kamu [192.168.1.1]: " MT_IP
MT_IP=${MT_IP:-192.168.1.1}
read -p "Masukkan SNMP community string [public]: " MT_COMM
MT_COMM=${MT_COMM:-public}

info "Test koneksi SNMP ke $MT_IP..."
python3 -c "
from pysnmp.hlapi import *
for (e,s,i,v) in getCmd(SnmpEngine(),
    CommunityData('$MT_COMM'),
    UdpTransportTarget(('$MT_IP',161),timeout=3,retries=1),
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.5.0'))):
    if e or s: print('GAGAL:', e or s)
    else: print('OK — Hostname:', v[0][1].prettyPrint())
" && success "SNMP berhasil terhubung!" || echo "Peringatan: SNMP test gagal. Cek IP dan community string di app.py"

# ── Update config di app.py ──────────────────────────────────────
info "Update konfigurasi di app.py..."
sed -i "s/\"host\": \"192.168.1.1\"/\"host\": \"$MT_IP\"/" app.py
sed -i "s/\"community\": \"public\"/\"community\": \"$MT_COMM\"/" app.py
success "Config diupdate"

# ── Buat systemd service ─────────────────────────────────────────
APP_DIR=$(pwd)
USERNAME=$(whoami)

info "Membuat systemd service..."
sudo tee /etc/systemd/system/mikrotik-noc.service > /dev/null <<EOF
[Unit]
Description=MikroTik NOC Monitor
After=network.target

[Service]
User=$USERNAME
WorkingDirectory=$APP_DIR
ExecStart=$APP_DIR/venv/bin/python $APP_DIR/app.py
Restart=always
RestartSec=5
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable mikrotik-noc
sudo systemctl start mikrotik-noc
success "Service mikrotik-noc diaktifkan dan dijalankan"

# ── Buka firewall ────────────────────────────────────────────────
info "Buka port 5000 di UFW (jika aktif)..."
sudo ufw allow 5000/tcp 2>/dev/null || true
success "Port 5000 dibuka"

# ── Done ─────────────────────────────────────────────────────────
echo ""
echo -e "${GREEN}════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  NOC Monitor BERHASIL dipasang!${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  Akses dashboard di: ${CYAN}http://$(hostname -I | awk '{print $1}'):5000${NC}"
echo ""
echo "  Perintah berguna:"
echo "    sudo systemctl status mikrotik-noc   # cek status"
echo "    sudo systemctl restart mikrotik-noc  # restart"
echo "    journalctl -u mikrotik-noc -f        # lihat log"
echo ""
echo -e "  ${CYAN}Setup SNMP di MikroTik (jalankan di terminal MikroTik):${NC}"
echo "    /snmp set enabled=yes"
echo "    /snmp community set name=$MT_COMM read-access=yes"
echo "    /ip firewall filter add chain=input protocol=udp dst-port=161 action=accept"
echo ""
