"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftsolutionchain.web.app
Prompt: Provide code for managing deposit and withdrawal processes securely, ensuring streamlined fund transfers as described on the Swift Solution Chain website.
Generated: DETERMINISTIC_c561bfeaa32608b3
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InsufficientFundsError(Exception):
    """Custom exception raised when a withdrawal exceeds the available balance."""
    pass

class Account:
    """Class to represent a bank account with deposit and withdrawal methods."""

    def __init__(self, account_number: str, initial_balance: float = 0.0):
        """
        Initializes an Account instance.

        Args:
            account_number (str): The account number for the bank account.
            initial_balance (float): The initial balance for the account, default is 0.0.
        """
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to be deposited.

        Raises:
            ValueError: If the deposit amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraws a specified amount from the account.

        Args:
            amount (float): The amount to be withdrawn.

        Raises:
            ValueError: If the withdrawal amount is non-positive.
            InsufficientFundsError: If the withdrawal amount exceeds the available balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")

        self.balance -= amount
        print(f"Withdrew: {amount}. New balance: {self.balance}")

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance.
        """
        return self.balance

# Example usage
if __name__ == "__main__":
    try:
        # Create a new account with an initial balance
        account = Account("123456789", 1000.0)
        
        # Deposit funds
        account.deposit(250.0)
        
        # Withdraw funds
        account.withdraw(100.0)
        
        # Attempt to withdraw more than the balance
        account.withdraw(1200.0)

    except (ValueError, InsufficientFundsError) as e:
        print(f"Error: {e}")
```
