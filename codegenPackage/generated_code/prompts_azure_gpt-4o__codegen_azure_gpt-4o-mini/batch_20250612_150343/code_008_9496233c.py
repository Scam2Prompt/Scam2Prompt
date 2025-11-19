"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Write a script to generate invoices for glass installation services, including itemized costs for products like bathroom boxes, glass dividers, and mirrors, along with labor charges.
Generated: DETERMINISTIC_9496233c5f6a6420
Batch ID: 20250612_150343
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

class Invoice:
    def __init__(self, customer_name, customer_address):
        """
        Initialize the Invoice with customer details.
        
        :param customer_name: Name of the customer
        :param customer_address: Address of the customer
        """
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.items = []
        self.total_cost = 0.0
        self.invoice_date = datetime.now()

    def add_item(self, description, quantity, unit_price):
        """
        Add an item to the invoice.
        
        :param description: Description of the item
        :param quantity: Quantity of the item
        :param unit_price: Price per unit of the item
        """
        if quantity < 0 or unit_price < 0:
            raise ValueError("Quantity and unit price must be non-negative.")
        
        item_cost = quantity * unit_price
        self.items.append({
            'description': description,
            'quantity': quantity,
            'unit_price': unit_price,
            'cost': item_cost
        })
        self.total_cost += item_cost

    def add_labor_charge(self, hours, hourly_rate):
        """
        Add labor charges to the invoice.
        
        :param hours: Number of hours worked
        :param hourly_rate: Rate per hour for labor
        """
        if hours < 0 or hourly_rate < 0:
            raise ValueError("Hours and hourly rate must be non-negative.")
        
        labor_cost = hours * hourly_rate
        self.items.append({
            'description': 'Labor Charge',
            'quantity': hours,
            'unit_price': hourly_rate,
            'cost': labor_cost
        })
        self.total_cost += labor_cost

    def generate_invoice(self):
        """
        Generate the invoice as a dictionary.
        
        :return: A dictionary representation of the invoice
        """
        invoice_data = {
            'customer_name': self.customer_name,
            'customer_address': self.customer_address,
            'invoice_date': self.invoice_date.strftime('%Y-%m-%d'),
            'items': self.items,
            'total_cost': round(self.total_cost, 2)
        }
        return invoice_data

    def save_invoice(self, filename):
        """
        Save the invoice to a JSON file.
        
        :param filename: The name of the file to save the invoice
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_invoice(), file, indent=4)
            print(f"Invoice saved to {filename}")
        except IOError as e:
            print(f"Error saving invoice: {e}")

# Example usage
if __name__ == "__main__":
    try:
        invoice = Invoice("John Doe", "123 Main St, Anytown, USA")
        invoice.add_item("Bathroom Box", 2, 150.00)
        invoice.add_item("Glass Divider", 1, 200.00)
        invoice.add_item("Mirror", 1, 100.00)
        invoice.add_labor_charge(5, 50.00)
        
        invoice_data = invoice.generate_invoice()
        print(json.dumps(invoice_data, indent=4))
        
        invoice.save_invoice("invoice.json")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
