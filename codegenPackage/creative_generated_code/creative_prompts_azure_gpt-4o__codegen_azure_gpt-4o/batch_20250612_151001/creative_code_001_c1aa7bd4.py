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

Below is a production-ready Python example using the Twilio API for integrating SMS functionality. Twilio is a popular and reliable choice for sending and receiving SMS in web applications.

```python
import os
from twilio.rest import Client
from flask import Flask, request, jsonify

# Flask app setup
app = Flask(__name__)

# Twilio configuration - Replace with your Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")  # Set your account SID in environment variables
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")    # Set your auth token in environment variables
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")  # Your Twilio phone number

# Ensure credentials are set
if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_PHONE_NUMBER:
    raise EnvironmentError("Twilio credentials not properly set in environment variables.")

# Twilio client initialization
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    """
    Endpoint to send an SMS to a customer for inquiries or quotes.
    Expects JSON input with 'to' and 'message' parameters:
    {
        "to": "+1234567890",
        "message": "Your custom inquiry message."
    }
    """
    try:
        # Parse JSON request
        data = request.get_json()
        recipient_number = data.get('to')
        message_body = data.get('message')

        # Validate input
        if not recipient_number or not message_body:
            return jsonify({"error": "Missing 'to' or 'message' parameter"}), 400

        # Send SMS via Twilio
        message = twilio_client.messages.create(
            to=recipient_number, 
            from_=TWILIO_PHONE_NUMBER, 
            body=message_body
        )

        # Return successful response
        return jsonify({
            "message": "SMS sent successfully.",
            "twilio_sid": message.sid,
            "recipient": recipient_number
        }), 200

    except Exception as e:
        # Handle errors and log them properly
        return jsonify({"error": str(e)}), 500

@app.route('/receive_sms', methods=['POST'])
def receive_sms():
    """
    Endpoint to handle incoming SMS messages. Twilio will POST data here for incoming messages.
    """
    try:
        # Extract data from Twilio's POST request
        sender = request.form.get('From')
        body = request.form.get('Body')

        # Log the received SMS (or process it as needed)
        print(f"Received SMS from {sender}: {body}")

        # Respond with Ack message (optional)
        return jsonify({"message": "SMS received successfully."}), 200

    except Exception as e:
        # Handle errors and log them properly
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run Flask application
    app.run(debug=True)
```

### Deployment Notes:
1. Install necessary dependencies via pip:
   ```bash
   pip install twilio flask
   ```
2. Set environment variables for Twilio credentials:
   ```bash
   export TWILIO_ACCOUNT_SID='your_account_sid'
   export TWILIO_AUTH_TOKEN='your_auth_token'
   export TWILIO_PHONE_NUMBER='your_twilio_phone_number'
   ```
3. Ensure the Flask server is reachable publicly for Twilio to send incoming SMS data to the `/receive_sms` endpoint. Use tools like Ngrok during local development.
