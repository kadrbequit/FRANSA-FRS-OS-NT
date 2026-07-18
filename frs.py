

import os
import sys
import time
from colorama import init, Fore, Style


sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
from mail_check import check as mail_check
from username_osint import search as username_osint
from ip_geo import locate as ip_geo
from wifi_scanner import scan as wifi_scanner
from tiktok_osint import get_info as tiktok_osint
from phone_lookup import lookup as phone_lookup

init(autoreset=True)

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(Fore.CYAN + """
    ╔═══════════════════════════════════════════════╗
    ║  🔥 FRS-OSINT - FRANSA Intelligence     ║
    ║  👤 Kurucu: KADRBEQUIT                       ║
    ║  📢 Kanal: FRANSA#FRS                        ║
    ║  🔗 https://t.me/fransafrs1                  ║
    ╚═══════════════════════════════════════════════╝
    """ + Style.RESET_ALL)

def menu():
    print(Fore.YELLOW + "\n[+] Ana Menü:")
    print(Fore.GREEN + " 1) Mail Sızdı mı? (HaveIBeenPwned)")
    print(" 2) Kullanıcı Adı Araştır (300+ platform)")
    print(" 3) IP Coğrafi Bilgi")
    print(" 4) Wi-Fi Tarayıcı (Çevredeki ağlar)")
    print(" 5) TikTok OSINT (Kullanıcı profili)")
    print(" 6) Telefon Numarası Sorgula")
    print(Fore.MAGENTA + " 7) Tüm Raporu Al (Toplu sorgu)")
    print(Fore.RED + " 8) Panik Modu (Tüm izleri temizle)")
    print(Fore.WHITE + " 9) Çıkış")
    print("-" * 50)

def panic_mode():
    print(Fore.RED + "\n[!] PANİK MODU AKTİF! Tüm loglar ve geçmiş siliniyor...")
    os.system("rm -rf logs/")
    os.system("rm -rf ~/.bash_history")
    os.system("rm -rf ~/.zsh_history")
    print(Fore.GREEN + "[✓] Temizlik tamamlandı. Çıkış yapılıyor...")
    sys.exit(0)

def main():
    while True:
        clear()
        banner()
        menu()
        choice = input(Fore.CYAN + "\n[?] Seçiminiz: " + Style.RESET_ALL)

        if choice == "1":
            mail = input("Mail adresi: ")
            mail_check(mail)
            input("\n[Enter] ile devam...")
        elif choice == "2":
            username = input("Kullanıcı adı: ")
            username_osint(username)
            input("\n[Enter] ile devam...")
        elif choice == "3":
            ip = input("IP adresi (boş bırakırsan kendi IP'n): ")
            ip_geo(ip if ip else "")
            input("\n[Enter] ile devam...")
        elif choice == "4":
            wifi_scanner()
            input("\n[Enter] ile devam...")
        elif choice == "5":
            user = input("TikTok kullanıcı adı (@'siz): ")
            tiktok_osint(user)
            input("\n[Enter] ile devam...")
        elif choice == "6":
            num = input("Telefon numarası (+90555...): ")
            phone_lookup(num)
            input("\n[Enter] ile devam...")
        elif choice == "7":
            target = input("Hedef mail: ")
            username = input("Hedef kullanıcı adı: ")
            ip = input("Hedef IP: ")
            print(Fore.CYAN + "\n[+] Toplu rapor alınıyor...")
            with open("rapor.txt", "w") as f:
                f.write("=== FRS-OSINT RAPOR ===\n")
                f.write(f"Hedef: {target} | {username} | {ip}\n\n")
            mail_check(target)
            username_osint(username)
            ip_geo(ip)
            print(Fore.GREEN + "[✓] Rapor 'rapor.txt' dosyasına kaydedildi.")
            input("\n[Enter] ile devam...")
        elif choice == "8":
            confirm = input(Fore.RED + "EMİN MİSİN? (evet/hayır): ")
            if confirm.lower() == "evet":
                panic_mode()
        elif choice == "9":
            print(Fore.GREEN + "\n[+] Çıkış yapılıyor... FRANSA#FRS'yi takipte kal!")
            sys.exit(0)
        else:
            print(Fore.RED + "[!] Geçersiz seçim!")
            time.sleep(1)

if __name__ == "__main__":
    main()
