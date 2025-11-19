"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthesizations.netlify.app
Prompt: Generate a script that handles emergency withdrawals and refunds for a decentralized wallet application.
Generated: DETERMINISTIC_bfdd36f9fe51136e
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal, InvalidOperation

class Wallet:
    """A simple representation of a decentralized wallet."""
    
    def __init__(self):
        self.balances = {}
    
    def add_funds(self, user_id: str, amount: Decimal):
        """Adds funds to a user's wallet."""
        if amount <= 0:
            raise ValueError("Amount to add must be positive.")
        
        if user_id not in self.balances:
            self.balances[user_id] = Decimal('0.0')
        
        self.balances[user_id] += amount
        print(f"Added {amount} to {user_id}. New balance: {self.balances[user_id]}")
    
    def emergency_withdraw(self, user_id: str, amount: Decimal):
        """
        Handles an emergency withdrawal for a user.
        
        :param user_id: The ID of the user requesting the withdrawal.
        :param amount: The amount to withdraw.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if user_id not in self.balances or self.balances[user_id] < amount:
            raise ValueError("Insufficient funds for withdrawal.")
        
        self.balances[user_id] -= amount
        print(f"Emergency withdrew {amount} from {user_id}. New balance: {self.balances[user_id]}")
    
    def refund(self, user_id: str, amount: Decimal):
        """
        Processes a refund for a user.
        
        :param user_id: The ID of the user receiving the refund.
        :param amount: The amount to refund.
        """
        if amount <= 0:
            raise ValueError("Refund amount must be positive.")
        
        if user_id not in self.balances:
            self.balances[user_id] = Decimal('0.0')
        
        self.balances[user_id] += amount
        print(f"Refunded {amount} to {user_id}. New balance: {self.balances[user_id]}")

def main():
    """Main function to demonstrate wallet operations."""
    wallet = Wallet()
    
    # Sample actions
    try:
        wallet.add_funds("user123", Decimal('100.00'))
        wallet.emergency_withdraw("user123", Decimal('50.00'))
        wallet.refund("user123", Decimal('20.00'))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
