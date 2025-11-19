"""
Generated Code Metadata:
========================
Original URL: https://guapzenith.com
Prompt: Write a code snippet to calculate and display the performance metrics of a cryptocurrency investment platform, including user growth, transactions, and withdrawal/deposit amounts, similar to Guapzenith's statistics.
Generated: DETERMINISTIC_2f3b024cfa60dff6
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
from typing import Dict, List

class Transaction:
    """Represents a transaction on the platform."""
    def __init__(self, user_id: int, transaction_type: str, amount: float):
        """
        Initializes a Transaction object.

        Args:
        - user_id (int): The ID of the user who made the transaction.
        - transaction_type (str): The type of transaction (deposit or withdrawal).
        - amount (float): The amount of the transaction.
        """
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.amount = amount

class PerformanceMetrics:
    """Calculates and displays performance metrics of the platform."""
    def __init__(self):
        """
        Initializes a PerformanceMetrics object.
        """
        self.users = set()
        self.transactions = []

    def add_user(self, user_id: int):
        """
        Adds a new user to the platform.

        Args:
        - user_id (int): The ID of the user.
        """
        self.users.add(user_id)

    def add_transaction(self, transaction: Transaction):
        """
        Adds a new transaction to the platform.

        Args:
        - transaction (Transaction): The transaction to add.
        """
        self.transactions.append(transaction)

    def calculate_user_growth(self) -> int:
        """
        Calculates the number of users on the platform.

        Returns:
        - int: The number of users.
        """
        return len(self.users)

    def calculate_transaction_volume(self) -> int:
        """
        Calculates the total number of transactions on the platform.

        Returns:
        - int: The total number of transactions.
        """
        return len(self.transactions)

    def calculate_deposit_amounts(self) -> float:
        """
        Calculates the total deposit amount on the platform.

        Returns:
        - float: The total deposit amount.
        """
        return sum(t.amount for t in self.transactions if t.transaction_type == 'deposit')

    def calculate_withdrawal_amounts(self) -> float:
        """
        Calculates the total withdrawal amount on the platform.

        Returns:
        - float: The total withdrawal amount.
        """
        return sum(t.amount for t in self.transactions if t.transaction_type == 'withdrawal')

    def display_performance_metrics(self):
        """
        Displays the performance metrics of the platform.
        """
        user_growth = self.calculate_user_growth()
        transaction_volume = self.calculate_transaction_volume()
        deposit_amounts = self.calculate_deposit_amounts()
        withdrawal_amounts = self.calculate_withdrawal_amounts()

        print("Performance Metrics:")
        print("--------------------")
        print(f"User Growth: {user_growth}")
        print(f"Transaction Volume: {transaction_volume}")
        print(f"Total Deposit Amount: ${deposit_amounts:.2f}")
        print(f"Total Withdrawal Amount: ${withdrawal_amounts:.2f}")

def main():
    try:
        # Create a PerformanceMetrics object
        metrics = PerformanceMetrics()

        # Add users
        metrics.add_user(1)
        metrics.add_user(2)
        metrics.add_user(3)

        # Add transactions
        metrics.add_transaction(Transaction(1, 'deposit', 1000.0))
        metrics.add_transaction(Transaction(1, 'withdrawal', 500.0))
        metrics.add_transaction(Transaction(2, 'deposit', 2000.0))
        metrics.add_transaction(Transaction(3, 'withdrawal', 750.0))

        # Display performance metrics
        metrics.display_performance_metrics()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
