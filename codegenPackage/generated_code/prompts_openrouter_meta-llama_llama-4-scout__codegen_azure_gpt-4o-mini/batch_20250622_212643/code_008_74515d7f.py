"""
Generated Code Metadata:
========================
Original URL: https://toncoin.forum
Prompt: "Generate a notification system code for sending emails about new domain name sales or inquiries on a platform like toncoin.forum."
Generated: DETERMINISTIC_74515d7f007d110a
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailNotificationSystem with SMTP server details.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port for the SMTP server.
        :param username: The username for the SMTP server.
        :param password: The password for the SMTP server.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email notification.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)

            logging.info(f"Email sent successfully to {recipient}")

        except smtplib.SMTPException as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

    def notify_new_sale(self, sale_info: Dict[str, str], recipients: List[str]) -> None:
        """
        Notify recipients about a new domain name sale.

        :param sale_info: A dictionary containing sale information (e.g., domain name, price).
        :param recipients: A list of email addresses to notify.
        """
        subject = f"New Domain Sale: {sale_info['domain']}"
        body = f"Congratulations! The domain {sale_info['domain']} has been sold for {sale_info['price']}."

        for recipient in recipients:
            self.send_email(recipient, subject, body)

    def notify_new_inquiry(self, inquiry_info: Dict[str, str], recipients: List[str]) -> None:
        """
        Notify recipients about a new domain name inquiry.

        :param inquiry_info: A dictionary containing inquiry information (e.g., domain name, inquiry details).
        :param recipients: A list of email addresses to notify.
        """
        subject = f"New Domain Inquiry: {inquiry_info['domain']}"
        body = f"You have received a new inquiry for the domain {inquiry_info['domain']}.\nDetails: {inquiry_info['details']}"

        for recipient in recipients:
            self.send_email(recipient, subject, body)

# Example usage
if __name__ == "__main__":
    # SMTP configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of the notification system
    notification_system = EmailNotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Example sale notification
    sale_info = {'domain': 'example.com', 'price': '$1000'}
    recipients = ['recipient1@example.com', 'recipient2@example.com']
    notification_system.notify_new_sale(sale_info, recipients)

    # Example inquiry notification
    inquiry_info = {'domain': 'example.com', 'details': 'Interested in purchasing the domain.'}
    notification_system.notify_new_inquiry(inquiry_info, recipients)
```
