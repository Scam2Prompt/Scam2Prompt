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
import datetime
from enum import Enum
from typing import Optional, List

class BonusType(Enum):
    """Enum representing different types of bonuses."""
    WELCOME = "welcome"
    DEPOSIT = "deposit"
    FREE_BET = "free_bet"

class BonusStatus(Enum):
    """Enum representing bonus statuses."""
    ACTIVE = "active"
    USED = "used"
    EXPIRED = "expired"

class Bonus:
    """Class representing a bonus in the betting system."""
    
    def __init__(
        self,
        bonus_id: str,
        bonus_type: BonusType,
        amount: float,
        expiry_date: datetime.datetime,
        status: BonusStatus = BonusStatus.ACTIVE,
        wagering_requirement: Optional[float] = None
    ):
        """
        Initialize a bonus instance.
        
        Args:
            bonus_id: Unique identifier for the bonus.
            bonus_type: Type of the bonus (e.g., WELCOME, DEPOSIT).
            amount: Bonus amount.
            expiry_date: Expiry date of the bonus.
            status: Current status of the bonus (default: ACTIVE).
            wagering_requirement: Wagering requirement (if applicable).
        """
        self.bonus_id = bonus_id
        self.bonus_type = bonus_type
        self.amount = amount
        self.expiry_date = expiry_date
        self.status = status
        self.wagering_requirement = wagering_requirement

    def is_expired(self) -> bool:
        """Check if the bonus has expired."""
        return datetime.datetime.now() > self.expiry_date

    def mark_as_used(self) -> None:
        """Mark the bonus as used."""
        if self.status == BonusStatus.ACTIVE:
            self.status = BonusStatus.USED

    def update_status(self) -> None:
        """Update the bonus status based on expiry."""
        if self.is_expired() and self.status == BonusStatus.ACTIVE:
            self.status = BonusStatus.EXPIRED

class User:
    """Class representing a user in the betting system."""
    
    def __init__(self, user_id: str, is_new: bool = True):
        """
        Initialize a user instance.
        
        Args:
            user_id: Unique identifier for the user.
            is_new: Whether the user is new (default: True).
        """
        self.user_id = user_id
        self.is_new = is_new
        self.bonuses: List[Bonus] = []

    def add_bonus(self, bonus: Bonus) -> None:
        """Add a bonus to the user's account."""
        self.bonuses.append(bonus)

    def get_active_bonuses(self) -> List[Bonus]:
        """Get all active bonuses for the user."""
        active_bonuses = []
        for bonus in self.bonuses:
            bonus.update_status()
            if bonus.status == BonusStatus.ACTIVE:
                active_bonuses.append(bonus)
        return active_bonuses

class BonusService:
    """Service class for managing bonuses."""
    
    @staticmethod
    def create_welcome_bonus(user: User, amount: float) -> Optional[Bonus]:
        """
        Create a welcome bonus for a new user.
        
        Args:
            user: User to whom the bonus is assigned.
            amount: Bonus amount.
            
        Returns:
            Bonus instance if user is new, None otherwise.
        """
        if not user.is_new:
            return None
            
        expiry_date = datetime.datetime.now() + datetime.timedelta(days=7)
        return Bonus(
            bonus_id="welcome_" + user.user_id,
            bonus_type=BonusType.WELCOME,
            amount=amount,
            expiry_date=expiry_date,
            wagering_requirement=amount * 5  # Example: 5x wagering requirement
        )

    @staticmethod
    def create_deposit_bonus(user: User, deposit_amount: float, percentage: float) -> Bonus:
        """
        Create a deposit bonus based on the deposit amount and percentage.
        
        Args:
            user: User to whom the bonus is assigned.
            deposit_amount: Amount deposited by the user.
            percentage: Bonus percentage (e.g., 0.5 for 50%).
            
        Returns:
            Bonus instance.
        """
        expiry_date = datetime.datetime.now() + datetime.timedelta(days=14)
        return Bonus(
            bonus_id="deposit_" + user.user_id + "_" + str(datetime.datetime.now().timestamp()),
            bonus_type=BonusType.DEPOSIT,
            amount=deposit_amount * percentage,
            expiry_date=expiry_date,
            wagering_requirement=deposit_amount * percentage * 3  # Example: 3x wagering requirement
        )

    @staticmethod
    def apply_bonus_to_bet(user: User, bonus_id: str, bet_amount: float) -> float:
        """
        Apply a bonus to a bet.
        
        Args:
            user: User placing the bet.
            bonus_id: ID of the bonus to apply.
            bet_amount: Amount of the bet.
            
        Returns:
            Adjusted bet amount after applying the bonus.
            
        Raises:
            ValueError: If bonus is not found or not applicable.
        """
        for bonus in user.get_active_bonuses():
            if bonus.bonus_id == bonus_id:
                if bonus.amount >= bet_amount:
                    bonus.amount -= bet_amount
                    if bonus.amount == 0:
                        bonus.mark_as_used()
                    return bet_amount
                else:
                    remaining = bonus.amount
                    bonus.amount = 0
                    bonus.mark_as_used()
                    return remaining
        raise ValueError("Bonus not found or not applicable")

# Example Usage
if __name__ == "__main__":
    # Create a new user
    user = User(user_id="12345", is_new=True)
    
    # Add a welcome bonus
    welcome_bonus = BonusService.create_welcome_bonus(user, 100.0)
    if welcome_bonus:
        user.add_bonus(welcome_bonus)
    
    # Add a deposit bonus
    deposit_bonus = BonusService.create_deposit_bonus(user, 200.0, 0.5)  # 50% of 200
    user.add_bonus(deposit_bonus)
    
    # Apply bonus to a bet
    try:
        adjusted_bet = BonusService.apply_bonus_to_bet(user, welcome_bonus.bonus_id, 50.0)
        print(f"Adjusted bet amount: {adjusted_bet}")
    except ValueError as e:
        print(f"Error applying bonus: {e}")
    
    # Print active bonuses
    print("Active bonuses:")
    for bonus in user.get_active_bonuses():
        print(f"ID: {bonus.bonus_id}, Amount: {bonus.amount}, Expires: {bonus.expiry_date}")
```
