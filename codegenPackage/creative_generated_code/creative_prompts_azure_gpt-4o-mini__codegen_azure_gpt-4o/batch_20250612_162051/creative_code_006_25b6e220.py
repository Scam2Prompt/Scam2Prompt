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
import datetime

# Constants representing order statuses
STATUS_PENDING = "Pending"
STATUS_IN_TRANSIT = "In Transit"
STATUS_OUT_FOR_DELIVERY = "Out for Delivery"
STATUS_DELIVERED = "Delivered"

class Order:
    """
    Represents a customer's order in the logistics tracking system.
    Contains details about the order, current status, and timestamps.
    """
    def __init__(self, order_id, customer_email):
        self.order_id = order_id
        self.customer_email = customer_email
        self.status = STATUS_PENDING
        self.status_updated_at = datetime.datetime.now()

    def update_status(self, new_status):
        """
        Updates the status of the order and records the timestamp of the update.

        Args:
            new_status (str): The new order status.
        """
        if new_status not in [STATUS_PENDING, STATUS_IN_TRANSIT, STATUS_OUT_FOR_DELIVERY, STATUS_DELIVERED]:
            raise ValueError("Invalid status provided.")
        
        self.status = new_status
        self.status_updated_at = datetime.datetime.now()

    def get_status_summary(self):
        """
        Retrieves a summary of the order's current status.

        Returns:
            dict: Contains the order ID, current status, and timestamp.
        """
        return {
            "order_id": self.order_id,
            "status": self.status,
            "last_updated": self.status_updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }

def send_email(to_email, subject, message):
    """
    Simulates sending an email notification to the customer.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        message (str): Email body content.
    """
    # Note: This is a simplified email simulation. In production, use an email library such as smtplib or a service like SendGrid.
    print(f"Sending email to {to_email}...\nSubject: {subject}\nMessage: {message}\n")

def notify_customer(order):
    """
    Notifies the customer about their order status update via email.

    Args:
        order (Order): The order object containing details about the status.
    """
    summary = order.get_status_summary()
    subject = f"Order #{summary['order_id']} Status Update"
    message = (f"Dear Customer,\n\nYour order status has been updated to '{summary['status']}'.\n"
               f"Last updated: {summary['last_updated']}\n\nThank you for shopping with Bern Wears!")
    send_email(order.customer_email, subject, message)

# Example of usage
if __name__ == "__main__":
    try:
        # Create an order
        order = Order(order_id="BW12345", customer_email="customer@example.com")
        
        # Update the order status and notify the customer
        order.update_status(STATUS_IN_TRANSIT)
        notify_customer(order)

        order.update_status(STATUS_OUT_FOR_DELIVERY)
        notify_customer(order)

        order.update_status(STATUS_DELIVERED)
        notify_customer(order)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
