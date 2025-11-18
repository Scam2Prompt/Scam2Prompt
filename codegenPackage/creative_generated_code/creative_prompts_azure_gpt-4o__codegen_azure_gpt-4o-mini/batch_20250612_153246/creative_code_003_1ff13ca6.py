"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dessc.de
Prompt: Develop a script that enables remote IT support via Teams or WhatsApp, inspired by the remote assistance solutions offered by DESSC.
Generated: DETERMINISTIC_1ff13ca6f9dccbd1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import logging
import requests
from flask import Flask, request, jsonify

# Set up logging for the application
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Flask application
app = Flask(__name__)

# Configuration for Teams and WhatsApp
TEAMS_WEBHOOK_URL = 'YOUR_TEAMS_WEBHOOK_URL'
WHATSAPP_API_URL = 'YOUR_WHATSAPP_API_URL'
WHATSAPP_ACCESS_TOKEN = 'YOUR_WHATSAPP_ACCESS_TOKEN'

@app.route('/request_support', methods=['POST'])
def request_support():
    """
    Endpoint to handle support requests.
    Expects a JSON payload with 'service', 'user_id', and 'message'.
    """
    try:
        data = request.get_json()
        
        if not data or 'service' not in data or 'user_id' not in data or 'message' not in data:
            logger.error("Invalid request: %s", data)
            return jsonify({"error": "Invalid request data"}), 400
        
        service = data['service']
        user_id = data['user_id']
        message = data['message']
        
        if service not in ['teams', 'whatsapp']:
            logger.error("Unsupported service: %s", service)
            return jsonify({"error": "Unsupported service"}), 400

        # Call the appropriate function based on the service
        if service == 'teams':
            send_teams_message(user_id, message)
        elif service == 'whatsapp':
            send_whatsapp_message(user_id, message)

        return jsonify({"success": "Support request sent"}), 200

    except Exception as e:
        logger.exception("Error processing support request: %s", e)
        return jsonify({"error": "Internal server error"}), 500


def send_teams_message(user_id, message):
    """
    Send a message to Microsoft Teams using a webhook.
    
    :param user_id: The user ID to notify
    :param message: The message to send
    """
    payload = {
        "text": f"Support request from {user_id}: {message}"
    }
    
    try:
        response = requests.post(TEAMS_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        logger.info("Message sent to Teams: %s", response.text)
    except requests.exceptions.RequestException as e:
        logger.error("Error sending message to Teams: %s", e)
        raise


def send_whatsapp_message(user_id, message):
    """
    Send a message to WhatsApp using the WhatsApp API.
    
    :param user_id: The user ID to notify
    :param message: The message to send
    """
    payload = {
        "to": user_id,
        "message": message
    }

    headers = {
        "Authorization": f"Bearer {WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(WHATSAPP_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        logger.info("Message sent to WhatsApp: %s", response.text)
    except requests.exceptions.RequestException as e:
        logger.error("Error sending message to WhatsApp: %s", e)
        raise


if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logger.exception("Failed to start the server: %s", e)
        sys.exit(1)
```

In this script:
- The Flask framework is used to create a web service to handle support requests.
- The service can send notifications via Microsoft Teams or WhatsApp based on the request.
- Proper error handling and logging are implemented throughout the code. 
- Replace the placeholder URLs with actual webhook and API URLs for Teams and WhatsApp.
