# 🔥 FRS-OSINT 

**Termux için Gelişmiş OSINT + Güvenlik Aracı**

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![Termux](https://img.shields.io/badge/termux-supported-orange)
![License](https://img.shields.io/badge/license-MIT-red)

---

## 👤 KÜNYE
- **Kurucu**: KADRBEQUIT
- **Kanal**: FRANSA#FRS
- **Telegram**: [https://t.me/fransafrs1](https://t.me/fransafrs1)

---

## 📌 ÖZELLİKLER

| Modül | Açıklama |
|-------|----------|
| 📧 Mail Sorgu | HaveIBeenPwned ile sızdırılmış mail kontrolü |
| 👤 Kullanıcı Adı | 300+ platformda username taraması (Sherlock) |
| 🌍 IP Coğrafi | IP'nin konum, ISP ve harita bilgisi |
| 📡 Wi-Fi Tarayıcı | Çevredeki ağları listeleme |
| 🎵 TikTok OSINT | Profil bilgisi, takipçi sayısı, bio |
| 📱 Telefon Numarası | Ülke, operatör, zaman dilimi |
| 🕵️ Panik Modu | Tüm logları ve geçmişi siler |

---

## 🚀 KURULUM

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/kadrbequit/FRANSA-FRS-OS-NT.git
cd FRANSA-FRS-OS-NT
pip install -r requirements.txt
python frs.py
