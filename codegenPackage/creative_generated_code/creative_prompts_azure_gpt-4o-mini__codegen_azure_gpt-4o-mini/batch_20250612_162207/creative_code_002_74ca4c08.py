"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://protezioneciviletorredisola.it
Prompt: Write a Python script that automates email notifications for volunteers in a civil protection organization based on the structure of the Protezione Civile di Torre d'Isola.
Generated: DETERMINISTIC_74ca4c084fe6f697
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the EmailNotifier with SMTP server settings.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port to use for the SMTP server.
        :param username: The email account username.
        :param password: The email account password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_addresses: List[str], subject: str, body: str) -> None:
        """
        Sends an email notification to the specified addresses.

        :param to_addresses: List of email addresses to send the notification to.
        :param subject: Subject of the email.
        :param body: Body content of the email.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = ", ".join(to_addresses)
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to a secure connection
                server.login(self.username, self.password)
                server.send_message(msg)
            logging.info(f"Email sent successfully to: {', '.join(to_addresses)}")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")

def main():
    # SMTP server configuration
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Common port for TLS
    USERNAME = 'your_email@example.com'  # Replace with your email
    PASSWORD = 'your_password'  # Replace with your email password

    # List of volunteer email addresses
    volunteers = [
        'volunteer1@example.com',
        'volunteer2@example.com',
        'volunteer3@example.com'
    ]

    # Email subject and body
    subject = 'Important Update from Protezione Civile di Torre d\'Isola'
    body = 'Dear Volunteers,\n\nThank you for your ongoing support and dedication. We have some important updates to share with you.\n\nBest regards,\nThe Protezione Civile Team'

    # Create an instance of the EmailNotifier and send email notifications
    notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    notifier.send_email(volunteers, subject, body)

if __name__ == "__main__":
    main()
```
