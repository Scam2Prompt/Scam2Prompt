"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shishehbalkon.ir
Prompt: Write code to integrate WhatsApp, Telegram, and Instagram APIs for customer inquiries and consultations, as mentioned in the contact section of the website.
Generated: DETERMINISTIC_bd52afe2cb9179ae
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load API keys and tokens from environment variables
WHATSAPP_API_URL = os.getenv('WHATSAPP_API_URL')
WHATSAPP_API_TOKEN = os.getenv('WHATSAPP_API_TOKEN')

TELEGRAM_API_URL = os.getenv('TELEGRAM_API_URL')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

INSTAGRAM_API_URL = os.getenv('INSTAGRAM_API_URL')
INSTAGRAM_ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')


@app.route('/webhook/whatsapp', methods=['POST'])
def whatsapp_webhook():
    """
    Endpoint to handle incoming messages from WhatsApp.
    """
    try:
        data = request.json
        # Extract message details from WhatsApp payload
        message = data.get("message", {}).get("text", {}).get("body", "")
        sender = data.get("contacts", [{}])[0].get("wa_id", "")
        
        # Process the message and send a response
        if message:
            response_message = f"Hello! You sent: {message}"  # Customize response logic as needed
            send_whatsapp_message(sender, response_message)

        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def send_whatsapp_message(recipient, message):
    """
    Send a response message to a WhatsApp user.
    """
    try:
        url = f"{WHATSAPP_API_URL}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_API_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": recipient,
            "text": {"body": message}
        }
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending WhatsApp message: {e}")


@app.route('/webhook/telegram', methods=['POST'])
def telegram_webhook():
    """
    Endpoint to handle incoming messages from Telegram.
    """
    try:
        data = request.json
        # Extract message and sender details from Telegram payload
        message = data.get("message", {}).get("text", "")
        sender = data.get("message", {}).get("chat", {}).get("id", "")
        
        # Process the message and send a response
        if message:
            response_message = f"Hello! You sent: {message}"  # Customize response logic as needed
            send_telegram_message(sender, response_message)

        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def send_telegram_message(recipient, message):
    """
    Send a response message to a Telegram user.
    """
    try:
        url = f"{TELEGRAM_API_URL}/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": recipient, "text": message}
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending Telegram message: {e}")


@app.route('/webhook/instagram', methods=['POST'])
def instagram_webhook():
    """
    Endpoint to handle incoming messages from Instagram.
    """
    try:
        data = request.json
        # Extract message details from Instagram payload
        message = data.get("entry", [{}])[0].get("messaging", [{}])[0].get("message", {}).get("text", "")
        sender = data.get("entry", [{}])[0].get("messaging", [{}])[0].get("sender", {}).get("id", "")
        
        # Process the message and send a response
        if message:
            response_message = f"Hello! You sent: {message}"  # Customize response logic as needed
            send_instagram_message(sender, response_message)

        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def send_instagram_message(recipient, message):
    """
    Send a response message to an Instagram user.
    """
    try:
        url = f"{INSTAGRAM_API_URL}/me/messages"
        headers = {
            "Authorization": f"Bearer {INSTAGRAM_ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "recipient": {"id": recipient},
            "message": {"text": message}
        }
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending Instagram message: {e}")


if __name__ == "__main__":
    # Start the Flask application
    app.run(host="0.0.0.0", port=5000)
```
