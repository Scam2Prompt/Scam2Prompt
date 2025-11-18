"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bllabs.co
Prompt: Create a program to track and display order statuses for research products, referencing the "Track My Order" functionality on BioLongevity Labs.
Generated: DETERMINISTIC_5cdfc0cb268745dd
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional

class Order:
    """Class to represent an order for a research product."""

    def __init__(self, product_name: str, customer_name: str, quantity: int):
        self.order_id: str = str(uuid.uuid4())  # Unique identifier for the order
        self.product_name: str = product_name
        self.customer_name: str = customer_name
        self.quantity: int = quantity
        self.status: str = "Pending"  # Initial status of the order
        self.created_at: datetime = datetime.now()  # Timestamp of order creation

    def update_status(self, new_status: str):
        """Update the status of the order."""
        valid_statuses = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status '{new_status}'. Valid statuses are: {valid_statuses}")


class OrderTrackingSystem:
    """Class to manage orders and track their statuses."""

    def __init__(self):
        self.orders: Dict[str, Order] = {}  # Dictionary to store orders by order_id

    def create_order(self, product_name: str, customer_name: str, quantity: int) -> Order:
        """Create a new order and store it in the tracking system."""
        order = Order(product_name, customer_name, quantity)
        self.orders[order.order_id] = order
        return order

    def update_order_status(self, order_id: str, new_status: str) -> Optional[str]:
        """Update the status of an existing order."""
        order = self.orders.get(order_id)
        if order:
            try:
                order.update_status(new_status)
                return f"Order {order_id} status updated to '{new_status}'."
            except ValueError as e:
                return str(e)
        else:
            return f"Order ID '{order_id}' not found."

    def get_order_status(self, order_id: str) -> Optional[Dict[str, str]]:
        """Retrieve the status of a specific order."""
        order = self.orders.get(order_id)
        if order:
            return {
                "Order ID": order.order_id,
                "Product Name": order.product_name,
                "Customer Name": order.customer_name,
                "Quantity": order.quantity,
                "Status": order.status,
                "Created At": order.created_at.strftime("%Y-%m-%d %H:%M:%S")
            }
        else:
            return None


def main():
    tracking_system = OrderTrackingSystem()

    # Example of creating and tracking orders
    order1 = tracking_system.create_order("Lab Equipment X", "Alice Smith", 2)
    print(f"Created Order: {order1.order_id}")

    order2 = tracking_system.create_order("Research Kit Y", "Bob Johnson", 5)
    print(f"Created Order: {order2.order_id}")

    # Update and track order status
    print(tracking_system.update_order_status(order1.order_id, "Processing"))
    status = tracking_system.get_order_status(order1.order_id)
    print(f"Order Status: {status}")

    # Attempt to update with an invalid status
    print(tracking_system.update_order_status(order1.order_id, "Unknown Status"))

    # Retrieve order status for a non-existent order
    print(tracking_system.get_order_status("non-existent-order-id"))


if __name__ == "__main__":
    main()
```
