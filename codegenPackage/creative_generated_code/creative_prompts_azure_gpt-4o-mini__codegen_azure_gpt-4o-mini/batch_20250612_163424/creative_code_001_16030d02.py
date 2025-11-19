"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salesstudios.com
Prompt: Write a code snippet that integrates SMS and email messaging for lead engagement, inspired by the Sales Studios Online System.
Generated: DETERMINISTIC_16030d02e03ec8b5
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from twilio.rest import Client
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LeadEngagement:
    def __init__(self, twilio_sid, twilio_auth_token, twilio_phone_number, smtp_server, smtp_port, email_user, email_password):
        # Initialize Twilio client and SMTP settings
        self.twilio_client = Client(twilio_sid, twilio_auth_token)
        self.twilio_phone_number = twilio_phone_number
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.email_password = email_password

    def send_sms(self, to_phone_number, message):
        """
        Sends an SMS message to a specified phone number.
        
        :param to_phone_number: str - The recipient's phone number
        :param message: str - The message to be sent
        """
        try:
            self.twilio_client.messages.create(
                body=message,
                from_=self.twilio_phone_number,
                to=to_phone_number
            )
            logging.info(f'SMS sent to {to_phone_number}: "{message}"')
        except Exception as e:
            logging.error(f'Failed to send SMS to {to_phone_number}: {e}')

    def send_email(self, to_email, subject, body):
        """
        Sends an email to a specified email address.
        
        :param to_email: str - The recipient's email address
        :param subject: str - The subject of the email
        :param body: str - The body of the email
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the message body to the email
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the SMTP connection
                server.login(self.email_user, self.email_password)
                server.send_message(msg)

            logging.info(f'Email sent to {to_email} with subject: "{subject}"')
        except Exception as e:
            logging.error(f'Failed to send email to {to_email}: {e}')

# Example Usage (replace with actual credentials and phone/email info)
if __name__ == '__main__':
    # Replace with actual Twilio and email credentials
    twilio_sid = 'YOUR_TWILIO_SID'
    twilio_auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'
    smtp_server = 'YOUR_SMTP_SERVER'
    smtp_port = 587  # Typically, 587 for TLS
    email_user = 'YOUR_EMAIL'
    email_password = 'YOUR_EMAIL_PASSWORD'

    lead_engagement = LeadEngagement(twilio_sid, twilio_auth_token, twilio_phone_number, smtp_server, smtp_port, email_user, email_password)

    # Send SMS
    lead_engagement.send_sms('+1234567890', 'Hello! Thanks for your interest in our services.')

    # Send Email
    lead_engagement.send_email('recipient@example.com', 'Welcome!', 'Thank you for reaching out to us.')
```
