"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-ai-migration-claim.pages.dev
Prompt: Develop a Fetch.ai-based agent that integrates with Slack and WhatsApp to provide real-time updates on mobility and IoT device statuses.
Generated: DETERMINISTIC_a743349ecf72f60b
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from flask import Flask, request, jsonify
from slack_sdk import WebClient as SlackClient
from slack_sdk.errors import SlackApiError
from twilio.rest import Client as TwilioClient

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Fetch.ai agent configuration
FETCH_AI_API_URL = os.getenv('FETCH_AI_API_URL')
FETCH_AI_API_KEY = os.getenv('FETCH_AI_API_KEY')

# Slack configuration
SLACK_TOKEN = os.getenv('SLACK_TOKEN')
slack_client = SlackClient(SLACK_TOKEN)

# Twilio configuration for WhatsApp
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')
twilio_client = TwilioClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Endpoint to fetch IoT device status
def fetch_iot_device_status(device_id):
    try:
        # Placeholder for Fetch.ai API request
        response = requests.get(f"{FETCH_AI_API_URL}/devices/{device_id}", 
                                headers={"Authorization": f"Bearer {FETCH_AI_API_KEY}"})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching device status: {e}")
        return None

# Function to send message to Slack
def send_slack_message(channel, text):
    try:
        slack_client.chat_postMessage(channel=channel, text=text)
    except SlackApiError as e:
        logging.error(f"Slack API Error: {e.response['error']}")

# Function to send message via WhatsApp
def send_whatsapp_message(to, text):
    try:
        message = twilio_client.messages.create(
            body=text,
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=f"whatsapp:{to}"
        )
        return message.sid
    except Exception as e:
        logging.error(f"Twilio API Error: {e}")

# Endpoint to receive updates and notify via Slack and WhatsApp
@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    device_id = data.get("device_id")
    user_id = data.get("user_id")
    slack_channel = data.get("slack_channel")
    whatsapp_number = data.get("whatsapp_number")

    # Fetch the status of the IoT device
    device_status = fetch_iot_device_status(device_id)

    if device_status:
        message_text = f"Device ID: {device_id}\nStatus: {device_status['status']}"
        # Send notifications
        send_slack_message(slack_channel, message_text)
        send_whatsapp_message(whatsapp_number, message_text)
        return jsonify({"message": "Notifications sent successfully!"}), 200
    else:
        return jsonify({"error": "Failed to fetch device status"}), 500

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**Environment Variables Required:**
- `FETCH_AI_API_URL`
- `FETCH_AI_API_KEY`
- `SLACK_TOKEN`
- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`
- `TWILIO_WHATSAPP_NUMBER`

**Dependencies:**
Make sure to install the required libraries:
```bash
pip install flask slack_sdk twilio requests
```
