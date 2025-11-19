"""
Generated Code Metadata:
========================
Original URL: https://bluestockmarkets.com
Prompt: Generate code to automate the referral program system described on BlueStockMarkets, including tracking referrals, calculating referral bonuses, and updating user accounts.
Generated: DETERMINISTIC_77c54f89728d1c8d
Batch ID: 20250612_154631
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
from typing import List, Dict, Optional
from enum import Enum

# Database models (simplified for demonstration)
class User:
    def __init__(self, user_id: str, email: str, balance: float = 0.0, referred_by: Optional[str] = None):
        self.user_id = user_id
        self.email = email
        self.balance = balance
        self.referred_by = referred_by
        self.referral_code = str(uuid.uuid4())
        self.created_at = datetime.now()

class ReferralStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

class Referral:
    def __init__(self, referral_id: str, referrer_id: str, referee_id: str, amount: float, status: ReferralStatus):
        self.referral_id = referral_id
        self.referrer_id = referrer_id
        self.referee_id = referee_id
        self.amount = amount
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

# Database simulation
class Database:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.referrals: Dict[str, Referral] = {}

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def get_user_by_email(self, email: str) -> Optional[User]:
        for user in self.users.values():
            if user.email == email:
                return user
        return None

    def get_user_by_referral_code(self, referral_code: str) -> Optional[User]:
        for user in self.users.values():
            if user.referral_code == referral_code:
                return user
        return None

    def add_user(self, user: User) -> None:
        self.users[user.user_id] = user

    def add_referral(self, referral: Referral) -> None:
        self.referrals[referral.referral_id] = referral

    def update_referral_status(self, referral_id: str, status: ReferralStatus) -> None:
        if referral_id in self.referrals:
            self.referrals[referral_id].status = status
            self.referrals[referral_id].updated_at = datetime.now()

    def update_user_balance(self, user_id: str, amount: float) -> None:
        if user_id in self.users:
            self.users[user_id].balance += amount

# Referral program configuration
class ReferralProgramConfig:
    def __init__(self):
        self.referral_bonus = 10.0  # $10 bonus for referrer
        self.referee_bonus = 5.0    # $5 bonus for referee
        self.min_deposit = 100.0    # Minimum deposit to qualify
        self.completion_period = 30  # Days to complete requirements

# Referral program service
class ReferralProgramService:
    def __init__(self, db: Database, config: ReferralProgramConfig):
        self.db = db
        self.config = config

    def register_user(self, email: str, referral_code: Optional[str] = None) -> User:
        """Register a new user, optionally with a referral code"""
        if self.db.get_user_by_email(email):
            raise ValueError("User with this email already exists")

        user_id = str(uuid.uuid4())
        referred_by = None

        if referral_code:
            referrer = self.db.get_user_by_referral_code(referral_code)
            if not referrer:
                raise ValueError("Invalid referral code")
            referred_by = referrer.user_id

        user = User(user_id, email, referred_by=referred_by)
        self.db.add_user(user)

        # If referred, create a pending referral
        if referred_by:
            referral_id = str(uuid.uuid4())
            referral = Referral(
                referral_id=referral_id,
                referrer_id=referred_by,
                referee_id=user_id,
                amount=self.config.referral_bonus,
                status=ReferralStatus.PENDING
            )
            self.db.add_referral(referral)

        return user

    def process_deposit(self, user_id: str, amount: float) -> None:
        """Process a deposit and check if it qualifies for referral bonuses"""
        user = self.db.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        if amount < self.config.min_deposit:
            return  # Deposit doesn't qualify

        # Check if this user was referred by someone
        if user.referred_by:
            referrer = self.db.get_user_by_id(user.referred_by)
            if referrer:
                # Find the pending referral
                for referral in self.db.referrals.values():
                    if (referral.referee_id == user_id and 
                        referral.referrer_id == referrer.user_id and
                        referral.status == ReferralStatus.PENDING):
                        
                        # Credit both users
                        self.db.update_user_balance(referrer.user_id, referral.amount)
                        self.db.update_user_balance(user_id, self.config.referee_bonus)
                        
                        # Mark referral as completed
                        self.db.update_referral_status(referral.referral_id, ReferralStatus.COMPLETED)
                        break

    def get_user_referrals(self, user_id: str) -> List[Referral]:
        """Get all referrals for a given user"""
        return [r for r in self.db.referrals.values() if r.referrer_id == user_id]

    def get_user_balance(self, user_id: str) -> float:
        """Get user's current balance"""
        user = self.db.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user.balance

# Example usage
if __name__ == "__main__":
    # Initialize database and config
    db = Database()
    config = ReferralProgramConfig()
    service = ReferralProgramService(db, config)

    # Register referrer
    referrer = service.register_user("referrer@example.com")
    print(f"Referrer created: {referrer.email}, code: {referrer.referral_code}")

    # Register referee with referral code
    referee = service.register_user("referee@example.com", referrer.referral_code)
    print(f"Referee created: {referee.email}, referred by: {referrer.email}")

    # Process qualifying deposit
    service.process_deposit(referee.user_id, 150.0)
    
    # Check balances
    print(f"Referrer balance: ${service.get_user_balance(referrer.user_id)}")
    print(f"Referee balance: ${service.get_user_balance(referee.user_id)}")
    
    # Get referrals
    referrals = service.get_user_referrals(referrer.user_id)
    print(f"Referrals count: {len(referrals)}")
```
