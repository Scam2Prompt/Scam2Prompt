"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Develop a script to automate the generation of invoices for purchases made on AirstyleArt, including itemized lists of stencils, paints, and accessories.
Generated: DETERMINISTIC_05d993082cfc511d
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict

class Invoice:
    def __init__(self, customer_name: str, items: List[Dict[str, float]], invoice_number: int):
        """
        Initialize the Invoice object.

        :param customer_name: Name of the customer
        :param items: List of items purchased, each represented as a dictionary with 'name' and 'price'
        :param invoice_number: Unique invoice number
        """
        self.customer_name = customer_name
        self.items = items
        self.invoice_number = invoice_number
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def calculate_total(self) -> float:
        """
        Calculate the total amount for the invoice.

        :return: Total amount as a float
        """
        return sum(item['price'] for item in self.items)

    def generate_invoice(self) -> str:
        """
        Generate a formatted invoice as a string.

        :return: Formatted invoice
        """
        total = self.calculate_total()
        invoice_lines = [f"Invoice Number: {self.invoice_number}",
                         f"Date: {self.date}",
                         f"Customer Name: {self.customer_name}",
                         "Items Purchased:"]
        
        for item in self.items:
            invoice_lines.append(f"- {item['name']}: ${item['price']:.2f}")

        invoice_lines.append(f"Total Amount: ${total:.2f}")
        return "\n".join(invoice_lines)

def save_invoice_to_file(invoice: Invoice, filename: str) -> None:
    """
    Save the generated invoice to a text file.

    :param invoice: Invoice object to save
    :param filename: Name of the file to save the invoice
    """
    try:
        with open(filename, 'w') as file:
            file.write(invoice.generate_invoice())
        print(f"Invoice saved to {filename}")
    except IOError as e:
        print(f"Error saving invoice to file: {e}")

def main():
    # Sample data for the invoice
    customer_name = "John Doe"
    items = [
        {"name": "Stencil A", "price": 15.99},
        {"name": "Paint B", "price": 7.49},
        {"name": "Accessory C", "price": 3.99}
    ]
    invoice_number = 1  # This should be generated dynamically in a real application

    # Create an Invoice object
    invoice = Invoice(customer_name, items, invoice_number)

    # Generate and save the invoice
    save_invoice_to_file(invoice, f"invoice_{invoice_number}.txt")

if __name__ == "__main__":
    main()
```
