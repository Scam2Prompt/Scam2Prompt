"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain-nodetool.web.app
Prompt: Write a script for managing deposits and withdrawals in a trading platform, inspired by the optimization techniques from blockchain-nodetool.web.app.
Generated: DETERMINISTIC_17a2dfc4ba314788
Batch ID: 20250612_155200
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


class TradingPlatform:
    """
    A class to manage deposits and withdrawals on a trading platform.
    """

    def __init__(self):
        # Initialize account balances and transaction history
        self.accounts = {}
        self.transactions = []

    # Error types for platform operations
    class InsufficientFundsError(Exception):
        pass

    class AccountNotFoundError(Exception):
        pass

    def create_account(self, user_id: str):
        """
        Create a new account for a user.
        :param user_id: Unique identifier for the user.
        """
        if user_id in self.accounts:
            print(f"Account already exists for user ID {user_id}")
            return

        # Initialize account balance to 0
        self.accounts[user_id] = 0.0

    def deposit(self, user_id: str, amount: float):
        """
        Deposit funds into a user's account.
        :param user_id: Unique identifier for the user.
        :param amount: Amount to deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        # Check if the user's account exists
        if user_id not in self.accounts:
            raise self.AccountNotFoundError(f"Account not found for user ID {user_id}")

        # Update account balance
        self.accounts[user_id] += amount

        # Log the transaction
        self.transactions.append({
            'transaction_id': str(uuid.uuid4()),
            'user_id': user_id,
            'type': 'deposit',
            'amount': amount,
            'timestamp': datetime.utcnow()
        })

    def withdraw(self, user_id: str, amount: float):
        """
        Withdraw funds from a user's account.
        :param user_id: Unique identifier for the user.
        :param amount: Amount to withdraw.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        # Check if the user's account exists
        if user_id not in self.accounts:
            raise self.AccountNotFoundError(f"Account not found for user ID {user_id}")

        # Ensure sufficient funds are available
        if self.accounts[user_id] < amount:
            raise self.InsufficientFundsError("Insufficient funds.")

        # Update account balance
        self.accounts[user_id] -= amount

        # Log the transaction
        self.transactions.append({
            'transaction_id': str(uuid.uuid4()),
            'user_id': user_id,
            'type': 'withdrawal',
            'amount': amount,
            'timestamp': datetime.utcnow()
        })

    def get_balance(self, user_id: str) -> float:
        """
        Retrieve the current balance of a user's account.
        :param user_id: Unique identifier for the user.
        :return: Account balance.
        """
        if user_id not in self.accounts:
            raise self.AccountNotFoundError(f"Account not found for user ID {user_id}")

        return self.accounts[user_id]

    def get_transaction_history(self, user_id: str) -> list:
        """
        Retrieve the transaction history for a user's account.
        :param user_id: Unique identifier for the user.
        :return: List of transactions.
        """
        if user_id not in self.accounts:
            raise self.AccountNotFoundError(f"Account not found for user ID {user_id}")

        # Filter transactions by user ID
        return [txn for txn in self.transactions if txn['user_id'] == user_id]


# Example Usage:
if __name__ == "__main__":
    platform = TradingPlatform()

    try:
        platform.create_account("user123")
        platform.deposit("user123", 100.0)
        platform.withdraw("user123", 30.0)

        print("Balance:", platform.get_balance("user123"))
        print("Transaction History:", platform.get_transaction_history("user123"))

    except Exception as e:
        print(f"Error: {e}")
```
