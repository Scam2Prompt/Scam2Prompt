"""
Generated Code Metadata:
========================
Original URL: https://eximiousglobal.com
Prompt: Write a script to manage daily financial transactions such as recording sales, purchases, receipts, and payments, ensuring accurate bookkeeping as described in Eximious Global's administrative support services.
Generated: DETERMINISTIC_1d2cc46d7f28e475
Batch ID: 20250612_151811
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

class Transaction:
    """Class to represent a financial transaction."""
    
    def __init__(self, transaction_type, amount, description, date=None):
        self.transaction_type = transaction_type  # Type of transaction: 'sale', 'purchase', 'receipt', 'payment'
        self.amount = amount                      # Amount of the transaction
        self.description = description            # Description of the transaction
        self.date = date if date else datetime.now().isoformat()  # Date of the transaction

    def to_dict(self):
        """Convert the transaction to a dictionary for easy serialization."""
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
            return []  # Return an empty list if file not found or empty

    def save_transactions(self):
        """Save transactions to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, transaction):
        """Add a new transaction to the list and save it."""
        if not isinstance(transaction, Transaction):
            raise ValueError("Invalid transaction object.")
        
        self.transactions.append(transaction.to_dict())
        self.save_transactions()

    def get_transactions(self):
        """Retrieve all transactions."""
        return self.transactions

    def get_balance(self):
        """Calculate the current balance based on transactions."""
        balance = 0
        for transaction in self.transactions:
            if transaction['transaction_type'] in ['sale', 'receipt']:
                balance += transaction['amount']
            elif transaction['transaction_type'] in ['purchase', 'payment']:
                balance -= transaction['amount']
        return balance

def main():
    """Main function to demonstrate transaction management."""
    manager = TransactionManager()

    # Example transactions
    try:
        sale = Transaction(transaction_type='sale', amount=150.00, description='Sale of product A')
        manager.add_transaction(sale)

        purchase = Transaction(transaction_type='purchase', amount=50.00, description='Purchase of supplies')
        manager.add_transaction(purchase)

        receipt = Transaction(transaction_type='receipt', amount=200.00, description='Received payment from client')
        manager.add_transaction(receipt)

        payment = Transaction(transaction_type='payment', amount=100.00, description='Payment for services')
        manager.add_transaction(payment)

        # Display all transactions and current balance
        print("All Transactions:")
        for transaction in manager.get_transactions():
            print(transaction)

        print(f"\nCurrent Balance: ${manager.get_balance():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
