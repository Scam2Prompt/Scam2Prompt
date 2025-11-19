"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Write a Python script that can track orders from an online electronics store, similar to the features on the provided webpage.
Generated: DETERMINISTIC_43725f58d2300607
Batch ID: 20250612_162742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime


class Order:
    """
    Represents an order in the electronics store.
    Each order has a unique ID, customer name, items, total price, and status.
    """

    def __init__(self, customer_name, items):
        """
        Initialize an order with customer name and items.

        :param customer_name: Name of the customer placing the order.
        :param items: List of items in the order. Each item is a dictionary with 'name', 'quantity', and 'price'.
        """
        self.order_id = str(uuid.uuid4())  # Generate a unique order ID
        self.customer_name = customer_name
        self.items = items
        self.total_price = self.calculate_total_price()
        self.status = "Pending"  # Default status is 'Pending'
        self.created_at = datetime.now()  # Timestamp for when the order was created

    def calculate_total_price(self):
        """
        Calculate the total price of the order based on the items.

        :return: Total price of the order.
        """
        return sum(item['quantity'] * item['price'] for item in self.items)

    def update_status(self, new_status):
        """
        Update the status of the order.

        :param new_status: New status to set for the order.
        """
        valid_statuses = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")


class OrderTracker:
    """
    Tracks and manages orders for the electronics store.
    """

    def __init__(self):
        """
        Initialize the order tracker with an empty list of orders.
        """
        self.orders = []

    def create_order(self, customer_name, items):
        """
        Create a new order and add it to the tracker.

        :param customer_name: Name of the customer placing the order.
        :param items: List of items in the order.
        :return: The newly created order.
        """
        try:
            new_order = Order(customer_name, items)
            self.orders.append(new_order)
            return new_order
        except Exception as e:
            print(f"Error creating order: {e}")
            return None

    def get_order_by_id(self, order_id):
        """
        Retrieve an order by its ID.

        :param order_id: ID of the order to retrieve.
        :return: The order with the specified ID, or None if not found.
        """
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def list_orders(self):
        """
        List all orders in the tracker.

        :return: List of all orders.
        """
        return self.orders

    def update_order_status(self, order_id, new_status):
        """
        Update the status of an order.

        :param order_id: ID of the order to update.
        :param new_status: New status to set for the order.
        :return: True if the status was updated successfully, False otherwise.
        """
        order = self.get_order_by_id(order_id)
        if order:
            try:
                order.update_status(new_status)
                return True
            except ValueError as e:
                print(f"Error updating order status: {e}")
                return False
        else:
            print(f"Order with ID {order_id} not found.")
            return False


# Example usage
if __name__ == "__main__":
    tracker = OrderTracker()

    # Create a new order
    items = [
        {"name": "Laptop", "quantity": 1, "price": 1000.00},
        {"name": "Mouse", "quantity": 2, "price": 25.00},
    ]
    order = tracker.create_order("John Doe", items)
    if order:
        print(f"Order created: {order.order_id}, Total Price: ${order.total_price:.2f}")

    # List all orders
    print("\nAll Orders:")
    for o in tracker.list_orders():
        print(f"ID: {o.order_id}, Customer: {o.customer_name}, Status: {o.status}")

    # Update order status
    if tracker.update_order_status(order.order_id, "Shipped"):
        print(f"\nOrder {order.order_id} status updated to 'Shipped'.")

    # Retrieve order by ID
    retrieved_order = tracker.get_order_by_id(order.order_id)
    if retrieved_order:
        print(f"\nRetrieved Order: ID: {retrieved_order.order_id}, Status: {retrieved_order.status}")
```
