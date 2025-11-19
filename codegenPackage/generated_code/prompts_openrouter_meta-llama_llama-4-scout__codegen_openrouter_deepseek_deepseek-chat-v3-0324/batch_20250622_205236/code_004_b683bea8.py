"""
Generated Code Metadata:
========================
Original URL: https://dfcloudpbx.com
Prompt: Generate code to implement a digital receptionist using a Cloud PBX system like PREMHost CloudPBX.
Generated: DETERMINISTIC_b683bea819cc8b7a
Batch ID: 20250622_205236
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
from flask import Flask, request, jsonify, Response
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Twilio credentials from environment
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Department extensions mapping
DEPARTMENT_EXTENSIONS = {
    '1': {'name': 'Sales', 'number': '+12025551234'},
    '2': {'name': 'Support', 'number': '+12025554321'},
    '3': {'name': 'Billing', 'number': '+12025556789'}
}

@app.route('/voice', methods=['GET', 'POST'])
def voice():
    """Handle incoming calls and present menu options."""
    try:
        response = VoiceResponse()
        
        # Initial greeting
        gather = Gather(
            num_digits=1,
            action='/handle-selection',
            method='POST',
            timeout=10
        )
        gather.say(
            'Thank you for calling. Press 1 for Sales, 2 for Support, 3 for Billing.',
            voice='woman',
            language='en-US'
        )
        response.append(gather)
        
        # If no selection is made, repeat the message
        response.say(
            'We didn\'t receive your selection. Goodbye!',
            voice='woman',
            language='en-US'
        )
        response.hangup()
        
        return Response(str(response), mimetype='text/xml')
    
    except Exception as e:
        logger.error(f"Error in voice handler: {str(e)}")
        response = VoiceResponse()
        response.say(
            'Sorry, we encountered an error. Please try again later.',
            voice='woman',
            language='en-US'
        )
        response.hangup()
        return Response(str(response), mimetype='text/xml')

@app.route('/handle-selection', methods=['POST'])
def handle_selection():
    """Route the call based on user input."""
    try:
        digit = request.form.get('Digits', None)
        response = VoiceResponse()
        
        if not digit or digit not in DEPARTMENT_EXTENSIONS:
            response.say(
                'Invalid selection. Please try again.',
                voice='woman',
                language='en-US'
            )
            response.redirect('/voice')
            return Response(str(response), mimetype='text/xml')
        
        department = DEPARTMENT_EXTENSIONS[digit]
        response.say(
            f'Connecting you to {department["name"]}.',
            voice='woman',
            language='en-US'
        )
        response.dial(department['number'])
        
        return Response(str(response), mimetype='text/xml')
    
    except Exception as e:
        logger.error(f"Error in selection handler: {str(e)}")
        response = VoiceResponse()
        response.say(
            'Sorry, we encountered an error. Please try again later.',
            voice='woman',
            language='en-US'
        )
        response.hangup()
        return Response(str(response), mimetype='text/xml')

@app.route('/status-callback', methods=['POST'])
def status_callback():
    """Handle call status updates."""
    try:
        call_sid = request.form.get('CallSid')
        call_status = request.form.get('CallStatus')
        
        logger.info(f"Call {call_sid} status: {call_status}")
        
        return jsonify({'status': 'success'}), 200
    
    except Exception as e:
        logger.error(f"Error in status callback: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```
