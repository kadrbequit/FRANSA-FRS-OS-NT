import requests
from bs4 import BeautifulSoup
from colorama import Fore

def get_info(username):
    print(Fore.CYAN + f"\n[+] TikTok: @{username} taranıyor...")
    try:
        url = f"https://www.tiktok.com/@{username}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            desc = soup.find("meta", {"name": "description"})
            if desc:
                content = desc.get("content", "")
                print(Fore.GREEN + f"\n[+] Profil Bilgileri:")
                for line in content.split("•"):
                    print(f"  {line.strip()}")
            else:
                print(Fore.YELLOW + "[!] TikTok meta verisi alınamadı.")
            
            followers = soup.find("strong", {"data-e2e": "followers-count"})
            if followers:
                print(Fore.CYAN + f"[+] Takipçi: {followers.text}")
        else:
            print(Fore.RED + "[!] Kullanıcı bulunamadı veya engelli.")
    except Exception as e:
        print(Fore.RED + f"[!] Hata: {e}")
