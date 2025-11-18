"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Write a program to generate a detailed invoice for a customer purchasing plexiglass and polycarbonate sheets, including CNC cutting services, as described on Bursa Pleksi Merkezi's website.
Generated: DETERMINISTIC_df244939e535b9ed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Invoice Generator for Plexiglass and Polycarbonate Sheets with CNC Cutting Services

This program calculates the total cost of an order for plexiglass and polycarbonate sheets,
as well as CNC cutting services. It generates a detailed invoice for the customer.

Written in Python.
"""

import sys

class InvoiceGenerator:
    def __init__(self, customer_name):
        """
        Initialize an InvoiceGenerator instance with customer details.
        :param customer_name: Name of the customer
        """
        self.customer_name = customer_name
        self.items = []

    def add_item(self, description, quantity, unit_price):
        """
        Add an item to the invoice.
        :param description: Item description (e.g., Plexiglass Sheets, CNC Cutting)
        :param quantity: Quantity of the item purchased
        :param unit_price: Unit price of the item
        """
        if quantity <= 0 or unit_price < 0:
            raise ValueError("Quantity must be positive and unit price cannot be negative.")
        self.items.append({"description": description, "quantity": quantity, "unit_price": unit_price})

    def calculate_total(self):
        """
        Calculate the total invoice amount.
        :return: Total amount for the invoice
        """
        return sum(item["quantity"] * item["unit_price"] for item in self.items)

    def generate_invoice(self):
        """
        Generate a detailed invoice for the customer.
        :return: Formatted invoice as a string
        """
        invoice = f"--- Invoice for {self.customer_name} ---\n"
        invoice += f"{'Item':<25} {'Qty':<10} {'Unit Price':<15} {'Total':<15}\n"
        invoice += "-" * 65 + "\n"

        for item in self.items:
            total = item["quantity"] * item["unit_price"]
            invoice += f"{item['description']:<25} {item['quantity']:<10} ${item['unit_price']:<15.2f} ${total:<15.2f}\n"

        invoice += "-" * 65 + "\n"
        invoice += f"GRAND TOTAL: ${self.calculate_total():.2f}\n"
        invoice += "-" * 65
        return invoice


def main():
    """
    Main function to demonstrate the functionality of InvoiceGenerator.
    """
    try:
        # Example customer and inputs
        customer_name = "John Doe"
        invoice = InvoiceGenerator(customer_name)

        # Adding items (description, quantity, unit price)
        invoice.add_item("Plexiglass Sheets (5mm)", 10, 50.0)
        invoice.add_item("Polycarbonate Sheets (3mm)", 5, 70.0)
        invoice.add_item("CNC Cutting Service", 2, 100.0)

        # Generate and print the invoice
        print(invoice.generate_invoice())
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
