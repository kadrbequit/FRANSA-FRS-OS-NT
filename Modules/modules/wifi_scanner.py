import subprocess
import re
from colorama import Fore

def scan():
    print(Fore.CYAN + "\n[+] Wi-Fi ağları taranıyor...")
    try:
        output = subprocess.check_output(["termux-wifi-scaninfo"], text=True)
        print(Fore.GREEN + output)
    except:
        try:
            output = subprocess.check_output(["dumpsys", "wifi"], text=True)
            ssids = re.findall(r'SSID: "(.+?)"', output)
            bssids = re.findall(r'BSSID: (.+?) ', output)
            levels = re.findall(r'level: (.+?),', output)
            
            print(Fore.GREEN + "\n[+] Bulunan Ağlar:")
            for i in range(min(len(ssids), 20)):
                print(f"  {i+1}. SSID: {ssids[i]} | MAC: {bssids[i] if i < len(bssids) else '?'} | Sinyal: {levels[i] if i < len(levels) else '?'} dBm")
        except:
            print(Fore.RED + "[!] Wi-Fi taraması için root veya termux-wifi paketi gerekli.")
            print("[!] Kurulum: pkg install termux-wifi")
