"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paaltoken.com
Prompt: Write a Python script that sends email notifications to users who sign up for updates, inspired by the subscription feature on paaltoken.com.
Generated: DETERMINISTIC_5544fc50d6e10626
Batch ID: 20250612_161420
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
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailNotifier with SMTP server details.

        :param smtp_server: The SMTP server hostname.
        :param smtp_port: The SMTP server port.
        :param username: The email account username.
        :param password: The email account password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email notification.

        :param recipient: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the body to the email
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the SMTP server
                server.send_message(msg)  # Send the email

            logging.info(f'Email sent to {recipient}')

        except smtplib.SMTPException as e:
            logging.error(f'Failed to send email to {recipient}: {e}')
        except Exception as e:
            logging.error(f'An unexpected error occurred: {e}')

def main():
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your-email@example.com'
    PASSWORD = 'your-email-password'

    notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # List of subscribers to notify
    subscribers: List[str] = [
        'user1@example.com',
        'user2@example.com',
        'user3@example.com'
    ]

    # Email configuration
    subject = 'Welcome to Our Updates!'
    body = 'Thank you for subscribing to our updates! Stay tuned for the latest news.'

    # Send email notifications to all subscribers
    for subscriber in subscribers:
        notifier.send_email(subscriber, subject, body)

if __name__ == '__main__':
    main()
```
