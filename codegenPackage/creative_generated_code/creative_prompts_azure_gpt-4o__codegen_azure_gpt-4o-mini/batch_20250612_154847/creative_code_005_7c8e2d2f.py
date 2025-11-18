"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bit-deer.com
Prompt: Create a program to automate notifications for users on a cryptocurrency hardware waiting list, referencing the Sealminer waiting list system.
Generated: DETERMINISTIC_7c8e2d2f1ffb2416
Batch ID: 20250612_154847
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

class NotificationService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """Send an email notification to the specified recipient."""
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Establish a connection to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f'Notification sent to {recipient}')
        except Exception as e:
            logging.error(f'Failed to send email to {recipient}: {e}')

class WaitingListNotifier:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def notify_users(self, user_emails: List[str], product_name: str) -> None:
        """Notify all users on the waiting list about product availability."""
        subject = f'Your {product_name} is Available!'
        body = f'Dear User,\n\nWe are excited to inform you that your requested {product_name} is now available for purchase.\n\nBest regards,\nSealminer Team'
        
        for email in user_emails:
            self.notification_service.send_email(email, subject, body)

def main():
    # Configuration for the SMTP server
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    username = 'your_email@example.com'
    password = 'your_email_password'
    
    # Sample waiting list of user emails
    user_emails = ['user1@example.com', 'user2@example.com']
    product_name = 'Sealminer Hardware'

    # Create the notification service instance
    notification_service = NotificationService(smtp_server, smtp_port, username, password)
    
    # Create the waiting list notifier instance
    waiting_list_notifier = WaitingListNotifier(notification_service)
    
    # Notify users
    waiting_list_notifier.notify_users(user_emails, product_name)

if __name__ == '__main__':
    main()
```
