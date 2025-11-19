"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isabellanoviyaonlinetechblog.blogspot.com
Prompt: Can you provide a code snippet for implementing a local bitcoin exchange feature in a Paxful clone?
Generated: DETERMINISTIC_12c8eba93d6db11b
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# BitcoinExchange.py

import json
from decimal import Decimal, InvalidOperation

class BitcoinExchange:
    def __init__(self):
        # Initialize an empty dictionary to store user balances
        self.user_balances = {}
        
    def add_user(self, user_id):
        """Add a new user to the exchange with an initial balance of 0."""
        if user_id not in self.user_balances:
            self.user_balances[user_id] = Decimal('0.0')
            print(f"User {user_id} added with a balance of 0 BTC.")
        else:
            raise ValueError("User already exists.")

    def deposit(self, user_id, amount):
        """Deposit a specified amount of BTC to a user's balance."""
        self._validate_user(user_id)
        self._validate_amount(amount)
        
        self.user_balances[user_id] += Decimal(amount)
        print(f"User {user_id} deposited {amount} BTC. New balance: {self.user_balances[user_id]} BTC.")

    def withdraw(self, user_id, amount):
        """Withdraw a specified amount of BTC from a user's balance."""
        self._validate_user(user_id)
        self._validate_amount(amount)
        
        if self.user_balances[user_id] < Decimal(amount):
            raise ValueError("Insufficient balance for withdrawal.")
        
        self.user_balances[user_id] -= Decimal(amount)
        print(f"User {user_id} withdrew {amount} BTC. New balance: {self.user_balances[user_id]} BTC.")

    def get_balance(self, user_id):
        """Return the current balance of a user."""
        self._validate_user(user_id)
        return self.user_balances[user_id]

    def _validate_user(self, user_id):
        """Check if the user exists in the exchange."""
        if user_id not in self.user_balances:
            raise ValueError("User does not exist.")

    def _validate_amount(self, amount):
        """Validate the amount to ensure it's a positive decimal."""
        try:
            if Decimal(amount) <= 0:
                raise ValueError("Amount must be greater than zero.")
        except InvalidOperation:
            raise ValueError("Invalid amount format.")

# Example usage
if __name__ == "__main__":
    exchange = BitcoinExchange()
    
    # Adding users to the exchange
    exchange.add_user("user1")
    exchange.add_user("user2")
    
    # Depositing funds
    exchange.deposit("user1", "0.5")
    exchange.deposit("user2", "0.2")
    
    # Withdrawing funds
    try:
        exchange.withdraw("user1", "0.3")
    except ValueError as e:
        print(f"Error: {e}")

    # Checking balance
    print(f"User1 Balance: {exchange.get_balance('user1')} BTC")
    print(f"User2 Balance: {exchange.get_balance('user2')} BTC")
```
