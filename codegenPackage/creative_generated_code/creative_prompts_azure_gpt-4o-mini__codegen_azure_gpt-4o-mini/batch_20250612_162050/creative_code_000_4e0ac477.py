"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cgbokhald.is
Prompt: Generate a Python script to automate the process of issuing invoices as described by CGBókhald's bookkeeping services.
Generated: DETERMINISTIC_4e0ac477fc3f232a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
import uuid
import os

class Invoice:
    """Class representing an invoice."""
    
    def __init__(self, customer_name, items, due_date):
        """
        Initialize an Invoice instance.
        
        :param customer_name: Name of the customer
        :param items: List of tuples containing item descriptions and their prices
        :param due_date: Due date for the invoice
        """
        self.invoice_id = str(uuid.uuid4())  # Unique identifier for the invoice
        self.customer_name = customer_name
        self.items = items  # List of (description, price)
        self.due_date = due_date
        self.issue_date = datetime.date.today()
        self.total_amount = self.calculate_total()

    def calculate_total(self):
        """Calculate the total amount of the invoice."""
        return sum(price for _, price in self.items)

    def to_dict(self):
        """Convert the invoice details to a dictionary."""
        return {
            'invoice_id': self.invoice_id,
            'customer_name': self.customer_name,
            'items': self.items,
            'due_date': self.due_date.isoformat(),
            'issue_date': self.issue_date.isoformat(),
            'total_amount': self.total_amount,
        }

    def save_to_file(self, directory='invoices'):
        """
        Save the invoice as a JSON file.
        
        :param directory: Directory to save the invoice file
        """
        os.makedirs(directory, exist_ok=True)  # Create directory if it does not exist
        file_path = os.path.join(directory, f'invoice_{self.invoice_id}.json')
        
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.to_dict(), json_file, indent=4)
            print(f'Invoice saved to {file_path}')
        except IOError as e:
            print(f'Error saving invoice to file: {e}')

def create_invoice(customer_name, items, due_date):
    """
    Create and save an invoice.
    
    :param customer_name: Name of the customer
    :param items: List of tuples containing item descriptions and their prices
    :param due_date: Due date for the invoice
    """
    try:
        invoice = Invoice(customer_name, items, due_date)
        invoice.save_to_file()
    except Exception as e:
        print(f'Error creating invoice: {e}')

if __name__ == '__main__':
    # Example usage of the create_invoice function
    customer = "John Doe"
    items = [("Service A", 150.00), ("Service B", 300.00)]
    due_date = datetime.date(2023, 12, 30)

    create_invoice(customer, items, due_date)
```
