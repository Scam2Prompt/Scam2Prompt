"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eximiousglobal.com
Prompt: Write a script to manage daily financial transactions such as recording sales, purchases, receipts, and payments, ensuring accurate bookkeeping as described in Eximious Global's administrative support services.
Generated: DETERMINISTIC_1d2cc46d7f28e475
Batch ID: 20250612_151811
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

class Transaction:
    """Class to represent a financial transaction."""
    
    def __init__(self, transaction_type, amount, description, date=None):
        self.transaction_type = transaction_type  # 'sale', 'purchase', 'receipt', or 'payment'
        self.amount = amount
        self.description = description
        self.date = date if date else datetime.now().isoformat()

    def to_dict(self):
        """Convert the transaction to a dictionary."""
        return {
            'transaction_type': self.transaction_type,
            'amount': self.amount,
            'description': self.description,
            'date': self.date
        }

class TransactionManager:
    """Class to manage financial transactions."""
    
    def __init__(self, filename='transactions.json'):
        self.filename = filename
        self.transactions = self.load_transactions()

    def load_transactions(self):
        """Load transactions from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Return empty list if file not found or empty

    def save_transactions(self):
        """Save transactions to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def record_transaction(self, transaction):
        """Record a new transaction."""
        if not isinstance(transaction, Transaction):
            raise ValueError("transaction must be an instance of Transaction")
        self.transactions.append(transaction.to_dict())
        self.save_transactions()

    def get_balance(self):
        """Calculate the current balance based on recorded transactions."""
        balance = 0
        for transaction in self.transactions:
            if transaction['transaction_type'] in ['sale', 'receipt']:
                balance += transaction['amount']
            elif transaction['transaction_type'] in ['purchase', 'payment']:
                balance -= transaction['amount']
        return balance

# Example usage
if __name__ == "__main__":
    # Initialize the transaction manager
    manager = TransactionManager()

    # Record various transactions
    try:
        manager.record_transaction(Transaction('sale', 150.00, 'Sale of goods'))
        manager.record_transaction(Transaction('purchase', 50.00, 'Purchase of supplies'))
        manager.record_transaction(Transaction('receipt', 200.00, 'Received payment from client'))
        manager.record_transaction(Transaction('payment', 75.00, 'Paid supplier'))

        # Print the current balance
        print(f"Current balance: ${manager.get_balance():.2f}")

    except ValueError as e:
        print(f"Error recording transaction: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
