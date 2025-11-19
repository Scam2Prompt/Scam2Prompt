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
import os
from flask import Flask, request, jsonify
from twilio.rest import Client
from datetime import datetime
import pytz

app = Flask(__name__)

# Twilio configuration
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_WHATSAPP_NUMBER = os.environ['TWILIO_WHATSAPP_NUMBER']
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Schedule structure to hold user sessions
scheduled_sessions = {}

@app.route('/schedule', methods=['POST'])
def schedule_session():
    """
    Schedule a private session for quitting smoking using Método Laudín.
    Expects a JSON payload with 'user_phone' and 'session_time'.
    """
    try:
        data = request.json
        user_phone = data['user_phone']
        session_time_str = data['session_time']
        
        # Parse session time and check if it's in the future
        session_time = datetime.strptime(session_time_str, '%Y-%m-%d %H:%M')
        if session_time < datetime.now(pytz.utc):
            return jsonify({"error": "Session time must be in the future."}), 400
        
        # Store the session in the scheduled sessions dictionary
        scheduled_sessions[user_phone] = session_time
        send_confirmation(user_phone, session_time)
        
        return jsonify({"message": "Session scheduled successfully."}), 200
    except KeyError as e:
        # Handle missing key in JSON payload
        return jsonify({"error": f"Missing parameter: {str(e)}"}), 400
    except ValueError:
        # Handle invalid date format
        return jsonify({"error": "Invalid session time format. Use 'YYYY-MM-DD HH:MM'."}), 400
    except Exception as e:
        # General error handling
        return jsonify({"error": str(e)}), 500

def send_confirmation(user_phone, session_time):
    """
    Send a confirmation message to the user via WhatsApp.
    
    :param user_phone: The phone number of the user in the format 'whatsapp:+<country_code><number>'
    :param session_time: The scheduled session time
    """
    message_body = (f"Your session for quitting smoking using Método Laudín is scheduled for "
                    f"{session_time.strftime('%Y-%m-%d %H:%M')} UTC.")
    
    try:
        # Send the message via Twilio
        client.messages.create(
            body=message_body,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=user_phone
        )
    except Exception as e:
        # Log the error if sending fails
        print(f"Failed to send message: {str(e)}")

if __name__ == '__main__':
    # Run the application on the default Flask port
    app.run(debug=True)
```

Make sure to set the necessary environment variables for Twilio credentials before running this code.
