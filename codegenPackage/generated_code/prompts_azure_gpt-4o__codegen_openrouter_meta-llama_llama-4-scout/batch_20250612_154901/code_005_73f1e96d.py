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
# bank_account.py

class BankAccount:
    """
    Represents a bank account with an account number, balance, overdraft limit, and available credit.
    """

    def __init__(self, account_number: str, balance: float = 0.0, overdraft_limit: float = 0.0, available_credit: float = 0.0):
        """
        Initializes a BankAccount object.

        Args:
            account_number (str): The unique account number.
            balance (float, optional): The current account balance. Defaults to 0.0.
            overdraft_limit (float, optional): The overdraft limit. Defaults to 0.0.
            available_credit (float, optional): The available credit. Defaults to 0.0.
        """
        self.account_number = account_number
        self.balance = balance
        self.overdraft_limit = overdraft_limit
        self.available_credit = available_credit

    def is_available(self) -> bool:
        """
        Checks if the account is available (i.e., not overdrawn and within credit limits).

        Returns:
            bool: True if the account is available, False otherwise.
        """
        return self.get_balance() >= -self.overdraft_limit and self.get_balance() <= self.available_credit

    def get_balance(self) -> float:
        """
        Gets the current account balance.

        Returns:
            float: The current account balance.
        """
        return self.balance

    def get_overdraft_limit(self) -> float:
        """
        Gets the overdraft limit.

        Returns:
            float: The overdraft limit.
        """
        return self.overdraft_limit

    def get_available_credit(self) -> float:
        """
        Gets the available credit.

        Returns:
            float: The available credit.
        """
        return self.available_credit

    def get_available_funds(self) -> float:
        """
        Calculates the available funds, considering the balance, overdraft limit, and available credit.

        Returns:
            float: The available funds.
        """
        return self.balance + self.overdraft_limit + self.available_credit

    def __str__(self):
        return f"Account Number: {self.account_number}\nBalance: {self.balance}\nOverdraft Limit: {self.overdraft_limit}\nAvailable Credit: {self.available_credit}"


def main():
    try:
        # Create a bank account object
        account = BankAccount(
            account_number="1234567890",
            balance=1000.0,
            overdraft_limit=500.0,
            available_credit=2000.0
        )

        # Print account details
        print(account)

        # Check account availability
        print(f"Account Available: {account.is_available()}")

        # Get account balance
        print(f"Account Balance: {account.get_balance()}")

        # Get overdraft limit
        print(f"Overdraft Limit: {account.get_overdraft_limit()}")

        # Get available credit
        print(f"Available Credit: {account.get_available_credit()}")

        # Calculate available funds
        print(f"Available Funds: {account.get_available_funds()}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
