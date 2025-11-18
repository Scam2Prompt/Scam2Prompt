"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashinfo.tech
Prompt: Write a script to send automated email notifications to customers about new arrivals or special offers at Akash Infotech.
Generated: DETERMINISTIC_588d508dd25a644e
Batch ID: 20250612_154115
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """
        Initializes the EmailNotifier with SMTP server details.

        :param smtp_server: The address of the SMTP server.
        :param smtp_port: The port for the SMTP server.
        :param smtp_user: The username for the SMTP server.
        :param smtp_password: The password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, subject: str, body: str, recipients: List[str]) -> None:
        """
        Sends an email with the given subject and body to the list of recipients.

        :param subject: The subject of the email.
        :param body: The body content of the email.
        :param recipients: A list of email addresses to send the email to.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject

            # Attach the body text to the email
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Start TLS encryption
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.smtp_user, recipients, msg.as_string())

            logging.info(f"Email sent successfully to: {', '.join(recipients)}")
        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email: {e}")

def main():
    # SMTP configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_USER = 'your_email@example.com'
    SMTP_PASSWORD = 'your_password'

    # Create an instance of EmailNotifier
    email_notifier = EmailNotifier(SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)

    # Define email subject and body
    subject = "New Arrivals and Special Offers at Akash Infotech!"
    body = """
    Dear Valued Customer,

    We are excited to inform you about our new arrivals and special offers! 
    Visit our website for more details and take advantage of these great deals.

    Best Regards,
    Akash Infotech Team
    """

    # List of recipient email addresses
    recipients = ['customer1@example.com', 'customer2@example.com']

    # Send the email notification
    email_notifier.send_email(subject, body, recipients)

if __name__ == "__main__":
    main()
```
