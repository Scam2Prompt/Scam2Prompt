"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://konveksibajumurah.com
Prompt: Generate code to automate order management for a garment manufacturing business, including tracking uniform sizes and delivery timelines, inspired by Real Garment's workflow.
Generated: DETERMINISTIC_cf5f9aed79c01bd6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Order:
    """
    Represents an order in the garment manufacturing business.
    Includes customer details, order details, and delivery timeline.
    """
    def __init__(self, order_id, customer_name, uniform_sizes, order_date, delivery_deadline):
        self.order_id = order_id
        self.customer_name = customer_name
        self.uniform_sizes = uniform_sizes  # Dictionary with sizes as keys and quantities as values
        self.order_date = order_date
        self.delivery_deadline = delivery_deadline
        self.status = "Pending"  # Status can be "Pending", "In Progress", or "Delivered"

    def update_status(self, new_status):
        """
        Updates the status of the order.
        """
        valid_statuses = ["Pending", "In Progress", "Delivered"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid options are: {valid_statuses}")

    def __str__(self):
        """
        Returns a string representation of the order details.
        """
        return (f"Order ID: {self.order_id}\n"
                f"Customer: {self.customer_name}\n"
                f"Sizes & Quantities: {self.uniform_sizes}\n"
                f"Order Date: {self.order_date.strftime('%Y-%m-%d')}\n"
                f"Delivery Deadline: {self.delivery_deadline.strftime('%Y-%m-%d')}\n"
                f"Status: {self.status}\n")


class OrderManager:
    """
    Manages multiple orders, allowing creation, tracking, updating, and delivery management.
    """
    def __init__(self):
        self.orders = {}  # Dictionary to store orders with order_id as the key

    def create_order(self, order_id, customer_name, uniform_sizes, delivery_deadline):
        """
        Creates a new order and adds it to the orders dictionary.
        """
        if order_id in self.orders:
            raise ValueError(f"Order ID {order_id} already exists. Please use a unique ID.")
        
        order_date = datetime.datetime.now()
        new_order = Order(order_id, customer_name, uniform_sizes, order_date, delivery_deadline)
        self.orders[order_id] = new_order

    def update_order_status(self, order_id, new_status):
        """
        Updates the status of an existing order.
        """
        if order_id not in self.orders:
            raise ValueError(f"Order ID {order_id} not found.")
        
        self.orders[order_id].update_status(new_status)

    def retrieve_order(self, order_id):
        """
        Retrieves the details of a specific order.
        """
        if order_id not in self.orders:
            raise ValueError(f"Order ID {order_id} not found.")
        
        return self.orders[order_id]

    def list_orders(self):
        """
        Lists all orders in the system.
        """
        return [str(order) for order in self.orders.values()]

    def check_delayed_orders(self):
        """
        Checks for orders that have passed their delivery deadline but are not marked as "Delivered".
        """
        delayed_orders = []
        current_date = datetime.datetime.now()
        for order in self.orders.values():
            if order.status != "Delivered" and order.delivery_deadline < current_date:
                delayed_orders.append(order)
        return [str(order) for order in delayed_orders]


# Example usage
if __name__ == "__main__":
    # Initialize the order manager
    manager = OrderManager()

    try:
        # Create some orders
        manager.create_order("001", "Alice", {"S": 10, "M": 20, "L": 15}, datetime.datetime(2023, 11, 15))
        manager.create_order("002", "Bob", {"S": 5, "M": 10}, datetime.datetime(2023, 11, 10))

        # Update order status
        manager.update_order_status("001", "In Progress")

        # Retrieve and print details of a specific order
        print(manager.retrieve_order("001"))

        # List all orders
        print("\nAll Orders:")
        for order in manager.list_orders():
            print(order)

        # Check for delayed orders
        print("\nDelayed Orders:")
        for order in manager.check_delayed_orders():
            print(order)

    except ValueError as e:
        print(f"Error: {e}")
```
