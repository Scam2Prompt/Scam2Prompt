"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Create code for a notification system that alerts customers about service updates, such as cleaning or insulation progress, as described in شركة انجاز's service offerings.
Generated: DETERMINISTIC_c2a1cf556ac2e240
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

class NotificationSystem:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the NotificationSystem with SMTP server details.

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
        Send an email notification to a recipient.

        :param recipient: Email address of the recipient
        :param subject: Subject of the email
        :param body: Body content of the email
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

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

    def notify_customers(self, customers: List[Dict[str, str]], update_message: str) -> None:
        """
        Notify a list of customers about service updates.

        :param customers: List of dictionaries containing customer information (name and email)
        :param update_message: Message to be sent to customers
        """
        for customer in customers:
            recipient = customer.get('email')
            if recipient:
                subject = "Service Update Notification"
                body = f"Dear {customer.get('name')},\n\n{update_message}\n\nBest regards,\nشركة انجاز"
                self.send_email(recipient, subject, body)
            else:
                logging.warning("Customer email is missing, skipping notification.")

# Example usage
if __name__ == "__main__":
    # SMTP server configuration
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    USERNAME = "your_email@example.com"
    PASSWORD = "your_password"

    # Create an instance of the NotificationSystem
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # List of customers to notify
    customers_list = [
        {"name": "Ali", "email": "ali@example.com"},
        {"name": "Fatima", "email": "fatima@example.com"},
        {"name": "Omar", "email": None}  # Example of a customer with a missing email
    ]

    # Service update message
    service_update_message = "We are pleased to inform you that your cleaning service is scheduled for tomorrow at 10 AM."

    # Notify customers
    notification_system.notify_customers(customers_list, service_update_message)
```
