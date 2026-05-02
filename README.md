# MikroTik NOC Monitor

Web dashboard monitoring MikroTik via SNMP — Ubuntu 22.04

## Fitur
- **CPU & RAM** — real-time gauge + histori grafik
- **Interface & Bandwidth** — semua interface, in/out Mbps, utilization %, errors
- **DHCP Leases** — tabel semua client dengan search (IP/hostname/MAC)
- **Firewall** — jumlah active connection
- **BGP Peers** — state, prefix received, pengelompokan prefix per AS number
- **VPN/PPP Sessions** — semua sesi aktif + uptime
- **Simple Queues** — bytes in/out, max limit
- **Alert Log** — notifikasi otomatis (CPU tinggi, interface down, BGP flap)

## Instalasi Cepat

```bash
# Clone / copy folder ini ke server Ubuntu 22
cd mikrotik-noc
chmod +x setup.sh
./setup.sh
```

Script setup.sh akan:
1. Buat virtual environment Python
2. Install semua dependency
3. Test koneksi SNMP ke MikroTik
4. Update konfigurasi IP & community string
5. Buat systemd service (auto-start)
6. Buka port 5000

## Instalasi Manual

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Edit konfigurasi dulu
nano app.py  # ubah host dan community

python3 app.py
```

Buka browser: `http://IP-SERVER:5000`

## Konfigurasi MikroTik (SNMP)

Jalankan di terminal MikroTik atau Winbox > New Terminal:

```
/snmp set enabled=yes
/snmp community set name=public read-access=yes
/ip firewall filter add chain=input protocol=udp dst-port=161 \
    src-address=IP-UBUNTU-KAMU action=accept comment="Allow SNMP from NOC"
```

## Edit Konfigurasi

Edit langsung di `app.py` bagian `CONFIG`:

```python
CONFIG = {
    "host": "192.168.1.1",     # IP MikroTik
    "community": "public",     # SNMP community string
    "poll_interval": 10,       # interval polling (detik)
    "bgp_enabled": True,       # aktifkan monitoring BGP
}
```

Atau via web di halaman **Config**.

## Struktur File

```
mikrotik-noc/
├── app.py              # Backend Flask + SNMP poller
├── requirements.txt    # Dependencies Python
├── setup.sh            # Script instalasi otomatis
└── templates/
    └── index.html      # Frontend dashboard
```

## Manajemen Service

```bash
sudo systemctl status mikrotik-noc    # cek status
sudo systemctl restart mikrotik-noc   # restart
sudo systemctl stop mikrotik-noc      # stop
journalctl -u mikrotik-noc -f         # lihat log real-time
```

## OID yang Digunakan

| Fitur | OID Base |
|-------|----------|
| CPU | 1.3.6.1.2.1.25.3.3.1.2 |
| Memory | 1.3.6.1.2.1.25.2.3.1 |
| Interfaces (64-bit) | 1.3.6.1.2.1.31.1.1.1 |
| DHCP Leases | 1.3.6.1.4.1.14988.1.1.6 |
| BGP (RFC) | 1.3.6.1.2.1.15.3 |
| Simple Queue | 1.3.6.1.4.1.14988.1.1.2.1 |
| VPN/PPP | 1.3.6.1.4.1.14988.1.1.2.2 |
| FW Connections | 1.3.6.1.4.1.14988.1.1.9.1.0 |

## Troubleshooting

**SNMP timeout:** Pastikan firewall MikroTik mengizinkan UDP port 161 dari IP server Ubuntu.

**BGP tidak muncul:** Pastikan MikroTik menjalankan BGP dan BGP4-MIB support aktif.

**Data kosong:** Cek log dengan `journalctl -u mikrotik-noc -f` untuk melihat error.
