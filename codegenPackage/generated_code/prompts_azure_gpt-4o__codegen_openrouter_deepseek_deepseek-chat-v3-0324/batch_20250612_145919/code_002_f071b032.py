"""
Generated Code Metadata:
========================
Original URL: https://vatanplatform.bet
Prompt: Generate code to create a loyalty program system for an online casino, including features like cashback on losses and tiered rewards, as described in BaxBet's offerings.
Generated: DETERMINISTIC_f071b032a768df2f
Batch ID: 20250612_145919
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
from typing import List, Dict, Optional
from dataclasses import dataclass
import uuid

class Tier(Enum):
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4
    DIAMOND = 5

@dataclass
class User:
    id: str
    username: str
    total_wagered: float = 0.0
    total_losses: float = 0.0
    loyalty_points: int = 0
    tier: Tier = Tier.BRONZE
    last_activity: datetime.datetime = datetime.datetime.now()

@dataclass
class Reward:
    id: str
    name: str
    points_required: int
    description: str
    tier_requirement: Optional[Tier] = None

@dataclass
class CashbackReward:
    id: str
    percentage: float
    min_loss: float
    max_cashback: float
    tier_requirement: Tier

class LoyaltyProgram:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.rewards: List[Reward] = []
        self.cashback_rewards: List[CashbackReward] = []
        self._initialize_default_rewards()

    def _initialize_default_rewards(self):
        # Tier-based cashback rewards
        self.cashback_rewards = [
            CashbackReward(str(uuid.uuid4()), 0.05, 10.0, 50.0, Tier.BRONZE),
            CashbackReward(str(uuid.uuid4()), 0.07, 10.0, 100.0, Tier.SILVER),
            CashbackReward(str(uuid.uuid4()), 0.10, 10.0, 200.0, Tier.GOLD),
            CashbackReward(str(uuid.uuid4()), 0.15, 10.0, 500.0, Tier.PLATINUM),
            CashbackReward(str(uuid.uuid4()), 0.20, 10.0, 1000.0, Tier.DIAMOND)
        ]

        # General rewards
        self.rewards = [
            Reward(str(uuid.uuid4()), "Free Spin", 100, "10 free spins on selected slot"),
            Reward(str(uuid.uuid4()), "Bonus Cash", 500, "$10 bonus cash", Tier.SILVER),
            Reward(str(uuid.uuid4()), "VIP Event", 2000, "Invitation to VIP event", Tier.GOLD),
            Reward(str(uuid.uuid4()), "Luxury Gift", 5000, "Exclusive luxury gift", Tier.PLATINUM),
            Reward(str(uuid.uuid4()), "Personal Manager", 10000, "Dedicated account manager", Tier.DIAMOND)
        ]

    def register_user(self, username: str) -> User:
        """Register a new user with default loyalty settings."""
        user_id = str(uuid.uuid4())
        user = User(id=user_id, username=username)
        self.users[user_id] = user
        return user

    def update_user_activity(self, user_id: str, wagered: float, loss: float) -> User:
        """Update user's wagering and loss amounts, and recalculate tier."""
        if user_id not in self.users:
            raise ValueError("User not found")

        user = self.users[user_id]
        user.total_wagered += wagered
        user.total_losses += loss
        
        # Calculate loyalty points (1 point per $10 wagered)
        points_earned = int(wagered / 10)
        user.loyalty_points += points_earned
        
        # Update tier based on total wagered
        if user.total_wagered >= 1000000:
            user.tier = Tier.DIAMOND
        elif user.total_wagered >= 500000:
            user.tier = Tier.PLATINUM
        elif user.total_wagered >= 100000:
            user.tier = Tier.GOLD
        elif user.total_wagered >= 50000:
            user.tier = Tier.SILVER
        else:
            user.tier = Tier.BRONZE
            
        user.last_activity = datetime.datetime.now()
        return user

    def calculate_cashback(self, user_id: str) -> float:
        """Calculate cashback amount based on user's losses and tier."""
        if user_id not in self.users:
            raise ValueError("User not found")

        user = self.users[user_id]
        if user.total_losses <= 0:
            return 0.0

        cashback_reward = next(
            (r for r in self.cashback_rewards if r.tier_requirement == user.tier),
            None
        )

        if not cashback_reward:
            return 0.0

        cashback = user.total_losses * cashback_reward.percentage
        return min(cashback, cashback_reward.max_cashback)

    def claim_cashback(self, user_id: str) -> float:
        """Claim cashback reward and reset user's loss counter."""
        cashback = self.calculate_cashback(user_id)
        if cashback > 0:
            self.users[user_id].total_losses = 0
        return cashback

    def get_available_rewards(self, user_id: str) -> List[Reward]:
        """Get list of rewards available to the user based on their points and tier."""
        if user_id not in self.users:
            raise ValueError("User not found")

        user = self.users[user_id]
        return [
            reward for reward in self.rewards
            if reward.points_required <= user.loyalty_points and
            (reward.tier_requirement is None or reward.tier_requirement.value <= user.tier.value)
        ]

    def redeem_reward(self, user_id: str, reward_id: str) -> Reward:
        """Redeem a reward if user has enough points and meets requirements."""
        if user_id not in self.users:
            raise ValueError("User not found")

        user = self.users[user_id]
        reward = next((r for r in self.rewards if r.id == reward_id), None)
        
        if not reward:
            raise ValueError("Reward not found")
        
        if reward.points_required > user.loyalty_points:
            raise ValueError("Not enough loyalty points")
            
        if reward.tier_requirement and reward.tier_requirement.value > user.tier.value:
            raise ValueError("Tier requirement not met")
            
        user.loyalty_points -= reward.points_required
        return reward

    def get_user_tier_progress(self, user_id: str) -> Dict:
        """Get user's current tier and progress to next tier."""
        if user_id not in self.users:
            raise ValueError("User not found")

        user = self.users[user_id]
        current_tier = user.tier
        next_tier = None
        progress = 0.0
        
        if current_tier != Tier.DIAMOND:
            next_tier_value = current_tier.value + 1
            next_tier = Tier(next_tier_value)
            
            tier_thresholds = {
                Tier.BRONZE: 0,
                Tier.SILVER: 50000,
                Tier.GOLD: 100000,
                Tier.PLATINUM: 500000,
                Tier.DIAMOND: 1000000
            }
            
            current_threshold = tier_thresholds[current_tier]
            next_threshold = tier_thresholds[next_tier]
            progress = min(100.0, (user.total_wagered - current_threshold) / (next_threshold - current_threshold) * 100)
        
        return {
            "current_tier": current_tier.name,
            "next_tier": next_tier.name if next_tier else None,
            "progress": progress,
            "total_wagered": user.total_wagered
        }
```
