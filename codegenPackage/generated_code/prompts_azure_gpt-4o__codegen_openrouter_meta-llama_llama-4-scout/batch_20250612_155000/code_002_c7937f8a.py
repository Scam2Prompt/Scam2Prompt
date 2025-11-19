"""
Generated Code Metadata:
========================
Original URL: https://la-guarida.com.ar
Prompt: Generate a Python script for automating email campaigns, referencing La Guarida's focus on digital solutions.
Generated: DETERMINISTIC_c7937f8aed2ff8db
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# email_campaign_automation.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import logging
import argparse
from typing import List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailCampaign:
    def __init__(self, sender_email: str, sender_password: str, smtp_server: str, smtp_port: int):
        """
        Initialize the EmailCampaign class.

        Args:
        - sender_email (str): The email address of the sender.
        - sender_password (str): The password of the sender's email account.
        - smtp_server (str): The SMTP server to use.
        - smtp_port (int): The port number of the SMTP server.
        """
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def create_message(self, recipient_email: str, subject: str, body: str) -> MIMEMultipart:
        """
        Create a multi-part email message.

        Args:
        - recipient_email (str): The email address of the recipient.
        - subject (str): The subject of the email.
        - body (str): The body of the email.

        Returns:
        - MIMEMultipart: A multi-part email message.
        """
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        return message

    def send_email(self, recipient_email: str, subject: str, body: str) -> None:
        """
        Send an email to a recipient.

        Args:
        - recipient_email (str): The email address of the recipient.
        - subject (str): The subject of the email.
        - body (str): The body of the email.
        """
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context) as server:
                server.login(self.sender_email, self.sender_password)
                message = self.create_message(recipient_email, subject, body)
                server.sendmail(self.sender_email, recipient_email, message.as_string())
                logging.info(f'Email sent to {recipient_email}')
        except smtplib.SMTPAuthenticationError:
            logging.error('Authentication error: Invalid email or password')
        except smtplib.SMTPException as e:
            logging.error(f'SMTP error: {e}')

    def automate_campaign(self, recipient_emails: List[str], subject: str, body: str) -> None:
        """
        Automate an email campaign by sending emails to a list of recipients.

        Args:
        - recipient_emails (List[str]): A list of recipient email addresses.
        - subject (str): The subject of the email.
        - body (str): The body of the email.
        """
        for recipient_email in recipient_emails:
            self.send_email(recipient_email, subject, body)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automate an email campaign')
    parser.add_argument('--sender_email', required=True, help='Sender email address')
    parser.add_argument('--sender_password', required=True, help='Sender email password')
    parser.add_argument('--smtp_server', required=True, help='SMTP server')
    parser.add_argument('--smtp_port', type=int, required=True, help='SMTP port')
    parser.add_argument('--recipient_emails', nargs='+', required=True, help='Recipient email addresses')
    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--body', required=True, help='Email body')
    args = parser.parse_args()

    campaign = EmailCampaign(args.sender_email, args.sender_password, args.smtp_server, args.smtp_port)
    campaign.automate_campaign(args.recipient_emails, args.subject, args.body)
```
