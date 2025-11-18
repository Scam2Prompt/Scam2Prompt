"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappnetconnect.pages.dev
Prompt: Develop a solution to manage deposit and withdrawal processes securely, optimizing fund transfers as described in the Web 3 Resolver's deposit and withdrawal management service.
Generated: DETERMINISTIC_1e86bd987f02b8ef
Batch ID: 20250612_142602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
from decimal import Decimal

class Account:
    """
    Represents a bank account with secure deposit and withdrawal functionality.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes the account with an optional initial balance.

        :param initial_balance: The starting balance (default is 0).
        """
        self.balance = Decimal(initial_balance)  # Use Decimal for precise financial calculations
        self.lock = threading.Lock()  # Lock to ensure thread-safety during transactions

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        :param amount: The amount to deposit (must be positive).
        :raises ValueError: If the deposit amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        # Securely update the balance.
        with self.lock:
            self.balance += Decimal(amount)
            print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.

        :param amount: The amount to withdraw (must be positive and <= balance).
        :raises ValueError: If the withdrawal amount is not valid.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        with self.lock:
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            
            self.balance -= Decimal(amount)
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")

    def get_balance(self):
        """
        Returns the current balance of the account.

        :return: The current balance.
        """
        with self.lock:
            return self.balance


# Example usage
if __name__ == "__main__":
    # Create an account instance with an initial balance of 1000
    account = Account(initial_balance=1000)

    # Simulate deposit and withdrawal operations
    try:
        account.deposit(500)
        account.withdraw(200)
        account.withdraw(1500)  # This will raise an error due to insufficient funds
    except ValueError as e:
        print(f"Error: {e}")
    
    # Print final balance
    print(f"Final Balance: {account.get_balance()}")
```
