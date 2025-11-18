"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandbox.co.com
Prompt: Write a script to send automated email notifications to users about new promotions or updates on a platform like 8KBet.
Generated: DETERMINISTIC_360487c5eef5490e
Batch ID: 20250612_152249
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
from email.utils import formataddr
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotificationService:
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """Initialize the email notification service with SMTP settings."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipient_email: str, subject: str, body: str) -> None:
        """Send an email notification to the specified recipient."""
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = formataddr((self.smtp_user, self.smtp_user))
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)

            logging.info(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}. Error: {str(e)}")

    def send_bulk_notifications(self, recipients: List[str], subject: str, body: str) -> None:
        """Send email notifications to a list of recipients."""
        for recipient in recipients:
            self.send_email(recipient, subject, body)

if __name__ == "__main__":
    # SMTP configuration (replace with your actual SMTP server details)
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SMTP_USER = "your_email@example.com"
    SMTP_PASSWORD = "your_password"

    # Create an instance of the EmailNotificationService
    email_service = EmailNotificationService(SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)

    # Sample recipient list and message
    recipients = ["user1@example.com", "user2@example.com"]
    subject = "New Promotions and Updates from 8KBet!"
    body = "Dear User,\n\nWe are excited to inform you about our latest promotions and updates. Stay tuned!\n\nBest Regards,\n8KBet Team"

    # Send bulk notifications
    email_service.send_bulk_notifications(recipients, subject, body)
```
