"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kktravelsolutions.co.tz
Prompt: Write a script to send automated travel advisories and updates to clients via email and WhatsApp, similar to the communication approach mentioned by KK Travel Solutions.
Generated: DETERMINISTIC_fa4e3d9cb7d37a2b
Batch ID: 20250612_154145
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
from twilio.rest import Client
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Email Configuration
EMAIL_HOST = 'smtp.your-email-provider.com'  # SMTP server address
EMAIL_PORT = 587  # SMTP port for TLS
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')  # Your email username
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Your email password

# Twilio Configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')  # Twilio Account SID
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')  # Twilio Auth Token
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')  # Your Twilio phone number

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_email(to_email, subject, body):
    """Send an email to the specified recipient."""
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USERNAME
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the server and send the email
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Upgrade connection to secure
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.send_message(msg)
            logger.info(f'Email sent to {to_email}')
    except Exception as e:
        logger.error(f'Failed to send email to {to_email}: {e}')

def send_whatsapp_message(to_number, message):
    """Send a WhatsApp message to the specified recipient."""
    try:
        message = twilio_client.messages.create(
            body=message,
            from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',  # Twilio WhatsApp number
            to=f'whatsapp:{to_number}'  # Recipient's WhatsApp number
        )
        logger.info(f'WhatsApp message sent to {to_number}: {message.sid}')
    except Exception as e:
        logger.error(f'Failed to send WhatsApp message to {to_number}: {e}')

def send_travel_advisory(to_email, to_whatsapp, subject, body):
    """Send travel advisories via email and WhatsApp."""
    send_email(to_email, subject, body)
    send_whatsapp_message(to_whatsapp, body)

if __name__ == '__main__':
    # Example usage
    client_email = 'client@example.com'
    client_whatsapp = '+1234567890'
    advisory_subject = 'Important Travel Advisory'
    advisory_body = 'Please be informed about the latest travel restrictions and updates.'

    send_travel_advisory(client_email, client_whatsapp, advisory_subject, advisory_body)
```
