"""
Generated Code Metadata:
========================
Original URL: https://starltoken.com
Prompt: Generate code to implement a bonus system for a crypto casino, including features like "200% deposit bonus" and "free spins" as described on the STARL Token website.
Generated: DETERMINISTIC_3ee2b51fba0940a5
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional, Dict

class BonusType(Enum):
    DEPOSIT_BONUS = "DEPOSIT_BONUS"
    FREE_SPINS = "FREE_SPINS"

class BonusStatus(Enum):
    ACTIVE = "ACTIVE"
    USED = "USED"
    EXPIRED = "EXPIRED"

class Bonus:
    def __init__(
        self,
        bonus_id: str,
        user_id: str,
        bonus_type: BonusType,
        amount: float,
        percentage: Optional[float] = None,
        free_spins: Optional[int] = None,
        expiry_date: Optional[datetime] = None,
        status: BonusStatus = BonusStatus.ACTIVE,
        wagering_requirement: Optional[float] = None
    ):
        self.bonus_id = bonus_id
        self.user_id = user_id
        self.bonus_type = bonus_type
        self.amount = amount
        self.percentage = percentage
        self.free_spins = free_spins
        self.expiry_date = expiry_date or (datetime.now() + timedelta(days=30))
        self.status = status
        self.wagering_requirement = wagering_requirement or 0.0
        self.created_at = datetime.now()

    def is_expired(self) -> bool:
        return datetime.now() > self.expiry_date

    def mark_as_used(self) -> None:
        self.status = BonusStatus.USED

    def update_status(self) -> None:
        if self.status == BonusStatus.ACTIVE and self.is_expired():
            self.status = BonusStatus.EXPIRED

class BonusSystem:
    def __init__(self):
        self.bonuses: Dict[str, Bonus] = {}

    def create_bonus(
        self,
        user_id: str,
        bonus_type: BonusType,
        amount: float,
        percentage: Optional[float] = None,
        free_spins: Optional[int] = None,
        expiry_days: int = 30,
        wagering_requirement: Optional[float] = None
    ) -> Bonus:
        bonus_id = str(uuid.uuid4())
        expiry_date = datetime.now() + timedelta(days=expiry_days)
        
        bonus = Bonus(
            bonus_id=bonus_id,
            user_id=user_id,
            bonus_type=bonus_type,
            amount=amount,
            percentage=percentage,
            free_spins=free_spins,
            expiry_date=expiry_date,
            wagering_requirement=wagering_requirement
        )
        
        self.bonuses[bonus_id] = bonus
        return bonus

    def get_user_bonuses(self, user_id: str, active_only: bool = True) -> List[Bonus]:
        user_bonuses = [b for b in self.bonuses.values() if b.user_id == user_id]
        
        if active_only:
            for bonus in user_bonuses:
                bonus.update_status()
            user_bonuses = [b for b in user_bonuses if b.status == BonusStatus.ACTIVE]
        
        return user_bonuses

    def apply_deposit_bonus(self, user_id: str, deposit_amount: float, percentage: float = 200.0) -> Bonus:
        bonus_amount = deposit_amount * (percentage / 100)
        return self.create_bonus(
            user_id=user_id,
            bonus_type=BonusType.DEPOSIT_BONUS,
            amount=bonus_amount,
            percentage=percentage,
            wagering_requirement=bonus_amount * 30  # 30x wagering requirement
        )

    def award_free_spins(self, user_id: str, num_spins: int, spin_value: float = 1.0) -> Bonus:
        bonus_amount = num_spins * spin_value
        return self.create_bonus(
            user_id=user_id,
            bonus_type=BonusType.FREE_SPINS,
            amount=bonus_amount,
            free_spins=num_spins,
            expiry_days=7,  # Free spins typically expire faster
            wagering_requirement=bonus_amount * 20  # 20x wagering requirement
        )

    def use_bonus(self, bonus_id: str) -> Optional[Bonus]:
        bonus = self.bonuses.get(bonus_id)
        if not bonus or bonus.status != BonusStatus.ACTIVE:
            return None
        
        bonus.mark_as_used()
        return bonus

    def check_wagering_requirement(self, user_id: str, wagered_amount: float) -> List[Bonus]:
        completed_bonuses = []
        user_bonuses = self.get_user_bonuses(user_id, active_only=True)
        
        for bonus in user_bonuses:
            if wagered_amount >= bonus.wagering_requirement:
                bonus.mark_as_used()
                completed_bonuses.append(bonus)
        
        return completed_bonuses

# Example usage
if __name__ == "__main__":
    bonus_system = BonusSystem()
    
    # Example: 200% deposit bonus
    deposit_bonus = bonus_system.apply_deposit_bonus("user123", 100.0)
    print(f"Created deposit bonus: {deposit_bonus.amount} with {deposit_bonus.percentage}%")
    
    # Example: Free spins
    free_spins = bonus_system.award_free_spins("user123", 50)
    print(f"Created free spins: {free_spins.free_spins} spins worth {free_spins.amount}")
    
    # Check user bonuses
    user_bonuses = bonus_system.get_user_bonuses("user123")
    print(f"User has {len(user_bonuses)} active bonuses")
```
