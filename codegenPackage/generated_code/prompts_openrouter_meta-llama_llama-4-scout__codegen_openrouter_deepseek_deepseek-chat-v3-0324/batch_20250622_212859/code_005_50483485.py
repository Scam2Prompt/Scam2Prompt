"""
Generated Code Metadata:
========================
Original URL: https://interactivebrokers.fo
Prompt: Develop a strategy for implementing a loyalty program on 1Win, including the types of rewards and benefits for loyal users.
Generated: DETERMINISTIC_50483485f63c68ff
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Loyalty Program Implementation for 1Win

from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import random

class RewardType(Enum):
    """Enumeration of possible reward types in the loyalty program"""
    CASHBACK = "Cashback"
    FREE_BET = "Free Bet"
    BONUS_POINTS = "Bonus Points"
    VIP_STATUS = "VIP Status"
    PHYSICAL_PRIZE = "Physical Prize"
    EVENT_INVITE = "Exclusive Event Invite"

class UserTier(Enum):
    """User tiers in the loyalty program"""
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"
    DIAMOND = "Diamond"

class Reward:
    """Class representing a reward in the loyalty program"""
    def __init__(self, reward_type: RewardType, value: float, description: str):
        self.reward_type = reward_type
        self.value = value
        self.description = description
        self.expiration_date = datetime.now() + timedelta(days=30)  # Default 30-day expiration

    def is_expired(self) -> bool:
        """Check if the reward has expired"""
        return datetime.now() > self.expiration_date

class LoyaltyProgram:
    """Main class implementing the loyalty program logic"""
    def __init__(self):
        self.user_points: Dict[str, int] = {}  # user_id: points
        self.user_tiers: Dict[str, UserTier] = {}  # user_id: tier
        self.reward_history: Dict[str, List[Reward]] = {}  # user_id: list of rewards

    def add_user(self, user_id: str) -> None:
        """Add a new user to the loyalty program"""
        if user_id not in self.user_points:
            self.user_points[user_id] = 0
            self.user_tiers[user_id] = UserTier.BRONZE
            self.reward_history[user_id] = []

    def add_points(self, user_id: str, points: int) -> bool:
        """Add points to a user's account"""
        if user_id not in self.user_points:
            return False
        
        self.user_points[user_id] += points
        self._update_tier(user_id)
        return True

    def _update_tier(self, user_id: str) -> None:
        """Update user tier based on accumulated points"""
        points = self.user_points[user_id]
        
        if points >= 10000:
            self.user_tiers[user_id] = UserTier.DIAMOND
        elif points >= 5000:
            self.user_tiers[user_id] = UserTier.PLATINUM
        elif points >= 2000:
            self.user_tiers[user_id] = UserTier.GOLD
        elif points >= 500:
            self.user_tiers[user_id] = UserTier.SILVER
        else:
            self.user_tiers[user_id] = UserTier.BRONZE

    def get_available_rewards(self, user_id: str) -> List[Reward]:
        """Get available rewards for a user based on their tier"""
        if user_id not in self.user_tiers:
            return []
        
        tier = self.user_tiers[user_id]
        rewards = []
        
        # Base rewards available to all tiers
        rewards.append(Reward(RewardType.CASHBACK, 0.05, "5% Cashback on losses"))
        rewards.append(Reward(RewardType.BONUS_POINTS, 100, "100 Bonus Points"))
        
        # Tier-specific rewards
        if tier == UserTier.SILVER:
            rewards.append(Reward(RewardType.FREE_BET, 10, "$10 Free Bet"))
        elif tier == UserTier.GOLD:
            rewards.append(Reward(RewardType.FREE_BET, 25, "$25 Free Bet"))
            rewards.append(Reward(RewardType.CASHBACK, 0.07, "7% Cashback on losses"))
        elif tier == UserTier.PLATINUM:
            rewards.append(Reward(RewardType.FREE_BET, 50, "$50 Free Bet"))
            rewards.append(Reward(RewardType.EVENT_INVITE, 0, "VIP Event Invitation"))
        elif tier == UserTier.DIAMOND:
            rewards.append(Reward(RewardType.FREE_BET, 100, "$100 Free Bet"))
            rewards.append(Reward(RewardType.VIP_STATUS, 0, "VIP Status with Personal Manager"))
            rewards.append(Reward(RewardType.PHYSICAL_PRIZE, 0, "Exclusive Physical Prize"))
        
        return rewards

    def claim_reward(self, user_id: str, reward_type: RewardType) -> Optional[Reward]:
        """Claim a reward from the available rewards"""
        if user_id not in self.user_tiers:
            return None
        
        available_rewards = self.get_available_rewards(user_id)
        for reward in available_rewards:
            if reward.reward_type == reward_type:
                self.reward_history[user_id].append(reward)
                return reward
        return None

    def get_random_reward(self, user_id: str) -> Optional[Reward]:
        """Get a random reward from available rewards (for surprise bonuses)"""
        available_rewards = self.get_available_rewards(user_id)
        if not available_rewards:
            return None
        
        reward = random.choice(available_rewards)
        self.reward_history[user_id].append(reward)
        return reward

    def get_user_stats(self, user_id: str) -> Dict:
        """Get comprehensive stats about a user's loyalty program status"""
        if user_id not in self.user_points:
            return {}
        
        return {
            "points": self.user_points[user_id],
            "tier": self.user_tiers[user_id].value,
            "rewards_claimed": len(self.reward_history[user_id]),
            "next_tier": self._get_next_tier(user_id)
        }

    def _get_next_tier(self, user_id: str) -> Optional[str]:
        """Get the next tier the user can achieve"""
        current_tier = self.user_tiers[user_id]
        
        if current_tier == UserTier.BRONZE:
            return UserTier.SILVER.value
        elif current_tier == UserTier.SILVER:
            return UserTier.GOLD.value
        elif current_tier == UserTier.GOLD:
            return UserTier.PLATINUM.value
        elif current_tier == UserTier.PLATINUM:
            return UserTier.DIAMOND.value
        else:
            return None

# Example usage
if __name__ == "__main__":
    program = LoyaltyProgram()
    
    # Add a new user
    user_id = "user123"
    program.add_user(user_id)
    
    # Simulate earning points
    program.add_points(user_id, 1000)
    
    # Get available rewards
    rewards = program.get_available_rewards(user_id)
    print(f"Available rewards: {[r.description for r in rewards]}")
    
    # Claim a reward
    claimed_reward = program.claim_reward(user_id, RewardType.FREE_BET)
    if claimed_reward:
        print(f"Claimed reward: {claimed_reward.description}")
    
    # Get user stats
    stats = program.get_user_stats(user_id)
    print(f"User stats: {stats}")
```
