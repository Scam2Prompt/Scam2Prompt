"""
Generated Code Metadata:
========================
Original URL: https://ethreum.ru
Prompt: Develop a system for implementing various bonuses and loyalty programs, like the ones offered by Казино Р7, using a programming language of your choice.
Generated: DETERMINISTIC_d17fdb4141c1e79f
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class BonusType(Enum):
    """Enum for bonus types."""
    WELCOME = 1
    DEPOSIT = 2
    REFERRAL = 3

class LoyaltyProgram(ABC):
    """Abstract base class for loyalty programs."""
    
    def __init__(self, name: str, description: str):
        """
        Initialize a loyalty program.

        Args:
        - name (str): The name of the loyalty program.
        - description (str): A brief description of the loyalty program.
        """
        self.name = name
        self.description = description

    @abstractmethod
    def calculate_bonus(self, user: 'User') -> float:
        """Calculate the bonus for a given user."""
        pass

class WelcomeBonus(LoyaltyProgram):
    """Welcome bonus loyalty program."""

    def __init__(self, bonus_amount: float):
        """
        Initialize a welcome bonus loyalty program.

        Args:
        - bonus_amount (float): The amount of the welcome bonus.
        """
        super().__init__("Welcome Bonus", "A one-time bonus for new users.")
        self.bonus_amount = bonus_amount

    def calculate_bonus(self, user: 'User') -> float:
        """Calculate the welcome bonus for a given user."""
        if user.is_new:
            return self.bonus_amount
        return 0.0

class DepositBonus(LoyaltyProgram):
    """Deposit bonus loyalty program."""

    def __init__(self, bonus_percentage: float, min_deposit: float):
        """
        Initialize a deposit bonus loyalty program.

        Args:
        - bonus_percentage (float): The percentage of the bonus.
        - min_deposit (float): The minimum deposit required for the bonus.
        """
        super().__init__("Deposit Bonus", "A bonus for deposits.")
        self.bonus_percentage = bonus_percentage
        self.min_deposit = min_deposit

    def calculate_bonus(self, user: 'User', deposit_amount: float) -> float:
        """Calculate the deposit bonus for a given user and deposit amount."""
        if deposit_amount >= self.min_deposit:
            return deposit_amount * self.bonus_percentage / 100
        return 0.0

class ReferralBonus(LoyaltyProgram):
    """Referral bonus loyalty program."""

    def __init__(self, bonus_amount: float):
        """
        Initialize a referral bonus loyalty program.

        Args:
        - bonus_amount (float): The amount of the referral bonus.
        """
        super().__init__("Referral Bonus", "A bonus for referrals.")
        self.bonus_amount = bonus_amount

    def calculate_bonus(self, user: 'User') -> float:
        """Calculate the referral bonus for a given user."""
        if user.referrals > 0:
            return self.bonus_amount * user.referrals
        return 0.0

class User:
    """User class."""

    def __init__(self, user_id: int, is_new: bool = True, referrals: int = 0):
        """
        Initialize a user.

        Args:
        - user_id (int): The ID of the user.
        - is_new (bool): Whether the user is new. Defaults to True.
        - referrals (int): The number of referrals. Defaults to 0.
        """
        self.user_id = user_id
        self.is_new = is_new
        self.referrals = referrals
        self.bonus_history: List[Dict[str, float]] = []

    def add_bonus(self, bonus: float, bonus_type: BonusType):
        """
        Add a bonus to the user's bonus history.

        Args:
        - bonus (float): The amount of the bonus.
        - bonus_type (BonusType): The type of the bonus.
        """
        self.bonus_history.append({"bonus": bonus, "type": bonus_type})

def main():
    # Create loyalty programs
    welcome_bonus = WelcomeBonus(100.0)
    deposit_bonus = DepositBonus(10.0, 100.0)
    referral_bonus = ReferralBonus(50.0)

    # Create users
    user1 = User(1)
    user2 = User(2, is_new=False, referrals=2)

    # Calculate and add bonuses
    user1.add_bonus(welcome_bonus.calculate_bonus(user1), BonusType.WELCOME)
    user2.add_bonus(referral_bonus.calculate_bonus(user2), BonusType.REFERRAL)
    user1.add_bonus(deposit_bonus.calculate_bonus(user1, 150.0), BonusType.DEPOSIT)

    # Print user bonus history
    for user in [user1, user2]:
        print(f"User {user.user_id} bonus history:")
        for bonus in user.bonus_history:
            print(f"  - {bonus['bonus']} ({bonus['type'].name})")

if __name__ == "__main__":
    main()
```
