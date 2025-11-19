"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Explain how to implement a promotional system for an online gambling platform that offers a "100% Bonus New Member" incentive.
Generated: DETERMINISTIC_0d84a68794a299f7
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class User:
    """Class representing a user in the gambling platform."""

    def __init__(self, username, initial_deposit):
        """
        Initialize a user with a username and an initial deposit.

        Args:
            username (str): The username of the user.
            initial_deposit (float): The initial deposit amount made by the user.
        """
        self.username = username
        self.balance = initial_deposit
        self.bonus_balance = 0.0
        self.is_bonus_claimed = False

    def claim_bonus(self):
        """Claim the 100% new member bonus on the first deposit."""
        if not self.is_bonus_claimed and self.initial_deposit > 0:
            self.bonus_balance = self.initial_deposit  # 100% bonus
            self.is_bonus_claimed = True
            print(f"Bonus claimed for {self.username}. Bonus balance: {self.bonus_balance:.2f}")
        else:
            print(f"Bonus already claimed or invalid initial deposit for {self.username}.")

    def deposit(self, amount):
        """
        Deposit an amount into the user's balance.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"{self.username} deposited {amount:.2f}. New balance: {self.balance:.2f}")

    def total_balance(self):
        """Return the total balance including bonus."""
        return self.balance + self.bonus_balance

def create_user(username, initial_deposit):
    """
    Create a new user and automatically claim the bonus if eligible.

    Args:
        username (str): The username of the new user.
        initial_deposit (float): The initial deposit amount made by the user.

    Returns:
        User: The created user object.
    """
    user = User(username, initial_deposit)
    user.claim_bonus()  # Automatically claim the bonus
    return user

def main():
    """Main function to demonstrate the promotional system."""
    try:
        # Example of creating a new user and making deposits
        new_user = create_user('john_doe', 100.0)  # Initial deposit
        new_user.deposit(50.0)  # Additional deposit
        print(f"Total balance for {new_user.username}: {new_user.total_balance():.2f}")

        # Attempt to claim bonus again
        new_user.claim_bonus()  # Should indicate bonus is already claimed

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
