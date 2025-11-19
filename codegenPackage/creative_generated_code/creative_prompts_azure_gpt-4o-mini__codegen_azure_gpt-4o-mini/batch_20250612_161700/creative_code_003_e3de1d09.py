"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://housitbnb.com
Prompt: Generate a Python script that sends an email to users when their account status changes to suspended.
Generated: DETERMINISTIC_e3de1d09e3119d16
Batch ID: 20250612_161700
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
from typing import List, Optional

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """Initialize EmailSender with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """Send an email to the specified recipient."""
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)  # Login to the server
                server.send_message(msg)  # Send the email
            print(f"Email sent successfully to {recipient}")
        except Exception as e:
            print(f"Failed to send email to {recipient}. Error: {e}")

def notify_users_of_suspension(users: List[str], email_sender: EmailSender) -> None:
    """Notify users about their account suspension status."""
    subject = "Account Status Update"
    body_template = "Dear User,\n\nYour account has been suspended.\n\nRegards,\nSupport Team"

    for user in users:
        try:
            email_sender.send_email(user, subject, body_template)
        except Exception as e:
            print(f"Error notifying {user}: {e}")

if __name__ == "__main__":
    # Configuration for the SMTP server
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_email_password'

    # List of users to notify (email addresses)
    users_to_notify = [
        'user1@example.com',
        'user2@example.com',
        'user3@example.com'
    ]

    # Create an instance of EmailSender
    email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Notify users of their account suspension
    notify_users_of_suspension(users_to_notify, email_sender)
```
