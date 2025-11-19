"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixels-dashboard.pages.dev
Prompt: Generate code to send a login code via SMS for a web application, inspired by the user login process on Pixels.
Generated: DETERMINISTIC_2a3c494ee2044180
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import random
import smtplib
from twilio.rest import Client
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Load environment variables for sensitive information
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Twilio client setup
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def generate_login_code(length=6):
    """
    Generate a random numeric login code of a specified length.
    
    Args:
        length (int): The length of the code to generate.
    
    Returns:
        str: A randomly generated numeric code.
    """
    return ''.join(random.choices('0123456789', k=length))

def send_sms(to_number, message):
    """
    Send an SMS message using Twilio's API.
    
    Args:
        to_number (str): The recipient's phone number.
        message (str): The message to send.
    
    Raises:
        Exception: If the SMS fails to send for any reason.
    """
    try:
        message_response = twilio_client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )
        return message_response.sid
    except Exception as e:
        # Log the exception appropriately in a real application
        raise RuntimeError(f"Failed to send SMS: {str(e)}")

@app.route('/send-login-code', methods=['POST'])
def send_login_code():
    """
    Endpoint to send a login code via SMS to the specified phone number.
    
    Request JSON structure:
    {
        "phone_number": "recipient_phone_number"
    }
    
    Returns:
        JSON response with the status of the SMS sending process.
    """
    data = request.get_json()
    
    if 'phone_number' not in data:
        return jsonify({'error': 'Phone number is required.'}), 400
    
    phone_number = data['phone_number']
    login_code = generate_login_code()
    message = f"Your login code is: {login_code}"

    try:
        send_sms(phone_number, message)
        return jsonify({'message': 'Login code sent successfully!'}), 200
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

Make sure to set the environment variables `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` before running this code.
