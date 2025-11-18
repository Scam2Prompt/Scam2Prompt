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
import os
import sys
import json
import logging
from flask import Flask, request, jsonify
from twilio.rest import Client
from microsoftteams import TeamsAPI  # Hypothetical library for Teams API integration

# Initialize Flask app for API
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load configuration from environment variables or a config file
CONFIG = {
    "TWILIO_ACCOUNT_SID": os.getenv("TWILIO_ACCOUNT_SID"),
    "TWILIO_AUTH_TOKEN": os.getenv("TWILIO_AUTH_TOKEN"),
    "TWILIO_PHONE_NUMBER": os.getenv("TWILIO_PHONE_NUMBER"),
    "TEAMS_API_KEY": os.getenv("TEAMS_API_KEY"),  # Hypothetical API key for Teams
    "IT_SUPPORT_PHONE": os.getenv("IT_SUPPORT_PHONE"),  # Phone number for IT support
    "IT_SUPPORT_TEAMS_ID": os.getenv("IT_SUPPORT_TEAMS_ID")  # Teams user ID for IT support
}

# Validate configuration
if not all(CONFIG.values()):
    logger.error("Missing required configuration. Please set all necessary environment variables.")
    sys.exit(1)

# Twilio client initialization
twilio_client = Client(CONFIG["TWILIO_ACCOUNT_SID"], CONFIG["TWILIO_AUTH_TOKEN"])

# Teams API initialization (hypothetical library)
teams_api = TeamsAPI(CONFIG["TEAMS_API_KEY"])

@app.route('/send_support_message', methods=['POST'])
def send_support_message():
    """
    Endpoint to send a support message to IT support via WhatsApp or Teams.
    """
    try:
        # Parse incoming JSON data
        data = request.json
        if "platform" not in data or "message" not in data:
            return jsonify({"error": "Invalid request. 'platform' and 'message' are required."}), 400

        platform = data["platform"].lower()
        message = data["message"]

        # Send message via the requested platform
        if platform == "whatsapp":
            send_whatsapp_message(message)
        elif platform == "teams":
            send_teams_message(message)
        else:
            return jsonify({"error": f"Unsupported platform: {platform}"}), 400

        return jsonify({"status": "success", "message": f"Support message sent via {platform}."}), 200

    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return jsonify({"error": "An internal error occurred."}), 500


def send_whatsapp_message(message):
    """
    Sends a WhatsApp message to IT support via Twilio API.
    """
    try:
        twilio_client.messages.create(
            body=message,
            from_=f'whatsapp:{CONFIG["TWILIO_PHONE_NUMBER"]}',
            to=f'whatsapp:{CONFIG["IT_SUPPORT_PHONE"]}'
        )
        logger.info("WhatsApp message sent successfully.")
    except Exception as e:
        logger.error(f"Failed to send WhatsApp message: {e}")
        raise


def send_teams_message(message):
    """
    Sends a Teams message to IT support via Teams API.
    """
    try:
        teams_api.send_message(
            recipient_id=CONFIG["IT_SUPPORT_TEAMS_ID"],
            message=message
        )
        logger.info("Teams message sent successfully.")
    except Exception as e:
        logger.error(f"Failed to send Teams message: {e}")
        raise


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### Notes:
- Replace `microsoftteams` with the actual library/API for Teams integration if available.
- Ensure that you set the required environment variables before running the script.
- This code assumes a hypothetical Teams API. You may need to adapt it to the actual Microsoft Teams API or SDK.
