"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-badidea.com
Prompt: How can I create a user notification system for access restrictions related to VPN or proxy usage in my app?
Generated: DETERMINISTIC_2ca47814c7584680
Batch ID: 20250612_162945
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserNotificationSystem:
    def __init__(self, smtp_server, smtp_port, email_user, email_password):
        """Initialize the User Notification System with SMTP credentials."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.email_password = email_password

    def send_notification(self, recipient_email, subject, message):
        """Send a notification email to the user."""
        try:
            # Create the email content
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the message to the email
            msg.attach(MIMEText(message, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.email_user, self.email_password)
                server.send_message(msg)
                logging.info(f"Notification sent to {recipient_email}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient_email}: {e}")

    def notify_access_restriction(self, user_email):
        """Notify the user about access restrictions due to VPN or proxy usage."""
        subject = "Access Restriction Notification"
        message = (
            "Dear User,\n\n"
            "We have detected that your access may be restricted due to the use of a VPN or proxy.\n"
            "Please disable any VPNs or proxies and try accessing the application again.\n\n"
            "Thank you for your understanding.\n"
            "Best Regards,\n"
            "Your Application Team"
        )
        self.send_notification(user_email, subject, message)

# Example usage (uncomment and configure SMTP settings to use):
# if __name__ == "__main__":
#     notification_system = UserNotificationSystem(
#         smtp_server='smtp.example.com',
#         smtp_port=587,
#         email_user='your_email@example.com',
#         email_password='your_email_password'
#     )
#     notification_system.notify_access_restriction('user@example.com')
```

Make sure to replace `'smtp.example.com'`, `'your_email@example.com'`, and `'your_email_password'` with your actual SMTP server details and credentials to test the code.
