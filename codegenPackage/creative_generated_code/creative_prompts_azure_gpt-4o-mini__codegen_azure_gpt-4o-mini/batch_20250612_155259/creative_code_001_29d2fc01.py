"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancellationflights.com
Prompt: How can I implement a notification system for users when their accounts are suspended?
Generated: DETERMINISTIC_29d2fc011be81150
Batch ID: 20250612_155259
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        """
        Initialize the NotificationSystem with SMTP server details.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Sender's email address
        :param sender_password: Sender's email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email: str, subject: str, body: str) -> None:
        """
        Send an email notification to the user.

        :param recipient_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Body of the email
        """
        try:
            # Create the email
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)  # Log in to the server
                server.send_message(msg)  # Send the email

            logging.info(f'Notification sent to {recipient_email}')
        except Exception as e:
            logging.error(f'Failed to send notification to {recipient_email}: {e}')

    def notify_user_account_suspension(self, user_email: str) -> None:
        """
        Notify the user about account suspension.

        :param user_email: Email of the user whose account is suspended
        """
        subject = "Account Suspension Notification"
        body = (
            "Dear User,\n\n"
            "We regret to inform you that your account has been suspended due to policy violations.\n"
            "For further details, please contact our support team.\n\n"
            "Best regards,\n"
            "The Support Team"
        )
        self.send_notification(user_email, subject, body)

# Example usage
if __name__ == "__main__":
    # Configuration for the SMTP server
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Replace with your SMTP port
    SENDER_EMAIL = 'noreply@example.com'  # Replace with your sender email
    SENDER_PASSWORD = 'your_password'  # Replace with your sender email password

    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)

    # Notify a user account suspension
    user_email = 'user@example.com'  # Replace with the user's email
    notification_system.notify_user_account_suspension(user_email)
```
