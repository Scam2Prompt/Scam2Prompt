"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uembark.org
Prompt: Recommend APIs or libraries to integrate email notifications for real-time updates, similar to the email list functionality described on uEmbark.
Generated: DETERMINISTIC_a7a04f44552ff8af
Batch ID: 20250612_154632
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

# Configure logging
logging.basicConfig(level=logging.INFO)

class EmailNotification:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailNotification class with SMTP server credentials.

        :param smtp_server: The SMTP server address (e.g., smtp.example.com).
        :param smtp_port: The port number for the SMTP server (e.g., 587).
        :param username: The username for SMTP authentication.
        :param password: The password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, subject: str, body: str, recipients: List[str]) -> None:
        """
        Send an email notification.

        :param subject: The subject of the email.
        :param body: The body content of the email.
        :param recipients: A list of email addresses to send the notification to.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject

            # Attach the body to the email
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Authenticate with the server
                server.sendmail(self.username, recipients, msg.as_string())  # Send the email
                logging.info(f"Email sent successfully to {recipients}")

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email: {e}")
            raise  # Re-raise the exception for further handling if necessary

# Example usage:
if __name__ == "__main__":
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_email@example.com"
    password = "your_password"

    email_notification = EmailNotification(smtp_server, smtp_port, username, password)
    
    subject = "Real-Time Update Notification"
    body = "This is a notification email for real-time updates."
    recipients = ["recipient1@example.com", "recipient2@example.com"]

    email_notification.send_email(subject, body, recipients)
```
