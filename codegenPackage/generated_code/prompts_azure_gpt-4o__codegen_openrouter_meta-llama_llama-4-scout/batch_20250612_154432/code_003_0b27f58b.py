"""
Generated Code Metadata:
========================
Original URL: https://uagra.com.ua
Prompt: Provide code examples for implementing a bonus system that matches Parimatch's +100% first deposit bonus with conditions like wagering requirements and expiration periods.
Generated: DETERMINISTIC_0b27f58b5ab0f786
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class BonusSystem:
    def __init__(self, bonus_percentage, wagering_requirement, expiration_period):
        """
        Initialize the bonus system.

        Args:
            bonus_percentage (float): The percentage of the bonus.
            wagering_requirement (int): The number of times the bonus must be wagered.
            expiration_period (int): The number of days until the bonus expires.
        """
        self.bonus_percentage = bonus_percentage
        self.wagering_requirement = wagering_requirement
        self.expiration_period = expiration_period

    def calculate_bonus(self, deposit_amount):
        """
        Calculate the bonus amount.

        Args:
            deposit_amount (float): The amount of the deposit.

        Returns:
            float: The bonus amount.
        """
        return deposit_amount * (self.bonus_percentage / 100)

    def get_wagering_requirement(self, bonus_amount):
        """
        Get the wagering requirement for the bonus.

        Args:
            bonus_amount (float): The amount of the bonus.

        Returns:
            float: The wagering requirement.
        """
        return bonus_amount * self.wagering_requirement

    def get_expiration_date(self):
        """
        Get the expiration date of the bonus.

        Returns:
            datetime: The expiration date.
        """
        return datetime.now() + timedelta(days=self.expiration_period)


class User:
    def __init__(self, id, deposit_amount):
        """
        Initialize the user.

        Args:
            id (int): The user's ID.
            deposit_amount (float): The amount of the deposit.
        """
        self.id = id
        self.deposit_amount = deposit_amount
        self.bonus_amount = 0
        self.wagering_requirement = 0
        self.expiration_date = None

    def apply_bonus(self, bonus_system):
        """
        Apply the bonus to the user.

        Args:
            bonus_system (BonusSystem): The bonus system.
        """
        self.bonus_amount = bonus_system.calculate_bonus(self.deposit_amount)
        self.wagering_requirement = bonus_system.get_wagering_requirement(self.bonus_amount)
        self.expiration_date = bonus_system.get_expiration_date()

    def wager(self, amount):
        """
        Record a wager.

        Args:
            amount (float): The amount of the wager.

        Returns:
            bool: Whether the wager was successful.
        """
        if self.wagering_requirement <= 0:
            print("No wagering requirement remaining.")
            return False

        if amount <= 0:
            print("Invalid wager amount.")
            return False

        self.wagering_requirement -= amount
        if self.wagering_requirement < 0:
            self.wagering_requirement = 0

        if self.wagering_requirement == 0:
            print("Wagering requirement met.")
            return True

        print(f"Wagering requirement remaining: {self.wagering_requirement}")
        return False

    def is_bonus_expired(self):
        """
        Check if the bonus has expired.

        Returns:
            bool: Whether the bonus has expired.
        """
        if self.expiration_date is None:
            return True

        return datetime.now() > self.expiration_date


def main():
    # Create a bonus system with a 100% bonus, 10x wagering requirement, and 30-day expiration period
    bonus_system = BonusSystem(100, 10, 30)

    # Create a user with a deposit amount of 100
    user = User(1, 100)

    # Apply the bonus to the user
    user.apply_bonus(bonus_system)

    print(f"Bonus Amount: {user.bonus_amount}")
    print(f"Wagering Requirement: {user.wagering_requirement}")
    print(f"Expiration Date: {user.expiration_date}")

    # Record wagers
    user.wager(500)
    user.wager(500)

    # Check if the bonus has expired
    if user.is_bonus_expired():
        print("The bonus has expired.")
    else:
        print("The bonus has not expired.")


if __name__ == "__main__":
    main()
```
