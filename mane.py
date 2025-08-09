from flask import Flask, request
import requests
import os

TOKEN = "8271406239:AAF1VnJsBVGBWHfhBMNFMgrbonYX1Z7B7TE"  # Tumhara Telegram bot token
URL = f"https://api.telegram.org/bot{TOKEN}/"

app = Flask(__name__)

def send_message(chat_id, text):
    url = URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        data = request.get_json()
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")
            
            # Simple reply logic
            if text.lower() == "/start":
                send_message(chat_id, "Welcome to Skill Pro Bot! 🚀")
            else:
                send_message(chat_id, f"You said: {text}")
                
        return {"ok": True}
    return "Skill Pro Bot Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
