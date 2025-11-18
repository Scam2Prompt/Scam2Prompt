"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Write a script to generate invoices for glass installation services, including itemized costs for products like bathroom boxes, glass dividers, and mirrors, along with labor charges.
Generated: DETERMINISTIC_9496233c5f6a6420
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class InvoiceItem:
    """Class representing an item in the invoice."""
    def __init__(self, description, unit_price, quantity):
        self.description = description
        self.unit_price = unit_price
        self.quantity = quantity

    def total_cost(self):
        """Calculate the total cost for this invoice item."""
        return self.unit_price * self.quantity


class Invoice:
    """Class representing the invoice for glass installation services."""
    def __init__(self, client_name):
        self.client_name = client_name
        self.items = []
        self labor_charge = 0

    def add_item(self, description, unit_price, quantity):
        """Add an item to the invoice."""
        item = InvoiceItem(description, unit_price, quantity)
        self.items.append(item)

    def set_labor_charge(self, labor_charge):
        """Set the labor charge for the installation service."""
        self.labor_charge = labor_charge

    def total_invoice(self):
        """Calculate the total invoice amount including labor charges."""
        total_items_cost = sum(item.total_cost() for item in self.items)
        return total_items_cost + self.labor_charge

    def generate_invoice(self):
        """Generate a formatted invoice summary."""
        invoice_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        invoice_summary = f"Invoice Date: {invoice_date}\nClient: {self.client_name}\n\nItems:\n"
        
        for item in self.items:
            invoice_summary += f"- {item.description}: ${item.unit_price:.2f} x {item.quantity} = ${item.total_cost():.2f}\n"
        
        invoice_summary += f"\nLabor Charge: ${self.labor_charge:.2f}\n"
        invoice_summary += f"Total Invoice Amount: ${self.total_invoice():.2f}\n"
        return invoice_summary


def main():
    """Main function to create and display an invoice for glass installation services."""
    try:
        # Collect client information and items for the invoice
        client_name = input("Enter client name: ")
        invoice = Invoice(client_name)

        # Adding items to the invoice
        while True:
            description = input("Enter item description (or type 'done' to finish): ")
            if description.lower() == 'done':
                break
            
            try:
                unit_price = float(input("Enter unit price: "))
                quantity = int(input("Enter quantity: "))
                invoice.add_item(description, unit_price, quantity)
            except ValueError:
                print("Invalid input. Please enter numeric values for unit price and quantity.")

        # Set labor charge
        try:
            labor_charge = float(input("Enter labor charge: "))
            invoice.set_labor_charge(labor_charge)
        except ValueError:
            print("Invalid input. Setting labor charge to $0.00.")
            invoice.set_labor_charge(0)

        # Generate and display the invoice
        print("\n" + "="*40)
        print(invoice.generate_invoice())
        print("="*40)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
