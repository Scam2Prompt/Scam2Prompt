"""
Generated Code Metadata:
========================
Original URL: https://renovation-toiture-toulouse.com
Prompt: "Create a sample invoice template for a roofing company in France, including items such as labor costs, materials, and taxes, inspired by the services offered by Renovation Toiture Toulouse."
Generated: DETERMINISTIC_c34630c7b3b1bc06
Batch ID: 20250622_210655
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
    def __init__(self, company_name, client_name, invoice_number):
        """
        Initialize the Invoice object with company and client details.
        
        :param company_name: Name of the roofing company
        :param client_name: Name of the client
        :param invoice_number: Unique invoice number
        """
        self.company_name = company_name
        self.client_name = client_name
        self.invoice_number = invoice_number
        self.items = []
        self.tax_rate = 0.20  # 20% VAT in France

    def add_item(self, description, quantity, unit_price):
        """
        Add an item to the invoice.
        
        :param description: Description of the item
        :param quantity: Quantity of the item
        :param unit_price: Price per unit of the item
        """
        if quantity <= 0 or unit_price < 0:
            raise ValueError("Quantity must be greater than 0 and unit price must be non-negative.")
        
        item_total = quantity * unit_price
        self.items.append({
            'description': description,
            'quantity': quantity,
            'unit_price': unit_price,
            'total': item_total
        })

    def calculate_total(self):
        """
        Calculate the total amount of the invoice including tax.
        
        :return: Total amount including tax
        """
        subtotal = sum(item['total'] for item in self.items)
        tax = subtotal * self.tax_rate
        total = subtotal + tax
        return total

    def generate_invoice(self):
        """
        Generate a JSON representation of the invoice.
        
        :return: JSON string of the invoice
        """
        invoice_data = {
            'invoice_number': self.invoice_number,
            'company_name': self.company_name,
            'client_name': self.client_name,
            'date': datetime.now().strftime("%Y-%m-%d"),
            'items': self.items,
            'subtotal': sum(item['total'] for item in self.items),
            'tax': self.calculate_total() - sum(item['total'] for item in self.items),
            'total': self.calculate_total()
        }
        return json.dumps(invoice_data, indent=4, ensure_ascii=False)

# Example usage
if __name__ == "__main__":
    try:
        invoice = Invoice("Renovation Toiture Toulouse", "Jean Dupont", "INV-001")
        invoice.add_item("Installation de toiture", 10, 150)  # Labor costs
        invoice.add_item("Tuiles en terre cuite", 100, 2)      # Materials
        invoice.add_item("Isolation", 50, 5)                    # Materials
        print(invoice.generate_invoice())
    except ValueError as e:
        print(f"Error: {e}")
```
