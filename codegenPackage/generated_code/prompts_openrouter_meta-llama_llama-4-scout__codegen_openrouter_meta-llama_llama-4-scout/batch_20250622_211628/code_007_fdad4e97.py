"""
Generated Code Metadata:
========================
Original URL: https://mary.finance
Prompt: "Write a code snippet that showcases MARY AI's code generation capabilities, specifically highlighting its ability to support rapid prototyping for clients."
Generated: DETERMINISTIC_fdad4e97640c1d8e
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mary_ai_prototyping_example.py

"""
Example code snippet showcasing MARY AI's code generation capabilities for rapid prototyping.

This script generates a simple banking system with deposit, withdrawal, and balance inquiry functionality.
"""

class BankAccount:
    """
    Represents a basic bank account.

    Attributes:
        account_number (str): Unique account number.
        account_holder (str): Account holder's name.
        balance (float): Current account balance.
    """

    def __init__(self, account_number, account_holder, initial_balance=0.0):
        """
        Initializes a BankAccount object.

        Args:
            account_number (str): Unique account number.
            account_holder (str): Account holder's name.
            initial_balance (float, optional): Initial account balance. Defaults to 0.0.

        Raises:
            ValueError: If initial balance is negative.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposits funds into the account.

        Args:
            amount (float): Amount to deposit.

        Raises:
            ValueError: If deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")

        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws funds from the account.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If withdrawal amount is negative or exceeds the current balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

    def get_balance(self):
        """
        Retrieves the current account balance.

        Returns:
            float: Current account balance.
        """
        return self.balance


def main():
    try:
        # Create a new bank account
        account = BankAccount("1234567890", "John Doe", 1000.0)

        # Perform transactions
        print(f"Initial balance: ${account.get_balance():.2f}")

        account.deposit(500.0)
        print(f"Balance after deposit: ${account.get_balance():.2f}")

        account.withdraw(200.0)
        print(f"Balance after withdrawal: ${account.get_balance():.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
