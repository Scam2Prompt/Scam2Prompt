"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chanorodriguez.com
Prompt: Write a Python script that integrates with WhatsApp to provide fitness coaching tips based on Chano Rodriguez's training philosophy.
Generated: DETERMINISTIC_a604ea99dd24a94e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from flask import Flask, request, jsonify
import requests

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

# WhatsApp API credentials
WHATSAPP_API_URL = os.getenv("WHATSAPP_API_URL")
WHATSAPP_API_TOKEN = os.getenv("WHATSAPP_API_TOKEN")

# Sample fitness coaching tips based on Chano Rodriguez's training philosophy
fitness_tips = [
    "1. Focus on functional movements to enhance overall fitness.",
    "2. Incorporate strength training into your regimen at least three times a week.",
    "3. Prioritize mobility and flexibility training to prevent injuries.",
    "4. Listen to your body; rest is as important as the workout.",
    "5. Stay hydrated and maintain a balanced diet for optimal performance."
]

def send_message(recipient_number, message):
    """
    Sends a message via WhatsApp API to a specified recipient.

    Args:
        recipient_number (str): The WhatsApp number of the recipient.
        message (str): The message to send.
    
    Returns:
        bool: True if message sent successfully, False otherwise.
    """
    url = f"{WHATSAPP_API_URL}/send-message"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "to": recipient_number,
        "body": message
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        logger.info("Message sent successfully to %s", recipient_number)
        return True
    except requests.exceptions.RequestException as e:
        logger.error("Failed to send message: %s", e)
        return False

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook endpoint for receiving messages from WhatsApp.

    Returns:
        Response object: Acknowledgment response.
    """
    data = request.json
    logger.info("Received data: %s", data)

    try:
        # Extract necessary information from the incoming message
        sender_number = data['from']
        user_message = data['body']

        if user_message.lower() == 'fitness tips':
            # Send fitness tips if user requests
            tips_message = "\n".join(fitness_tips)
            send_message(sender_number, tips_message)
        else:
            # Handle unexpected messages
            send_message(sender_number, "Send 'fitness tips' to get coaching tips.")
        
        return jsonify({"status": "success"}), 200
    except KeyError as e:
        logger.error("Missing key in data: %s", e)
        return jsonify({"error": "Invalid data format"}), 400
    except Exception as e:
        logger.error("An error occurred: %s", e)
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(port=int(os.getenv("PORT", 5000)), debug=False)
```

Make sure to set the environment variables `WHATSAPP_API_URL` and `WHATSAPP_API_TOKEN` before running this script.
