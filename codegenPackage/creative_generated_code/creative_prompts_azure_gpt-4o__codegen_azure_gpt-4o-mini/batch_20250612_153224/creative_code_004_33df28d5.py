"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Write code to integrate WhatsApp messaging for client communication in a legal firm, referencing the contact methods provided by the Complexo de Advocacia Adriano Geoffrey.
Generated: DETERMINISTIC_33df28d552f0ad79
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Initialize Flask app
app = Flask(__name__)

# Load environment variables for Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send-message', methods=['POST'])
def send_message():
    """
    Send a WhatsApp message using Twilio API.

    Request JSON should contain:
    {
        "to": "whatsapp:+1234567890",
        "message": "Your message here"
    }
    Returns a JSON response indicating success or failure.
    """
    data = request.get_json()

    # Validate incoming JSON payload
    if not data or 'to' not in data or 'message' not in data:
        return jsonify({"error": "Invalid request. Please provide 'to' and 'message'."}), 400

    to = data['to']
    message = data['message']

    try:
        # Send message via Twilio WhatsApp
        message_response = twilio_client.messages.create(
            body=message,
            from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
            to=to
        )
        return jsonify({"success": True, "sid": message_response.sid}), 200
    except TwilioRestException as e:
        # Handle specific Twilio errors
        return jsonify({"error": str(e)}, 500)
    except Exception as e:
        # Handle any other exceptions
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    # Ensure the app runs only if this script is executed directly
    app.run(debug=True)
```

**Note:** Make sure to set the environment variables `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` with the appropriate values before running the application. Install the required libraries using `pip install Flask twilio`.
