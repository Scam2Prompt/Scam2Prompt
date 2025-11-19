"""
Generated Code Metadata:
========================
Original URL: https://wynn-seven.vercel.app
Prompt: Generate code to implement a referral system for a cryptocurrency platform, where users can earn rewards and multipliers for inviting friends.
Generated: DETERMINISTIC_a335ff1da3d2a762
Batch ID: 20250622_212746
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
from typing import Optional, List, Dict
from enum import Enum
import hashlib

# Database models would typically be defined here
# For this example, we'll use simple in-memory structures
class User:
    def __init__(self, user_id: str, email: str, referral_code: str, referred_by: Optional[str] = None):
        self.user_id = user_id
        self.email = email
        self.referral_code = referral_code
        self.referred_by = referred_by
        self.registration_date = datetime.now()
        self.referrals: List[str] = []
        self.total_rewards = 0.0
        self.tier = 1

class Reward:
    def __init__(self, reward_id: str, user_id: str, amount: float, reward_type: str, timestamp: datetime):
        self.reward_id = reward_id
        self.user_id = user_id
        self.amount = amount
        self.reward_type = reward_type
        self.timestamp = timestamp
        self.status = "pending"  # pending, paid, cancelled

class ReferralTier(Enum):
    TIER_1 = (1, 0.1)  # 10% reward
    TIER_2 = (2, 0.15)  # 15% reward
    TIER_3 = (3, 0.2)   # 20% reward

    def __init__(self, tier: int, reward_multiplier: float):
        self.tier = tier
        self.reward_multiplier = reward_multiplier

class ReferralSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.rewards: Dict[str, Reward] = {}
        self.referral_codes: Dict[str, str] = {}  # code -> user_id

    def register_user(self, email: str, referred_by_code: Optional[str] = None) -> User:
        """Register a new user, optionally with a referral code."""
        if not email:
            raise ValueError("Email is required")
        
        # Check if user already exists
        for user in self.users.values():
            if user.email == email:
                raise ValueError("User already exists")

        user_id = str(uuid.uuid4())
        referral_code = self._generate_referral_code(email)
        
        referred_by = None
        if referred_by_code:
            referred_by = self.referral_codes.get(referred_by_code)
            if not referred_by:
                raise ValueError("Invalid referral code")

        new_user = User(user_id, email, referral_code, referred_by)
        self.users[user_id] = new_user
        self.referral_codes[referral_code] = user_id

        if referred_by:
            self._process_referral(referred_by, user_id)

        return new_user

    def _generate_referral_code(self, email: str) -> str:
        """Generate a unique referral code based on user email."""
        salt = str(uuid.uuid4())
        hash_input = f"{email}{salt}{datetime.now().timestamp()}".encode('utf-8')
        code = hashlib.sha256(hash_input).hexdigest()[:8].upper()
        return code

    def _process_referral(self, referrer_id: str, referee_id: str):
        """Process a successful referral."""
        referrer = self.users.get(referrer_id)
        referee = self.users.get(referee_id)

        if not referrer or not referee:
            raise ValueError("Invalid user IDs")

        referrer.referrals.append(referee_id)
        self._update_user_tier(referrer)
        
        # Calculate reward based on current tier
        reward_amount = self._calculate_reward(referrer.tier)
        self._create_reward(referrer.user_id, reward_amount, "referral")

    def _calculate_reward(self, tier: int) -> float:
        """Calculate reward amount based on tier."""
        for referral_tier in ReferralTier:
            if referral_tier.tier == tier:
                return referral_tier.reward_multiplier
        return ReferralTier.TIER_1.reward_multiplier

    def _create_reward(self, user_id: str, amount: float, reward_type: str) -> Reward:
        """Create a new reward entry."""
        reward_id = str(uuid.uuid4())
        reward = Reward(reward_id, user_id, amount, reward_type, datetime.now())
        self.rewards[reward_id] = reward
        self.users[user_id].total_rewards += amount
        return reward

    def _update_user_tier(self, user: User):
        """Update user's tier based on number of successful referrals."""
        referral_count = len(user.referrals)
        
        if referral_count >= 50:
            user.tier = ReferralTier.TIER_3.tier
        elif referral_count >= 10:
            user.tier = ReferralTier.TIER_2.tier
        else:
            user.tier = ReferralTier.TIER_1.tier

    def get_user_rewards(self, user_id: str) -> List[Reward]:
        """Get all rewards for a user."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        return [reward for reward in self.rewards.values() if reward.user_id == user_id]

    def get_user_referrals(self, user_id: str) -> List[User]:
        """Get all referrals for a user."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        user = self.users[user_id]
        return [self.users[ref_id] for ref_id in user.referrals if ref_id in self.users]

    def get_referral_stats(self, user_id: str) -> Dict:
        """Get referral statistics for a user."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        user = self.users[user_id]
        return {
            "total_referrals": len(user.referrals),
            "total_rewards": user.total_rewards,
            "current_tier": user.tier,
            "referral_code": user.referral_code
        }

    def process_reward_payout(self, reward_id: str) -> bool:
        """Process payout for a reward."""
        reward = self.rewards.get(reward_id)
        if not reward:
            raise ValueError("Reward not found")
        
        if reward.status != "pending":
            raise ValueError(f"Reward already {reward.status}")
        
        # In a real implementation, this would connect to payment processor
        reward.status = "paid"
        return True
```
