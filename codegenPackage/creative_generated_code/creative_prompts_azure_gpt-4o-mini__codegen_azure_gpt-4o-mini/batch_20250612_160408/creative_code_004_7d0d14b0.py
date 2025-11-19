"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.org
Prompt: Write a function that simulates the investment process (deposit, invest, withdraw) as outlined in the Astragoldbitx.org workflow.
Generated: DETERMINISTIC_7d0d14b0848cefdd
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentError(Exception):
    """Custom exception for investment related errors."""
    pass

class Account:
    """Class to represent a user's investment account."""
    
    def __init__(self):
        """Initialize the account with zero balance and no investments."""
        self.balance = 0.0
        self.investments = 0.0

    def deposit(self, amount):
        """Deposit a specified amount into the account.
        
        Args:
            amount (float): The amount to deposit.

        Raises:
            InvestmentError: If the deposit amount is negative.
        """
        if amount < 0:
            raise InvestmentError("Deposit amount must be positive.")
        
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}.")

    def invest(self, amount):
        """Invest a specified amount from the account balance.
        
        Args:
            amount (float): The amount to invest.

        Raises:
            InvestmentError: If the investment amount exceeds the available balance.
        """
        if amount < 0:
            raise InvestmentError("Investment amount must be positive.")
        if amount > self.balance:
            raise InvestmentError("Insufficient funds for investment.")
        
        self.balance -= amount
        self.investments += amount
        print(f"Invested: {amount}. Remaining balance: {self.balance}. Total investments: {self.investments}.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account balance.
        
        Args:
            amount (float): The amount to withdraw.

        Raises:
            InvestmentError: If the withdrawal amount is negative or exceeds the available balance.
        """
        if amount < 0:
            raise InvestmentError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InvestmentError("Insufficient funds for withdrawal.")
        
        self.balance -= amount
        print(f"Withdrew: {amount}. New balance: {self.balance}.")

    def get_balance(self):
        """Get the current balance of the account.
        
        Returns:
            float: The current balance.
        """
        return self.balance

    def get_investments(self):
        """Get the total investments made by the user.
        
        Returns:
            float: The total amount invested.
        """
        return self.investments

# Example usage
if __name__ == "__main__":
    try:
        account = Account()
        account.deposit(1000)
        account.invest(200)
        account.withdraw(150)
        print(f"Final Balance: {account.get_balance()}")
        print(f"Total Investments: {account.get_investments()}")
    except InvestmentError as e:
        print(f"Error: {e}")
```
