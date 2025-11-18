"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Create code for a notification system that alerts customers about service updates, such as cleaning or insulation progress, as described in شركة انجاز's service offerings.
Generated: DETERMINISTIC_c2a1cf556ac2e240
Batch ID: 20250612_153224
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

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class NotificationSystem:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initializes the NotificationSystem with SMTP server details and sender credentials.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param sender_email: Sender's email address
        :param sender_password: Sender's email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email, subject, message):
        """
        Sends a notification email to the specified recipient.
        
        :param recipient_email: Recipient's email address
        :param subject: Subject of the email
        :param message: Body of the email
        :raises Exception: If an error occurs during email sending
        """
        try:
            # Create the email
            email = MIMEMultipart()
            email['From'] = self.sender_email
            email['To'] = recipient_email
            email['Subject'] = subject
            email.attach(MIMEText(message, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure (TLS)
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, email.as_string())

            logging.info(f"Notification sent to {recipient_email} successfully.")
        except Exception as e:
            logging.error(f"Failed to send notification to {recipient_email}: {e}")
            raise

if __name__ == "__main__":
    # Example usage of the NotificationSystem
    try:
        # Initialize notification system with SMTP server details
        notification_system = NotificationSystem(
            smtp_server="smtp.example.com",
            smtp_port=587,
            sender_email="your-email@example.com",
            sender_password="your-email-password"
        )

        # Send a notification to a customer
        recipient_email = "customer@example.com"
        subject = "Service Update: Cleaning Progress"
        message = "Dear Customer,\n\nWe are pleased to inform you that your cleaning service is progressing smoothly and is expected to be completed by the end of the day.\n\nBest regards,\nشركة انجاز"

        notification_system.send_notification(recipient_email, subject, message)
    except Exception as e:
        logging.error(f"An error occurred during the notification system execution: {e}")
```
