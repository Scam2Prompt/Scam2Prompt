"""
Generated Code Metadata:
========================
Original URL: https://invictacobrancas.com.br
Prompt: Suggest tools or frameworks to build a mobile app for debt collection management, including features like SMS FLASH and WhatsApp integration, as offered by Invicta Cobranças.
Generated: DETERMINISTIC_06af1fefa0d66220
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from twilio.rest import Client
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Twilio configuration for SMS and WhatsApp
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
WHATSAPP_NUMBER = 'whatsapp:+your_whatsapp_number'

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    """
    Send an SMS message to a specified phone number.
    Expects JSON payload with 'to' and 'message' fields.
    """
    try:
        data = request.get_json()
        to_number = data['to']
        message = data['message']

        # Send SMS using Twilio
        message_response = twilio_client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )

        return jsonify({'status': 'success', 'message_sid': message_response.sid}), 200

    except KeyError as e:
        logging.error(f'Missing key: {e}')
        return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400
    except Exception as e:
        logging.error(f'Error sending SMS: {e}')
        return jsonify({'status': 'error', 'message': 'Failed to send SMS'}), 500

@app.route('/send_whatsapp', methods=['POST'])
def send_whatsapp():
    """
    Send a WhatsApp message to a specified number.
    Expects JSON payload with 'to' and 'message' fields.
    """
    try:
        data = request.get_json()
        to_number = data['to']
        message = data['message']

        # Send WhatsApp message using Twilio
        message_response = twilio_client.messages.create(
            body=message,
            from_=WHATSAPP_NUMBER,
            to=f'whatsapp:{to_number}'
        )

        return jsonify({'status': 'success', 'message_sid': message_response.sid}), 200

    except KeyError as e:
        logging.error(f'Missing key: {e}')
        return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400
    except Exception as e:
        logging.error(f'Error sending WhatsApp message: {e}')
        return jsonify({'status': 'error', 'message': 'Failed to send WhatsApp message'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Requirements:
- Install Flask and Twilio SDK:
```bash
pip install Flask twilio
```

### Note:
- Replace placeholders for `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`, and `WHATSAPP_NUMBER` with actual values from your Twilio account.
- This code provides a simple API for sending SMS and WhatsApp messages, which can be integrated into a mobile app for debt collection management.
