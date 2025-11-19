"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Write a script to determine the availability and balance of a bank account, including calculations for overdraft limits and available credit, as described in the webpage.
Generated: DETERMINISTIC_73f1e96df441dc61
Batch ID: 20250612_154901
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
    A class to represent a bank account with balance, overdraft limit, and available credit.
    """

    def __init__(self, account_number, balance=0.0, overdraft_limit=0.0):
        """
        Initializes a new bank account instance.

        :param account_number: Unique identifier for the bank account
        :param balance: Initial balance of the account (default is 0.0)
        :param overdraft_limit: Maximum overdraft limit for the account (default is 0.0)
        """
        self.account_number = account_number
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        :param amount: Amount to deposit (must be positive)
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        :param amount: Amount to withdraw (must be positive)
        :raises ValueError: If the amount is negative or exceeds available funds
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.available_balance():
            raise ValueError("Insufficient funds for this withdrawal.")
        self.balance -= amount

    def available_balance(self):
        """
        Calculates the available balance considering the overdraft limit.

        :return: Available balance including overdraft limit
        """
        return self.balance + self.overdraft_limit

    def get_balance(self):
        """
        Returns the current balance of the account.

        :return: Current balance
        """
        return self.balance

    def get_account_info(self):
        """
        Returns a summary of the account information.

        :return: Dictionary containing account number, balance, overdraft limit, and available balance
        """
        return {
            "account_number": self.account_number,
            "balance": self.balance,
            "overdraft_limit": self.overdraft_limit,
            "available_balance": self.available_balance()
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a new bank account
        account = BankAccount(account_number="123456789", balance=100.0, overdraft_limit=50.0)

        # Display account information
        print(account.get_account_info())

        # Deposit money
        account.deposit(50.0)
        print("After deposit:", account.get_account_info())

        # Withdraw money
        account.withdraw(120.0)
        print("After withdrawal:", account.get_account_info())

    except ValueError as e:
        print(f"Error: {e}")
```
