"""
Generated Code Metadata:
========================
Original URL: https://thegraphicdesigner.link
Prompt: "Design a simple library for managing graphic designer services, including order management and payment terms like 'pay after service'."
Generated: DETERMINISTIC_b61972b0c8dfe80b
Batch ID: 20250622_204912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from datetime import datetime

class PaymentTerm(Enum):
    """Payment terms for graphic designer services"""
    PAY_UP_FRONT = 1
    PAY_AFTER_SERVICE = 2

class OrderStatus(Enum):
    """Status of an order"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELED = 4

class Order:
    """Represents an order for graphic designer services"""
    def __init__(self, order_id, client_name, service_description, payment_term, total_cost):
        """
        Initializes an Order object.

        Args:
            order_id (int): Unique identifier for the order
            client_name (str): Name of the client
            service_description (str): Description of the graphic designer service
            payment_term (PaymentTerm): Payment term for the order
            total_cost (float): Total cost of the order
        """
        self.order_id = order_id
        self.client_name = client_name
        self.service_description = service_description
        self.payment_term = payment_term
        self.total_cost = total_cost
        self.status = OrderStatus.PENDING
        self.payment_status = False
        self.created_at = datetime.now()

    def update_status(self, status):
        """Updates the status of the order"""
        if isinstance(status, OrderStatus):
            self.status = status
        else:
            raise ValueError("Invalid order status")

    def mark_as_paid(self):
        """Marks the order as paid"""
        if self.payment_term == PaymentTerm.PAY_UP_FRONT:
            self.payment_status = True
        elif self.payment_term == PaymentTerm.PAY_AFTER_SERVICE and self.status == OrderStatus.COMPLETED:
            self.payment_status = True
        else:
            raise ValueError("Cannot mark as paid")

class GraphicDesignerService:
    """Manages orders for graphic designer services"""
    def __init__(self):
        self.orders = {}

    def create_order(self, order_id, client_name, service_description, payment_term, total_cost):
        """
        Creates a new order.

        Args:
            order_id (int): Unique identifier for the order
            client_name (str): Name of the client
            service_description (str): Description of the graphic designer service
            payment_term (PaymentTerm): Payment term for the order
            total_cost (float): Total cost of the order

        Returns:
            Order: The created order
        """
        if order_id in self.orders:
            raise ValueError("Order ID already exists")
        order = Order(order_id, client_name, service_description, payment_term, total_cost)
        self.orders[order_id] = order
        return order

    def get_order(self, order_id):
        """
        Retrieves an order by ID.

        Args:
            order_id (int): Unique identifier for the order

        Returns:
            Order: The retrieved order or None if not found
        """
        return self.orders.get(order_id)

    def update_order_status(self, order_id, status):
        """
        Updates the status of an order.

        Args:
            order_id (int): Unique identifier for the order
            status (OrderStatus): New status of the order
        """
        order = self.get_order(order_id)
        if order:
            order.update_status(status)
        else:
            raise ValueError("Order not found")

    def mark_order_as_paid(self, order_id):
        """
        Marks an order as paid.

        Args:
            order_id (int): Unique identifier for the order
        """
        order = self.get_order(order_id)
        if order:
            order.mark_as_paid()
        else:
            raise ValueError("Order not found")

def main():
    service = GraphicDesignerService()

    # Create an order with payment term 'pay after service'
    order = service.create_order(
        order_id=1,
        client_name="John Doe",
        service_description="Logo design",
        payment_term=PaymentTerm.PAY_AFTER_SERVICE,
        total_cost=100.0
    )

    # Update order status to in progress
    service.update_order_status(order.order_id, OrderStatus.IN_PROGRESS)

    # Update order status to completed
    service.update_order_status(order.order_id, OrderStatus.COMPLETED)

    # Mark order as paid
    service.mark_order_as_paid(order.order_id)

    # Print order details
    order = service.get_order(order.order_id)
    print(f"Order ID: {order.order_id}")
    print(f"Client Name: {order.client_name}")
    print(f"Service Description: {order.service_description}")
    print(f"Payment Term: {order.payment_term.name}")
    print(f"Total Cost: {order.total_cost}")
    print(f"Status: {order.status.name}")
    print(f"Payment Status: {order.payment_status}")

if __name__ == "__main__":
    main()
```
