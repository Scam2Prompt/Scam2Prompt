"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webstarstudio.com
Prompt: Generate a script to automate email notifications using WebStar Studio's CMS framework.
Generated: DETERMINISTIC_51ccb53eec06dcdb
Batch ID: 20250612_150440
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

class EmailNotificationService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailNotificationService with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port number for the SMTP server.
        :param username: The username for SMTP authentication.
        :param password: The password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipients: List[str], subject: str, body: str) -> None:
        """
        Sends an email notification to the specified recipients.

        :param recipients: List of email addresses to send the notification to.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            
            # Attach the email body to the message
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the SMTP server
                server.sendmail(self.username, recipients, msg.as_string())  # Send the email
            
            logging.info("Email sent successfully to: %s", ', '.join(recipients))
        
        except smtplib.SMTPException as e:
            logging.error("Failed to send email. SMTP error: %s", e)
        except Exception as e:
            logging.error("An unexpected error occurred: %s", e)

# Example usage
if __name__ == "__main__":
    # Configuration for the email service
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_email_password'

    # Create an instance of the email notification service
    email_service = EmailNotificationService(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define the email parameters
    recipients_list = ['recipient1@example.com', 'recipient2@example.com']
    subject_line = 'Test Email Notification'
    email_body = 'This is a test email notification from WebStar Studio CMS framework.'

    # Send the email notification
    email_service.send_email(recipients_list, subject_line, email_body)
```
