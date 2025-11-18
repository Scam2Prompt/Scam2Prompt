"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.danngol.com
Prompt: Generate Python code for managing a virtual currency system called "단골머니," including functions for adding credits, deducting credits, and tracking transactions.
Generated: DETERMINISTIC_fb97f1824781f06b
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VirtualCurrencySystem:
    """A class to manage a virtual currency system called '단골머니'."""

    def __init__(self):
        """Initialize the currency system with zero credits and an empty transaction log."""
        self.balance = 0.0
        self.transactions = []

    def add_credits(self, amount):
        """
        Add credits to the user's balance.

        Parameters:
        amount (float): The amount of credits to add.

        Raises:
        ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        
        self.balance += amount
        self.transactions.append(f"Added: {amount}")
        print(f"Successfully added {amount:.2f} credits.")

    def deduct_credits(self, amount):
        """
        Deduct credits from the user's balance.

        Parameters:
        amount (float): The amount of credits to deduct.

        Raises:
        ValueError: If the amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Amount to deduct must be non-negative.")
        if amount > self.balance:
            raise ValueError("Cannot deduct more credits than available in the balance.")

        self.balance -= amount
        self.transactions.append(f"Deducted: {amount}")
        print(f"Successfully deducted {amount:.2f} credits.")

    def get_balance(self):
        """
        Get the current balance of credits.

        Returns:
        float: The current balance.
        """
        return self.balance

    def get_transaction_history(self):
        """
        Get the transaction history.

        Returns:
        list: A list of transactions.
        """
        return self.transactions

# Example usage (this should be commented out in production code)
if __name__ == "__main__":
    currency_system = VirtualCurrencySystem()
    
    try:
        currency_system.add_credits(100.0)
        currency_system.deduct_credits(30.0)
        print(f"Current Balance: {currency_system.get_balance():.2f}")
        print("Transaction History:", currency_system.get_transaction_history())
    except ValueError as e:
        print(f"Error: {e}")
```
