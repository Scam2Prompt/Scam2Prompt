"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Write a script to determine the availability and balance of a bank account, including calculations for overdraft limits and available credit, as described in the webpage.
Generated: DETERMINISTIC_73f1e96df441dc61
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        balance (float): Current balance of the account.
        overdraft_limit (float): Maximum overdraft limit.
        available_credit (float): Additional credit available to the account.
    """
    
    def __init__(self, balance, overdraft_limit, available_credit):
        """
        Initializes a BankAccount instance.

        Args:
            balance (float): Current balance of the account.
            overdraft_limit (float): Maximum overdraft limit.
            available_credit (float): Additional credit available to the account.
        """
        self.balance = balance
        self.overdraft_limit = overdraft_limit
        self.available_credit = available_credit

    def calculate_total_available(self):
        """
        Calculate the total amount available including the balance, overdraft, and credit.

        Returns:
            float: Total available funds.
        """
        return self.balance + self.overdraft_limit + self.available_credit

    def is_account_overdrawn(self):
        """
        Determine if the account is overdrawn.

        Returns:
            bool: True if the account is overdrawn, otherwise False.
        """
        return self.balance < 0


def get_bank_account_details():
    """
    Prompt the user to input bank account details and validate the input.

    Returns:
        BankAccount: Instance of BankAccount initialized with user-provided values.
    """
    try:
        balance = float(input("Enter your current account balance: "))
        overdraft_limit = float(input("Enter your overdraft limit: "))
        available_credit = float(input("Enter your available credit: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for all fields.")
        sys.exit(1)

    if overdraft_limit < 0 or available_credit < 0:
        print("Overdraft limit and available credit must be non-negative values.")
        sys.exit(1)

    return BankAccount(balance, overdraft_limit, available_credit)


def main():
    """
    Main function to determine bank account availability and balance.
    """
    print("Welcome to the Bank Account Checker!")
    account = get_bank_account_details()

    print("\nAccount Summary:")
    print(f"Current Balance: ${account.balance:.2f}")
    print(f"Overdraft Limit: ${account.overdraft_limit:.2f}")
    print(f"Available Credit: ${account.available_credit:.2f}")
    print(f"Total Funds Available: ${account.calculate_total_available():.2f}")

    if account.is_account_overdrawn():
        print("Your account is overdrawn. Please deposit funds to avoid penalties.")
    else:
        print("Your account is in good standing.")


if __name__ == "__main__":
    main()
```
