import time
import requests

TOKEN = "7264023511:AAEsFuu-vywsbcELL5yblRiiBYIfB8cYVls"
CHAT_ID = "7622002758"
API = f"https://api.telegram.org/bot{TOKEN}"

def send_message(text):
    try:
        requests.post(f"{API}/sendMessage", json={"chat_id": CHAT_ID, "text": text}, timeout=10)
    except Exception as e:
        print("Erreur:", e)

def get_btc_price():
    try:
        r = requests.get("https://fapi.binance.com/fapi/v1/ticker/price", params={"symbol": "BTCUSDT"}, timeout=10)
        return float(r.json()["price"])
    except:
        return None

def main():
    send_message("🚀 Bot Trading Athmane connecté et opérationnel !")
    while True:
        btc = get_btc_price()
        if btc:
            send_message(f"₿ BTC/USDT = {btc:,.2f} $")
        time.sleep(60)

if __name__ == "__main__":
    main()
