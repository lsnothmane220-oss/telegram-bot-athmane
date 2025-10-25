import requests
import time

TOKEN = "8226089903:AAHZlQpz4AjSDMxAyvqHRUEpPKzf1Xk6wEU"
CHAT_ID = "7622002758"

def get_btc_price():
    try:
        response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        data = response.json()
        return float(data["price"])
    except Exception as e:
        return None

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Erreur envoi message:", e)

def main():
    last_price = 0
    send_message("🚀 Bot de surveillance BTC lancé avec succès.")
    
    while True:
        price = get_btc_price()
        if price:
            if abs(price - last_price) > 100:  # alerte variation
                send_message(f"📊 BTC: {price:.2f} USD")
                last_price = price
        time.sleep(60)  # vérifie toutes les minutes

if __name__ == "__main__":
    main()
