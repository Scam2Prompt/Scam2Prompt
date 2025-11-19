"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatealpha.co
Prompt: Generate a code snippet for a demo account feature that allows users to practice trading strategies on Immediate Mentax without financial risk.
Generated: DETERMINISTIC_f8d6f29184bc9e3b
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import random
from datetime import datetime, timedelta

class DemoAccount:
    """
    A class to represent a demo trading account for practicing trading strategies.
    """

    def __init__(self, initial_balance=10000):
        """
        Initialize the demo account with an initial balance.
        :param initial_balance: The starting balance for the demo account. Default is 10,000.
        """
        self.account_id = str(uuid.uuid4())  # Generate a unique account ID
        self.balance = initial_balance  # Set the initial balance
        self.transactions = []  # List to store transaction history
        self.created_at = datetime.now()  # Timestamp when the account is created

    def add_transaction(self, transaction_type, amount):
        """
        Add a transaction to the demo account.
        :param transaction_type: Type of transaction ('buy' or 'sell').
        :param amount: Amount involved in the transaction.
        :return: None
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        if transaction_type not in ['buy', 'sell']:
            raise ValueError("Transaction type must be either 'buy' or 'sell'.")

        # Check if balance is sufficient for 'buy' transactions
        if transaction_type == 'buy' and amount > self.balance:
            raise ValueError("Insufficient balance for this transaction.")

        # Adjust balance based on transaction type
        if transaction_type == 'buy':
            self.balance -= amount
        elif transaction_type == 'sell':
            self.balance += amount

        # Record transaction
        transaction = {
            'transaction_id': str(uuid.uuid4()),
            'type': transaction_type,
            'amount': amount,
            'timestamp': datetime.now()
        }
        self.transactions.append(transaction)

    def get_transaction_history(self):
        """
        Retrieve the transaction history for the demo account.
        :return: List of transactions.
        """
        return self.transactions

    def reset_account(self):
        """
        Reset the demo account to its initial state.
        :return: None
        """
        self.balance = 10000
        self.transactions = []

# Demo usage of the DemoAccount class
def main():
    try:
        # Create a demo account
        demo_account = DemoAccount()

        # Add a few transactions
        demo_account.add_transaction(transaction_type='buy', amount=1000)
        demo_account.add_transaction(transaction_type='sell', amount=500)

        # Display transaction history
        print("Transaction History:")
        for transaction in demo_account.get_transaction_history():
            print(transaction)

        # Display current balance
        print("Current Balance:", demo_account.balance)

        # Reset the account
        demo_account.reset_account()
        print("Account successfully reset!")

        # Display current balance after reset
        print("Current Balance (After Reset):", demo_account.balance)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the demo
if __name__ == "__main__":
    main()
```
