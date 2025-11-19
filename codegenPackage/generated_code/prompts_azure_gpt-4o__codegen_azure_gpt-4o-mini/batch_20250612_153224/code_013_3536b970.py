"""
Generated Code Metadata:
========================
Original URL: https://alexashipping.com
Prompt: Write a script to automate customer notifications for shipment updates, inspired by Alexa Shipping's personalized service approach.
Generated: DETERMINISTIC_3536b9706884920b
Batch ID: 20250612_153224
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

class ShipmentNotification:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the ShipmentNotification class with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email notification.

        :param recipient: Recipient's email address
        :param subject: Subject of the email
        :param body: Body of the email
        """
        try:
            # Create the email message
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
                logging.info(f"Email sent to {recipient} with subject: {subject}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}. Error: {e}")

    def notify_customers(self, shipments: List[Dict[str, str]]) -> None:
        """
        Notify customers about their shipment updates.

        :param shipments: List of shipments with customer email, subject, and body
        """
        for shipment in shipments:
            recipient = shipment.get('email')
            subject = shipment.get('subject')
            body = shipment.get('body')

            if recipient and subject and body:
                self.send_email(recipient, subject, body)
            else:
                logging.warning("Incomplete shipment information, skipping notification.")

# Example usage
if __name__ == "__main__":
    # SMTP configuration
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    USERNAME = 'your_email@example.com'
    PASSWORD = 'your_password'

    # Create an instance of ShipmentNotification
    notifier = ShipmentNotification(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Example shipment updates
    shipments_to_notify = [
        {
            'email': 'customer1@example.com',
            'subject': 'Your shipment is on the way!',
            'body': 'Hello! Your order has been shipped and is on its way to you.'
        },
        {
            'email': 'customer2@example.com',
            'subject': 'Your shipment has been delivered!',
            'body': 'Good news! Your order has been delivered. Thank you for shopping with us.'
        }
    ]

    # Notify customers
    notifier.notify_customers(shipments_to_notify)
```
