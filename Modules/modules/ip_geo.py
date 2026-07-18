import requests
from colorama import Fore

def locate(ip=None):
    if not ip:
        ip = requests.get("https://api.ipify.org").text
    
    print(Fore.CYAN + f"\n[+] {ip} sorgulanıyor...")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response["status"] == "success":
            print(Fore.GREEN + f"""
    Ülke     : {response['country']} ({response['countryCode']})
    Şehir    : {response['city']}
    Bölge    : {response['regionName']}
    ISP      : {response['isp']}
    Koordinat: {response['lat']}, {response['lon']}
    Zaman    : {response['timezone']}
            """)
            lat = float(response['lat'])
            print("Harita: " + "█" * int((lat + 90) / 2) + "⬤" + "█" * (90 - int((lat + 90) / 2)))
        else:
            print(Fore.RED + "[!] IP bulunamadı.")
    except:
        print(Fore.RED + "[!] Bağlantı hatası.")
