"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-qf-manager-bhrfz6odu-bootnode.vercel.app
Prompt: How do I implement a notification system for updates in the Gitcoin Round Manager?
Generated: DETERMINISTIC_01e2508114489aa4
Batch ID: 20250612_161356
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

# Notification System for Gitcoin Round Manager Updates

class NotificationSystem:
    def __init__(self, smtp_server: str, port: int, sender_email: str, sender_password: str):
        """
        Initialize the NotificationSystem with SMTP server details.
        
        Args:
            smtp_server (str): The SMTP server address.
            port (int): The port number for the SMTP server.
            sender_email (str): The email address used to send notifications.
            sender_password (str): The password for the sender email.
        """
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_email_notification(self, recipient_email: str, subject: str, message: str) -> None:
        """
        Send an email notification to a single recipient.

        Args:
            recipient_email (str): The email address of the recipient.
            subject (str): The subject of the email.
            message (str): The body of the email.

        Raises:
            Exception: Raises an exception if the email cannot be sent.
        """
        try:
            # Create the email components
            email = MIMEMultipart()
            email['From'] = self.sender_email
            email['To'] = recipient_email
            email['Subject'] = subject
            email.attach(MIMEText(message, 'plain'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Enable encryption
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, email.as_string())
        except Exception as e:
            # Handle any error in sending the email
            raise Exception(f"Failed to send email to {recipient_email}: {str(e)}")
    
    def notify_users(self, recipients: List[str], subject: str, message: str) -> None:
        """
        Send notifications to multiple recipients.

        Args:
            recipients (List[str]): A list of recipient emails.
            subject (str): The subject of the email.
            message (str): The body of the email.
        """
        for recipient in recipients:
            try:
                self.send_email_notification(recipient, subject, message)
                print(f"Notification sent to {recipient}")
            except Exception as e:
                print(f"Error sending notification to {recipient}: {e}")

# Example usage:

if __name__ == "__main__":
    # Configuration for the SMTP server
    SMTP_SERVER = "smtp.example.com"
    PORT = 587
    SENDER_EMAIL = "your_email@example.com"
    SENDER_PASSWORD = "your_password"
    
    # Initialize the notification system
    notifier = NotificationSystem(SMTP_SERVER, PORT, SENDER_EMAIL, SENDER_PASSWORD)
    
    # List of recipients
    recipients = ["user1@example.com", "user2@example.com", "user3@example.com"]
    
    # Subject and message for the notification
    subject = "Gitcoin Round Manager Update"
    message = "A new update has been made to the Gitcoin Round Manager. Please check the system for details."
    
    # Send notifications
    notifier.notify_users(recipients, subject, message)
```
