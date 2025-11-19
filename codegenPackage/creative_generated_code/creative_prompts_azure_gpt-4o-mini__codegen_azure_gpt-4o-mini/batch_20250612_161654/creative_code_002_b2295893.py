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
from email.utils import formataddr
import logging

# Set up logging for monitoring errors and events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotificationService:
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initialize the EmailNotificationService with SMTP server details.

        :param smtp_server: SMTP server address (e.g., smtp.gmail.com)
        :param smtp_port: Port number for the SMTP server (e.g., 587)
        :param username: Email account username for authentication
        :param password: Email account password for authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body):
        """
        Send an email notification to a customer support email.

        :param to_email: Recipient's email address
        :param subject: Subject of the email
        :param body: Email body content
        :raises Exception: If email sending fails
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = formataddr(('Support Team', self.username))
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to TLS
                server.login(self.username, self.password)  # Login to the email account
                server.send_message(msg)  # Send the email
                logging.info(f"Email sent to {to_email} with subject: '{subject}'")

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {to_email}: {e}")
            raise Exception("Email sending failed") from e

if __name__ == "__main__":
    # Example usage of the EmailNotificationService
    # Make sure to replace with actual SMTP credentials
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your-email@example.com"
    password = "your-password"

    # Initialize the email notification service
    email_service = EmailNotificationService(smtp_server, smtp_port, username, password)

    # Define the recipient, subject, and body of the email
    recipient_email = "customer@example.com"
    email_subject = "Your Support Request Has Been Received"
    email_body = "Thank you for reaching out to us. We will respond to your request shortly."

    # Send the email notification
    try:
        email_service.send_email(recipient_email, email_subject, email_body)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
