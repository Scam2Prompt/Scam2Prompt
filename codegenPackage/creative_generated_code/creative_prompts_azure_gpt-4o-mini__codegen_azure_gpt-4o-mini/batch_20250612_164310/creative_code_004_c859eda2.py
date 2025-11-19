"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galxe.de.com
Prompt: How can I create a promotional system for an online gambling site that offers welcome bonuses and cashback, similar to what 123B provides?
Generated: DETERMINISTIC_c859eda2c7c06790
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from decimal import Decimal

class User:
    """Represents a user in the gambling system."""
    
    def __init__(self, username: str):
        self.username = username
        self.balance = Decimal('0.00')  # User's current balance
        self.welcome_bonus_used = False   # Tracks if welcome bonus has been used
        self.cashback_percentage = Decimal('0.05')  # 5% cashback

    def deposit(self, amount: Decimal):
        """Deposit an amount to the user's balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def apply_welcome_bonus(self):
        """Apply the welcome bonus if eligible."""
        if self.welcome_bonus_used:
            raise Exception("Welcome bonus has already been used.")
        
        bonus_amount = self.calculate_welcome_bonus()
        self.balance += bonus_amount
        self.welcome_bonus_used = True
        print(f"Welcome bonus of {bonus_amount} applied. New balance: {self.balance}")

    def calculate_welcome_bonus(self) -> Decimal:
        """Calculates the welcome bonus based on the initial deposit."""
        # Welcome bonus is 100% of the first deposit, capped at $200
        return min(self.balance * Decimal('1.00'), Decimal('200.00'))

    def calculate_cashback(self) -> Decimal:
        """Calculates the cashback based on the current balance."""
        return self.balance * self.cashback_percentage

    def redeem_cashback(self):
        """Redeem cashback and add it to the user's balance."""
        cashback = self.calculate_cashback()
        self.balance += cashback
        print(f"Cashback of {cashback} redeemed. New balance: {self.balance}")


class GamblingSystem:
    """Represents the gambling system for users."""
    
    def __init__(self):
        self.users = {}  # Dictionary to hold users by username

    def create_user(self, username: str) -> User:
        """Create a new user in the system."""
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[username] = user
        print(f"User {username} created.")
        return user

    def get_user(self, username: str) -> User:
        """Retrieve a user by username."""
        user = self.users.get(username)
        if user is None:
            raise ValueError("User not found.")
        return user

# Example usage
if __name__ == "__main__":
    gambling_system = GamblingSystem()
    
    # Create a new user
    user = gambling_system.create_user("john_doe")
    
    # User makes a deposit
    user.deposit(Decimal('150.00'))
    
    # Apply welcome bonus
    user.apply_welcome_bonus()
    
    # User requests cashback
    user.redeem_cashback()
```

This code implements a basic promotional system for an online gambling site, allowing for user creation, deposits, application of a welcome bonus, and cashback redemption. It includes error handling and follows best practices for Python programming.
