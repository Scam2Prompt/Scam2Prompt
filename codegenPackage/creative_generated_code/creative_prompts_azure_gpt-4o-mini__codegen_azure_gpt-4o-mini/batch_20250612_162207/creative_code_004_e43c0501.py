"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degen-4g1.pages.dev
Prompt: Illustrate how to implement a feature for users to receive updates on upcoming drops and product releases from Highlight.
Generated: DETERMINISTIC_e43c0501be7abd0e
Batch ID: 20250612_162207
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
from datetime import datetime, timedelta
from typing import List, Dict
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UpdateNotifier:
    def __init__(self, email_server: str, email_port: int, email_user: str, email_password: str):
        """
        Initialize the UpdateNotifier with email server configuration.

        :param email_server: SMTP server address for sending emails
        :param email_port: SMTP server port
        :param email_user: Email account username
        :param email_password: Email account password
        """
        self.email_server = email_server
        self.email_port = email_port
        self.email_user = email_user
        self.email_password = email_password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email notification to a user.

        :param recipient: The email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        try:
            # Create a multipart email
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secure session with the server
            with smtplib.SMTP(self.email_server, self.email_port) as server:
                server.starttls()  # Upgrade to secure connection
                server.login(self.email_user, self.email_password)
                server.send_message(msg)
            logging.info(f"Email successfully sent to {recipient}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

    def notify_users(self, users: List[Dict[str, str]], updates: List[str]) -> None:
        """
        Notify users about upcoming drops and product releases.

        :param users: List of users with email and name
        :param updates: List of updates to send to users
        """
        for user in users:
            email = user.get('email')
            name = user.get('name')
            if email:
                subject = "Upcoming Drops and Product Releases"
                body = f"Hello {name},\n\nHere are the upcoming drops and product releases:\n\n" + "\n".join(updates)
                self.send_email(email, subject, body)

# Example usage
if __name__ == "__main__":
    # Sample configuration, replace with valid data
    EMAIL_SERVER = "smtp.example.com"
    EMAIL_PORT = 587
    EMAIL_USER = "your_email@example.com"
    EMAIL_PASSWORD = "your_password"

    # Sample user list
    users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
    ]

    # Sample updates
    updates = [
        "New product drop on October 15, 2023.",
        "Exclusive release event on October 20, 2023.",
        "Limited edition merchandise available soon.",
    ]

    # Create an instance of UpdateNotifier
    notifier = UpdateNotifier(EMAIL_SERVER, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD)

    # Notify users about updates
    notifier.notify_users(users, updates)
```
