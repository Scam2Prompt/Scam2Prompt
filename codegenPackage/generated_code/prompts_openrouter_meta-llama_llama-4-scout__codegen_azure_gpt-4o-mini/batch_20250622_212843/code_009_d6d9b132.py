"""
Generated Code Metadata:
========================
Original URL: https://florerialima.com
Prompt: Write a Python script to automate the process of sending order confirmations and thank-you messages to customers who purchase from Florería Lima's online store.
Generated: DETERMINISTIC_d6d9b1320d2fa448
Batch ID: 20250622_212843
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
                logging.info(f"Email sent to {recipient} successfully.")
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")

def create_order_confirmation_email(customer_name: str, order_details: Dict) -> str:
    """
    Create the order confirmation email content.
    
    :param customer_name: Name of the customer
    :param order_details: Dictionary containing order details
    :return: Formatted email body
    """
    order_items = "\n".join([f"{item['name']} (Qty: {item['quantity']})" for item in order_details['items']])
    return (f"Dear {customer_name},\n\n"
            f"Thank you for your order! Here are the details:\n\n"
            f"Order ID: {order_details['order_id']}\n"
            f"Items:\n{order_items}\n\n"
            "We appreciate your business!\n"
            "Best regards,\n"
            "Florería Lima")

def create_thank_you_email(customer_name: str) -> str:
    """
    Create the thank-you email content.
    
    :param customer_name: Name of the customer
    :return: Formatted email body
    """
    return (f"Dear {customer_name},\n\n"
            "Thank you for shopping with us! We hope you enjoy your purchase.\n"
            "If you have any questions, feel free to reach out.\n\n"
            "Best wishes,\n"
            "Florería Lima")

def main(orders: List[Dict], email_sender: EmailSender) -> None:
    """
    Main function to send order confirmation and thank-you emails.
    
    :param orders: List of orders with customer details
    :param email_sender: Instance of EmailSender to send emails
    """
    for order in orders:
        customer_name = order['customer_name']
        recipient_email = order['email']
        
        # Create and send order confirmation email
        order_confirmation_email = create_order_confirmation_email(customer_name, order)
        email_sender.send_email(recipient_email, "Order Confirmation", order_confirmation_email)
        
        # Create and send thank-you email
        thank_you_email = create_thank_you_email(customer_name)
        email_sender.send_email(recipient_email, "Thank You for Your Purchase", thank_you_email)

if __name__ == "__main__":
    # Example SMTP configuration (replace with actual credentials)
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    USERNAME = "your_email@example.com"
    PASSWORD = "your_password"

    # Sample orders data
    orders_data = [
        {
            'customer_name': 'John Doe',
            'email': 'john.doe@example.com',
            'order_id': '12345',
            'items': [{'name': 'Roses', 'quantity': 2}, {'name': 'Tulips', 'quantity': 5}]
        },
        {
            'customer_name': 'Jane Smith',
            'email': 'jane.smith@example.com',
            'order_id': '12346',
            'items': [{'name': 'Lilies', 'quantity': 3}]
        }
    ]

    # Create an instance of EmailSender
    email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Send emails for the orders
    main(orders_data, email_sender)
```
