"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Develop a feature for an e-commerce site to manage customer orders and track purchases, inspired by the "Meus Pedidos" functionality on ebrasilbrazz.
Generated: DETERMINISTIC_91442800e4221f8a
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# order_manager.py

from enum import Enum
from typing import List, Dict
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OrderStatus(str, Enum):
    """Order status types"""
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELED = "canceled"

class Order:
    """Represents a customer order"""
    def __init__(self, order_id: int, customer_id: int, order_date: datetime, status: OrderStatus):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.status = status
        self.items: List[Dict] = []

    def add_item(self, product_id: int, quantity: int, price: float):
        """Add an item to the order"""
        self.items.append({"product_id": product_id, "quantity": quantity, "price": price})

    def update_status(self, status: OrderStatus):
        """Update the order status"""
        self.status = status

    def __repr__(self):
        return f"Order(order_id={self.order_id}, customer_id={self.customer_id}, status={self.status})"

class OrderManager:
    """Manages customer orders and tracks purchases"""
    def __init__(self):
        self.orders: Dict[int, Order] = {}

    def create_order(self, customer_id: int) -> Order:
        """Create a new order for a customer"""
        order_id = len(self.orders) + 1
        order = Order(order_id, customer_id, datetime.now(), OrderStatus.PENDING)
        self.orders[order_id] = order
        return order

    def get_order(self, order_id: int) -> Order:
        """Retrieve an order by ID"""
        try:
            return self.orders[order_id]
        except KeyError:
            logger.error(f"Order not found: {order_id}")
            raise ValueError(f"Order not found: {order_id}")

    def update_order_status(self, order_id: int, status: OrderStatus):
        """Update the status of an order"""
        try:
            order = self.get_order(order_id)
            order.update_status(status)
        except ValueError as e:
            logger.error(e)

    def add_item_to_order(self, order_id: int, product_id: int, quantity: int, price: float):
        """Add an item to an order"""
        try:
            order = self.get_order(order_id)
            order.add_item(product_id, quantity, price)
        except ValueError as e:
            logger.error(e)

    def list_orders(self, customer_id: int) -> List[Order]:
        """List all orders for a customer"""
        return [order for order in self.orders.values() if order.customer_id == customer_id]

def main():
    # Example usage
    order_manager = OrderManager()

    # Create a new order
    customer_id = 1
    order = order_manager.create_order(customer_id)
    print(f"Created order: {order}")

    # Add items to the order
    order_manager.add_item_to_order(order.order_id, 1, 2, 10.99)
    order_manager.add_item_to_order(order.order_id, 2, 1, 5.99)

    # Update order status
    order_manager.update_order_status(order.order_id, OrderStatus.SHIPPED)

    # List all orders for the customer
    orders = order_manager.list_orders(customer_id)
    print(f"Orders for customer {customer_id}: {orders}")

if __name__ == "__main__":
    main()
```
