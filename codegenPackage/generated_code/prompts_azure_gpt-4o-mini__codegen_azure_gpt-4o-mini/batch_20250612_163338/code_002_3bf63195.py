"""
Generated Code Metadata:
========================
Original URL: https://binance.wallet.consulting
Prompt: Write a code snippet that demonstrates how to create a simple wallet application for managing cryptocurrencies, inspired by the concepts of decentralized finance mentioned on the site.
Generated: DETERMINISTIC_3bf631955c5c8e4f
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
from decimal import Decimal

class Wallet:
    """A simple wallet class for managing cryptocurrencies."""

    def __init__(self):
        """Initialize a new wallet with an empty balance."""
        self.balance = Decimal('0.00')
        self.transactions = []

    def deposit(self, amount):
        """Deposit a specified amount into the wallet.

        Args:
            amount (Decimal): The amount to deposit.

        Raises:
            ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        self.transactions.append({
            'id': str(uuid.uuid4()),
            'type': 'deposit',
            'amount': str(amount),
            'balance_after': str(self.balance)
        })

    def withdraw(self, amount):
        """Withdraw a specified amount from the wallet.

        Args:
            amount (Decimal): The amount to withdraw.

        Raises:
            ValueError: If the amount is negative, zero, or exceeds the balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        
        self.balance -= amount
        self.transactions.append({
            'id': str(uuid.uuid4()),
            'type': 'withdrawal',
            'amount': str(amount),
            'balance_after': str(self.balance)
        })

    def get_balance(self):
        """Return the current balance of the wallet."""
        return self.balance

    def get_transaction_history(self):
        """Return the transaction history of the wallet."""
        return self.transactions

    def save_to_file(self, filename):
        """Save the wallet data to a JSON file.

        Args:
            filename (str): The name of the file to save the wallet data.

        Raises:
            IOError: If there is an error writing to the file.
        """
        wallet_data = {
            'balance': str(self.balance),
            'transactions': self.transactions
        }
        try:
            with open(filename, 'w') as file:
                json.dump(wallet_data, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving wallet to file: {e}")

    def load_from_file(self, filename):
        """Load wallet data from a JSON file.

        Args:
            filename (str): The name of the file to load the wallet data from.

        Raises:
            IOError: If there is an error reading the file.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(filename, 'r') as file:
                wallet_data = json.load(file)
                self.balance = Decimal(wallet_data['balance'])
                self.transactions = wallet_data['transactions']
        except IOError as e:
            raise IOError(f"Error loading wallet from file: {e}")
        except (ValueError, KeyError) as e:
            raise ValueError(f"Invalid data in wallet file: {e}")

# Example usage
if __name__ == "__main__":
    my_wallet = Wallet()
    my_wallet.deposit(Decimal('100.00'))
    my_wallet.withdraw(Decimal('30.00'))
    print(f"Current Balance: {my_wallet.get_balance()}")
    print("Transaction History:", my_wallet.get_transaction_history())
    my_wallet.save_to_file('wallet_data.json')
    my_wallet.load_from_file('wallet_data.json')
```
