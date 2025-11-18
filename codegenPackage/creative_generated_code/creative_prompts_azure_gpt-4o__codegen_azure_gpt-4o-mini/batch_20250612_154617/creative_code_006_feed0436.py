"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Create a program that generates invoices for automotive glass replacement materials ordered from "Гарант," including payment terms like deferred payment options mentioned on the site.
Generated: DETERMINISTIC_feed043614af1dd3
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class Invoice:
    def __init__(self, customer_name, customer_address, items, payment_terms):
        """
        Initialize an invoice with customer details, items, and payment terms.

        :param customer_name: str - Name of the customer
        :param customer_address: str - Address of the customer
        :param items: list - List of items (dicts) with 'description', 'quantity', and 'price_per_item'
        :param payment_terms: str - Payment terms, e.g., 'Deferred payment'
        """
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.items = items
        self.payment_terms = payment_terms
        self.invoice_number = self.generate_invoice_number()
        self.date_issued = datetime.now()
        self.due_date = self.calculate_due_date()

    def generate_invoice_number(self):
        """Generate a unique invoice number based on the current timestamp."""
        return f"INV-{int(datetime.now().timestamp())}"

    def calculate_due_date(self):
        """
        Calculate the due date based on payment terms.
        Assuming deferred payment is 30 days from the date issued.
        """
        if self.payment_terms.lower() == "deferred payment":
            return self.date_issued + timedelta(days=30)
        return self.date_issued  # Same day payment for other terms

    def calculate_total(self):
        """Calculate the total amount of the invoice."""
        total = sum(item['quantity'] * item['price_per_item'] for item in self.items)
        return total

    def to_dict(self):
        """Convert invoice details to a dictionary format."""
        return {
            'invoice_number': self.invoice_number,
            'date_issued': self.date_issued.strftime('%Y-%m-%d'),
            'due_date': self.due_date.strftime('%Y-%m-%d'),
            'customer': {
                'name': self.customer_name,
                'address': self.customer_address
            },
            'items': self.items,
            'total_amount': self.calculate_total(),
            'payment_terms': self.payment_terms
        }

    def save_to_file(self, filename):
        """
        Save the invoice to a JSON file.

        :param filename: str - Filename to save the invoice
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.to_dict(), f, indent=4)
            print(f"Invoice saved to {filename}")
        except IOError as e:
            print(f"Error saving invoice: {e}")


def main():
    # Sample customer details
    customer_name = "John Doe"
    customer_address = "1234 Elm St, Springfield"
    
    # Sample items ordered
    items = [
        {'description': 'Windshield Replacement', 'quantity': 1, 'price_per_item': 300.00},
        {'description': 'Side Window Replacement', 'quantity': 2, 'price_per_item': 150.00},
    ]
    
    # Payment terms
    payment_terms = "Deferred payment"
    
    # Create an invoice instance
    invoice = Invoice(customer_name, customer_address, items, payment_terms)
    
    # Save the invoice to a file
    invoice.save_to_file('invoice.json')

if __name__ == '__main__':
    main()
```
