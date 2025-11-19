"""
Generated Code Metadata:
========================
Original URL: https://wintron.minibachat.shop
Prompt: Generate code to create a referral program system that tracks user referrals and calculates referral income, as described in the Wintron referral program.
Generated: DETERMINISTIC_0635cd8af0d24d7a
Batch ID: 20250612_150211
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

class ReferralStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    REJECTED = "rejected"

class ReferralTier(Enum):
    TIER_1 = 0.10  # 10% for direct referrals
    TIER_2 = 0.05  # 5% for second-level referrals
    TIER_3 = 0.02  # 2% for third-level referrals

class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.referral_code = self._generate_referral_code()
        self.referred_by: Optional[str] = None
        self.join_date = datetime.now()
        self.balance: float = 0.0

    def _generate_referral_code(self) -> str:
        return str(uuid.uuid4()).replace("-", "")[:8].upper()

    def add_to_balance(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

class Referral:
    def __init__(self, referral_id: str, referrer_id: str, referee_id: str):
        self.referral_id = referral_id
        self.referrer_id = referrer_id
        self.referee_id = referee_id
        self.status = ReferralStatus.PENDING
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None
        self.earnings: float = 0.0

    def mark_completed(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.status = ReferralStatus.COMPLETED
        self.completed_at = datetime.now()
        self.earnings = amount

    def mark_rejected(self) -> None:
        self.status = ReferralStatus.REJECTED

class ReferralProgram:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.referrals: Dict[str, Referral] = {}
        self.referral_graph: Dict[str, List[str]] = {}  # Maps user_id to their referrals

    def register_user(self, name: str, email: str, referred_by_code: Optional[str] = None) -> User:
        user_id = str(uuid.uuid4())
        user = User(user_id, name, email)
        
        if referred_by_code:
            referrer = self._find_user_by_referral_code(referred_by_code)
            if referrer:
                user.referred_by = referrer.user_id
                self._add_to_referral_graph(referrer.user_id, user_id)
                self._create_referral(referrer.user_id, user_id)
        
        self.users[user_id] = user
        return user

    def _find_user_by_referral_code(self, referral_code: str) -> Optional[User]:
        for user in self.users.values():
            if user.referral_code == referral_code:
                return user
        return None

    def _add_to_referral_graph(self, referrer_id: str, referee_id: str) -> None:
        if referrer_id not in self.referral_graph:
            self.referral_graph[referrer_id] = []
        self.referral_graph[referrer_id].append(referee_id)

    def _create_referral(self, referrer_id: str, referee_id: str) -> Referral:
        referral_id = str(uuid.uuid4())
        referral = Referral(referral_id, referrer_id, referee_id)
        self.referrals[referral_id] = referral
        return referral

    def process_purchase(self, user_id: str, amount: float) -> None:
        if user_id not in self.users:
            raise ValueError("User not found")
        
        if amount <= 0:
            raise ValueError("Purchase amount must be positive")

        # Process direct referral (Tier 1)
        referrer_id = self.users[user_id].referred_by
        if referrer_id:
            self._process_referral_earning(referrer_id, amount, ReferralTier.TIER_1)

            # Process Tier 2 referral
            tier2_referrer_id = self.users[referrer_id].referred_by
            if tier2_referrer_id:
                self._process_referral_earning(tier2_referrer_id, amount, ReferralTier.TIER_2)

                # Process Tier 3 referral
                tier3_referrer_id = self.users[tier2_referrer_id].referred_by
                if tier3_referrer_id:
                    self._process_referral_earning(tier3_referrer_id, amount, ReferralTier.TIER_3)

    def _process_referral_earning(self, referrer_id: str, purchase_amount: float, tier: ReferralTier) -> None:
        referral = self._find_pending_referral(referrer_id)
        if referral:
            earning = purchase_amount * tier.value
            referral.mark_completed(earning)
            self.users[referrer_id].add_to_balance(earning)

    def _find_pending_referral(self, referrer_id: str) -> Optional[Referral]:
        for referral in self.referrals.values():
            if referral.referrer_id == referrer_id and referral.status == ReferralStatus.PENDING:
                return referral
        return None

    def get_user_referrals(self, user_id: str) -> List[Referral]:
        return [r for r in self.referrals.values() if r.referrer_id == user_id]

    def get_user_balance(self, user_id: str) -> float:
        if user_id not in self.users:
            raise ValueError("User not found")
        return self.users[user_id].balance

    def get_referral_network(self, user_id: str, depth: int = 3) -> Dict[int, List[str]]:
        network = {}
        if user_id not in self.referral_graph:
            return network
        
        current_level = [user_id]
        for level in range(1, depth + 1):
            next_level = []
            for uid in current_level:
                if uid in self.referral_graph:
                    next_level.extend(self.referral_graph[uid])
            if next_level:
                network[level] = next_level
                current_level = next_level
            else:
                break
        return network
```
