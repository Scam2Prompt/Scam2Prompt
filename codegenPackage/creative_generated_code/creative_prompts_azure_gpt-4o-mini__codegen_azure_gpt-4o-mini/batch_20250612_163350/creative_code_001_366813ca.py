"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2.zks.app
Prompt: How can I implement a withdrawal function for L2 assets in a DEX like ZKSwap?
Generated: DETERMINISTIC_366813ca44b6742c
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DEX:
    def __init__(self):
        # Initialize the DEX with a dictionary to hold user balances
        self.balances = {}

    def deposit(self, user: str, amount: float) -> None:
        """
        Deposit an amount into the user's balance.

        :param user: The user making the deposit.
        :param amount: The amount to deposit.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        
        if user not in self.balances:
            self.balances[user] = 0.0
        
        self.balances[user] += amount

    def withdraw(self, user: str, amount: float) -> None:
        """
        Withdraw an amount from the user's balance.

        :param user: The user making the withdrawal.
        :param amount: The amount to withdraw.
        :raises ValueError: If the amount is negative or exceeds the user's balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        
        if user not in self.balances:
            raise ValueError("User does not have an account.")
        
        if self.balances[user] < amount:
            raise ValueError("Insufficient funds for withdrawal.")

        # Deduct the amount from the user's balance
        self.balances[user] -= amount

    def get_balance(self, user: str) -> float:
        """
        Get the current balance of a user.

        :param user: The user whose balance is to be fetched.
        :return: The user's balance.
        :raises ValueError: If the user does not exist.
        """
        if user not in self.balances:
            raise ValueError("User does not have an account.")
        
        return self.balances[user]

# Example usage
if __name__ == "__main__":
    dex = DEX()
    
    # User deposit
    dex.deposit("Alice", 100.0)
    
    # User withdraw
    try:
        dex.withdraw("Alice", 50.0)
        print(f"Alice's balance after withdrawal: {dex.get_balance('Alice')}")
    except ValueError as e:
        print(f"Error: {e}")

    # Trying to withdraw more than balance
    try:
        dex.withdraw("Alice", 60.0)
    except ValueError as e:
        print(f"Error: {e}")
```
