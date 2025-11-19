"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Write a Python script to manage accounts payable and receivable for a small business, including tasks like payment tracking and invoice generation, similar to services offered by CG Bókhald.
Generated: DETERMINISTIC_66ac95e7670b4511
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

class Account:
    """Class to represent a financial account for a business."""
    
    def __init__(self, name):
        self.name = name
        self.payables = []
        self.receivables = []

    def add_payable(self, amount, due_date, description):
        """Add a payable entry to the account."""
        payable = {
            'amount': amount,
            'due_date': due_date,
            'description': description,
            'paid': False
        }
        self.payables.append(payable)

    def add_receivable(self, amount, due_date, description):
        """Add a receivable entry to the account."""
        receivable = {
            'amount': amount,
            'due_date': due_date,
            'description': description,
            'received': False
        }
        self.receivables.append(receivable)

    def mark_payable_as_paid(self, index):
        """Mark a payable as paid by its index."""
        try:
            self.payables[index]['paid'] = True
        except IndexError:
            print("Error: Payable index out of range.")

    def mark_receivable_as_received(self, index):
        """Mark a receivable as received by its index."""
        try:
            self.receivables[index]['received'] = True
        except IndexError:
            print("Error: Receivable index out of range.")

    def generate_invoice(self, index):
        """Generate an invoice for a receivable."""
        try:
            receivable = self.receivables[index]
            invoice = f"Invoice for {receivable['description']}\n" \
                      f"Amount: {receivable['amount']}\n" \
                      f"Due Date: {receivable['due_date']}\n"
            return invoice
        except IndexError:
            return "Error: Receivable index out of range."

    def save_to_file(self, filename):
        """Save account data to a JSON file."""
        data = {
            'name': self.name,
            'payables': self.payables,
            'receivables': self.receivables
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_file(cls, filename):
        """Load account data from a JSON file."""
        if not os.path.exists(filename):
            print("Error: File not found.")
            return None
        with open(filename, 'r') as f:
            data = json.load(f)
            account = cls(data['name'])
            account.payables = data['payables']
            account.receivables = data['receivables']
            return account

def main():
    """Main function to demonstrate account management."""
    account = Account("Small Business")

    # Adding payables
    account.add_payable(1500, datetime.date(2023, 12, 1), "Office Rent")
    account.add_payable(300, datetime.date(2023, 11, 15), "Utilities")

    # Adding receivables
    account.add_receivable(2000, datetime.date(2023, 11, 30), "Client Invoice #1")
    account.add_receivable(500, datetime.date(2023, 12, 15), "Client Invoice #2")

    # Marking a payable as paid
    account.mark_payable_as_paid(0)

    # Generating an invoice
    invoice = account.generate_invoice(0)
    print(invoice)

    # Saving account data to a file
    account.save_to_file('account_data.json')

    # Loading account data from a file
    loaded_account = Account.load_from_file('account_data.json')
    if loaded_account:
        print(f"Loaded account: {loaded_account.name}")

if __name__ == "__main__":
    main()
```
