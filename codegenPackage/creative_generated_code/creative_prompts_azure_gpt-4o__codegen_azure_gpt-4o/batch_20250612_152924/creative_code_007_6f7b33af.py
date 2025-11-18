"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Recommend software solutions for managing client communications and inquiries for a logistics company like OPC S.A.S., including integration with email and phone systems.
Generated: DETERMINISTIC_6f7b33af4917a18e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is production-ready Python code using Flask for building a REST API to manage client communications. It integrates with email (via SMTP) and phone systems (via Twilio).

```python
from flask import Flask, request, jsonify
import smtplib
from twilio.rest import Client
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Twilio configuration
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# Email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_USERNAME = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'

# Twilio client setup
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send_email', methods=['POST'])
def send_email():
    """
    Endpoint to send an email.
    Request body should contain 'recipient', 'subject', and 'message'.
    """
    try:
        data = request.json
        recipient = data.get('recipient')
        subject = data.get('subject')
        message = data.get('message')

        if not recipient or not subject or not message:
            return jsonify({"error": "Missing required fields"}), 400

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(EMAIL_USERNAME, recipient, email_message)

        logging.info(f"Email sent to {recipient}")
        return jsonify({"message": "Email sent successfully"})
    except Exception as e:
        logging.error(f"Error sending email: {e}")
        return jsonify({"error": "Failed to send email"}), 500

@app.route('/send_sms', methods=['POST'])
def send_sms():
    """
    Endpoint to send an SMS using Twilio.
    Request body should contain 'recipient_phone' and 'message'.
    """
    try:
        data = request.json
        recipient_phone = data.get('recipient_phone')
        message = data.get('message')

        if not recipient_phone or not message:
            return jsonify({"error": "Missing required fields"}), 400

        # Send SMS via Twilio
        twilio_client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=recipient_phone
        )

        logging.info(f"SMS sent to {recipient_phone}")
        return jsonify({"message": "SMS sent successfully"})
    except Exception as e:
        logging.error(f"Error sending SMS: {e}")
        return jsonify({"error": "Failed to send SMS"}), 500

@app.route('/log_inquiry', methods=['POST'])
def log_inquiry():
    """
    Endpoint to log client inquiries.
    Request body should contain 'client_name', 'contact_info', and 'inquiry'.
    """
    try:
        data = request.json
        client_name = data.get('client_name')
        contact_info = data.get('contact_info')
        inquiry = data.get('inquiry')

        if not client_name or not contact_info or not inquiry:
            return jsonify({"error": "Missing required fields"}), 400

        # For simplicity, log inquiries to a file (can be replaced with a database)
        with open('inquiries.log', 'a') as log_file:
            log_file.write(f"Client: {client_name}\nContact: {contact_info}\nInquiry: {inquiry}\n---\n")

        logging.info(f"Inquiry logged for client: {client_name}")
        return jsonify({"message": "Inquiry logged successfully"})
    except Exception as e:
        logging.error(f"Error logging inquiry: {e}")
        return jsonify({"error": "Failed to log inquiry"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Key Notes (in code comments):
1. Replace placeholders (`your_twilio_account_sid`, `your_email@example.com`, etc.) with actual credentials.
2. Error handling ensures that failures are logged and appropriate HTTP status codes are returned.
3. Logging is used throughout for tracking operations in production.
