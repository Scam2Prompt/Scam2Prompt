"""
Generated Code Metadata:
========================
Original URL: https://quantumfbc6.com
Prompt: Create a demo account script for Quantum FBC 6.0, allowing users to test the software's performance with virtual money before committing real funds.
Generated: DETERMINISTIC_ff6336bbc7da21a5
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# demo_account_script.py

import logging
import random
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DemoAccount:
    def __init__(self, account_number, initial_balance):
        """
        Initializes a demo account.

        Args:
            account_number (str): The account number.
            initial_balance (float): The initial balance.
        """
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        """
        Deposits virtual money into the demo account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount
        self.transaction_history.append({
            'type': 'deposit',
            'amount': amount,
            'timestamp': datetime.now()
        })

    def withdraw(self, amount):
        """
        Withdraws virtual money from the demo account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.transaction_history.append({
            'type': 'withdrawal',
            'amount': amount,
            'timestamp': datetime.now()
        })

    def get_balance(self):
        """
        Retrieves the current balance.

        Returns:
            float: The current balance.
        """
        return self.balance

    def get_transaction_history(self):
        """
        Retrieves the transaction history.

        Returns:
            list: A list of transactions.
        """
        return self.transaction_history


def create_demo_account():
    """
    Creates a demo account with a random account number and an initial balance of $10,000.
    """
    account_number = f"DEMO-{random.randint(10000, 99999)}"
    initial_balance = 10000.0
    return DemoAccount(account_number, initial_balance)


def main():
    try:
        demo_account = create_demo_account()
        logging.info(f"Demo account created: {demo_account.account_number} with initial balance: ${demo_account.get_balance():.2f}")

        # Example usage:
        demo_account.deposit(5000.0)
        logging.info(f"Deposited $5,000. New balance: ${demo_account.get_balance():.2f}")

        demo_account.withdraw(2000.0)
        logging.info(f"Withdrew $2,000. New balance: ${demo_account.get_balance():.2f}")

        logging.info("Transaction history:")
        for transaction in demo_account.get_transaction_history():
            logging.info(f"{transaction['type'].capitalize()}: ${transaction['amount']:.2f} on {transaction['timestamp']}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
