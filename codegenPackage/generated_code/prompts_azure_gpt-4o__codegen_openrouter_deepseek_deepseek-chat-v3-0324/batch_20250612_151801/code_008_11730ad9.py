"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Write code to implement a promotional event system where users can claim bonuses like "Depo 25 Bonus 25" based on deposit amounts and membership status.
Generated: DETERMINISTIC_11730ad95b0fb72b
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Dict, List
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MembershipTier(Enum):
    """Enum representing different membership tiers."""
    BRONZE = auto()
    SILVER = auto()
    GOLD = auto()
    PLATINUM = auto()

@dataclass
class User:
    """Class representing a user in the system."""
    user_id: str
    name: str
    membership_tier: MembershipTier
    total_deposits: float = 0.0

@dataclass
class Bonus:
    """Class representing a bonus offer."""
    name: str
    deposit_requirement: float
    bonus_amount: float
    applicable_tiers: List[MembershipTier]
    start_date: datetime.date
    end_date: datetime.date
    max_claims: Optional[int] = None
    total_claims: int = 0

class BonusEventSystem:
    """System to manage promotional bonus events."""
    
    def __init__(self):
        self.available_bonuses: Dict[str, Bonus] = {}
        self.user_bonus_claims: Dict[str, Dict[str, int]] = {}  # user_id -> {bonus_name: claims}
    
    def add_bonus(self, bonus: Bonus) -> bool:
        """Add a new bonus to the system."""
        if bonus.name in self.available_bonuses:
            logger.warning(f"Bonus {bonus.name} already exists")
            return False
        
        if bonus.end_date < bonus.start_date:
            logger.error("End date cannot be before start date")
            return False
        
        self.available_bonuses[bonus.name] = bonus
        logger.info(f"Added new bonus: {bonus.name}")
        return True
    
    def is_bonus_active(self, bonus_name: str) -> bool:
        """Check if a bonus is currently active."""
        bonus = self.available_bonuses.get(bonus_name)
        if not bonus:
            return False
            
        today = datetime.date.today()
        return bonus.start_date <= today <= bonus.end_date
    
    def can_user_claim_bonus(self, user: User, bonus_name: str) -> bool:
        """Check if a user can claim a specific bonus."""
        bonus = self.available_bonuses.get(bonus_name)
        if not bonus:
            logger.warning(f"Bonus {bonus_name} not found")
            return False
            
        if not self.is_bonus_active(bonus_name):
            logger.warning(f"Bonus {bonus_name} is not active")
            return False
            
        if user.membership_tier not in bonus.applicable_tiers:
            logger.warning(f"User {user.user_id} is not eligible for bonus {bonus_name}")
            return False
            
        if user.total_deposits < bonus.deposit_requirement:
            logger.warning(f"User {user.user_id} has not met deposit requirement for {bonus_name}")
            return False
            
        if bonus.max_claims is not None and bonus.total_claims >= bonus.max_claims:
            logger.warning(f"Bonus {bonus_name} has reached maximum claims")
            return False
            
        user_claims = self.user_bonus_claims.get(user.user_id, {}).get(bonus_name, 0)
        if bonus.max_claims is not None and user_claims >= bonus.max_claims:
            logger.warning(f"User {user.user_id} has reached maximum claims for {bonus_name}")
            return False
            
        return True
    
    def claim_bonus(self, user: User, bonus_name: str) -> bool:
        """Attempt to claim a bonus for a user."""
        if not self.can_user_claim_bonus(user, bonus_name):
            return False
            
        bonus = self.available_bonuses[bonus_name]
        
        # Update bonus claims
        bonus.total_claims += 1
        
        # Update user's claim history
        if user.user_id not in self.user_bonus_claims:
            self.user_bonus_claims[user.user_id] = {}
            
        self.user_bonus_claims[user.user_id][bonus_name] = self.user_bonus_claims[user.user_id].get(bonus_name, 0) + 1
        
        logger.info(f"User {user.user_id} successfully claimed bonus {bonus_name}")
        return True
    
    def get_available_bonuses_for_user(self, user: User) -> List[Bonus]:
        """Get all available bonuses for a user."""
        available = []
        for bonus in self.available_bonuses.values():
            if self.can_user_claim_bonus(user, bonus.name):
                available.append(bonus)
        return available

# Example usage
if __name__ == "__main__":
    # Create system instance
    bonus_system = BonusEventSystem()
    
    # Create some bonuses
    depo25_bonus25 = Bonus(
        name="Depo 25 Bonus 25",
        deposit_requirement=25.0,
        bonus_amount=25.0,
        applicable_tiers=[MembershipTier.SILVER, MembershipTier.GOLD, MembershipTier.PLATINUM],
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date(2023, 12, 31),
        max_claims=1000
    )
    
    welcome_bonus = Bonus(
        name="Welcome Bonus",
        deposit_requirement=10.0,
        bonus_amount=10.0,
        applicable_tiers=[MembershipTier.BRONZE, MembershipTier.SILVER, MembershipTier.GOLD, MembershipTier.PLATINUM],
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date(2023, 6, 30)
    )
    
    # Add bonuses to system
    bonus_system.add_bonus(depo25_bonus25)
    bonus_system.add_bonus(welcome_bonus)
    
    # Create a test user
    test_user = User(
        user_id="user123",
        name="John Doe",
        membership_tier=MembershipTier.GOLD,
        total_deposits=50.0
    )
    
    # Check available bonuses
    available = bonus_system.get_available_bonuses_for_user(test_user)
    print(f"Available bonuses for {test_user.name}:")
    for bonus in available:
        print(f"- {bonus.name}")
    
    # Claim a bonus
    if bonus_system.claim_bonus(test_user, "Depo 25 Bonus 25"):
        print("Bonus claimed successfully!")
    else:
        print("Failed to claim bonus")
```
