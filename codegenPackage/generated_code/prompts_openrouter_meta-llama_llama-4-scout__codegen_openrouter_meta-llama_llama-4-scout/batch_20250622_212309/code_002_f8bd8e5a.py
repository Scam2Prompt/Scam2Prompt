"""
Generated Code Metadata:
========================
Original URL: https://amara.finance
Prompt: How would you implement a basic financial transaction system using Python, inspired by services offered by Amara Finance?
Generated: DETERMINISTIC_f8bd8e5a30534f65
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_transaction_system.py

from enum import Enum
from typing import Dict, List
from datetime import datetime

class TransactionType(str, Enum):
    """Transaction types."""
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"

class Transaction:
    """Represents a financial transaction."""

    def __init__(self, 
                 transaction_id: int, 
                 user_id: int, 
                 transaction_type: TransactionType, 
                 amount: float, 
                 timestamp: datetime = None):
        """
        Initializes a Transaction.

        Args:
        - transaction_id (int): Unique transaction ID.
        - user_id (int): ID of the user performing the transaction.
        - transaction_type (TransactionType): Type of transaction.
        - amount (float): Transaction amount.
        - timestamp (datetime): Timestamp of the transaction. Defaults to current time.
        """
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = timestamp if timestamp else datetime.now()

class User:
    """Represents a user in the system."""

    def __init__(self, user_id: int, balance: float = 0.0):
        """
        Initializes a User.

        Args:
        - user_id (int): Unique user ID.
        - balance (float): Initial user balance. Defaults to 0.0.
        """
        self.user_id = user_id
        self.balance = balance
        self.transactions: List[Transaction] = []

class FinancialTransactionSystem:
    """Basic financial transaction system."""

    def __init__(self):
        self.users: Dict[int, User] = {}
        self.transaction_id_counter = 1

    def create_user(self, user_id: int, initial_balance: float = 0.0):
        """
        Creates a new user.

        Args:
        - user_id (int): Unique user ID.
        - initial_balance (float): Initial user balance. Defaults to 0.0.

        Raises:
        - ValueError: If user ID already exists.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists")
        self.users[user_id] = User(user_id, initial_balance)

    def deposit(self, user_id: int, amount: float):
        """
        Deposits funds into a user's account.

        Args:
        - user_id (int): ID of the user.
        - amount (float): Deposit amount.

        Raises:
        - ValueError: If user ID does not exist or deposit amount is negative.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist")
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")

        user = self.users[user_id]
        user.balance += amount

        transaction = Transaction(
            self.transaction_id_counter, 
            user_id, 
            TransactionType.DEPOSIT, 
            amount
        )
        user.transactions.append(transaction)
        self.transaction_id_counter += 1

    def withdraw(self, user_id: int, amount: float):
        """
        Withdraws funds from a user's account.

        Args:
        - user_id (int): ID of the user.
        - amount (float): Withdrawal amount.

        Raises:
        - ValueError: If user ID does not exist, withdrawal amount is negative, or exceeds user balance.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist")
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        user = self.users[user_id]
        if amount > user.balance:
            raise ValueError("Insufficient funds")

        user.balance -= amount

        transaction = Transaction(
            self.transaction_id_counter, 
            user_id, 
            TransactionType.WITHDRAWAL, 
            amount
        )
        user.transactions.append(transaction)
        self.transaction_id_counter += 1

    def transfer(self, sender_id: int, recipient_id: int, amount: float):
        """
        Transfers funds between users.

        Args:
        - sender_id (int): ID of the sender.
        - recipient_id (int): ID of the recipient.
        - amount (float): Transfer amount.

        Raises:
        - ValueError: If sender or recipient ID does not exist, transfer amount is negative, or exceeds sender balance.
        """
        if sender_id not in self.users or recipient_id not in self.users:
            raise ValueError("Sender or recipient ID does not exist")
        if amount < 0:
            raise ValueError("Transfer amount cannot be negative")
        sender = self.users[sender_id]
        if amount > sender.balance:
            raise ValueError("Insufficient funds")

        sender.balance -= amount
        self.users[recipient_id].balance += amount

        sender_transaction = Transaction(
            self.transaction_id_counter, 
            sender_id, 
            TransactionType.TRANSFER, 
            amount
        )
        sender.transactions.append(sender_transaction)

        recipient_transaction = Transaction(
            self.transaction_id_counter + 1, 
            recipient_id, 
            TransactionType.TRANSFER, 
            amount
        )
        self.users[recipient_id].transactions.append(recipient_transaction)
        self.transaction_id_counter += 2

def main():
    system = FinancialTransactionSystem()

    system.create_user(1, 1000.0)
    system.create_user(2)

    system.deposit(2, 500.0)
    system.transfer(1, 2, 200.0)
    system.withdraw(2, 100.0)

    for user_id, user in system.users.items():
        print(f"User {user_id} balance: {user.balance}")
        for transaction in user.transactions:
            print(f"  - Transaction {transaction.transaction_id}: {transaction.transaction_type} {transaction.amount} at {transaction.timestamp}")

if __name__ == "__main__":
    main()
```
