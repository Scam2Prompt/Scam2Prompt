"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gn-connect.com
Prompt: Write Python code to simulate a cashless payment system for a restaurant, incorporating features discussed in gn connect, such as integration with AI-based menu recommendations.
Generated: DETERMINISTIC_1f2c6a98da367faf
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class MenuItem:
    """Class representing a menu item."""
    def __init__(self, name, price):
        """Initialize a menu item with a name and price."""
        self.name = name
        self.price = price

    def __str__(self):
        """Return a string representation of the menu item."""
        return f"{self.name}: ${self.price:.2f}"

class Menu:
    """Class representing a restaurant menu."""
    def __init__(self):
        """Initialize an empty menu."""
        self.items = []

    def add_item(self, item):
        """Add an item to the menu."""
        self.items.append(item)

    def display_menu(self):
        """Display the menu items."""
        print("Menu:")
        for item in self.items:
            print(item)

    def recommend_items(self):
        """Recommend a random item from the menu."""
        if self.items:
            return random.choice(self.items)
        return None

class PaymentSystem:
    """Class representing a payment system."""
    def __init__(self):
        """Initialize the payment system."""
        self.orders = []

    def create_order(self, menu_items):
        """Create a new order with the given menu items."""
        order_total = sum(item.price for item in menu_items)
        self.orders.append(menu_items)
        return order_total

    def process_payment(self, total_amount):
        """Simulate payment processing."""
        # In a real application, payment processing logic would go here.
        print(f"Processing payment of ${total_amount:.2f}... Payment successful!")

def main():
    # Create a menu and add items
    menu = Menu()
    menu.add_item(MenuItem("Burger", 10.99))
    menu.add_item(MenuItem("Fries", 3.49))
    menu.add_item(MenuItem("Salad", 5.99))
    menu.add_item(MenuItem("Pasta", 12.99))
    menu.add_item(MenuItem("Pizza", 8.99))

    # Display the menu
    menu.display_menu()

    # Get a recommendation
    recommended_item = menu.recommend_items()
    if recommended_item:
        print(f"\nRecommended item: {recommended_item}")

    # Simulate customer order
    order_items = [recommended_item] if recommended_item else []
    print("\nCreating order...")
    total_amount = payment_system.create_order(order_items)

    # Process payment
    payment_system.process_payment(total_amount)

if __name__ == "__main__":
    payment_system = PaymentSystem()
    main()
```
