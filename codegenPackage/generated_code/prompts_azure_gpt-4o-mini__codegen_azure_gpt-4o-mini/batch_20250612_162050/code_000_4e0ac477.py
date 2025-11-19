"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Generate a Python script to automate the process of issuing invoices as described by CGBókhald's bookkeeping services.
Generated: DETERMINISTIC_4e0ac477fc3f232a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import List, Dict

class Invoice:
    """Class to represent an invoice."""
    
    def __init__(self, invoice_id: str, client_name: str, items: List[Dict[str, float]], due_date: str):
        """
        Initialize an Invoice instance.

        :param invoice_id: Unique identifier for the invoice
        :param client_name: Name of the client
        :param items: List of items in the invoice, each item is a dict with 'description' and 'amount'
        :param due_date: Due date for the invoice in 'YYYY-MM-DD' format
        """
        self.invoice_id = invoice_id
        self.client_name = client_name
        self.items = items
        self.due_date = due_date
        self.total_amount = self.calculate_total()

    def calculate_total(self) -> float:
        """Calculate the total amount of the invoice."""
        return sum(item['amount'] for item in self.items)

    def to_dict(self) -> Dict:
        """Convert the invoice to a dictionary for JSON serialization."""
        return {
            'invoice_id': self.invoice_id,
            'client_name': self.client_name,
            'items': self.items,
            'due_date': self.due_date,
            'total_amount': self.total_amount
        }

    def save_to_file(self, directory: str) -> None:
        """Save the invoice to a JSON file."""
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        file_path = os.path.join(directory, f"{self.invoice_id}.json")
        with open(file_path, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

def create_invoice(invoice_id: str, client_name: str, items: List[Dict[str, float]], due_date: str) -> Invoice:
    """
    Create an invoice and save it to a file.

    :param invoice_id: Unique identifier for the invoice
    :param client_name: Name of the client
    :param items: List of items in the invoice
    :param due_date: Due date for the invoice
    :return: Invoice object
    """
    try:
        invoice = Invoice(invoice_id, client_name, items, due_date)
        invoice.save_to_file('invoices')
        return invoice
    except Exception as e:
        print(f"Error creating invoice: {e}")
        raise

def main():
    """Main function to execute the invoice creation process."""
    # Example data for the invoice
    invoice_id = f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    client_name = "CGBókhald"
    items = [
        {"description": "Bookkeeping Service", "amount": 150.00},
        {"description": "Consultation Fee", "amount": 75.00}
    ]
    due_date = "2023-12-31"

    try:
        invoice = create_invoice(invoice_id, client_name, items, due_date)
        print(f"Invoice created successfully: {invoice.invoice_id}")
    except Exception as e:
        print(f"Failed to create invoice: {e}")

if __name__ == "__main__":
    main()
```
