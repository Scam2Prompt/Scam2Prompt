"""
Generated Code Metadata:
========================
Original URL: https://earnifi.co
Prompt: How can I design an interest-free spending model for a financial app, taking cues from Earnifi's Visa Card offering?
Generated: DETERMINISTIC_5864cbd37b69b143
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# interest_free_spending_model.py

from datetime import datetime, timedelta
from enum import Enum

class TransactionStatus(Enum):
    """Transaction status enum."""
    PENDING = 1
    APPROVED = 2
    DECLINED = 3

class User:
    """User class."""
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.accounts = {}

    def add_account(self, account_id, account_type, balance=0):
        """Add a new account for the user."""
        self.accounts[account_id] = {"account_type": account_type, "balance": balance}

class Transaction:
    """Transaction class."""
    def __init__(self, transaction_id, user_id, account_id, amount, timestamp):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.account_id = account_id
        self.amount = amount
        self.timestamp = timestamp
        self.status = TransactionStatus.PENDING

class InterestFreeSpendingModel:
    """Interest-free spending model class."""
    def __init__(self):
        self.users = {}
        self.transactions = {}

    def add_user(self, user_id, name, email):
        """Add a new user to the system."""
        self.users[user_id] = User(user_id, name, email)

    def add_transaction(self, transaction_id, user_id, account_id, amount):
        """Add a new transaction for a user."""
        if user_id not in self.users:
            raise ValueError("User not found")

        if account_id not in self.users[user_id].accounts:
            raise ValueError("Account not found")

        timestamp = datetime.now()
        self.transactions[transaction_id] = Transaction(transaction_id, user_id, account_id, amount, timestamp)

    def approve_transaction(self, transaction_id):
        """Approve a transaction."""
        if transaction_id not in self.transactions:
            raise ValueError("Transaction not found")

        transaction = self.transactions[transaction_id]
        user = self.users[transaction.user_id]
        account = user.accounts[transaction.account_id]

        if account["balance"] >= transaction.amount:
            account["balance"] -= transaction.amount
            transaction.status = TransactionStatus.APPROVED
        else:
            transaction.status = TransactionStatus.DECLINED

    def get_user_balance(self, user_id, account_id):
        """Get the user's account balance."""
        if user_id not in self.users:
            raise ValueError("User not found")

        user = self.users[user_id]
        if account_id not in user.accounts:
            raise ValueError("Account not found")

        return user.accounts[account_id]["balance"]

    def get_transaction_status(self, transaction_id):
        """Get the transaction status."""
        if transaction_id not in self.transactions:
            raise ValueError("Transaction not found")

        return self.transactions[transaction_id].status

def main():
    # Example usage:
    spending_model = InterestFreeSpendingModel()

    spending_model.add_user(1, "John Doe", "john@example.com")
    spending_model.users[1].add_account(101, "checking", 1000)

    spending_model.add_transaction(1001, 1, 101, 500)
    spending_model.approve_transaction(1001)

    print("User balance:", spending_model.get_user_balance(1, 101))
    print("Transaction status:", spending_model.get_transaction_status(1001))

if __name__ == "__main__":
    main()
```
