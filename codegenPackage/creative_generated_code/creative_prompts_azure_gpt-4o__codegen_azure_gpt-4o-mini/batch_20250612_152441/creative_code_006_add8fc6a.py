"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-inscribe.pages.dev
Prompt: Create a script to send notifications to users about their eligibility for Inscribe Mainnet rewards and alpha quest participation.
Generated: DETERMINISTIC_add8fc6a14c7f5e2
Batch ID: 20250612_152441
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
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the NotificationSender with SMTP server details.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Username for the SMTP server
        :param password: Password for the SMTP server
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
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.username, self.password)  # Log in to the server
                server.sendmail(self.username, recipient, msg.as_string())  # Send email

            logging.info(f"Email sent successfully to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

def main(recipients: List[str]) -> None:
    """
    Main function to notify users about their eligibility for rewards.
    
    :param recipients: List of user email addresses to notify
    """
    # SMTP configuration (replace with actual values)
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of NotificationSender
    notification_sender = NotificationSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Email details
    subject = "Eligibility for Inscribe Mainnet Rewards and Alpha Quest Participation"
    body = """\
    Dear User,

    We're excited to inform you that you are eligible for Inscribe Mainnet rewards and can participate in the alpha quest!

    Please visit our website for more details.

    Best regards,
    The Inscribe Team
    """

    # Send notifications to all recipients
    for recipient in recipients:
        notification_sender.send_email(recipient, subject, body)

if __name__ == "__main__":
    # List of users to notify (replace with actual email addresses)
    user_emails = [
        'user1@example.com',
        'user2@example.com',
        'user3@example.com'
    ]

    main(user_emails)
```
