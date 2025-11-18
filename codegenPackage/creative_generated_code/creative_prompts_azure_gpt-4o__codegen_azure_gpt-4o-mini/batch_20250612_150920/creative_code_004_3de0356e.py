"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-sync.com
Prompt: Create a script for automating missed call/text back functionality for a business, referencing Sync Media's approach to client communication.
Generated: DETERMINISTIC_3de0356ea66b5d35
Batch ID: 20250612_150920
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
from datetime import datetime
from twilio.rest import Client
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Error handling class
class MissedCallError(Exception):
    pass

# Function to send SMS
def send_sms(to, body):
    """Send an SMS message using Twilio."""
    try:
        message = client.messages.create(
            body=body,
            from_=TWILIO_PHONE_NUMBER,
            to=to
        )
        logging.info(f"Sent message to {to}: {body}")
    except Exception as e:
        logging.error(f"Failed to send message to {to}: {str(e)}")
        raise MissedCallError(f"Could not send SMS to {to}")

# Route to handle missed call notifications
@app.route('/missed_call', methods=['POST'])
def missed_call():
    """Receive missed call notifications and trigger a callback."""
    data = request.json
    if not data or 'caller' not in data:
        return jsonify({"error": "Invalid request"}), 400

    caller_number = data['caller']
    callback_message = f"Sorry we missed your call at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}. We'll get back to you shortly."

    try:
        send_sms(caller_number, callback_message)
        return jsonify({"status": "success", "message": "Callback SMS sent"}), 200
    except MissedCallError as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)
```

Make sure to set the environment variables `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` before running the application.
