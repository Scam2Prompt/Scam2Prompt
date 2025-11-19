"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Generate a Python script to automate email subscription for sending updates on interior design trends and exclusive materials, similar to the "Fique por Dentro" feature on the website.
Generated: DETERMINISTIC_82f7c394fdc70452
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# email_subscription.py

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a rotating file handler
file_handler = RotatingFileHandler('email_subscription.log', maxBytes=1024*1024*10, backupCount=5)
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

class EmailSubscription:
    def __init__(self, sender_email, sender_password, smtp_server, smtp_port):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient_email, subject, body):
        try:
            # Create a secure SSL context
            context = ssl.create_default_context()

            # Set up the SMTP server
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context) as server:
                server.login(self.sender_email, self.sender_password)

                # Create a multipart message
                message = MIMEMultipart()
                message['From'] = self.sender_email
                message['To'] = recipient_email
                message['Subject'] = subject

                # Attach the body to the message
                message.attach(MIMEText(body, 'plain'))

                # Send the email
                server.sendmail(self.sender_email, recipient_email, message.as_string())

            logger.info(f'Email sent to {recipient_email} successfully')

        except smtplib.SMTPAuthenticationError:
            logger.error('SMTP authentication error')
        except smtplib.SMTPException as e:
            logger.error(f'SMTP error: {e}')
        except Exception as e:
            logger.error(f'An error occurred: {e}')

    def subscribe(self, recipient_email):
        try:
            # Fetch interior design trends and exclusive materials
            trends_url = os.getenv('TRENDS_URL')
            materials_url = os.getenv('MATERIALS_URL')

            trends_response = requests.get(trends_url)
            materials_response = requests.get(materials_url)

            trends_response.raise_for_status()
            materials_response.raise_for_status()

            trends = trends_response.json()
            materials = materials_response.json()

            # Create the email body
            body = f'Dear subscriber,\n\nHere are the latest interior design trends and exclusive materials:\n\nTrends:\n'
            for trend in trends:
                body += f'- {trend["name"]}\n'
            body += f'\nMaterials:\n'
            for material in materials:
                body += f'- {material["name"]}\n'

            # Send the email
            subject = 'Your Interior Design Update'
            self.send_email(recipient_email, subject, body)

        except requests.RequestException as e:
            logger.error(f'Request error: {e}')
        except Exception as e:
            logger.error(f'An error occurred: {e}')


if __name__ == '__main__':
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))

    email_subscription = EmailSubscription(sender_email, sender_password, smtp_server, smtp_port)

    recipient_email = 'recipient@example.com'  # Replace with the recipient's email
    email_subscription.subscribe(recipient_email)
```
