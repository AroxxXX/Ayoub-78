
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7998658311:AAFZPaGMo1VbpVUhPiTmw16GVsxLguJtplM"
CHAT_ID = "6132891183"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    signal = data.get('signal', 'Alerte')
    symbol = data.get('symbol', 'Symbole inconnu')
    message = f"Signal détecté : {signal} sur {symbol}"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
