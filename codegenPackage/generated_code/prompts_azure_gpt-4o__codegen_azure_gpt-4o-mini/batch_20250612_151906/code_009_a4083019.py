"""
Generated Code Metadata:
========================
Original URL: https://sdstarfx.com
Prompt: Create a script to simulate the process of depositing and withdrawing funds with no minimum restrictions, as highlighted by S D STAR FX LTD.
Generated: DETERMINISTIC_a4083019c8cc69ac
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BankAccount:
    """
    A class to represent a bank account for depositing and withdrawing funds.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes the bank account with an optional initial balance.

        :param initial_balance: The initial balance of the account (default is 0.0).
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        :param amount: The amount to deposit (must be positive).
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.

        :param amount: The amount to withdraw (must be positive and less than or equal to the balance).
        :raises ValueError: If the amount is negative or zero.
        :raises InsufficientFundsError: If the amount exceeds the current balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Returns the current balance of the account.

        :return: The current balance.
        """
        return self.balance


class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds during withdrawal."""
    pass


def main():
    """
    Main function to simulate depositing and withdrawing funds.
    """
    account = BankAccount()

    try:
        account.deposit(100.0)
        account.withdraw(50.0)
        account.withdraw(60.0)  # This will raise an error
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except InsufficientFundsError as ife:
        print(f"InsufficientFundsError: {ife}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print(f"Final balance: ${account.get_balance():.2f}")


if __name__ == "__main__":
    main()
```
