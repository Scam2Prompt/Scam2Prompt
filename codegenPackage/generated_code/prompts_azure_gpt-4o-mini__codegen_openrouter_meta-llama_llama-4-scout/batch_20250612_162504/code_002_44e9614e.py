"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Write a Python script that automates sending cash offer emails to users who submit their property information through a form, inspired by the process described on Metis Assets' site.
Generated: DETERMINISTIC_44e9614e15b716be
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Script to automate sending cash offer emails to users who submit their property information.

Inspired by the process described on Metis Assets' site.
"""

import os
import logging
from logging.handlers import RotatingFileHandler
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from flask import Flask, request, jsonify

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a rotating file handler
file_handler = RotatingFileHandler('app.log', maxBytes=1024*1024*10, backupCount=10)
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and attach it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

app = Flask(__name__)

# Load email configuration from environment variables
SMTP_SERVER = os.environ.get('SMTP_SERVER')
SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
FROM_EMAIL = os.environ.get('FROM_EMAIL')
PASSWORD = os.environ.get('PASSWORD')

# Load email template from file
with open('email_template.html', 'r') as f:
    email_template = f.read()

@app.route('/submit-property', methods=['POST'])
def submit_property():
    try:
        data = request.get_json()
        if not data:
            logger.error('Invalid request data')
            return jsonify({'error': 'Invalid request data'}), 400

        # Validate required fields
        required_fields = ['name', 'email', 'property_address', 'property_type']
        if not all(field in data for field in required_fields):
            logger.error('Missing required fields')
            return jsonify({'error': 'Missing required fields'}), 400

        # Send cash offer email
        send_cash_offer_email(data)

        logger.info('Cash offer email sent successfully')
        return jsonify({'message': 'Cash offer email sent successfully'}), 200

    except Exception as e:
        logger.error('Error sending cash offer email: %s', str(e))
        return jsonify({'error': 'Error sending cash offer email'}), 500

def send_cash_offer_email(data):
    try:
        # Create a text version of the email
        text_message = f"""
        Dear {data['name']},

        Thank you for submitting your property information. We are excited to present you with a cash offer for your {data['property_type']} located at {data['property_address']}.

        Please find the details of our offer below:

        [Insert offer details]

        If you are interested in accepting our offer, please reply to this email or give us a call at [insert phone number].

        Best regards,
        [Your Name]
        """

        # Create an HTML version of the email using the template
        html_message = email_template.format(
            name=data['name'],
            property_address=data['property_address'],
            property_type=data['property_type']
        )

        # Set up the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, PASSWORD)

        # Create the email message
        message = MIMEMultipart('alternative')
        message['From'] = FROM_EMAIL
        message['To'] = data['email']
        message['Subject'] = 'Cash Offer for Your Property'

        # Attach the text and HTML versions of the email
        message.attach(MIMEText(text_message, 'plain'))
        message.attach(MIMEText(html_message, 'html'))

        # Send the email
        server.sendmail(FROM_EMAIL, data['email'], message.as_string())
        server.quit()

    except smtplib.SMTPException as e:
        logger.error('Error sending email: %s', str(e))

if __name__ == '__main__':
    app.run(debug=True)
```
