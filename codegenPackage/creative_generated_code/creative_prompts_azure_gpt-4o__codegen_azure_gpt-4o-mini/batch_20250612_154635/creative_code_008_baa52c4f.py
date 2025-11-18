"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mellstroy-eth.vercel.app
Prompt: Write code to implement a notification system for updates about campaigns and rewards, similar to the "Sign up for updates" feature on the MELLSTROY website.
Generated: DETERMINISTIC_baa52c4fe304edf3
Batch ID: 20250612_154635
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

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the NotificationSystem with SMTP server credentials.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Username for SMTP authentication
        :param password: Password for SMTP authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email notification.

        :param recipient: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        try:
            # Create the email content
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
                server.login(self.username, self.password)  # Log in to the SMTP server
                server.sendmail(self.username, recipient, msg.as_string())  # Send the email
            
            logging.info(f'Email sent successfully to {recipient}')
        except Exception as e:
            logging.error(f'Failed to send email to {recipient}: {str(e)}')

    def notify_users(self, recipients: List[str], subject: str, body: str) -> None:
        """
        Notify a list of users via email.

        :param recipients: List of email addresses to notify
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        for recipient in recipients:
            self.send_email(recipient, subject, body)

# Example of how to use the NotificationSystem
if __name__ == '__main__':
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Initialize the notification system
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Example list of recipients
    recipients_list = ['user1@example.com', 'user2@example.com']

    # Email subject and body
    email_subject = 'Updates on Campaigns and Rewards'
    email_body = 'Hello! Stay tuned for the latest updates on our campaigns and rewards.'

    # Notify users
    notification_system.notify_users(recipients_list, email_subject, email_body)
```
