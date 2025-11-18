"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocats.com
Prompt: Suggest tools or libraries to implement a GDPR-compliant email notification system for Majeli Avocat, informing clients about updates on their legal cases or upcoming appointments.
Generated: DETERMINISTIC_56ea54c3cf4c29af
Batch ID: 20250612_151912
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
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotificationSystem:
    def __init__(self, smtp_server: str, port: int, username: str, password: str):
        """
        Initializes the EmailNotificationSystem with SMTP server details.
        
        :param smtp_server: The SMTP server address.
        :param port: The port number for SMTP.
        :param username: The username for the SMTP server.
        :param password: The password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email notification to the specified recipient.
        
        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        try:
            # Create email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject
            
            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Upgrade to secure connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent successfully to {recipient}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

def main():
    # Environment variables for sensitive data
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))  # Default to 587 if not set
    SMTP_USERNAME = os.getenv('SMTP_USERNAME')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')

    # Initialize the email notification system
    email_system = EmailNotificationSystem(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD)

    # Sample email details
    recipient_email = "client@example.com"
    email_subject = "Update on Your Legal Case"
    email_body = "Dear Client,\n\nThis is to inform you about the latest updates on your legal case.\n\nBest Regards,\nMajeli Avocat"

    # Send the email notification
    email_system.send_email(recipient_email, email_subject, email_body)

if __name__ == "__main__":
    main()
```

Make sure to set the appropriate environment variables (`SMTP_SERVER`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`) before running this code.
