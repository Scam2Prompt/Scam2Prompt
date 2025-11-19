"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Develop a code snippet for a debit card management system that allows users to track their transactions and balances, inspired by GICU's debit card services.
Generated: DETERMINISTIC_52e083e68af74e67
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class DebitCard:
    """
    A class to represent a debit card for managing transactions and balances.
    """

    def __init__(self, card_number, cardholder_name, initial_balance=0.0):
        """
        Initialize the debit card with card details and an initial balance.
        """
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        self.balance = initial_balance
        self.transactions = []  # List to store transaction history

    def deposit(self, amount):
        """
        Deposit money into the debit card account.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        self._add_transaction("Deposit", amount)

    def withdraw(self, amount):
        """
        Withdraw money from the debit card account.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for this transaction.")
        self.balance -= amount
        self._add_transaction("Withdrawal", amount)

    def _add_transaction(self, transaction_type, amount):
        """
        Add a transaction to the transaction history.
        """
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "balance_after": self.balance
        }
        self.transactions.append(transaction)

    def get_balance(self):
        """
        Get the current balance of the debit card account.
        """
        return self.balance

    def get_transaction_history(self):
        """
        Get the transaction history of the debit card account.
        """
        return self.transactions


# Example usage
if __name__ == "__main__":
    try:
        # Create a new debit card instance
        my_card = DebitCard(card_number="1234-5678-9876-5432", cardholder_name="John Doe", initial_balance=1000.0)

        # Perform some transactions
        my_card.deposit(500.0)
        my_card.withdraw(200.0)

        # Print current balance
        print(f"Current Balance: ${my_card.get_balance():.2f}")

        # Print transaction history
        print("\nTransaction History:")
        for transaction in my_card.get_transaction_history():
            print(transaction)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
