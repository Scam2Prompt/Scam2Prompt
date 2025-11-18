"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.danngol.com
Prompt: Generate Python code for managing a virtual currency system called "단골머니," including functions for adding credits, deducting credits, and tracking transactions.
Generated: DETERMINISTIC_fb97f1824781f06b
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class CurrencyTransaction:
    """
    Class to represent a single transaction in the 단골머니 system.
    """
    def __init__(self, transaction_id, type, amount, balance_after, timestamp=None):
        self.transaction_id = transaction_id
        self.type = type  # 'credit' or 'debit'
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = timestamp if timestamp else datetime.utcnow()

    def __str__(self):
        return (f"Transaction ID: {self.transaction_id}, Type: {self.type}, "
                f"Amount: {self.amount}, Balance After: {self.balance_after}, "
                f"Timestamp: {self.timestamp}")


class DangolMoneyAccount:
    """
    Class to manage a virtual currency account called 단골머니.
    """
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        self.transactions = []

    def add_credits(self, amount):
        """
        Adds credits to the account.
        :param amount: Amount of credits to add (must be positive)
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.balance += amount
        transaction_id = uuid.uuid4()
        transaction = CurrencyTransaction(
            transaction_id=transaction_id, 
            type="credit", 
            amount=amount, 
            balance_after=self.balance
        )
        self.transactions.append(transaction)
        return transaction

    def deduct_credits(self, amount):
        """
        Deducts credits from the account.
        :param amount: Amount of credits to deduct (must be positive and <= current balance)
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        transaction_id = uuid.uuid4()
        transaction = CurrencyTransaction(
            transaction_id=transaction_id, 
            type="debit", 
            amount=amount, 
            balance_after=self.balance
        )
        self.transactions.append(transaction)
        return transaction

    def get_balance(self):
        """
        Returns the current balance of the account.
        """
        return self.balance

    def get_transaction_history(self):
        """
        Returns a list of all transactions.
        """
        return self.transactions

# Example usage (this would not be included in a production library/module):
if __name__ == "__main__":
    try:
        account = DangolMoneyAccount(owner="John Doe")
        print(f"Account created for: {account.owner}")
        print(f"Initial Balance: {account.get_balance()}")

        # Add credits
        transaction1 = account.add_credits(100)
        print(f"Added Credits: {transaction1}")

        # Deduct credits
        transaction2 = account.deduct_credits(50)
        print(f"Deducted Credits: {transaction2}")

        # Show balance
        print(f"Current Balance: {account.get_balance()}")

        # Show transaction history
        print("Transaction History:")
        for transaction in account.get_transaction_history():
            print(transaction)

    except ValueError as e:
        print(f"Error: {e}")
```
