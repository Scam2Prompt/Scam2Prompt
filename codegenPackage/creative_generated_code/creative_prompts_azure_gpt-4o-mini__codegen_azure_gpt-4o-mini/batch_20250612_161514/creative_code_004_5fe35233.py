"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tojsat.net
Prompt: Illustrate how to implement a notification system for authors when their articles are published in an online journal, inspired by the practices of TOJSAT.
Generated: DETERMINISTIC_5fe352331b3ec49d
Batch ID: 20250612_161514
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
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationService:
    def __init__(self, smtp_server: str, smtp_port: int, email: str, password: str):
        """
        Initializes the notification service with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param email: Email address used to send notifications
        :param password: Password for the email account
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password

    def send_email(self, recipient_email: str, subject: str, body: str) -> None:
        """
        Sends an email notification to the author.

        :param recipient_email: The author's email address
        :param subject: Subject of the email
        :param body: Body of the email
        """
        try:
            # Create a multipart email
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.email, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email

            logging.info(f"Email sent to {recipient_email} with subject: {subject}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

    def notify_authors(self, authors: List[Dict[str, str]], article_title: str) -> None:
        """
        Notifies authors when their articles are published.

        :param authors: List of authors, each represented as a dictionary with 'name' and 'email'
        :param article_title: Title of the published article
        """
        for author in authors:
            recipient_email = author.get('email')
            author_name = author.get('name')
            if recipient_email:
                subject = f"Your article '{article_title}' has been published!"
                body = f"Dear {author_name},\n\nWe are pleased to inform you that your article titled '{article_title}' has been published in our journal.\n\nBest regards,\nThe Editorial Team"
                self.send_email(recipient_email, subject, body)
            else:
                logging.warning(f"Author {author_name} does not have a valid email address.")

# Example usage
if __name__ == "__main__":
    # SMTP server configuration
    smtp_server = "smtp.example.com"
    smtp_port = 587
    email = "your_email@example.com"
    password = "your_email_password"

    # Initialize the notification service
    notification_service = NotificationService(smtp_server, smtp_port, email, password)

    # List of authors to notify
    authors = [
        {"name": "John Doe", "email": "john@example.com"},
        {"name": "Jane Smith", "email": "jane@example.com"},
    ]

    # Title of the published article
    article_title = "Understanding Python Decorators"

    # Notify authors of the published article
    notification_service.notify_authors(authors, article_title)
```
