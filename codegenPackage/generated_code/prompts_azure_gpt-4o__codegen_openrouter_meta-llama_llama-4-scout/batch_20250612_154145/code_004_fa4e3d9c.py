"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Write a script to send automated travel advisories and updates to clients via email and WhatsApp, similar to the communication approach mentioned by KK Travel Solutions.
Generated: DETERMINISTIC_fa4e3d9cb7d37a2b
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Travel Advisory Script**
=========================

### Prerequisites

* Python 3.8+
* `smtplib` and `email` libraries for email functionality
* `twilio` library for WhatsApp functionality

### Script
```python
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client

# Configuration
class Config:
    """Configuration class for email and WhatsApp settings"""
    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
    EMAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

# Email service
class EmailService:
    """Email service class for sending emails"""
    def __init__(self, config):
        self.config = config

    def send_email(self, recipient, subject, body):
        """Send an email to a recipient"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config.EMAIL_USERNAME
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(self.config.EMAIL_HOST, self.config.EMAIL_PORT)
            server.starttls()
            server.login(self.config.EMAIL_USERNAME, self.config.EMAIL_PASSWORD)
            text = msg.as_string()
            server.sendmail(self.config.EMAIL_USERNAME, recipient, text)
            server.quit()
            print(f"Email sent to {recipient}")
        except Exception as e:
            print(f"Error sending email: {str(e)}")

# WhatsApp service
class WhatsAppService:
    """WhatsApp service class for sending WhatsApp messages"""
    def __init__(self, config):
        self.config = config
        self.client = Client(self.config.TWILIO_ACCOUNT_SID, self.config.TWILIO_AUTH_TOKEN)

    def send_whatsapp(self, recipient, message):
        """Send a WhatsApp message to a recipient"""
        try:
            message = self.client.messages.create(
                body=message,
                from_=self.config.TWILIO_PHONE_NUMBER,
                to=recipient
            )
            print(f"WhatsApp sent to {recipient}")
        except Exception as e:
            print(f"Error sending WhatsApp: {str(e)}")

# Travel advisory service
class TravelAdvisoryService:
    """Travel advisory service class for sending travel advisories"""
    def __init__(self, email_service, whatsapp_service):
        self.email_service = email_service
        self.whatsapp_service = whatsapp_service

    def send_travel_advisory(self, client, advisory):
        """Send a travel advisory to a client via email and WhatsApp"""
        try:
            # Send email
            subject = "Travel Advisory Update"
            body = advisory
            self.email_service.send_email(client['email'], subject, body)

            # Send WhatsApp
            message = advisory
            self.whatsapp_service.send_whatsapp(client['whatsapp'], message)
        except Exception as e:
            print(f"Error sending travel advisory: {str(e)}")

# Main function
def main():
    config = Config()
    email_service = EmailService(config)
    whatsapp_service = WhatsAppService(config)
    travel_advisory_service = TravelAdvisoryService(email_service, whatsapp_service)

    # Example clients
    clients = [
        {'email': 'client1@example.com', 'whatsapp': '+1234567890'},
        {'email': 'client2@example.com', 'whatsapp': '+9876543210'}
    ]

    # Example travel advisory
    advisory = "Travel advisory: Please be aware of the latest travel restrictions."

    for client in clients:
        travel_advisory_service.send_travel_advisory(client, advisory)

if __name__ == "__main__":
    main()
```
### Environment Variables

* `EMAIL_HOST`
* `EMAIL_PORT`
* `EMAIL_USERNAME`
* `EMAIL_PASSWORD`
* `TWILIO_ACCOUNT_SID`
* `TWILIO_AUTH_TOKEN`
* `TWILIO_PHONE_NUMBER`

### Usage

1. Set environment variables for email and WhatsApp settings.
2. Install required libraries: `pip install twilio`
3. Run the script: `python travel_advisory_script.py`
