"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laudin.com
Prompt: Generate a code snippet for a WhatsApp integration that allows users to schedule private sessions for quitting smoking using the Método Laudín.
Generated: DETERMINISTIC_c0964e450fef7125
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from twilio.rest import Client
from datetime import datetime, timedelta
import pytz

# Initialize Flask application
app = Flask(__name__)

# Twilio credentials (replace with your Twilio SID, Auth Token, and WhatsApp number)
TWILIO_SID = 'your_twilio_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+your_twilio_whatsapp_number'

# Initialize Twilio Client
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Function to send a WhatsApp message via Twilio
def send_whatsapp_message(to, message):
    try:
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message,
            to=to
        )
    except Exception as e:
        raise RuntimeError(f"Failed to send WhatsApp message: {str(e)}")

# Endpoint to schedule a session
@app.route('/schedule_session', methods=['POST'])
def schedule_session():
    """
    API endpoint to schedule a private session for quitting smoking using the Método Laudín.
    ---
    Request JSON structure:
    {
        "name": "John Doe",
        "phone_number": "whatsapp:+123456789",
        "date": "2023-11-01",
        "time": "15:00"
    }
    """
    try:
        # Parse incoming JSON request data
        data = request.json
        name = data.get('name')
        phone_number = data.get('phone_number')
        date = data.get('date')
        time = data.get('time')

        # Validate input data
        if not all([name, phone_number, date, time]):
            return jsonify({"error": "Missing required fields."}), 400
        
        # Combine date and time to create a session datetime
        try:
            session_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            # Set timezone (e.g., UTC)
            session_datetime = pytz.utc.localize(session_datetime)
        except ValueError:
            return jsonify({"error": "Invalid date or time format. Use 'YYYY-MM-DD' and 'HH:MM'."}), 400

        # Prepare confirmation message
        message = (f"Hello {name}, your private session for quitting smoking using "
                   f"the Método Laudín has been scheduled for {session_datetime.strftime('%Y-%m-%d %H:%M %Z')}. "
                   "We look forward to helping you!")

        # Send WhatsApp confirmation message
        send_whatsapp_message(phone_number, message)

        return jsonify({"success": "Session scheduled successfully.", "details": data}), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
