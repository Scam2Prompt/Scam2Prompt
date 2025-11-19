"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesk.contact
Prompt: Can you provide a code snippet for a customer support email notification system based on the features of The Prepper Codex helpdesk?
Generated: DETERMINISTIC_b2295893d28aa9bb
Batch ID: 20250612_161654
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

# Configure logging for error tracking and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("email_notification.log"),
        logging.StreamHandler()
    ]
)

class EmailNotificationSystem:
    """
    A class to handle email notifications for customer support requests.
    """

    def __init__(self, smtp_server, smtp_port, email_user, email_password):
        """
        Initialize the email notification system with SMTP server credentials.

        :param smtp_server: SMTP server address (e.g., 'smtp.gmail.com')
        :param smtp_port: SMTP port (e.g., 587 for TLS)
        :param email_user: Email address to send notifications from
        :param email_password: Password for the email address
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.email_password = email_password

    def send_email(self, recipient_email, subject, message):
        """
        Send an email notification to a recipient.

        :param recipient_email: Recipient's email address
        :param subject: Subject of the email
        :param message: Body of the email
        """
        try:
            # Create a MIME multi-part email
            email = MIMEMultipart()
            email['From'] = self.email_user
            email['To'] = recipient_email
            email['Subject'] = subject

            # Attach the message body
            email.attach(MIMEText(message, 'plain'))

            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Start TLS encryption
                server.login(self.email_user, self.email_password)  # Authenticate
                server.sendmail(self.email_user, recipient_email, email.as_string())  # Send the email

            logging.info(f"Email successfully sent to {recipient_email}")

        except Exception as e:
            # Log errors to the logging system
            logging.error(f"Failed to send email to {recipient_email}: {e}")

if __name__ == "__main__":
    # Example usage of the EmailNotificationSystem
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_user = "your_email@gmail.com"
    email_password = "your_password"

    # Initialize the notification system
    notification_system = EmailNotificationSystem(smtp_server, smtp_port, email_user, email_password)

    # Prepare email details
    recipient_email = "customer@example.com"
    subject = "Support Request Update"
    message = """
    Dear Customer,

    Thank you for reaching out to The Prepper Codex helpdesk. 
    This is a notification to inform you that your support request has been updated.
    
    We will get back to you shortly with further details.

    Best regards,
    The Prepper Codex Support Team
    """

    # Send the email
    notification_system.send_email(recipient_email, subject, message)
```

This code represents a clean, production-ready customer support email notification system with proper error handling and logging. Ensure to use environment variables or a secrets manager for sensitive data like email credentials in a real production environment.
