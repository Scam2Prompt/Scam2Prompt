"""
Generated Code Metadata:
========================
Original URL: https://www.dessc.de
Prompt: Write a Python script that facilitates secure communication between a client and an IT support team using WhatsApp, based on DESSC's remote support model.
Generated: DETERMINISTIC_f25b0d8ac1eae553
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    """
    Handle incoming WhatsApp messages from clients.
    Responds to the client and forwards the message to the IT support team.
    """
    try:
        # Get the incoming message details
        incoming_msg = request.values.get('Body', '').strip()
        from_number = request.values.get('From', '')

        logging.info(f"Received message from {from_number}: {incoming_msg}")

        # Forward the message to the IT support team
        support_team_number = os.getenv('SUPPORT_TEAM_NUMBER')
        twilio_client.messages.create(
            body=f"Message from {from_number}: {incoming_msg}",
            from_=TWILIO_PHONE_NUMBER,
            to=support_team_number
        )

        # Create a response for the client
        response = MessagingResponse()
        response.message("Your message has been received by our IT support team. We will get back to you shortly.")
        return str(response)

    except Exception as e:
        logging.error(f"Error processing message: {e}")
        return jsonify({"error": "An error occurred while processing your message."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=5000)
```

### Environment Variables Required:
- `TWILIO_ACCOUNT_SID`: Your Twilio account SID.
- `TWILIO_AUTH_TOKEN`: Your Twilio auth token.
- `TWILIO_PHONE_NUMBER`: Your Twilio WhatsApp-enabled phone number.
- `SUPPORT_TEAM_NUMBER`: The phone number of the IT support team to receive messages.
