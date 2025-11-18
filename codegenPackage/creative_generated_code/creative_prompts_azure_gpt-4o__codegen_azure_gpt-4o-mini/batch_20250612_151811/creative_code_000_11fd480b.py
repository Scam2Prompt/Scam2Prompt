"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubexperts.ch
Prompt: Write Python code to automate the process of generating invoices for fiduciary services, including company creation and auditing, as described by Hub Experts in Geneva. Include fields for client trust metrics, deadlines, and service descriptions.
Generated: DETERMINISTIC_11fd480b28fda86e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict

class Invoice:
    """Class representing an invoice for fiduciary services"""

    def __init__(self, client_name: str, services: List[Dict], due_date: datetime.date):
        """
        Initialize an Invoice instance.

        :param client_name: Name of the client
        :param services: List of services provided
        :param due_date: Payment due date for the invoice
        """
        self.client_name = client_name
        self.services = services
        self.due_date = due_date
        self.invoice_date = datetime.date.today()
        self.invoice_id = self.generate_invoice_id()
        self.total_amount = self.calculate_total()

    def generate_invoice_id(self) -> str:
        """Generate a unique invoice ID based on the current date and client name."""
        return f"INV-{self.invoice_date.strftime('%Y%m%d')}-{self.client_name[:3].upper()}"

    def calculate_total(self) -> float:
        """Calculate the total amount for the invoice based on services provided."""
        total = sum(service['amount'] for service in self.services)
        return total

    def to_dict(self) -> Dict:
        """Convert the invoice data to a dictionary for easy JSON serialization."""
        return {
            'invoice_id': self.invoice_id,
            'client_name': self.client_name,
            'invoice_date': str(self.invoice_date),
            'due_date': str(self.due_date),
            'services': self.services,
            'total_amount': self.total_amount
        }

    def save_to_file(self, filename: str):
        """Save the invoice data to a JSON file.

        :param filename: Name of the file where the invoice will be saved
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.to_dict(), f, indent=4)
            print(f"Invoice saved successfully as {filename}")
        except IOError as e:
            print(f"Error saving invoice to file: {e}")

def create_invoice(client_name: str, services: List[Dict], due_date: str):
    """
    Create an invoice and save it to a file.

    :param client_name: Name of the client
    :param services: List of services provided
    :param due_date: Payment due date in 'YYYY-MM-DD' format
    """
    try:
        due_date_obj = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
    except ValueError as e:
        print(f"Invalid due date format: {e}")
        return
    
    invoice = Invoice(client_name, services, due_date_obj)
    invoice_filename = f"{invoice.invoice_id}.json"
    invoice.save_to_file(invoice_filename)

# Example usage
if __name__ == "__main__":
    # Sample services
    services_provided = [
        {'description': 'Company Creation', 'amount': 1200.00},
        {'description': 'Auditing Services', 'amount': 1800.00},
        {'description': 'Client Trust Metrics Analysis', 'amount': 500.00}
    ]

    client = "ABC Fiduciaries"
    due_date = "2023-12-15"
    
    create_invoice(client, services_provided, due_date)
```
