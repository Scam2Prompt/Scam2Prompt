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
import datetime
from enum import Enum
from typing import Optional, List

class BonusStatus(Enum):
    """Enum representing the status of a bonus."""
    ACTIVE = "ACTIVE"
    USED = "USED"
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"

class Bonus:
    """Class representing a bonus in the system."""
    
    def __init__(
        self,
        bonus_id: str,
        user_id: str,
        amount: float,
        wagering_requirement: float,
        expiration_days: int,
        created_at: Optional[datetime.datetime] = None
    ):
        """
        Initialize a bonus instance.
        
        Args:
            bonus_id: Unique identifier for the bonus
            user_id: ID of the user who received the bonus
            amount: Bonus amount
            wagering_requirement: Wagering requirement multiplier (e.g., 5x)
            expiration_days: Number of days until bonus expires
            created_at: Optional creation timestamp (defaults to now)
        """
        self.bonus_id = bonus_id
        self.user_id = user_id
        self.amount = amount
        self.wagered_amount = 0.0
        self.wagering_requirement = wagering_requirement
        self.status = BonusStatus.ACTIVE
        self.created_at = created_at or datetime.datetime.now()
        self.expires_at = self.created_at + datetime.timedelta(days=expiration_days)
    
    def apply_wager(self, amount: float) -> None:
        """
        Apply a wager amount to the bonus.
        
        Args:
            amount: The amount to add to the wagered total
        """
        if self.status != BonusStatus.ACTIVE:
            raise ValueError("Cannot apply wager to inactive bonus")
        
        self.wagered_amount += amount
    
    def check_requirements_met(self) -> bool:
        """Check if wagering requirements are met."""
        return self.wagered_amount >= (self.amount * self.wagering_requirement)
    
    def check_expired(self) -> bool:
        """Check if bonus has expired."""
        return datetime.datetime.now() > self.expires_at
    
    def update_status(self) -> None:
        """Update bonus status based on current conditions."""
        if self.status != BonusStatus.ACTIVE:
            return
        
        if self.check_requirements_met():
            self.status = BonusStatus.USED
        elif self.check_expired():
            self.status = BonusStatus.EXPIRED

class BonusSystem:
    """Class managing the bonus system."""
    
    def __init__(self):
        self.bonuses = {}  # bonus_id: Bonus
    
    def create_first_deposit_bonus(
        self,
        user_id: str,
        deposit_amount: float,
        bonus_percentage: float = 1.0,
        wagering_requirement: float = 5.0,
        expiration_days: int = 30
    ) -> Bonus:
        """
        Create a first deposit bonus for a user.
        
        Args:
            user_id: ID of the user
            deposit_amount: Amount of the first deposit
            bonus_percentage: Percentage of deposit to give as bonus (default 100%)
            wagering_requirement: Wagering requirement multiplier (default 5x)
            expiration_days: Days until bonus expires (default 30)
            
        Returns:
            The created Bonus object
        """
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        bonus_amount = deposit_amount * bonus_percentage
        bonus_id = f"bonus_{user_id}_{datetime.datetime.now().timestamp()}"
        
        bonus = Bonus(
            bonus_id=bonus_id,
            user_id=user_id,
            amount=bonus_amount,
            wagering_requirement=wagering_requirement,
            expiration_days=expiration_days
        )
        
        self.bonuses[bonus_id] = bonus
        return bonus
    
    def get_user_bonuses(self, user_id: str, status: Optional[BonusStatus] = None) -> List[Bonus]:
        """
        Get bonuses for a user, optionally filtered by status.
        
        Args:
            user_id: ID of the user
            status: Optional status to filter by
            
        Returns:
            List of matching Bonus objects
        """
        user_bonuses = [b for b in self.bonuses.values() if b.user_id == user_id]
        
        if status is not None:
            user_bonuses = [b for b in user_bonuses if b.status == status]
        
        # Update statuses before returning
        for bonus in user_bonuses:
            bonus.update_status()
        
        return user_bonuses
    
    def apply_wager_to_bonus(self, user_id: str, wager_amount: float) -> None:
        """
        Apply a wager amount to all active bonuses for a user.
        
        Args:
            user_id: ID of the user
            wager_amount: Amount to apply to wagering requirements
        """
        if wager_amount <= 0:
            raise ValueError("Wager amount must be positive")
        
        active_bonuses = self.get_user_bonuses(user_id, BonusStatus.ACTIVE)
        
        for bonus in active_bonuses:
            bonus.apply_wager(wager_amount)
            bonus.update_status()
    
    def cancel_bonus(self, bonus_id: str) -> None:
        """
        Cancel a bonus.
        
        Args:
            bonus_id: ID of the bonus to cancel
        """
        if bonus_id not in self.bonuses:
            raise ValueError("Bonus not found")
        
        bonus = self.bonuses[bonus_id]
        if bonus.status != BonusStatus.ACTIVE:
            raise ValueError("Only active bonuses can be cancelled")
        
        bonus.status = BonusStatus.CANCELLED

# Example usage
if __name__ == "__main__":
    bonus_system = BonusSystem()
    
    # User makes first deposit
    user_id = "user123"
    deposit_amount = 100.0
    bonus = bonus_system.create_first_deposit_bonus(user_id, deposit_amount)
    print(f"Created bonus: {bonus.amount} with {bonus.wagering_requirement}x wagering")
    
    # User places bets
    try:
        bonus_system.apply_wager_to_bonus(user_id, 200.0)
        bonus_system.apply_wager_to_bonus(user_id, 300.0)
    except ValueError as e:
        print(f"Error applying wager: {e}")
    
    # Check bonus status
    user_bonuses = bonus_system.get_user_bonuses(user_id)
    for b in user_bonuses:
        print(f"Bonus {b.bonus_id}: Status={b.status}, Wagered={b.wagered_amount}/{b.amount * b.wagering_requirement}")
```
