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
class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        account_number (str): The account number of the bank account.
        balance (float): The current balance of the bank account.
        overdraft_limit (float): The overdraft limit for the account.
        available_credit (float): The available credit for the account.
    """

    def __init__(self, account_number: str, balance: float, overdraft_limit: float):
        """
        Initializes a new BankAccount instance.

        Args:
            account_number (str): The account number.
            balance (float): The initial balance.
            overdraft_limit (float): The overdraft limit.
        """
        self.account_number = account_number
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def check_availability(self) -> dict:
        """
        Checks the availability and balance of the bank account.

        Returns:
            dict: A dictionary containing the balance, overdraft limit,
            and available credit.
        """
        available_credit = self.overdraft_limit + self.balance
        return {
            "balance": self.balance,
            "overdraft_limit": self.overdraft_limit,
            "available_credit": available_credit
        }

    def deposit(self, amount: float) -> None:
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraws a specified amount from the account if funds are available.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is negative or exceeds available funds.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount

# Example usage:
if __name__ == "__main__":
    try:
        account = BankAccount(account_number="123456789", balance=1000.0, overdraft_limit=500.0)
        account.deposit(200.0)
        account.withdraw(1500.0)
        
        account_info = account.check_availability()
        print("Account Information:")
        print(f"Balance: {account_info['balance']:.2f}")
        print(f"Overdraft Limit: {account_info['overdraft_limit']:.2f}")
        print(f"Available Credit: {account_info['available_credit']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
