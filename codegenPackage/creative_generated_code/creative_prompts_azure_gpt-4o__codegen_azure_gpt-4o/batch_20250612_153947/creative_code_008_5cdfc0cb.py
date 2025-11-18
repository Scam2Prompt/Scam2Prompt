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

Below is a Python program that tracks and displays order statuses for research products, inspired by "Track My Order" functionality.

```python
import uuid

class Order:
    """
    Class to represent an order in the system.
    """

    def __init__(self, product_name, customer_name):
        """
        Initialize an Order object.
        :param product_name: Name of the product in the order.
        :param customer_name: Name of the customer placing the order.
        """
        self.order_id = str(uuid.uuid4())  # Generate a unique order ID
        self.product_name = product_name
        self.customer_name = customer_name
        self.status = "Pending"  # Default order status
    
    def update_status(self, new_status):
        """
        Update the status of the order.
        :param new_status: The new status to set for the order.
        """
        valid_statuses = {"Pending", "Processing", "Shipped", "Delivered", "Cancelled"}
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Must be one of {valid_statuses}.")
        self.status = new_status
    
    def __str__(self):
        """
        Return a string representation of the order.
        """
        return f"Order ID: {self.order_id}\nCustomer: {self.customer_name}\nProduct: {self.product_name}\nStatus: {self.status}"


class OrderTracker:
    """
    Class to track and manage multiple orders.
    """

    def __init__(self):
        """
        Initialize an OrderTracker object.
        """
        self.orders = {}  # Dictionary to store orders by their ID
    
    def create_order(self, product_name, customer_name):
        """
        Create a new order and add it to the tracker.
        :param product_name: Name of the product in the order.
        :param customer_name: Name of the customer placing the order.
        :return: The created Order object.
        """
        order = Order(product_name, customer_name)
        self.orders[order.order_id] = order
        return order
    
    def get_order(self, order_id):
        """
        Retrieve an order by its ID.
        :param order_id: ID of the order to retrieve.
        :return: The Order object if found, otherwise raises KeyError.
        """
        if order_id not in self.orders:
            raise KeyError(f"Order ID {order_id} not found.")
        return self.orders[order_id]
    
    def update_order_status(self, order_id, new_status):
        """
        Update the status of an existing order.
        :param order_id: ID of the order to update.
        :param new_status: The new status to set for the order.
        """
        order = self.get_order(order_id)
        order.update_status(new_status)

    def display_all_orders(self):
        """
        Display all orders and their statuses.
        """
        if not self.orders:
            print("No orders found.")
            return
        
        print("All Orders:")
        for order in self.orders.values():
            print(order)
            print("-" * 30)


# Main program functionality
if __name__ == "__main__":
    # Create an OrderTracker instance
    tracker = OrderTracker()

    try:
        # Create sample orders
        order1 = tracker.create_order("Stem Cell Research Kit", "Dr. Alice")
        order2 = tracker.create_order("Genomics Analysis Package", "Dr. Bob")
        
        # Update order statuses
        tracker.update_order_status(order1.order_id, "Processing")
        tracker.update_order_status(order2.order_id, "Shipped")
        
        # Display all orders
        tracker.display_all_orders()
        
        # Retrieve a specific order
        specific_order = tracker.get_order(order1.order_id)
        print("\nDetails of a specific order:")
        print(specific_order)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```

This program creates and tracks orders for research products, allowing functionality such as creating orders, updating statuses, and displaying orders with proper error handling and adherence to best practices.
