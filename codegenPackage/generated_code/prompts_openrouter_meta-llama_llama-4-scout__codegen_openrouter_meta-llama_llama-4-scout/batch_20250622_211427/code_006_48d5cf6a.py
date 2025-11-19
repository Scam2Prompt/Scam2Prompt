"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Write a script to automate the process of sending travel advisories and updates to clients, using email or WhatsApp APIs.
Generated: DETERMINISTIC_48d5cf6a4e60e1ab
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from dotenv import load_dotenv
from twilio.rest import Client
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TravelAdvisorySender:
    def __init__(self, email_config, whatsapp_config):
        """
        Initialize the TravelAdvisorySender class.

        Args:
            email_config (dict): Email configuration dictionary.
            whatsapp_config (dict): WhatsApp configuration dictionary.
        """
        self.email_config = email_config
        self.whatsapp_config = whatsapp_config

    def send_email(self, recipient, subject, message):
        """
        Send an email to a recipient.

        Args:
            recipient (str): Recipient's email address.
            subject (str): Email subject.
            message (str): Email body.

        Returns:
            bool: True if email is sent successfully, False otherwise.
        """
        try:
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = self.email_config['sender_email']
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Send email using SMTP server
            server = smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port'])
            server.starttls()
            server.login(self.email_config['sender_email'], self.email_config['sender_password'])
            text = msg.as_string()
            server.sendmail(self.email_config['sender_email'], recipient, text)
            server.quit()

            logger.info(f"Email sent to {recipient} successfully.")
            return True
        except Exception as e:
            logger.error(f"Error sending email to {recipient}: {str(e)}")
            return False

    def send_whatsapp(self, recipient, message):
        """
        Send a WhatsApp message to a recipient.

        Args:
            recipient (str): Recipient's WhatsApp phone number.
            message (str): WhatsApp message.

        Returns:
            bool: True if message is sent successfully, False otherwise.
        """
        try:
            # Initialize Twilio client
            client = Client(self.whatsapp_config['account_sid'], self.whatsapp_config['auth_token'])

            # Send WhatsApp message
            message = client.messages.create(
                body=message,
                from_=self.whatsapp_config['twilio_phone_number'],
                to=recipient
            )

            logger.info(f"WhatsApp message sent to {recipient} successfully.")
            return True
        except Exception as e:
            logger.error(f"Error sending WhatsApp message to {recipient}: {str(e)}")
            return False

    def send_travel_advisory(self, recipient, advisory_type, message):
        """
        Send a travel advisory or update to a client.

        Args:
            recipient (str): Client's contact information (email or WhatsApp phone number).
            advisory_type (str): Type of advisory (email or whatsapp).
            message (str): Advisory message.

        Returns:
            bool: True if advisory is sent successfully, False otherwise.
        """
        if advisory_type == 'email':
            return self.send_email(recipient, 'Travel Advisory', message)
        elif advisory_type == 'whatsapp':
            return self.send_whatsapp(recipient, message)
        else:
            logger.error(f"Invalid advisory type: {advisory_type}")
            return False


def main():
    # Email configuration
    email_config = {
        'sender_email': os.getenv('EMAIL_SENDER'),
        'sender_password': os.getenv('EMAIL_PASSWORD'),
        'smtp_server': os.getenv('EMAIL_SMTP_SERVER'),
        'smtp_port': int(os.getenv('EMAIL_SMTP_PORT'))
    }

    # WhatsApp configuration
    whatsapp_config = {
        'account_sid': os.getenv('TWILIO_ACCOUNT_SID'),
        'auth_token': os.getenv('TWILIO_AUTH_TOKEN'),
        'twilio_phone_number': os.getenv('TWILIO_PHONE_NUMBER')
    }

    # Initialize TravelAdvisorySender
    sender = TravelAdvisorySender(email_config, whatsapp_config)

    # Example usage
    client_email = 'client@example.com'
    client_whatsapp = '+1234567890'
    advisory_message = 'Travel advisory: Avoid traveling to certain areas due to safety concerns.'

    sender.send_travel_advisory(client_email, 'email', advisory_message)
    sender.send_travel_advisory(client_whatsapp, 'whatsapp', advisory_message)


if __name__ == '__main__':
    main()
```
