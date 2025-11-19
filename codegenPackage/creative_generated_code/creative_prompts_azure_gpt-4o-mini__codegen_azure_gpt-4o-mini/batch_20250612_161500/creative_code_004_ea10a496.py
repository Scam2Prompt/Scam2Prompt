"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://byb-usdt.pages.dev
Prompt: How can I implement a notification system for account suspension alerts using a specific programming language?
Generated: DETERMINISTIC_ea10a4967409ff4f
Batch ID: 20250612_161500
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

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationSystem:
    def __init__(self, smtp_server, smtp_port, email, password):
        """
        Initialize the NotificationSystem with SMTP server details.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param email: Sender's email address
        :param password: Sender's email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password

    def send_notification(self, recipient_email, subject, message):
        """
        Send an email notification.
        
        :param recipient_email: Recipient's email address
        :param subject: Subject of the email
        :param message: Body of the email
        """
        try:
            # Create the email content
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(message, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
                server.login(self.email, self.password)  # Login to the email server
                server.send_message(msg)  # Send the email
                logging.info(f"Notification sent to {recipient_email}")
        
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send notification: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

def main():
    # Example configuration (replace with your actual email settings)
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    EMAIL = 'your-email@example.com'
    PASSWORD = 'your-email-password'

    # Create an instance of the NotificationSystem
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, EMAIL, PASSWORD)

    # Example usage: send a suspension alert
    recipient_email = 'user@example.com'
    subject = 'Account Suspension Alert'
    message = 'Dear User,\n\nYour account has been suspended due to policy violations.\nPlease contact support for further assistance.\n\nBest regards,\nSupport Team'
    
    notification_system.send_notification(recipient_email, subject, message)

if __name__ == "__main__":
    main()
```
