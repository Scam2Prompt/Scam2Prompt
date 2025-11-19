"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bernwears.com
Prompt: Provide a code example for a logistics tracking system that updates customers on their order status, as described in the shipping process of Bern Wears.
Generated: DETERMINISTIC_25b6e2206f28ea68
Batch ID: 20250612_162051
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

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OrderStatus:
    """Class representing the status of an order in the logistics tracking system."""
    
    def __init__(self, order_id, customer_email):
        self.order_id = order_id
        self.customer_email = customer_email
        self.status = "Pending"  # Initial order status

    def update_status(self, new_status):
        """Update the status of the order and notify the customer."""
        if new_status not in ["Pending", "Shipped", "In Transit", "Delivered", "Cancelled"]:
            logging.error("Invalid status update attempted: %s", new_status)
            raise ValueError("Invalid status update.")
        
        logging.info("Updating order %s status from %s to %s", self.order_id, self.status, new_status)
        self.status = new_status
        self.notify_customer()

    def notify_customer(self):
        """Notify the customer via email about the status update."""
        try:
            # Set up email server and credentials
            email_sender = "your_email@example.com"
            email_password = "your_password"
            email_receiver = self.customer_email

            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = email_sender
            msg['To'] = email_receiver
            msg['Subject'] = f"Order Status Update: {self.order_id}"

            # Email body
            body = f"Dear Customer,\n\nYour order {self.order_id} status has been updated to: {self.status}.\n\nThank you for shopping with us!"
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            with smtplib.SMTP('smtp.example.com', 587) as server:  # Use your SMTP server details
                server.starttls()  # Upgrade to a secure connection
                server.login(email_sender, email_password)
                server.sendmail(email_sender, email_receiver, msg.as_string())
                
            logging.info("Notification email sent to %s for order %s", email_receiver, self.order_id)

        except Exception as e:
            logging.error("Failed to send email notification: %s", str(e))
            raise

# Example usage
if __name__ == "__main__":
    try:
        order = OrderStatus(order_id="12345", customer_email="customer@example.com")
        order.update_status("Shipped")
        order.update_status("In Transit")
        order.update_status("Delivered")
    except Exception as e:
        logging.critical("An error occurred: %s", str(e))
```
