"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uagra.com.ua
Prompt: Write a code example for implementing a bonus system in a betting application that mimics the Parimatch bonus offerings for new users.
Generated: DETERMINISTIC_ff03cc8a30645c3c
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class to represent a user in the betting application."""
    
    def __init__(self, username, initial_balance):
        """
        Initializes a new user with a username and an initial balance.

        :param username: str - The username of the user
        :param initial_balance: float - The initial balance for the user
        """
        self.username = username
        self.balance = initial_balance
        self.bonus_balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the user's main balance.

        :param amount: float - The amount to deposit
        :raises ValueError: If the deposit amount is negative
        """
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.balance += amount

    def apply_bonus(self, bonus_amount):
        """
        Applies a bonus to the user's bonus balance.

        :param bonus_amount: float - The bonus amount to apply
        :raises ValueError: If the bonus amount is negative
        """
        if bonus_amount < 0:
            raise ValueError("Bonus amount must be non-negative.")
        self.bonus_balance += bonus_amount

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the user's main balance.

        :param amount: float - The amount to withdraw
        :raises ValueError: If the withdrawal amount is greater than the available balance
        """
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount

    def get_total_balance(self):
        """
        Returns the total balance including both main and bonus balances.

        :return: float - The total balance
        """
        return self.balance + self.bonus_balance


class BonusSystem:
    """Class to handle the bonus system for new users."""

    @staticmethod
    def register_new_user(username, initial_deposit):
        """
        Registers a new user and applies a bonus based on the initial deposit.
        
        :param username: str - The username of the new user
        :param initial_deposit: float - The initial deposit made by the user
        :return: User - The newly created User object
        :raises ValueError: If the initial deposit is negative
        """
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be non-negative.")
        
        # Create a new user
        new_user = User(username, initial_deposit)
        
        # Apply bonus: 100% of the initial deposit as a bonus (simulating Parimatch)
        bonus_amount = initial_deposit
        new_user.apply_bonus(bonus_amount)
        
        return new_user


# Example usage
if __name__ == "__main__":
    try:
        # Register a new user with an initial deposit
        user = BonusSystem.register_new_user("john_doe", 100.0)
        
        print(f"User: {user.username}")
        print(f"Main Balance: {user.balance}")
        print(f"Bonus Balance: {user.bonus_balance}")
        print(f"Total Balance: {user.get_total_balance()}")

        # Withdraw some funds
        user.withdraw(50.0)
        print(f"Main Balance after withdrawal: {user.balance}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
