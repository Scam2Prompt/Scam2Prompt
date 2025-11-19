"""
Generated Code Metadata:
========================
Original URL: https://manaftech.com
Prompt: Write a Python script to calculate the total cost of items in a shopping cart and generate a receipt using the Bixilon SRP-352plusIII Thermal Printer.
Generated: DETERMINISTIC_633f628f24f2c702
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import time
from escpos.printer import Usb

# Constants for printer configuration
VENDOR_ID = 0x04b8  # Replace with your printer's vendor ID
PRODUCT_ID = 0x0202  # Replace with your printer's product ID

class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, name, price, quantity):
        """Add an item to the shopping cart.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item.
        """
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def calculate_total(self):
        """Calculate the total cost of items in the shopping cart.

        Returns:
            float: The total cost.
        """
        return sum(item['price'] * item['quantity'] for item in self.items)

    def generate_receipt(self):
        """Generate a formatted receipt for the items in the shopping cart.

        Returns:
            str: The formatted receipt.
        """
        receipt_lines = ["Receipt", "-------------------------"]
        for item in self.items:
            line = f"{item['name']} x {item['quantity']} @ ${item['price']:.2f} = ${item['price'] * item['quantity']:.2f}"
            receipt_lines.append(line)
        receipt_lines.append("-------------------------")
        receipt_lines.append(f"Total: ${self.calculate_total():.2f}")
        return "\n".join(receipt_lines)

def print_receipt(receipt):
    """Print the receipt using the thermal printer.

    Args:
        receipt (str): The receipt to print.
    """
    try:
        # Initialize the printer
        printer = Usb(VENDOR_ID, PRODUCT_ID)
        printer.text(receipt + "\n")
        printer.cut()
    except Exception as e:
        print(f"Error printing receipt: {e}", file=sys.stderr)

def main():
    """Main function to run the shopping cart application."""
    cart = ShoppingCart()

    # Example items to add to the cart
    try:
        cart.add_item("Apple", 0.50, 3)
        cart.add_item("Bread", 2.00, 1)
        cart.add_item("Milk", 1.50, 2)

        # Calculate total and generate receipt
        total_cost = cart.calculate_total()
        receipt = cart.generate_receipt()

        # Print the receipt
        print_receipt(receipt)

        print("Receipt printed successfully.")
    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```

Make sure to install the `python-escpos` library to interact with the thermal printer:

```bash
pip install python-escpos
```

Also, replace the `VENDOR_ID` and `PRODUCT_ID` with the actual values for your Bixilon SRP-352plusIII Thermal Printer.
