"""
Generated Code Metadata:
========================
Original URL: https://printserves.com
Prompt: "Write a Python script to automate the process of sending order confirmations and shipping updates to customers for an online printing service like Printserves Nigeria."
Generated: DETERMINISTIC_84767cb8e848f809
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailSender with SMTP server details.

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
        Send an email to the specified recipient.

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
                logging.info(f"Email sent to {recipient} with subject: {subject}")

        except Exception as e:
            logging.error(f"Failed to send email to {recipient}. Error: {e}")

def send_order_confirmation(email_sender: EmailSender, customer_email: str, order_id: str) -> None:
    """
    Send an order confirmation email to the customer.

    :param email_sender: Instance of EmailSender
    :param customer_email: Customer's email address
    :param order_id: Order ID for the confirmation
    """
    subject = "Order Confirmation"
    body = f"Dear Customer,\n\nThank you for your order! Your order ID is {order_id}.\n\nBest regards,\nPrintserves Nigeria"
    email_sender.send_email(customer_email, subject, body)

def send_shipping_update(email_sender: EmailSender, customer_email: str, order_id: str, tracking_number: str) -> None:
    """
    Send a shipping update email to the customer.

    :param email_sender: Instance of EmailSender
    :param customer_email: Customer's email address
    :param order_id: Order ID for the update
    :param tracking_number: Tracking number for the shipment
    """
    subject = "Shipping Update"
    body = f"Dear Customer,\n\nYour order ID {order_id} has been shipped. Your tracking number is {tracking_number}.\n\nBest regards,\nPrintserves Nigeria"
    email_sender.send_email(customer_email, subject, body)

if __name__ == "__main__":
    # Example usage
    SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
    SMTP_PORT = 587  # Replace with your SMTP port
    USERNAME = "your_email@example.com"  # Replace with your email
    PASSWORD = "your_password"  # Replace with your email password

    email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Send order confirmation
    send_order_confirmation(email_sender, "customer@example.com", "123456")

    # Send shipping update
    send_shipping_update(email_sender, "customer@example.com", "123456", "TRACK123456")
```
