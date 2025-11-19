"""
Generated Code Metadata:
========================
Original URL: https://uagra.com.ua
Prompt: Write a code example for implementing a bonus system in a betting application that mimics the Parimatch bonus offerings for new users.
Generated: DETERMINISTIC_ff03cc8a30645c3c
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bonus_system.py

class User:
    """Represents a user in the betting application."""

    def __init__(self, user_id, username):
        """
        Initializes a User object.

        Args:
            user_id (int): Unique identifier for the user.
            username (str): Username chosen by the user.
        """
        self.user_id = user_id
        self.username = username
        self.balance = 0.0
        self.bonus_balance = 0.0
        self.bonus_status = "inactive"


class BonusSystem:
    """Manages the bonus system for new users."""

    def __init__(self, bonus_amount, wagering_requirement):
        """
        Initializes a BonusSystem object.

        Args:
            bonus_amount (float): The bonus amount offered to new users.
            wagering_requirement (int): The number of times the bonus must be wagered.
        """
        self.bonus_amount = bonus_amount
        self.wagering_requirement = wagering_requirement

    def activate_bonus(self, user):
        """
        Activates the bonus for a new user.

        Args:
            user (User): The user to activate the bonus for.

        Raises:
            ValueError: If the user's bonus is already active.
        """
        if user.bonus_status == "active":
            raise ValueError("Bonus is already active for this user")

        user.bonus_balance = self.bonus_amount
        user.bonus_status = "active"

    def deposit(self, user, amount):
        """
        Deposits funds into a user's account.

        Args:
            user (User): The user to deposit funds for.
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")

        user.balance += amount

    def place_bet(self, user, amount):
        """
        Places a bet using a user's balance or bonus balance.

        Args:
            user (User): The user placing the bet.
            amount (float): The amount to bet.

        Raises:
            ValueError: If the bet amount is negative or exceeds the user's available balance.
        """
        if amount < 0:
            raise ValueError("Bet amount cannot be negative")

        if user.bonus_status == "active":
            if user.bonus_balance >= amount:
                user.bonus_balance -= amount
            elif user.balance >= amount:
                user.balance -= amount
            else:
                raise ValueError("Insufficient balance")
        elif user.balance >= amount:
            user.balance -= amount
        else:
            raise ValueError("Insufficient balance")

        # Update wagering requirement
        if user.bonus_status == "active":
            user.bonus_balance -= amount

    def update_wagering_requirement(self, user):
        """
        Updates the wagering requirement for a user's bonus.

        Args:
            user (User): The user to update the wagering requirement for.

        Raises:
            ValueError: If the user's bonus is not active.
        """
        if user.bonus_status != "active":
            raise ValueError("Bonus is not active for this user")

        if user.bonus_balance <= 0:
            user.bonus_status = "inactive"

    def withdraw(self, user, amount):
        """
        Withdraws funds from a user's account.

        Args:
            user (User): The user to withdraw funds for.
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is negative or exceeds the user's available balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")

        if user.balance >= amount:
            user.balance -= amount
        else:
            raise ValueError("Insufficient balance")


def main():
    # Create a new user
    user = User(1, "example_user")

    # Create a bonus system
    bonus_system = BonusSystem(100.0, 5)

    # Activate the bonus for the user
    bonus_system.activate_bonus(user)

    # Deposit funds into the user's account
    bonus_system.deposit(user, 100.0)

    # Place bets using the user's balance and bonus balance
    bonus_system.place_bet(user, 20.0)
    bonus_system.place_bet(user, 30.0)

    # Update the wagering requirement
    bonus_system.update_wagering_requirement(user)

    # Withdraw funds from the user's account
    bonus_system.withdraw(user, 50.0)

    # Print the user's final balance and bonus balance
    print(f"User Balance: {user.balance}")
    print(f"User Bonus Balance: {user.bonus_balance}")


if __name__ == "__main__":
    main()
```
