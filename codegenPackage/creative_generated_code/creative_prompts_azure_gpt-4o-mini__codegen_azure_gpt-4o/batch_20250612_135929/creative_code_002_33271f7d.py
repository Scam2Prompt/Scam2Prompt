"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://romellglobal.com
Prompt: Write a Python script that simulates the functionality of the Royal Trader Account, allowing users to deposit, transfer, and withdraw funds through an online banking interface.
Generated: DETERMINISTIC_33271f7d7e2ca56c
Batch ID: 20250612_135929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class RoyalTraderAccount:
    """
    Class to simulate an online banking account for deposit, transfer, and withdraw functionality.
    """
    def __init__(self, account_name, initial_balance=0.0):
        """
        Initializes the account with a name and an optional initial balance.
        """
        self.account_name = account_name
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        :param amount: Amount to be deposited (must be positive).
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"{amount} deposited successfully. Current balance: {self.balance}")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        :param amount: Amount to be withdrawn (must be positive and less than or equal to balance).
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        print(f"{amount} withdrawn successfully. Current balance: {self.balance}")

    def transfer(self, target_account, amount):
        """
        Transfer money from the current account to another account.
        :param target_account: An instance of RoyalTraderAccount to transfer money to.
        :param amount: Amount to be transferred (must be positive and less than or equal to balance).
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer.")
        self.withdraw(amount)  # Deduct from the current account
        target_account.deposit(amount)  # Add to the target account
        print(f"{amount} transferred successfully to {target_account.account_name}. Current balance: {self.balance}")

    def get_balance(self):
        """
        Get the current balance of the account.
        :return: The account's current balance.
        """
        return self.balance


def main():
    """
    Main function to simulate the Royal Trader Account operations.
    """
    try:
        print("Welcome to Royal Trader Online Banking.")
        
        # Create user accounts
        user_account = RoyalTraderAccount("UserAccount", initial_balance=1000.0)
        savings_account = RoyalTraderAccount("SavingsAccount", initial_balance=500.0)
        
        # Deposit into the user account
        user_account.deposit(200.0)
        
        # Withdraw from the user account
        user_account.withdraw(300.0)
        
        # Transfer funds to the savings account
        user_account.transfer(savings_account, 400.0)
        
        # Check balances
        print(f"{user_account.account_name} Balance: {user_account.get_balance()}")
        print(f"{savings_account.account_name} Balance: {savings_account.get_balance()}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
