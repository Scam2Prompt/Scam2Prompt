"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Generate code to automate order management for a garment manufacturing business, including tracking uniform sizes and delivery timelines, inspired by Real Garment's workflow.
Generated: DETERMINISTIC_cf5f9aed79c01bd6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Order:
    """Class to represent an order in the garment manufacturing business."""
    
    def __init__(self, order_id: int, customer_name: str, uniform_size: str, quantity: int, delivery_date: datetime.date):
        self.order_id = order_id
        self.customer_name = customer_name
        self.uniform_size = uniform_size
        self.quantity = quantity
        self.delivery_date = delivery_date
        self.status = 'Pending'  # Initial status of the order

    def update_status(self, new_status: str):
        """Update the status of the order."""
        valid_statuses = ['Pending', 'In Production', 'Shipped', 'Delivered', 'Cancelled']
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")

class OrderManager:
    """Class to manage orders in the garment manufacturing business."""
    
    def __init__(self):
        self.orders: List[Order] = []  # List to store orders

    def add_order(self, order: Order):
        """Add a new order to the order list."""
        self.orders.append(order)

    def get_order(self, order_id: int) -> Optional[Order]:
        """Retrieve an order by its ID."""
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None  # Return None if order not found

    def update_order_status(self, order_id: int, new_status: str):
        """Update the status of an existing order."""
        order = self.get_order(order_id)
        if order:
            order.update_status(new_status)
        else:
            raise ValueError(f"Order with ID {order_id} not found.")

    def list_orders(self) -> List[Dict]:
        """List all orders with their details."""
        return [{
            'order_id': order.order_id,
            'customer_name': order.customer_name,
            'uniform_size': order.uniform_size,
            'quantity': order.quantity,
            'delivery_date': order.delivery_date,
            'status': order.status
        } for order in self.orders]

def main():
    """Main function to demonstrate order management."""
    order_manager = OrderManager()

    # Example orders
    try:
        order1 = Order(order_id=1, customer_name='John Doe', uniform_size='M', quantity=10, delivery_date=datetime.date(2023, 12, 1))
        order_manager.add_order(order1)

        order2 = Order(order_id=2, customer_name='Jane Smith', uniform_size='L', quantity=5, delivery_date=datetime.date(2023, 11, 15))
        order_manager.add_order(order2)

        # Update order status
        order_manager.update_order_status(1, 'In Production')

        # List all orders
        orders = order_manager.list_orders()
        for order in orders:
            print(order)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
