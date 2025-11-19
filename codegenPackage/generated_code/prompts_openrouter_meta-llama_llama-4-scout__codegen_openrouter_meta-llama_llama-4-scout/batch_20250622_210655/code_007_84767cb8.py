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
# Import required libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from logging.handlers import RotatingFileHandler
import os

# Set up logging configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a rotating file handler
file_handler = RotatingFileHandler('printing_service.log', maxBytes=1024*1024*10, backupCount=5)
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and attach it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class PrintingService:
    def __init__(self, smtp_server, smtp_port, from_email, password):
        """
        Initialize the PrintingService class.

        Args:
            smtp_server (str): The SMTP server to use.
            smtp_port (int): The SMTP port to use.
            from_email (str): The email address to send from.
            password (str): The password for the email account.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password

    def send_order_confirmation(self, to_email, order_number, order_details):
        """
        Send an order confirmation email to the customer.

        Args:
            to_email (str): The customer's email address.
            order_number (str): The order number.
            order_details (str): The order details.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = to_email
            msg['Subject'] = f"Order Confirmation: {order_number}"

            body = f"Dear Customer,\n\nYour order {order_number} has been confirmed.\n\nOrder Details:\n{order_details}\n\nThank you for your business."
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.password)
            text = msg.as_string()
            server.sendmail(self.from_email, to_email, text)
            server.quit()

            logger.info(f"Order confirmation email sent to {to_email} for order {order_number}")
            return True

        except Exception as e:
            logger.error(f"Error sending order confirmation email: {str(e)}")
            return False

    def send_shipping_update(self, to_email, order_number, shipping_update):
        """
        Send a shipping update email to the customer.

        Args:
            to_email (str): The customer's email address.
            order_number (str): The order number.
            shipping_update (str): The shipping update.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = to_email
            msg['Subject'] = f"Shipping Update: {order_number}"

            body = f"Dear Customer,\n\nWe have an update on the shipping status of your order {order_number}:\n\n{shipping_update}\n\nThank you for your patience."
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.password)
            text = msg.as_string()
            server.sendmail(self.from_email, to_email, text)
            server.quit()

            logger.info(f"Shipping update email sent to {to_email} for order {order_number}")
            return True

        except Exception as e:
            logger.error(f"Error sending shipping update email: {str(e)}")
            return False


def main():
    # SMTP server settings
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "your-email@gmail.com"
    password = "your-password"

    printing_service = PrintingService(smtp_server, smtp_port, from_email, password)

    # Example usage
    to_email = "customer@example.com"
    order_number = "ORD-12345"
    order_details = "1 x Business Card (500pcs)\n1 x Brochure (1000pcs)"
    shipping_update = "Your order has been shipped via UPS and will be delivered within 3-5 business days."

    printing_service.send_order_confirmation(to_email, order_number, order_details)
    printing_service.send_shipping_update(to_email, order_number, shipping_update)


if __name__ == "__main__":
    main()
```
