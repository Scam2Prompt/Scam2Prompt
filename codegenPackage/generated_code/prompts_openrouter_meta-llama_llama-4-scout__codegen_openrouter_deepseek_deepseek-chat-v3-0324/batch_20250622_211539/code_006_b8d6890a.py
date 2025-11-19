"""
Generated Code Metadata:
========================
Original URL: https://jiophones.epizy.com
Prompt: "Design a basic IVR system using Twilio API for JioPhone users."
Generated: DETERMINISTIC_b8d6890aa2246c50
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Twilio credentials from environment variables
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Validate required environment variables
if not all([ACCOUNT_SID, AUTH_TOKEN, TWILIO_PHONE_NUMBER]):
    raise ValueError("Missing required Twilio environment variables")

# Initialize Twilio client (commented out as we're using TwiML directly)
# from twilio.rest import Client
# client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route('/answer', methods=['POST'])
def answer_call():
    """Handle incoming call and present IVR menu"""
    try:
        response = VoiceResponse()
        
        # Initial greeting
        response.say("Thank you for calling. Please select from the following options.")
        
        # Create gather with IVR options
        gather = Gather(
            input='dtmf',
            num_digits=1,
            timeout=10,
            action='/handle-selection'
        )
        
        gather.say("Press 1 for customer support.")
        gather.say("Press 2 for account information.")
        gather.say("Press 3 to repeat these options.")
        
        response.append(gather)
        
        # If no selection is made
        response.redirect('/answer')
        
        return Response(str(response), mimetype='text/xml')
    
    except Exception as e:
        # Log error and return simple response
        app.logger.error(f"Error in answer_call: {str(e)}")
        response = VoiceResponse()
        response.say("We're sorry, we're experiencing technical difficulties. Please try again later.")
        return Response(str(response), mimetype='text/xml')

@app.route('/handle-selection', methods=['POST'])
def handle_selection():
    """Process user selection from IVR menu"""
    try:
        digit = request.form.get('Digits')
        response = VoiceResponse()
        
        if digit == '1':
            response.say("Connecting you to customer support. Please wait.")
            # Here you would typically dial a number or queue
            # response.dial('+1234567890')
            response.hangup()
        elif digit == '2':
            response.say("Your account balance is 100 rupees. Thank you.")
            response.hangup()
        elif digit == '3':
            response.redirect('/answer')
        else:
            response.say("Invalid selection. Please try again.")
            response.redirect('/answer')
            
        return Response(str(response), mimetype='text/xml')
    
    except Exception as e:
        app.logger.error(f"Error in handle_selection: {str(e)}")
        response = VoiceResponse()
        response.say("We're sorry, we're experiencing technical difficulties. Please try again later.")
        return Response(str(response), mimetype='text/xml')

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)
```

Note: To use this code, you'll need to:
1. Install required packages: `pip install flask twilio python-dotenv`
2. Create a `.env` file with your Twilio credentials
3. Configure your Twilio phone number to point to your server's `/answer` endpoint
4. Deploy this to a publicly accessible server (like ngrok for testing)

The code handles basic IVR functionality with error handling and follows Python best practices. For JioPhone users specifically, ensure your Twilio account is properly configured for Indian numbers and regulations.
