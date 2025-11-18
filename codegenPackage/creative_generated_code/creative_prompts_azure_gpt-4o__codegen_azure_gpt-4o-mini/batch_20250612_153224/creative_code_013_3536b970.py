"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Write a script to automate customer notifications for shipment updates, inspired by Alexa Shipping's personalized service approach.
Generated: DETERMINISTIC_3536b9706884920b
Batch ID: 20250612_153224
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
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ShipmentNotification:
    def __init__(self, smtp_server: str, smtp_port: int, smtp_user: str, smtp_password: str):
        """Initialize the ShipmentNotification with SMTP server configuration."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """Send an email notification to the customer."""
        # Create a multipart email
        msg = MIMEMultipart()
        msg['From'] = self.smtp_user
        msg['To'] = recipient
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)
                logging.info(f'Email sent to {recipient}')
        except Exception as e:
            logging.error(f'Failed to send email to {recipient}: {e}')

    def notify_customers(self, customer_data: List[Dict[str, str]]) -> None:
        """Notify all customers about their shipment updates."""
        for customer in customer_data:
            email = customer.get('email')
            shipment_status = customer.get('shipment_status')

            if email and shipment_status:
                subject = "Your Shipment Update"
                body = f"Hello {customer.get('name')},\n\nYour shipment status is: {shipment_status}.\n\nThank you for choosing us!"
                self.send_email(email, subject, body)
            else:
                logging.warning(f"Missing email or shipment status for customer: {customer}")

if __name__ == '__main__':
    # Example SMTP configuration (replace with actual values)
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_USER = 'user@example.com'
    SMTP_PASSWORD = 'yourpassword'

    # Sample customer data
    customers = [
        {'name': 'Alice', 'email': 'alice@example.com', 'shipment_status': 'Shipped'},
        {'name': 'Bob', 'email': 'bob@example.com', 'shipment_status': 'In Transit'},
        {'name': 'Charlie', 'email': '', 'shipment_status': 'Delivered'},  # Example of missing email
    ]

    # Create an instance of ShipmentNotification and notify customers
    notifier = ShipmentNotification(SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)
    notifier.notify_customers(customers)
```
