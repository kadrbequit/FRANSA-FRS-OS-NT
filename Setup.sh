

echo "[+] FRS-OSINT Kurulumu Başlatılıyor..."


pkg update -y
pkg upgrade -y
pkg install python git rust binutils cmake -y


pip install -r requirements.txt


if ! command -v termux-wifi-scaninfo &> /dev/null; then
    echo "[!] termux-wifi paketi kurulu değil. Kuruluyor..."
    pkg install termux-wifi -y
fi

echo "[✓] Kurulum tamamlandı!"
echo "[+] Çalıştırmak için: python frs.py"
