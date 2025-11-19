"""
Generated Code Metadata:
========================
Original URL: https://financeimpactpro.com
Prompt: Create a Python script to track and log recent transactions (deposits and withdrawals) for users, similar to the "Latest Transactions" section on Finance Impact Pro.
Generated: DETERMINISTIC_f0e08f5b79cc7578
Batch ID: 20250612_154601
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

class Transaction:
    """Class to represent a financial transaction."""
    
    def __init__(self, user_id, amount, transaction_type):
        """
        Initialize a new transaction.

        :param user_id: ID of the user making the transaction
        :param amount: Amount of the transaction (positive for deposits, negative for withdrawals)
        :param transaction_type: Type of transaction ('deposit' or 'withdrawal')
        """
        self.user_id = user_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        """Convert the transaction to a dictionary for easy serialization."""
        return {
            'user_id': self.user_id,
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'timestamp': self.timestamp
        }

class TransactionLogger:
    """Class to log transactions to a JSON file."""
    
    def __init__(self, log_file='transactions.json'):
        """
        Initialize the transaction logger.

        :param log_file: Path to the JSON file where transactions will be logged
        """
        self.log_file = log_file
        self.transactions = self.load_transactions()

    def load_transactions(self):
        """Load existing transactions from the log file."""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []  # Return an empty list if the file is empty or corrupted
        return []

    def save_transactions(self):
        """Save the current transactions to the log file."""
        with open(self.log_file, 'w') as file:
            json.dump(self.transactions, file, indent=4)

    def log_transaction(self, transaction):
        """
        Log a new transaction.

        :param transaction: Transaction object to log
        """
        self.transactions.append(transaction.to_dict())
        self.save_transactions()

    def get_recent_transactions(self, user_id, limit=5):
        """
        Retrieve recent transactions for a specific user.

        :param user_id: ID of the user to retrieve transactions for
        :param limit: Number of recent transactions to return
        :return: List of recent transactions for the user
        """
        user_transactions = [t for t in self.transactions if t['user_id'] == user_id]
        return user_transactions[-limit:]

def main():
    """Main function to demonstrate transaction logging."""
    logger = TransactionLogger()

    # Example transactions
    try:
        logger.log_transaction(Transaction(user_id='user123', amount=100.0, transaction_type='deposit'))
        logger.log_transaction(Transaction(user_id='user123', amount=-50.0, transaction_type='withdrawal'))
        logger.log_transaction(Transaction(user_id='user456', amount=200.0, transaction_type='deposit'))

        # Retrieve and print recent transactions for user123
        recent_transactions = logger.get_recent_transactions(user_id='user123')
        print("Recent Transactions for user123:")
        for transaction in recent_transactions:
            print(transaction)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
