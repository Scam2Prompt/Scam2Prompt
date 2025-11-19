"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truebit.pages.dev
Prompt: What developer tools does Truebit offer for building on blockchain, specifically for managing treasury with USDC?
Generated: DETERMINISTIC_7d940e8ce6d2dadc
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Truebit Treasury Manager
This script provides a basic implementation for managing a treasury using USDC on a blockchain.
It includes functionalities to deposit, withdraw, and check the balance of USDC.
"""

class TreasuryManager:
    def __init__(self, initial_balance=0):
        """
        Initialize the TreasuryManager with an initial USDC balance.
        
        :param initial_balance: Initial balance of USDC, defaults to 0
        """
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposit USDC into the treasury.

        :param amount: Amount of USDC to deposit
        :raises ValueError: If the amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount} USDC. New balance: {self.balance} USDC.")

    def withdraw(self, amount):
        """
        Withdraw USDC from the treasury.

        :param amount: Amount of USDC to withdraw
        :raises ValueError: If the amount is not positive or exceeds the balance
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount
        print(f"Withdrew {amount} USDC. New balance: {self.balance} USDC.")

    def get_balance(self):
        """
        Get the current balance of USDC in the treasury.

        :return: Current balance of USDC
        """
        return self.balance

def main():
    """
    Main function to demonstrate the TreasuryManager functionality.
    """
    try:
        treasury = TreasuryManager()

        # Example transactions
        treasury.deposit(100)  # Deposit 100 USDC
        treasury.withdraw(50)   # Withdraw 50 USDC
        print(f"Final balance: {treasury.get_balance()} USDC")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
