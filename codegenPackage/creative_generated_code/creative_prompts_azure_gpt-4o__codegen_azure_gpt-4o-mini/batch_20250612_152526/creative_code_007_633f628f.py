"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manaftech.com
Prompt: Write a Python script to calculate the total cost of items in a shopping cart and generate a receipt using the Bixilon SRP-352plusIII Thermal Printer.
Generated: DETERMINISTIC_633f628f24f2c702
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import os
from escpos.printer import Serial
from decimal import Decimal, InvalidOperation

class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, name, price, quantity):
        """Add an item to the cart.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if price < 0:
            raise ValueError("Price must not be negative.")
        total_price = Decimal(price) * Decimal(quantity)
        self.items.append({'name': name, 'price': Decimal(price), 'quantity': quantity, 'total': total_price})

    def calculate_total(self):
        """Calculate the total cost of the items in the cart.

        Returns:
            Decimal: Total cost of the items in the cart.
        """
        return sum(item['total'] for item in self.items)

    def generate_receipt(self):
        """Generate a formatted receipt for the cart items.

        Returns:
            str: Formatted receipt string.
        """
        receipt_lines = ["Receipt:", "-" * 30]
        for item in self.items:
            receipt_lines.append(f"{item['name']} x{item['quantity']} - ${item['total']:.2f}")
        receipt_lines.append("-" * 30)
        receipt_lines.append(f"Total: ${self.calculate_total():.2f}")
        return "\n".join(receipt_lines)

def print_receipt(receipt):
    """Print the receipt using a thermal printer.

    Args:
        receipt (str): The receipt text to print.

    Raises:
        Exception: If printer connection fails or print fails.
    """
    try:
        # Replace '/dev/ttyUSB0' with your printer's correct port
        printer = Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)
        printer.text(receipt + "\n")
        printer.cut()
    except Exception as e:
        print(f"Error printing receipt: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """Main function to run the shopping cart program."""
    cart = ShoppingCart()
    
    # Example items
    items_to_add = [
        ("Milk", 2.50, 2),
        ("Bread", 1.20, 1),
        ("Eggs", 3.00, 1)
    ]
    
    for name, price, quantity in items_to_add:
        try:
            cart.add_item(name, price, quantity)
        except ValueError as e:
            print(f"Failed to add item '{name}': {e}", file=sys.stderr)
            continue

    total_cost = cart.calculate_total()
    print(f"Total cost: ${total_cost:.2f}")

    receipt = cart.generate_receipt()
    print(receipt)
    
    # Print the receipt
    print_receipt(receipt)

if __name__ == "__main__":
    main()
```
