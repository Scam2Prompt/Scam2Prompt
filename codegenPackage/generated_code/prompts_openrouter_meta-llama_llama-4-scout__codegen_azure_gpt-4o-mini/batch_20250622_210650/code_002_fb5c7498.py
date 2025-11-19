"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Generate a sample code for creating and sending invoices to clients, including calculating taxes and discounts, inspired by the invoicing services provided by CG Bókhald.
Generated: DETERMINISTIC_fb5c74983ea8e527
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime

class Invoice:
    def __init__(self, client_name, client_email):
        """
        Initialize an Invoice instance.

        :param client_name: Name of the client
        :param client_email: Email of the client
        """
        self.client_name = client_name
        self.client_email = client_email
        self.items = []
        self.tax_rate = Decimal('0.20')  # 20% tax rate
        self.discount_rate = Decimal('0.10')  # 10% discount rate

    def add_item(self, description, quantity, unit_price):
        """
        Add an item to the invoice.

        :param description: Description of the item
        :param quantity: Quantity of the item
        :param unit_price: Price per unit of the item
        """
        if quantity <= 0 or unit_price < 0:
            raise ValueError("Quantity must be greater than 0 and unit price must be non-negative.")
        
        item_total = Decimal(quantity) * Decimal(unit_price)
        self.items.append({
            'description': description,
            'quantity': quantity,
            'unit_price': unit_price,
            'total': item_total
        })

    def calculate_subtotal(self):
        """
        Calculate the subtotal of the invoice.

        :return: Subtotal amount
        """
        return sum(item['total'] for item in self.items)

    def calculate_tax(self):
        """
        Calculate the tax based on the subtotal.

        :return: Tax amount
        """
        subtotal = self.calculate_subtotal()
        return (subtotal * self.tax_rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def calculate_discount(self):
        """
        Calculate the discount based on the subtotal.

        :return: Discount amount
        """
        subtotal = self.calculate_subtotal()
        return (subtotal * self.discount_rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def calculate_total(self):
        """
        Calculate the total amount of the invoice.

        :return: Total amount after tax and discount
        """
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        discount = self.calculate_discount()
        total = subtotal + tax - discount
        return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def generate_invoice(self):
        """
        Generate a JSON representation of the invoice.

        :return: JSON string of the invoice
        """
        invoice_data = {
            'client_name': self.client_name,
            'client_email': self.client_email,
            'items': self.items,
            'subtotal': str(self.calculate_subtotal()),
            'tax': str(self.calculate_tax()),
            'discount': str(self.calculate_discount()),
            'total': str(self.calculate_total()),
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        return json.dumps(invoice_data, indent=4)

    def send_invoice(self):
        """
        Simulate sending the invoice to the client via email.

        :return: None
        """
        invoice_json = self.generate_invoice()
        # Here you would integrate with an email service to send the invoice
        print(f"Sending invoice to {self.client_email}:\n{invoice_json}")

# Example usage
if __name__ == "__main__":
    try:
        invoice = Invoice("John Doe", "john.doe@example.com")
        invoice.add_item("Web Development Services", 5, 100.00)
        invoice.add_item("Hosting Fee", 1, 50.00)
        invoice.send_invoice()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
