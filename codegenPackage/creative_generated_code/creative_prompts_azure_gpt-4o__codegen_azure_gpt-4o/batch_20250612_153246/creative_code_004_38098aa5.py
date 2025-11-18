"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aliahtirafia.com
Prompt: Suggest APIs for integrating WhatsApp communication into a home service booking platform, inspired by شركة الاحترافية's "إتصل الآن واتساب" feature.
Generated: DETERMINISTIC_38098aa549ba8ba3
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.twilio.com/.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here's a Python example demonstrating how to integrate WhatsApp communication into a home service booking platform using Twilio's API for WhatsApp:

```python
import os
from twilio.rest import Client
from flask import Flask, request, jsonify

# Flask application for handling WhatsApp communication
app = Flask(__name__)

# Twilio credentials (Set these as environment variables for security)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")  # Example: 'whatsapp:+14155238886'

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send-whatsapp-message', methods=['POST'])
def send_whatsapp_message():
    """
    Endpoint to send WhatsApp messages using Twilio API.
    Expects a JSON payload with 'to' (recipient number) and 'message' (message content).
    """
    try:
        # Parse the request payload
        data = request.get_json()
        to_number = data.get('to')  # Recipient's WhatsApp number (e.g., 'whatsapp:+1234567890')
        message_content = data.get('message')  # Message content to be sent

        # Validate inputs
        if not to_number or not message_content:
            return jsonify({"error": "Both 'to' and 'message' fields are required."}), 400

        # Send WhatsApp message using Twilio API
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            to=to_number,
            body=message_content
        )

        # Respond with message SID (unique identifier) confirming successful delivery
        return jsonify({"message_sid": message.sid, "status": "Message sent successfully."}), 200

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app in debug mode for testing (disable debug in production)
    app.run(debug=True)
```

### Notes:
1. **Twilio Setup**:
   - Sign up for a Twilio account at https://www.twilio.com/.
   - Activate the WhatsApp Sandbox in Twilio for testing or set up a production WhatsApp number.

2. **Environment Variables**:
   - Store sensitive credentials like `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_WHATSAPP_NUMBER` securely as environment variables.

3. **API Testing**:
   - Use tools like Postman or curl to test the `/send-whatsapp-message` endpoint with correct JSON payloads:
     ```
     {
       "to": "whatsapp:+1234567890",
       "message": "Hello, this is a test message from our home service booking platform!"
     }
     ```

4. **Production Deployment**:
   - Deploy using a production-ready server (e.g., Gunicorn or uWSGI) and secure HTTPS with services like AWS, Google Cloud, or Heroku.
