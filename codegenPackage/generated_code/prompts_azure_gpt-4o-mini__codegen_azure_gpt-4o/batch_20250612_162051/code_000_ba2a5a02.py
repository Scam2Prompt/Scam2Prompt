"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Generate a Python script that simulates a cloud kitchen model for food delivery, inspired by the operational strategies of Perfect Food Corner.
Generated: DETERMINISTIC_ba2a5a024cae4c58
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from datetime import datetime

# Define constants
MENU = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Pasta": 7.49,
    "Salad": 4.99,
    "Sushi": 12.99
}

ORDER_STATUSES = ["Received", "Preparing", "Ready for Delivery", "Out for Delivery", "Delivered"]

# Define classes
class Order:
    """
    Represents a food order in the cloud kitchen system.
    """
    def __init__(self, customer_name, items):
        self.order_id = self.generate_order_id()
        self.customer_name = customer_name
        self.items = items
        self.total_cost = self.calculate_total_cost()
        self.status = ORDER_STATUSES[0]
        self.timestamp = datetime.now()

    def generate_order_id(self):
        """
        Generates a unique order ID.
        """
        return f"ORD-{random.randint(1000, 9999)}"

    def calculate_total_cost(self):
        """
        Calculates the total cost of the order based on the menu prices.
        """
        return sum(MENU[item] for item in self.items)

    def update_status(self):
        """
        Updates the order status to the next stage.
        """
        current_index = ORDER_STATUSES.index(self.status)
        if current_index < len(ORDER_STATUSES) - 1:
            self.status = ORDER_STATUSES[current_index + 1]

    def __str__(self):
        """
        Returns a string representation of the order.
        """
        return (f"Order ID: {self.order_id}\n"
                f"Customer: {self.customer_name}\n"
                f"Items: {', '.join(self.items)}\n"
                f"Total Cost: ${self.total_cost:.2f}\n"
                f"Status: {self.status}\n"
                f"Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")


class CloudKitchen:
    """
    Represents the cloud kitchen system.
    """
    def __init__(self):
        self.orders = []

    def place_order(self, customer_name, items):
        """
        Places a new order in the system.
        """
        if not items:
            raise ValueError("Order must contain at least one item.")
        for item in items:
            if item not in MENU:
                raise ValueError(f"Item '{item}' is not available in the menu.")
        
        order = Order(customer_name, items)
        self.orders.append(order)
        print(f"Order placed successfully!\n{order}")
        return order

    def process_orders(self):
        """
        Simulates the processing of orders in the kitchen.
        """
        for order in self.orders:
            while order.status != "Delivered":
                time.sleep(1)  # Simulate time taken for each stage
                order.update_status()
                print(f"Order Update:\n{order}")

    def display_menu(self):
        """
        Displays the menu with prices.
        """
        print("Menu:")
        for item, price in MENU.items():
            print(f"{item}: ${price:.2f}")

# Main script
if __name__ == "__main__":
    kitchen = CloudKitchen()
    kitchen.display_menu()

    try:
        # Simulate placing orders
        order1 = kitchen.place_order("Alice", ["Burger", "Salad"])
        order2 = kitchen.place_order("Bob", ["Pizza", "Sushi"])

        # Simulate processing orders
        kitchen.process_orders()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
