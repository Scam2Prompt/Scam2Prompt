"""
Generated Code Metadata:
========================
Original URL: https://putrastarboy.github.io
Prompt: Write a Python script to manage coffee orders for a shop like 8 Coffee, including taking orders, calculating totals, and providing a "Pesan Sekarang" (Order Now) functionality.
Generated: DETERMINISTIC_8c717749cd346111
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class CoffeeOrder:
    """Class to manage coffee orders for a coffee shop."""

    def __init__(self):
        """Initialize the coffee menu and an empty order list."""
        self.menu = {
            'Espresso': 2.50,
            'Latte': 3.50,
            'Cappuccino': 3.00,
            'Americano': 2.00,
            'Mocha': 3.75
        }
        self.orders = []

    def display_menu(self):
        """Display the coffee menu with prices."""
        print("Coffee Menu:")
        for coffee, price in self.menu.items():
            print(f"{coffee}: ${price:.2f}")

    def take_order(self):
        """Take an order from the user."""
        while True:
            coffee_type = input("Enter the coffee you want to order (or 'done' to finish): ").strip()
            if coffee_type.lower() == 'done':
                break
            if coffee_type in self.menu:
                self.orders.append(coffee_type)
                print(f"Added {coffee_type} to your order.")
            else:
                print("Sorry, we don't have that coffee. Please choose from the menu.")

    def calculate_total(self):
        """Calculate the total cost of the orders."""
        total = sum(self.menu[coffee] for coffee in self.orders)
        return total

    def place_order(self):
        """Place the order and display the total."""
        if not self.orders:
            print("No orders to place. Please add items to your order.")
            return
        
        total = self.calculate_total()
        print("\nYour order:")
        for coffee in self.orders:
            print(f"- {coffee}")
        print(f"Total: ${total:.2f}")
        print("Thank you for your order!")

def main():
    """Main function to run the coffee order management system."""
    coffee_order = CoffeeOrder()
    
    coffee_order.display_menu()
    coffee_order.take_order()
    coffee_order.place_order()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
```
