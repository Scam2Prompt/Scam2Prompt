"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mnswap.org
Prompt: Write code to send automated email updates to subscribers about upcoming MN SWAP events, using the website's email subscription feature as a reference.
Generated: DETERMINISTIC_8eb7ca9594b80b7a
Batch ID: 20250612_142640
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

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """Initialize the EmailSender with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, subject: str, body: str, subscribers: List[str]) -> None:
        """Send an email to a list of subscribers.

        Args:
            subject (str): The subject of the email.
            body (str): The body of the email.
            subscribers (List[str]): A list of subscriber email addresses.

        Raises:
            Exception: If an error occurs while sending the email.
        """
        # Create a multipart email message
        message = MIMEMultipart()
        message['From'] = self.username
        message['Subject'] = subject

        # Attach the email body
        message.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send emails
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)

                for subscriber in subscribers:
                    message['To'] = subscriber
                    server.sendmail(self.username, subscriber, message.as_string())
                    logging.info(f"Email sent to {subscriber}")

        except Exception as e:
            logging.error(f"Failed to send email: {e}")
            raise

def main():
    """Main function to send automated email updates."""
    # Email server configuration - replace with actual credentials
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # List of subscribers (replace with actual list)
    subscribers = [
        'subscriber1@example.com',
        'subscriber2@example.com',
        'subscriber3@example.com'
    ]

    # Email content
    subject = "Upcoming MN SWAP Events"
    body = """\
    Hello,

    We are excited to inform you about the upcoming MN SWAP events. Stay tuned for more details!

    Best,
    The MN SWAP Team
    """

    # Instantiate the EmailSender and send the email
    email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    email_sender.send_email(subject, body, subscribers)

if __name__ == "__main__":
    main()
```
