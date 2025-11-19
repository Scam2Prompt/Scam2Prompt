"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Develop a program to manage customer orders for personalized promotional items, incorporating customization options like DTF printing and vinyl textile designs.
Generated: DETERMINISTIC_f5bcbc010a77c73c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from typing import List, Dict, Optional

class Order:
    """Class to represent a customer order for personalized promotional items."""
    
    def __init__(self, customer_name: str, item: str, customization: str):
        self.order_id: str = str(uuid.uuid4())  # Unique identifier for the order
        self.customer_name: str = customer_name  # Name of the customer
        self.item: str = item  # Item being ordered
        self.customization: str = customization  # Customization details
        self.status: str = "Pending"  # Initial status of the order

    def update_status(self, new_status: str) -> None:
        """Update the status of the order."""
        valid_statuses = ["Pending", "In Progress", "Completed", "Cancelled"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")

    def __repr__(self) -> str:
        return f"Order({self.order_id}, {self.customer_name}, {self.item}, {self.customization}, {self.status})"


class OrderManager:
    """Class to manage customer orders."""
    
    def __init__(self):
        self.orders: List[Order] = []  # List to store orders

    def create_order(self, customer_name: str, item: str, customization: str) -> Order:
        """Create a new order and add it to the order list."""
        if not customer_name or not item or not customization:
            raise ValueError("Customer name, item, and customization cannot be empty.")
        
        new_order = Order(customer_name, item, customization)
        self.orders.append(new_order)
        return new_order

    def get_order(self, order_id: str) -> Optional[Order]:
        """Retrieve an order by its ID."""
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None  # Return None if order not found

    def update_order_status(self, order_id: str, new_status: str) -> None:
        """Update the status of an existing order."""
        order = self.get_order(order_id)
        if order:
            order.update_status(new_status)
        else:
            raise ValueError(f"Order with ID {order_id} not found.")

    def list_orders(self) -> List[Dict]:
        """List all orders in a readable format."""
        return [vars(order) for order in self.orders]


# Example usage
if __name__ == "__main__":
    order_manager = OrderManager()
    
    try:
        # Create a new order
        order1 = order_manager.create_order("Alice Smith", "T-Shirt", "DTF Printing")
        print(f"Created Order: {order1}")

        # Update order status
        order_manager.update_order_status(order1.order_id, "In Progress")
        print(f"Updated Order: {order_manager.get_order(order1.order_id)}")

        # List all orders
        print("All Orders:", order_manager.list_orders())

    except ValueError as e:
        print(f"Error: {e}")
```
