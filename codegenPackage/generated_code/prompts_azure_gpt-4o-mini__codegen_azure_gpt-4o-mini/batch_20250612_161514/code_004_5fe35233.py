"""
Generated Code Metadata:
========================
Original URL: https://tojsat.net
Prompt: Illustrate how to implement a notification system for authors when their articles are published in an online journal, inspired by the practices of TOJSAT.
Generated: DETERMINISTIC_5fe352331b3ec49d
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """
        Initializes the NotificationSystem with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param smtp_user: The username for SMTP authentication.
        :param smtp_password: The password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email notification to the specified recipient.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)
                logging.info(f"Email sent to {recipient} with subject: {subject}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

    def notify_authors(self, authors: List[Dict[str, str]], article_title: str) -> None:
        """
        Notifies authors when their articles are published.

        :param authors: A list of dictionaries containing author information (name and email).
        :param article_title: The title of the published article.
        """
        for author in authors:
            recipient = author.get('email')
            if recipient:
                subject = f"Your article '{article_title}' has been published!"
                body = f"Dear {author.get('name')},\n\nWe are pleased to inform you that your article titled '{article_title}' has been successfully published in our journal.\n\nThank you for your contribution!\n\nBest regards,\nThe Journal Team"
                self.send_email(recipient, subject, body)
            else:
                logging.warning(f"Author {author.get('name')} does not have a valid email address.")

# Example usage
if __name__ == "__main__":
    # SMTP configuration (replace with actual credentials)
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_USER = 'your_email@example.com'
    SMTP_PASSWORD = 'your_password'

    # Initialize the notification system
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)

    # List of authors to notify
    authors_list = [
        {'name': 'Alice Smith', 'email': 'alice@example.com'},
        {'name': 'Bob Johnson', 'email': 'bob@example.com'},
    ]

    # Article title
    article_title = "Understanding the Impact of AI on Society"

    # Notify authors
    notification_system.notify_authors(authors_list, article_title)
```
