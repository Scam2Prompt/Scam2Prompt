"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectfoodcorner.com
Prompt: Generate a Python script that simulates a cloud kitchen model for food delivery, inspired by the operational strategies of Perfect Food Corner.
Generated: DETERMINISTIC_ba2a5a024cae4c58
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from typing import List, Dict

class MenuItem:
    """Class representing a menu item in the cloud kitchen."""
    def __init__(self, name: str, price: float, prep_time: int):
        self.name = name
        self.price = price
        self.prep_time = prep_time

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Prep time: {self.prep_time} mins)"

class Order:
    """Class representing an order made by a customer."""
    def __init__(self, items: List[MenuItem]):
        self.items = items
        self.total_price = sum(item.price for item in items)
        self.total_prep_time = max(item.prep_time for item in items)  # Assume max prep time for the order

    def __str__(self):
        items_str = ', '.join(str(item) for item in self.items)
        return f"Order: [{items_str}] | Total Price: ${self.total_price:.2f} | Total Prep Time: {self.total_prep_time} mins"

class CloudKitchen:
    """Class representing the cloud kitchen, managing menu items and processing orders."""
    def __init__(self, menu: List[MenuItem]):
        self.menu = menu

    def display_menu(self):
        """Displays the available menu items."""
        print("Menu:")
        for item in self.menu:
            print(item)

    def take_order(self, selected_items: List[str]) -> Order:
        """Processes an order based on selected menu item names."""
        order_items = []
        for item_name in selected_items:
            item = self.find_menu_item(item_name)
            if item:
                order_items.append(item)
            else:
                raise ValueError(f"Menu item '{item_name}' not found.")
        
        order = Order(order_items)
        return order

    def find_menu_item(self, item_name: str) -> MenuItem:
        """Finds a menu item by its name."""
        for item in self.menu:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def simulate_order_processing(self, order: Order):
        """Simulates the order processing time."""
        print(f"Processing order: {order}")
        print("Starting preparation...")
        time.sleep(order.total_prep_time)  # Simulating time taken for preparation
        print("Order is ready for delivery!")

def main():
    # Create sample menu items
    menu_items = [
        MenuItem("Margherita Pizza", 8.99, 15),
        MenuItem("Vegetable Pasta", 7.49, 10),
        MenuItem("Caesar Salad", 6.99, 5),
        MenuItem("Chocolate Cake", 4.99, 8),
        MenuItem("Grilled Chicken", 12.99, 20)
    ]

    # Initialize the Cloud Kitchen with the menu
    kitchen = CloudKitchen(menu_items)

    # Display menu
    kitchen.display_menu()

    # Simulate taking an order; in a real application, this could come from a user input
    selected_items = random.sample([item.name for item in menu_items], k=3)  # Randomly select 3 items

    try:
        order = kitchen.take_order(selected_items)
        kitchen.simulate_order_processing(order)
    except ValueError as e:
        print(f"Error processing order: {e}")

if __name__ == "__main__":
    main()
```
