"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Generate code to automate email notifications for an educational institution, using the contact email format provided on the IEBCA website (e.g., ined.benjamincorrea@gmail.com).
Generated: DETERMINISTIC_ef1b6177021df322
Batch ID: 20250612_152527
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
from typing import List
import logging

# Set up logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailNotifier with SMTP server information.

        :param smtp_server: The SMTP server address
        :param smtp_port: The SMTP server port
        :param username: The email account username
        :param password: The email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email notification.

        :param recipient: The recipient's email address
        :param subject: The subject of the email
        :param body: The body content of the email
        :raises Exception: Raises an exception if sending the email fails
        """
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr(("Educational Institution", self.username))
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
                logging.info(f"Email sent successfully to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")
            raise  # Re-raise the exception for further handling if necessary

def main():
    # SMTP server configuration (example configuration)
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@gmail.com'  # Replace with your email
    PASSWORD = 'your_password'  # Replace with your email password

    # Create an instance of the EmailNotifier
    notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # List of recipients (example)
    recipients = [
        'ined.benjamincorrea@gmail.com',
        # Add more email addresses as needed
    ]

    # Sending email notifications
    for recipient in recipients:
        subject = "Important Notification"
        body = "Dear Student,\n\nThis is an important notification from the educational institution.\n\nBest regards,\nEducational Institution"
        try:
            notifier.send_email(recipient, subject, body)
        except Exception as e:
            logging.error(f"Error sending email to {recipient}: {e}")

if __name__ == "__main__":
    main()
```
