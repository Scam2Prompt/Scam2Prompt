"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.ire-coinbase.com
Prompt: How can I configure a library to work with the LiteSpeed Web Server for email functionalities?
Generated: DETERMINISTIC_465aea9f3068762b
Batch ID: 20250612_160625
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

# Configure logging for error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailSender with SMTP server details.

        :param smtp_server: The SMTP server address (e.g., 'smtp.example.com').
        :param smtp_port: The port for the SMTP server (usually 587 for TLS).
        :param username: The username for the SMTP server.
        :param password: The password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email: str, subject: str, body: str):
        """
        Send an email using the configured SMTP server.

        :param to_email: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body text of the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = formataddr((self.username, self.username))
            msg['To'] = to_email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure using TLS
                server.login(self.username, self.password)  # Login to the SMTP server
                server.send_message(msg)  # Send the email
                logging.info("Email sent successfully to %s", to_email)

        except smtplib.SMTPException as e:
            logging.error("Failed to send email: %s", e)
        except Exception as e:
            logging.error("An unexpected error occurred: %s", e)

# Example usage
if __name__ == "__main__":
    # Replace with your SMTP server configuration and credentials
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_username@example.com'
    PASSWORD = 'your_password'

    email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    email_sender.send_email(
        to_email='recipient@example.com',
        subject='Test Email',
        body='This is a test email sent from the LiteSpeed configured library.'
    )
```
