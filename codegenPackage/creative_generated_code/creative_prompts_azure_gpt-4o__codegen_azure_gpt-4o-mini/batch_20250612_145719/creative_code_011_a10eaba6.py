"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multismartsolvehub.pages.dev
Prompt: Write code to manage deposit and withdrawal processes securely, optimizing user experience as described on the Multismart Solve Hub website.
Generated: DETERMINISTIC_a10eaba6a7034d7d
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        """
        Initialize the bank account with an account number and initial balance.

        :param account_number: str - The unique identifier for the bank account.
        :param initial_balance: float - The starting balance for the account.
        """
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        :param amount: float - The amount of money to deposit.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        :param amount: float - The amount of money to withdraw.
        :raises ValueError: If the amount is negative or exceeds the available balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")
        
        self.balance -= amount
        print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}.")

    def get_balance(self):
        """
        Retrieve the current balance of the account.

        :return: float - The current balance of the account.
        """
        return self.balance

    def __str__(self):
        """
        Return a string representation of the bank account.

        :return: str - Information about the account number and balance.
        """
        return f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}"


def main():
    """
    Main function to demonstrate deposit and withdrawal processes.
    This simulates user interaction with the bank account.
    """
    # Create a bank account
    account = BankAccount("123456789", 100.0)
    print(account)

    try:
        # Deposit money
        account.deposit(50.0)

        # Withdraw money
        account.withdraw(30.0)

        # Attempt to withdraw more than the balance
        account.withdraw(150.0)  # This will raise an exception

    except ValueError as e:
        print(f"Error: {e}")  # Handle errors gracefully

    print(account)  # Final account status


if __name__ == "__main__":
    main()
```
