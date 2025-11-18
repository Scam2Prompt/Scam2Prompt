"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dessc.de
Prompt: Write a Python script that facilitates secure communication between a client and an IT support team using WhatsApp, based on DESSC's remote support model.
Generated: DETERMINISTIC_f25b0d8ac1eae553
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
import logging
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.exceptions import TwilioRestException

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send_message', methods=['POST'])
def send_message():
    """
    Sends a message to the IT support team via WhatsApp.
    Expects JSON input with the keys 'to' and 'message'.
    """
    data = request.get_json()

    if not data or 'to' not in data or 'message' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    to_number = data['to']
    message_body = data['message']

    try:
        # Sending message using Twilio API
        message = twilio_client.messages.create(
            body=message_body,
            from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
            to=f'whatsapp:{to_number}'
        )
        logger.info(f'Message sent: {message.sid}')
        return jsonify({'message_sid': message.sid}), 200

    except TwilioRestException as e:
        logger.error(f'Error sending message: {e}')
        return jsonify({'error': 'Failed to send message'}), 500

@app.route('/receive_messages', methods=['POST'])
def receive_messages():
    """
    Receives and processes incoming WhatsApp messages.
    This endpoint should be configured as a webhook in Twilio.
    """
    data = request.form
    from_number = data.get('From')
    message_body = data.get('Body')

    if not from_number or not message_body:
        logger.warning('Received empty message.')
        return '', 200  # Acknowledge receipt of the message

    # Here you can add logic to process the incoming message
    logger.info(f'Received message from {from_number}: {message_body}')

    return '', 200  # Acknowledge receipt of the message

if __name__ == '__main__':
    # Running the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Make sure to set the environment variables `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` before running the script. This code provides endpoints for sending and receiving messages via WhatsApp using Twilio.
