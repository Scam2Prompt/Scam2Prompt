"""
Generated Code Metadata:
========================
Original URL: https://coindoor.trade
Prompt: Illustrate how to implement a referral program in a trading application, inspired by Coindoor's five-level referral income structure.
Generated: DETERMINISTIC_371b63606d7b6b28
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum

# Database models (simplified for illustration)
class User:
    def __init__(self, user_id: str, referrer_id: Optional[str] = None):
        self.user_id = user_id
        self.referrer_id = referrer_id
        self.registration_date = datetime.now()

class ReferralLevel(Enum):
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4
    LEVEL_5 = 5

class ReferralBonus:
    def __init__(self, level: ReferralLevel, percentage: float):
        self.level = level
        self.percentage = percentage

class ReferralEarning:
    def __init__(self, user_id: str, referrer_id: str, level: ReferralLevel, amount: float, transaction_id: str):
        self.user_id = user_id
        self.referrer_id = referrer_id
        self.level = level
        self.amount = amount
        self.transaction_id = transaction_id
        self.timestamp = datetime.now()

# Database simulation
class Database:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.referral_earnings: List[ReferralEarning] = []
        self.referral_bonuses = {
            ReferralLevel.LEVEL_1: ReferralBonus(ReferralLevel.LEVEL_1, 0.30),
            ReferralLevel.LEVEL_2: ReferralBonus(ReferralLevel.LEVEL_2, 0.20),
            ReferralLevel.LEVEL_3: ReferralBonus(ReferralLevel.LEVEL_3, 0.15),
            ReferralLevel.LEVEL_4: ReferralBonus(ReferralLevel.LEVEL_4, 0.10),
            ReferralLevel.LEVEL_5: ReferralBonus(ReferralLevel.LEVEL_5, 0.05)
        }

    def add_user(self, user: User) -> None:
        self.users[user.user_id] = user

    def get_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def add_referral_earning(self, earning: ReferralEarning) -> None:
        self.referral_earnings.append(earning)

    def get_referral_bonus(self, level: ReferralLevel) -> Optional[ReferralBonus]:
        return self.referral_bonuses.get(level)

# Referral service
class ReferralService:
    def __init__(self, db: Database):
        self.db = db

    def register_user(self, user_id: str, referrer_id: Optional[str] = None) -> User:
        """Register a new user with optional referrer."""
        if user_id in self.db.users:
            raise ValueError("User already exists")
        
        if referrer_id and referrer_id not in self.db.users:
            raise ValueError("Referrer does not exist")
        
        user = User(user_id, referrer_id)
        self.db.add_user(user)
        return user

    def get_referral_hierarchy(self, user_id: str, max_level: int = 5) -> Dict[int, Optional[str]]:
        """Get the referral hierarchy up to max_level depth."""
        hierarchy = {}
        current_user_id = user_id
        for level in range(1, max_level + 1):
            user = self.db.get_user(current_user_id)
            if not user or not user.referrer_id:
                hierarchy[level] = None
                break
            hierarchy[level] = user.referrer_id
            current_user_id = user.referrer_id
        return hierarchy

    def process_referral_earnings(self, user_id: str, transaction_amount: float, transaction_id: str) -> List[ReferralEarning]:
        """Process referral earnings for a transaction based on 5-level hierarchy."""
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be positive")
        
        hierarchy = self.get_referral_hierarchy(user_id)
        if not hierarchy:
            return []
        
        earnings = []
        for level, referrer_id in hierarchy.items():
            if not referrer_id:
                continue
            
            bonus = self.db.get_referral_bonus(ReferralLevel(level))
            if not bonus:
                continue
            
            earning_amount = transaction_amount * bonus.percentage
            earning = ReferralEarning(
                user_id=user_id,
                referrer_id=referrer_id,
                level=ReferralLevel(level),
                amount=earning_amount,
                transaction_id=transaction_id
            )
            self.db.add_referral_earning(earning)
            earnings.append(earning)
        
        return earnings

# Example usage
if __name__ == "__main__":
    # Initialize database and service
    db = Database()
    referral_service = ReferralService(db)

    # Register users with referral chain: user1 -> user2 -> user3 -> user4 -> user5 -> user6
    user1 = referral_service.register_user("user1")
    user2 = referral_service.register_user("user2", "user1")
    user3 = referral_service.register_user("user3", "user2")
    user4 = referral_service.register_user("user4", "user3")
    user5 = referral_service.register_user("user5", "user4")
    user6 = referral_service.register_user("user6", "user5")

    # Process a transaction for user6
    transaction_id = str(uuid.uuid4())
    earnings = referral_service.process_referral_earnings("user6", 1000.0, transaction_id)

    # Print earnings
    for earning in earnings:
        print(f"Level {earning.level.value}: {earning.referrer_id} earned {earning.amount}")
```
