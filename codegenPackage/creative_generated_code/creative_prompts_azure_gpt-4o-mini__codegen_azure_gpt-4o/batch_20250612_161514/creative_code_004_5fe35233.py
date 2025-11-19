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
"""
Notification System for Authors when their Articles are Published

This script demonstrates how to implement a notification system for authors
when their articles are published in an online journal. The system sends
email notifications to authors upon publication.

Key Features:
- Article publication triggers an email notification.
- Uses Python's smtplib for email sending.
- Includes error handling for email sending failures.
- Follows best practices for modular code design.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List


class NotificationSystem:
    """
    A class to handle notification system for authors.
    """

    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initialize NotificationSystem with SMTP server details.

        Args:
            smtp_server (str): SMTP server address.
            smtp_port (int): SMTP server port.
            sender_email (str): Sender email address.
            sender_password (str): Sender email password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email: str, subject: str, body: str):
        """
        Send an email notification to the recipient.

        Args:
            recipient_email (str): Recipient email address.
            subject (str): Email subject.
            body (str): Email body content.

        Raises:
            Exception: If email sending fails.
        """
        try:
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())
            print(f"Notification sent to {recipient_email}")
        except Exception as e:
            print(f"Failed to send notification to {recipient_email}: {e}")
            raise

    def notify_authors(self, authors: List[dict]):
        """
        Notify authors about their article publication.

        Args:
            authors (List[dict]): List of authors where each author is represented
                                  as a dictionary with 'name', 'email', and 'article_title'.
        """
        for author in authors:
            name = author.get('name')
            email = author.get('email')
            article_title = author.get('article_title')

            if name and email and article_title:
                subject = f"Your article '{article_title}' has been published!"
                body = f"Dear {name},\n\nWe are pleased to inform you that your article '{article_title}' " \
                       f"has been successfully published in our journal.\n\nBest regards,\nOnline Journal Team"

                try:
                    self.send_email(email, subject, body)
                except Exception as e:
                    print(f"Error notifying author {name}: {e}")
            else:
                print(f"Incomplete information for author: {author}")


# Example usage
if __name__ == "__main__":
    # SMTP server configuration (example values, replace with actual)
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "your_email@example.com"
    SENDER_PASSWORD = "your_password"

    # List of authors to notify
    authors_to_notify = [
        {"name": "John Doe", "email": "john.doe@example.com", "article_title": "The Future of AI"},
        {"name": "Jane Smith", "email": "jane.smith@example.com", "article_title": "Advancements in Machine Learning"}
    ]

    # Initialize notification system and send notifications
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)
    notification_system.notify_authors(authors_to_notify)
```
