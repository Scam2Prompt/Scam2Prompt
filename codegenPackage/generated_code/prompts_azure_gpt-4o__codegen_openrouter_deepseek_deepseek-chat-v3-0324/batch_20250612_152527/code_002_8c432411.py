"""
Generated Code Metadata:
========================
Original URL: https://shubaswap.com
Prompt: Generate code to implement a bonus system for new users, daily cashback, and promotional offers, as described on the MESIN128 platform.
Generated: DETERMINISTIC_8c4324117db5f3ec
Batch ID: 20250612_152527
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
from typing import Optional, List, Dict
from dataclasses import dataclass
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BonusType(Enum):
    """Enum representing different types of bonuses"""
    NEW_USER = "new_user"
    DAILY_CASHBACK = "daily_cashback"
    PROMOTIONAL = "promotional"

@dataclass
class Bonus:
    """Data class representing a bonus"""
    bonus_id: str
    bonus_type: BonusType
    amount: float
    description: str
    valid_from: datetime.datetime
    valid_to: datetime.datetime
    is_active: bool = True

    def is_valid(self) -> bool:
        """Check if the bonus is currently valid"""
        now = datetime.datetime.now()
        return self.is_active and self.valid_from <= now <= self.valid_to

class User:
    """Class representing a user"""
    def __init__(self, user_id: str, is_new: bool = True):
        self.user_id = user_id
        self.is_new = is_new
        self.balance: float = 0.0
        self.claimed_bonuses: Dict[str, Bonus] = {}
        self.last_cashback_date: Optional[datetime.date] = None

    def can_claim_daily_cashback(self) -> bool:
        """Check if user can claim daily cashback"""
        today = datetime.date.today()
        return self.last_cashback_date != today

class BonusSystem:
    """Main bonus system implementation"""
    def __init__(self):
        self.available_bonuses: Dict[str, Bonus] = {}
        self.promotional_codes: Dict[str, Bonus] = {}

    def add_bonus(self, bonus: Bonus) -> None:
        """Add a new bonus to the system"""
        if bonus.bonus_id in self.available_bonuses:
            raise ValueError(f"Bonus ID {bonus.bonus_id} already exists")
        self.available_bonuses[bonus.bonus_id] = bonus
        logger.info(f"Added bonus: {bonus.bonus_id}")

    def add_promotional_code(self, code: str, bonus: Bonus) -> None:
        """Add a promotional code to the system"""
        if code in self.promotional_codes:
            raise ValueError(f"Promotional code {code} already exists")
        self.promotional_codes[code] = bonus
        logger.info(f"Added promotional code: {code}")

    def claim_new_user_bonus(self, user: User) -> float:
        """Claim new user bonus if eligible"""
        if not user.is_new:
            logger.warning(f"User {user.user_id} is not eligible for new user bonus")
            return 0.0

        bonus = next(
            (b for b in self.available_bonuses.values() 
             if b.bonus_type == BonusType.NEW_USER and b.is_valid()),
            None
        )

        if not bonus:
            logger.warning("No valid new user bonus available")
            return 0.0

        if bonus.bonus_id in user.claimed_bonuses:
            logger.warning(f"User {user.user_id} already claimed new user bonus")
            return 0.0

        user.balance += bonus.amount
        user.claimed_bonuses[bonus.bonus_id] = bonus
        user.is_new = False
        logger.info(f"User {user.user_id} claimed new user bonus: {bonus.amount}")
        return bonus.amount

    def claim_daily_cashback(self, user: User) -> float:
        """Claim daily cashback if eligible"""
        if not user.can_claim_daily_cashback():
            logger.warning(f"User {user.user_id} already claimed cashback today")
            return 0.0

        bonus = next(
            (b for b in self.available_bonuses.values() 
             if b.bonus_type == BonusType.DAILY_CASHBACK and b.is_valid()),
            None
        )

        if not bonus:
            logger.warning("No valid daily cashback bonus available")
            return 0.0

        user.balance += bonus.amount
        user.last_cashback_date = datetime.date.today()
        logger.info(f"User {user.user_id} claimed daily cashback: {bonus.amount}")
        return bonus.amount

    def claim_promotional_code(self, user: User, code: str) -> float:
        """Claim promotional code if valid"""
        if code not in self.promotional_codes:
            logger.warning(f"Invalid promotional code: {code}")
            return 0.0

        bonus = self.promotional_codes[code]
        if not bonus.is_valid():
            logger.warning(f"Promotional code {code} is expired or inactive")
            return 0.0

        if bonus.bonus_id in user.claimed_bonuses:
            logger.warning(f"User {user.user_id} already claimed this promotional code")
            return 0.0

        user.balance += bonus.amount
        user.claimed_bonuses[bonus.bonus_id] = bonus
        logger.info(f"User {user.user_id} claimed promotional code {code}: {bonus.amount}")
        return bonus.amount

    def generate_random_promotional_code(self, prefix: str = "PROMO") -> str:
        """Generate a random promotional code"""
        code = f"{prefix}-{random.randint(1000, 9999)}"
        while code in self.promotional_codes:
            code = f"{prefix}-{random.randint(1000, 9999)}"
        return code

# Example usage
if __name__ == "__main__":
    # Initialize bonus system
    bonus_system = BonusSystem()

    # Add some bonuses
    new_user_bonus = Bonus(
        bonus_id="new_user_2023",
        bonus_type=BonusType.NEW_USER,
        amount=10.0,
        description="Welcome bonus for new users",
        valid_from=datetime.datetime(2023, 1, 1),
        valid_to=datetime.datetime(2023, 12, 31)
    )
    bonus_system.add_bonus(new_user_bonus)

    daily_cashback = Bonus(
        bonus_id="daily_cashback_2023",
        bonus_type=BonusType.DAILY_CASHBACK,
        amount=1.0,
        description="Daily cashback for active users",
        valid_from=datetime.datetime(2023, 1, 1),
        valid_to=datetime.datetime(2023, 12, 31)
    )
    bonus_system.add_bonus(daily_cashback)

    # Add promotional code
    promo_code = bonus_system.generate_random_promotional_code()
    promotional_bonus = Bonus(
        bonus_id="summer_promo_2023",
        bonus_type=BonusType.PROMOTIONAL,
        amount=5.0,
        description="Summer promotional offer",
        valid_from=datetime.datetime(2023, 6, 1),
        valid_to=datetime.datetime(2023, 8, 31)
    )
    bonus_system.add_promotional_code(promo_code, promotional_bonus)

    # Create a new user
    user = User("user123", is_new=True)

    # Claim bonuses
    bonus_system.claim_new_user_bonus(user)
    bonus_system.claim_daily_cashback(user)
    bonus_system.claim_promotional_code(user, promo_code)

    print(f"User balance: {user.balance}")
```
