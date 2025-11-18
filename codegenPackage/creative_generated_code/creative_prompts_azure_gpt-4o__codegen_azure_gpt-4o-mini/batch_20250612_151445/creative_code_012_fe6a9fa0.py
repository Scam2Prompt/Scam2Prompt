"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Write a script to automate email and SMS notifications for account registration and deposit confirmations, inspired by DominoBet's process.
Generated: DETERMINISTIC_fe6a9fa035d8b0ef
Batch ID: 20250612_151445
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
from twilio.rest import Client
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationService:
    def __init__(self, email_config, sms_config):
        """
        Initialize the NotificationService with email and SMS configuration.

        :param email_config: Dictionary containing SMTP server details and sender email credentials.
        :param sms_config: Dictionary containing Twilio account SID, auth token, and sender phone number.
        """
        self.email_config = email_config
        self.sms_config = sms_config

    def send_email(self, recipient, subject, message):
        """
        Send an email notification.

        :param recipient: The email address of the recipient.
        :param subject: Subject of the email.
        :param message: Body of the email.
        """
        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = self.email_config['sender_email']
            msg['To'] = recipient
            
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                server.starttls()  # Secure the connection
                server.login(self.email_config['sender_email'], self.email_config['password'])
                server.sendmail(msg['From'], [msg['To']], msg.as_string())
                logging.info(f"Email sent to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

    def send_sms(self, recipient, message):
        """
        Send an SMS notification.

        :param recipient: The phone number of the recipient.
        :param message: Body of the SMS.
        """
        try:
            client = Client(self.sms_config['account_sid'], self.sms_config['auth_token'])
            message = client.messages.create(
                to=recipient,
                from_=self.sms_config['from_number'],
                body=message
            )
            logging.info(f"SMS sent to {recipient}: {message.sid}")
        except Exception as e:
            logging.error(f"Failed to send SMS to {recipient}: {e}")

# Example usage
if __name__ == "__main__":
    # Configuration for email and SMS services
    email_config = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'sender_email': 'your_email@example.com',
        'password': 'your_password'
    }

    sms_config = {
        'account_sid': 'your_account_sid',
        'auth_token': 'your_auth_token',
        'from_number': '+1234567890'  # Your Twilio number
    }
    
    notification_service = NotificationService(email_config, sms_config)

    # Simulate sending notifications on account registration and deposit confirmation
    recipient_email = 'user@example.com'
    recipient_phone = '+0987654321'
    
    notification_service.send_email(
        recipient=recipient_email,
        subject="Welcome to DominoBet!",
        message="Thank you for registering with us. Your account has been successfully created."
    )
    
    notification_service.send_sms(
        recipient=recipient_phone,
        message="Your deposit has been confirmed. Thank you for choosing DominoBet!"
    )
```
