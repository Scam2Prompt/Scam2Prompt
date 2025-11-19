"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dbabak.info
Prompt: How can I implement a bonus system for new members in a gaming site like PANSOS4D, ensuring secure transactions?
Generated: DETERMINISTIC_5d6cf0ca4cf64b74
Batch ID: 20250612_155606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal
import uuid
import hashlib
from datetime import datetime, timedelta

class User:
    def __init__(self, username):
        self.username = username
        self.balance = Decimal('0.00')
        self.bonus_activated = False
        self.bonus_expiration = None

    def activate_bonus(self, bonus_amount):
        """Activate bonus for the user if not already activated."""
        if not self.bonus_activated:
            self.bonus_activated = True
            self.bonus_expiration = datetime.now() + timedelta(days=30)  # Bonus valid for 30 days
            self.balance += Decimal(bonus_amount)
            print(f"Bonus of {bonus_amount} activated for user {self.username}.")
        else:
            print("Bonus already activated for this user.")

    def check_bonus_status(self):
        """Check if the bonus is still active."""
        if self.bonus_activated and datetime.now() < self.bonus_expiration:
            return True
        else:
            self.bonus_activated = False  # Reset bonus if expired
            return False

    def withdraw(self, amount):
        """Withdraw funds from the user's balance if sufficient."""
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= Decimal(amount)
        print(f"Withdrew {amount} from user {self.username}. New balance: {self.balance}")

    def deposit(self, amount):
        """Deposit funds to the user's balance."""
        self.balance += Decimal(amount)
        print(f"Deposited {amount} to user {self.username}. New balance: {self.balance}")

class BonusSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        """Add a new user to the system."""
        if username in self.users:
            raise ValueError("User already exists.")
        self.users[username] = User(username)
        print(f"User {username} added.")

    def apply_bonus(self, username, bonus_amount):
        """Apply a bonus to a user's account."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        user = self.users[username]
        user.activate_bonus(bonus_amount)

    def get_user_balance(self, username):
        """Return the user's current balance."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        return self.users[username].balance

# Example usage
if __name__ == "__main__":
    try:
        bonus_system = BonusSystem()
        bonus_system.add_user("player1")
        bonus_system.apply_bonus("player1", 100.00)
        
        print(f"Player1 balance: {bonus_system.get_user_balance('player1')}")
        bonus_system.users["player1"].withdraw(50.00)
        print(f"Player1 balance after withdrawal: {bonus_system.get_user_balance('player1')}")
        
        # Check bonus status
        if bonus_system.users["player1"].check_bonus_status():
            print("Bonus is still active.")
        else:
            print("Bonus has expired.")
            
    except ValueError as e:
        print(f"Error: {e}")
```
