"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e-digitsr.com
Prompt: Generate code to implement a minimum withdrawal limit of 30 USDT in a blockchain-based financial system, similar to the constraints described on the E-DIGITS platform.
Generated: DETERMINISTIC_a0b49ec3fc569d07
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BlockchainFinancialSystem:
    """
    A class to represent a blockchain-based financial system with withdrawal functionality.
    """

    def __init__(self):
        """
        Initializes the financial system with a minimum withdrawal limit.
        """
        self.minimum_withdrawal_limit = 30.0  # Minimum withdrawal limit in USDT
        self.balance = 0.0  # User balance in USDT

    def deposit(self, amount: float) -> None:
        """
        Deposit an amount into the user's balance.

        :param amount: Amount in USDT to deposit
        :raises ValueError: If the deposit amount is negative
        """
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw an amount from the user's balance, enforcing the minimum withdrawal limit.

        :param amount: Amount in USDT to withdraw
        :raises ValueError: If the withdrawal amount is below the minimum limit or exceeds the current balance
        """
        if amount < self.minimum_withdrawal_limit:
            raise ValueError(f"Withdrawal amount must be at least {self.minimum_withdrawal_limit} USDT.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")

        self.balance -= amount

    def get_balance(self) -> float:
        """
        Get the current balance of the user.

        :return: Current balance in USDT
        """
        return self.balance


# Example usage
if __name__ == "__main__":
    try:
        financial_system = BlockchainFinancialSystem()
        financial_system.deposit(100.0)  # Deposit 100 USDT
        print(f"Current Balance: {financial_system.get_balance()} USDT")
        
        financial_system.withdraw(25.0)  # Attempt to withdraw below the minimum limit
    except ValueError as e:
        print(f"Error: {e}")

    try:
        financial_system.withdraw(50.0)  # Attempt to withdraw more than balance
    except ValueError as e:
        print(f"Error: {e}")

    try:
        financial_system.withdraw(30.0)  # Successful withdrawal
        print(f"Current Balance after withdrawal: {financial_system.get_balance()} USDT")
    except ValueError as e:
        print(f"Error: {e}")
```
