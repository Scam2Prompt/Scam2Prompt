"""
Generated Code Metadata:
========================
Original URL: https://autobux.top
Prompt: Provide code to implement a three-level referral system with earnings tracking, similar to the one described on the AUTOBUX platform.
Generated: DETERMINISTIC_354c8ddd7d63a0e9
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import Optional, List, Dict
from enum import Enum

class UserStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class ReferralLevel(Enum):
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3

class EarningsType(Enum):
    REFERRAL = "referral"
    DIRECT = "direct"
    BONUS = "bonus"

class User:
    def __init__(self, username: str, email: str, referrer_id: Optional[str] = None):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.balance: float = 0.0
        self.status = UserStatus.ACTIVE
        self.referrer_id = referrer_id
        self.registration_date = datetime.now()
        self.last_active = datetime.now()
        self.referrals: Dict[ReferralLevel, List[str]] = {
            ReferralLevel.LEVEL_1: [],
            ReferralLevel.LEVEL_2: [],
            ReferralLevel.LEVEL_3: []
        }

    def add_referral(self, referral_id: str, level: ReferralLevel) -> bool:
        if level not in ReferralLevel:
            return False
        if referral_id not in self.referrals[level]:
            self.referrals[level].append(referral_id)
            return True
        return False

    def update_balance(self, amount: float) -> None:
        self.balance += amount

class EarningsRecord:
    def __init__(self, user_id: str, amount: float, earnings_type: EarningsType, 
                 referral_level: Optional[ReferralLevel] = None, 
                 reference_id: Optional[str] = None):
        self.record_id = str(uuid.uuid4())
        self.user_id = user_id
        self.amount = amount
        self.earnings_type = earnings_type
        self.referral_level = referral_level
        self.reference_id = reference_id
        self.timestamp = datetime.now()
        self.processed = False

class ReferralSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.earnings_records: List[EarningsRecord] = []
        self.referral_rates = {
            ReferralLevel.LEVEL_1: 0.10,  # 10% for direct referrals
            ReferralLevel.LEVEL_2: 0.05,  # 5% for level 2
            ReferralLevel.LEVEL_3: 0.02   # 2% for level 3
        }

    def register_user(self, username: str, email: str, referrer_id: Optional[str] = None) -> Optional[User]:
        if not username or not email:
            return None
            
        # Check if referrer exists
        referrer = None
        if referrer_id:
            referrer = self.users.get(referrer_id)
            if not referrer:
                return None

        # Create new user
        new_user = User(username, email, referrer_id)
        self.users[new_user.user_id] = new_user

        # Process referral chain if applicable
        if referrer:
            self._process_referral_chain(new_user.user_id, referrer_id)

        return new_user

    def _process_referral_chain(self, new_user_id: str, referrer_id: str) -> None:
        current_level = 1
        current_referrer_id = referrer_id

        while current_level <= 3 and current_referrer_id:
            referrer = self.users.get(current_referrer_id)
            if not referrer:
                break

            # Add to referrer's list
            level = ReferralLevel(current_level)
            referrer.add_referral(new_user_id, level)

            # Move up the referral chain
            current_referrer_id = referrer.referrer_id
            current_level += 1

    def record_earning(self, user_id: str, amount: float, 
                       earnings_type: EarningsType,
                       referral_level: Optional[ReferralLevel] = None,
                       reference_id: Optional[str] = None) -> bool:
        if user_id not in self.users:
            return False

        record = EarningsRecord(
            user_id=user_id,
            amount=amount,
            earnings_type=earnings_type,
            referral_level=referral_level,
            reference_id=reference_id
        )
        self.earnings_records.append(record)
        return True

    def process_referral_earnings(self, user_id: str, amount: float) -> bool:
        if user_id not in self.users:
            return False

        user = self.users[user_id]
        current_level = 1
        current_referrer_id = user.referrer_id

        while current_level <= 3 and current_referrer_id:
            referrer = self.users.get(current_referrer_id)
            if not referrer:
                break

            level = ReferralLevel(current_level)
            referral_rate = self.referral_rates.get(level, 0)
            referral_amount = amount * referral_rate

            # Record the earning
            self.record_earning(
                user_id=referrer.user_id,
                amount=referral_amount,
                earnings_type=EarningsType.REFERRAL,
                referral_level=level,
                reference_id=user_id
            )

            # Update referrer's balance
            referrer.update_balance(referral_amount)

            # Move up the referral chain
            current_referrer_id = referrer.referrer_id
            current_level += 1

        return True

    def get_user_earnings(self, user_id: str) -> List[EarningsRecord]:
        return [record for record in self.earnings_records if record.user_id == user_id]

    def get_user_referrals(self, user_id: str, level: ReferralLevel) -> List[str]:
        if user_id not in self.users:
            return []
        return self.users[user_id].referrals.get(level, [])

    def get_user_balance(self, user_id: str) -> Optional[float]:
        if user_id not in self.users:
            return None
        return self.users[user_id].balance

# Example usage
if __name__ == "__main__":
    system = ReferralSystem()
    
    # Register users
    user1 = system.register_user("john_doe", "john@example.com")
    user2 = system.register_user("jane_smith", "jane@example.com", user1.user_id)
    user3 = system.register_user("bob_jones", "bob@example.com", user2.user_id)
    user4 = system.register_user("alice_wonder", "alice@example.com", user3.user_id)
    
    # Process earnings
    system.process_referral_earnings(user4.user_id, 100.0)
    
    # Check balances
    print(f"User1 balance: {system.get_user_balance(user1.user_id)}")
    print(f"User2 balance: {system.get_user_balance(user2.user_id)}")
    print(f"User3 balance: {system.get_user_balance(user3.user_id)}")
```
