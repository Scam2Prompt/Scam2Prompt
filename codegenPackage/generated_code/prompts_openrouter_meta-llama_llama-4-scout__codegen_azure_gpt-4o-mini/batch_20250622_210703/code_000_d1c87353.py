"""
Generated Code Metadata:
========================
Original URL: https://hameiriz.co.il
Prompt: Write a Python script to manage invoices and expenses for a small business in Israel, considering tax regulations and accounting standards.
Generated: DETERMINISTIC_d1c873534af2177d
Batch ID: 20250622_210703
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
from decimal import Decimal, InvalidOperation

class Invoice:
    """Class to represent an invoice."""
    
    def __init__(self, invoice_id, client_name, amount, tax_rate=0.17):
        self.invoice_id = invoice_id
        self.client_name = client_name
        self.amount = Decimal(amount)
        self.tax_rate = Decimal(tax_rate)
        self.date_created = datetime.now()
        self.is_paid = False

    def calculate_tax(self):
        """Calculate the tax amount based on the invoice amount."""
        return self.amount * self.tax_rate

    def total_amount(self):
        """Calculate the total amount including tax."""
        return self.amount + self.calculate_tax()

    def mark_as_paid(self):
        """Mark the invoice as paid."""
        self.is_paid = True

    def to_dict(self):
        """Convert the invoice to a dictionary for JSON serialization."""
        return {
            'invoice_id': self.invoice_id,
            'client_name': self.client_name,
            'amount': str(self.amount),
            'tax_rate': str(self.tax_rate),
            'date_created': self.date_created.isoformat(),
            'is_paid': self.is_paid
        }

class Expense:
    """Class to represent an expense."""
    
    def __init__(self, expense_id, description, amount, tax_rate=0.17):
        self.expense_id = expense_id
        self.description = description
        self.amount = Decimal(amount)
        self.tax_rate = Decimal(tax_rate)
        self.date_created = datetime.now()

    def calculate_tax(self):
        """Calculate the tax amount based on the expense amount."""
        return self.amount * self.tax_rate

    def total_amount(self):
        """Calculate the total amount including tax."""
        return self.amount + self.calculate_tax()

    def to_dict(self):
        """Convert the expense to a dictionary for JSON serialization."""
        return {
            'expense_id': self.expense_id,
            'description': self.description,
            'amount': str(self.amount),
            'tax_rate': str(self.tax_rate),
            'date_created': self.date_created.isoformat()
        }

class InvoiceManager:
    """Class to manage invoices and expenses."""
    
    def __init__(self, filename='invoices_expenses.json'):
        self.filename = filename
        self.invoices = []
        self.expenses = []
        self.load_data()

    def load_data(self):
        """Load invoices and expenses from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.invoices = [Invoice(**inv) for inv in data.get('invoices', [])]
                self.expenses = [Expense(**exp) for exp in data.get('expenses', [])]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")

    def save_data(self):
        """Save invoices and expenses to a JSON file."""
        data = {
            'invoices': [inv.to_dict() for inv in self.invoices],
            'expenses': [exp.to_dict() for exp in self.expenses]
        }
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def add_invoice(self, invoice):
        """Add a new invoice to the manager."""
        self.invoices.append(invoice)
        self.save_data()

    def add_expense(self, expense):
        """Add a new expense to the manager."""
        self.expenses.append(expense)
        self.save_data()

    def get_total_invoices(self):
        """Calculate the total amount of all invoices."""
        return sum(inv.total_amount() for inv in self.invoices)

    def get_total_expenses(self):
        """Calculate the total amount of all expenses."""
        return sum(exp.total_amount() for exp in self.expenses)

def main():
    """Main function to run the invoice and expense manager."""
    manager = InvoiceManager()

    # Example usage
    try:
        # Adding an invoice
        invoice1 = Invoice(invoice_id='INV001', client_name='Client A', amount='1000.00')
        manager.add_invoice(invoice1)

        # Adding an expense
        expense1 = Expense(expense_id='EXP001', description='Office Supplies', amount='200.00')
        manager.add_expense(expense1)

        # Print totals
        print(f"Total Invoices: {manager.get_total_invoices()}")
        print(f"Total Expenses: {manager.get_total_expenses()}")

    except InvalidOperation as e:
        print(f"Error in amount format: {e}")

if __name__ == "__main__":
    main()
```
