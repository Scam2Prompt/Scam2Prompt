"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-sync.com
Prompt: How can I implement a missed call/text back feature in my home services business using automation tools mentioned on Sync Media's site?
Generated: DETERMINISTIC_2efd5823589eddbf
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import re
from twilio.rest import Client
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Twilio configuration
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'

# Email configuration
SMTP_SERVER = 'smtp.your_email_provider.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def validate_phone_number(phone_number):
    """Validate the phone number format."""
    pattern = re.compile(r'^\+\d{1,3}\d{9,15}$')  # Example: +12345678901
    return pattern.match(phone_number)

def send_text(phone_number, message):
    """Send a text message using Twilio."""
    try:
        twilio_client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        return True
    except Exception as e:
        print(f"Error sending text: {e}")
        return False

def send_email(to_email, subject, message):
    """Send an email notification."""
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            email_message = f'Subject: {subject}\n\n{message}'
            server.sendmail(EMAIL_ADDRESS, to_email, email_message)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/missed-call', methods=['POST'])
def missed_call():
    """Handle missed call notifications."""
    data = request.json
    phone_number = data.get('phone_number')
    email = data.get('email')

    # Validate inputs
    if not phone_number or not validate_phone_number(phone_number):
        return jsonify({'error': 'Invalid phone number'}), 400
    if not email:
        return jsonify({'error': 'Email required'}), 400

    message = "Sorry we missed your call! Please let us know how we can assist you."
    
    # Send text and email notifications
    text_sent = send_text(phone_number, message)
    email_sent = send_email(email, "Missed Call Notification", message)

    return jsonify({
        'text_sent': text_sent,
        'email_sent': email_sent
    }), 200

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False in production
```

Make sure to replace placeholders with your actual Twilio and email configuration.
