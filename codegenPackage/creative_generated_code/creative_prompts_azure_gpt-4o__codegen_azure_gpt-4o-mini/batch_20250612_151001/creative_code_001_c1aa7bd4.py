"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Recommend a library or API for integrating SMS functionality into a web application to allow customers to text for quotes or inquiries, as described on the Junk In The Box ATL website.
Generated: DETERMINISTIC_c1aa7bd49d98b4bf
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Initialize the Flask application
app = Flask(__name__)

# Twilio configuration - replace with your own credentials
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# Create a Twilio client instance
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    """Endpoint to send an SMS message."""
    # Get data from the request
    data = request.get_json()

    # Validate request data
    phone_number = data.get('phone_number')
    message_body = data.get('message_body')

    if not phone_number or not message_body:
        return jsonify({'error': 'Phone number and message body are required.'}), 400

    try:
        # Send an SMS using Twilio
        message = twilio_client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        # Return success response
        return jsonify({'message': 'SMS sent successfully!', 'message_sid': message.sid}), 200

    except TwilioRestException as e:
        # Handle Twilio exceptions
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle general exceptions
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
