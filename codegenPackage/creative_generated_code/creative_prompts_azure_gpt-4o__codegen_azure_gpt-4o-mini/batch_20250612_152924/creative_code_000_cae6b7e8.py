"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivadainfotech.com
Prompt: Write Python code to automate lead generation for hospitals using the SKLS method described by Vivada Infotech, including email and WhatsApp marketing integration.
Generated: DETERMINISTIC_cae6b7e881b000b8
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import json
import logging
from twilio.rest import Client

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LeadGenerator:
    def __init__(self, email_config, sms_config):
        self.email_config = email_config
        self.sms_config = sms_config

    def send_email(self, recipient_email, subject, body):
        """Send an email to the specified recipient."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_config['sender_email']
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                server.starttls()  # Enable security
                server.login(self.email_config['sender_email'], self.email_config['password'])
                server.send_message(msg)
                logging.info(f'Email sent to {recipient_email}')
        except Exception as e:
            logging.error(f'Failed to send email to {recipient_email}: {e}')

    def send_whatsapp_message(self, recipient_number, message):
        """Send a WhatsApp message to the specified recipient."""
        try:
            client = Client(self.sms_config['account_sid'], self.sms_config['auth_token'])
            message = client.messages.create(
                body=message,
                from_=self.sms_config['from_number'],
                to=f"whatsapp:{recipient_number}"
            )
            logging.info(f'WhatsApp message sent to {recipient_number}')
        except Exception as e:
            logging.error(f'Failed to send WhatsApp message to {recipient_number}: {e}')

    def generate_leads(self, leads_data):
        """Generate leads and send marketing messages."""
        for lead in leads_data:
            email = lead.get('email')
            phone = lead.get('phone')
            name = lead.get('name')
            if email:
                self.send_email(email, "Welcome to Our Hospital", f"Dear {name}, we are glad to have you.")
            if phone:
                self.send_whatsapp_message(phone, f"Hello {name}, welcome to our hospital services.")

if __name__ == "__main__":
    # Configuration for email and SMS
    email_config = {
        'sender_email': 'your_email@example.com',
        'password': 'your_password',
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587
    }

    sms_config = {
        'account_sid': 'your_twilio_account_sid',
        'auth_token': 'your_twilio_auth_token',
        'from_number': 'your_twilio_number'
    }

    # Sample leads data
    leads_data = [
        {'name': 'John Doe', 'email': 'john@example.com', 'phone': '+1234567890'},
        {'name': 'Jane Smith', 'email': 'jane@example.com', 'phone': '+0987654321'}
    ]

    # Initialize the lead generator
    lead_generator = LeadGenerator(email_config, sms_config)
    
    # Generate leads
    lead_generator.generate_leads(leads_data)
```

Make sure to replace placeholder values in the `email_config` and `sms_config` dictionaries with your actual credentials and configurations before running the code.
