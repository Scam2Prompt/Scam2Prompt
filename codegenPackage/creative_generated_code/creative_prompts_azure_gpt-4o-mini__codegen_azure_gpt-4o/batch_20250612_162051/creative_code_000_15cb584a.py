"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bernwears.com
Prompt: Generate a code snippet for a custom sportswear order management system that includes features for material sourcing and quality control, as described by Bern Wears.
Generated: DETERMINISTIC_15cb584aee66af21
Batch ID: 20250612_162051
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


class Order:
    """
    Represents a custom sportswear order.
    """
    def __init__(self, customer_name, items, delivery_date):
        self.order_id = str(uuid.uuid4())  # Unique identifier for each order
        self.customer_name = customer_name
        self.items = items  # List of items in the order
        self.delivery_date = delivery_date  # Expected delivery date
        self.materials_sourced = False  # Flag for material sourcing status
        self.quality_checked = False  # Flag for quality control status
        self.order_status = "Pending"  # Initial order status
        self.created_at = datetime.now()  # Timestamp when order was created

    def source_materials(self):
        """
        Simulates material sourcing for the order.
        """
        try:
            # Simulating material sourcing (could involve database updates, etc.)
            self.materials_sourced = True
            print(f"Materials sourced for order {self.order_id}.")
        except Exception as e:
            print(f"Error sourcing materials for order {self.order_id}: {e}")

    def conduct_quality_control(self):
        """
        Simulates quality control checks for the order.
        """
        try:
            # Simulating quality control (could involve inspections, etc.)
            if not self.materials_sourced:
                raise ValueError("Materials must be sourced before conducting quality checks.")
            self.quality_checked = True
            print(f"Quality control completed for order {self.order_id}.")
        except Exception as e:
            print(f"Error during quality control for order {self.order_id}: {e}")

    def update_order_status(self, status):
        """
        Updates the status of the order.
        :param status: New status for the order (e.g., "In Progress", "Completed").
        """
        valid_statuses = ["Pending", "In Progress", "Completed", "Cancelled"]

        if status not in valid_statuses:
            raise ValueError(f"Invalid order status: {status}. Valid statuses are: {valid_statuses}.")
        self.order_status = status
        print(f"Order {self.order_id} status updated to '{self.order_status}'.")

    def __str__(self):
        """
        Returns a string representation of the order.
        """
        return (
            f"Order ID: {self.order_id}\n"
            f"Customer Name: {self.customer_name}\n"
            f"Items: {', '.join(self.items)}\n"
            f"Delivery Date: {self.delivery_date.strftime('%Y-%m-%d')}\n"
            f"Materials Sourced: {self.materials_sourced}\n"
            f"Quality Checked: {self.quality_checked}\n"
            f"Order Status: {self.order_status}\n"
            f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )


class OrderManagementSystem:
    """
    Manages custom sportswear orders.
    """
    def __init__(self):
        self.orders = []  # Stores all orders

    def create_order(self, customer_name, items, delivery_date):
        """
        Creates a new custom sportswear order.
        :param customer_name: Name of the customer placing the order.
        :param items: List of items included in the order.
        :param delivery_date: Expected delivery date for the order.
        """
        try:
            new_order = Order(customer_name, items, delivery_date)
            self.orders.append(new_order)
            print(f"Order created successfully: {new_order.order_id}")
            return new_order
        except Exception as e:
            print(f"Error creating order: {e}")

    def get_order_by_id(self, order_id):
        """
        Retrieves an order by its ID.
        :param order_id: Unique identifier of the order.
        :return: Order object if found; None otherwise.
        """
        for order in self.orders:
            if order.order_id == order_id:
                return order
        print(f"Order with ID {order_id} not found.")
        return None

    def list_orders(self):
        """
        Lists all orders in the system.
        """
        if not self.orders:
            print("No orders found.")
            return
        for order in self.orders:
            print(order)


if __name__ == "__main__":
    # Example usage of the Order Management System

    # Initialize the order management system
    system = OrderManagementSystem()

    # Create a new order
    order = system.create_order(
        customer_name="Bern Wears",
        items=["Custom Shirt - Blue", "Custom Shorts - Black"],
        delivery_date=datetime(2023, 12, 25)
    )

    # Source materials for the order
    if order:
        order.source_materials()

    # Conduct quality control
    if order:
        order.conduct_quality_control()

    # Update the order status
    if order:
        order.update_order_status("In Progress")

    # List all orders
    system.list_orders()
```
