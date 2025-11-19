"""
Generated Code Metadata:
========================
Original URL: https://jups.io
Prompt: "Design a system architecture for a VIP club program, like Jups.io's, including user tier management and reward distribution, using a suitable programming language and APIs."
Generated: DETERMINISTIC_94f308ac867ca4e4
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
VIP Club Program System Architecture
This system handles user tier management and reward distribution for a VIP club program.
"""

import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional
import logging
from datetime import datetime
import uuid

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TierLevel(Enum):
    """Enum representing VIP tier levels"""
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4
    DIAMOND = 5

@dataclass
class User:
    """Class representing a VIP club user"""
    user_id: str
    name: str
    email: str
    points: int = 0
    tier: TierLevel = TierLevel.BRONZE
    join_date: datetime = datetime.now()
    last_activity: datetime = datetime.now()

    def update_tier(self, new_tier: TierLevel) -> None:
        """Update user's tier level"""
        if not isinstance(new_tier, TierLevel):
            raise ValueError("Invalid tier level")
        self.tier = new_tier
        logger.info(f"User {self.user_id} updated to {new_tier.name} tier")

@dataclass
class Reward:
    """Class representing a reward"""
    reward_id: str
    name: str
    description: str
    points_cost: int
    tier_requirement: TierLevel

class RewardSystem:
    """Handles reward distribution and management"""
    def __init__(self):
        self.available_rewards: Dict[str, Reward] = {}
        
    def add_reward(self, reward: Reward) -> None:
        """Add a new reward to the system"""
        if reward.reward_id in self.available_rewards:
            raise ValueError("Reward ID already exists")
        self.available_rewards[reward.reward_id] = reward
        logger.info(f"Added reward: {reward.name}")

    def claim_reward(self, user: User, reward_id: str) -> bool:
        """Process reward claim for a user"""
        if reward_id not in self.available_rewards:
            logger.error(f"Reward {reward_id} not found")
            return False
            
        reward = self.available_rewards[reward_id]
        
        if user.points < reward.points_cost:
            logger.warning(f"User {user.user_id} has insufficient points for reward {reward_id}")
            return False
            
        if user.tier.value < reward.tier_requirement.value:
            logger.warning(f"User {user.user_id} doesn't meet tier requirement for reward {reward_id}")
            return False
            
        user.points -= reward.points_cost
        logger.info(f"User {user.user_id} claimed reward {reward_id}")
        return True

class TierManager:
    """Manages user tier promotions and demotions"""
    def __init__(self):
        self.tier_thresholds = {
            TierLevel.BRONZE: 0,
            TierLevel.SILVER: 1000,
            TierLevel.GOLD: 5000,
            TierLevel.PLATINUM: 15000,
            TierLevel.DIAMOND: 30000
        }
        
    def check_tier_promotion(self, user: User) -> Optional[TierLevel]:
        """Check if user qualifies for tier promotion"""
        current_points = user.points
        current_tier = user.tier
        
        # Check for higher tiers first
        for tier in sorted(TierLevel, reverse=True):
            if current_points >= self.tier_thresholds[tier] and tier.value > current_tier.value:
                return tier
        return None

class VIPClubAPI:
    """Main API for VIP club operations"""
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.reward_system = RewardSystem()
        self.tier_manager = TierManager()
        
    def register_user(self, name: str, email: str) -> User:
        """Register a new user"""
        user_id = str(uuid.uuid4())
        new_user = User(user_id=user_id, name=name, email=email)
        self.users[user_id] = new_user
        logger.info(f"Registered new user: {user_id}")
        return new_user
        
    def add_points(self, user_id: str, points: int) -> bool:
        """Add points to user's account"""
        if user_id not in self.users:
            logger.error(f"User {user_id} not found")
            return False
            
        if points <= 0:
            logger.error("Points must be positive")
            return False
            
        self.users[user_id].points += points
        self.users[user_id].last_activity = datetime.now()
        
        # Check for tier promotion
        new_tier = self.tier_manager.check_tier_promotion(self.users[user_id])
        if new_tier:
            self.users[user_id].update_tier(new_tier)
            
        logger.info(f"Added {points} points to user {user_id}")
        return True
        
    def claim_reward(self, user_id: str, reward_id: str) -> bool:
        """Handle reward claim request"""
        if user_id not in self.users:
            logger.error(f"User {user_id} not found")
            return False
            
        return self.reward_system.claim_reward(self.users[user_id], reward_id)
        
    def get_user_info(self, user_id: str) -> Optional[Dict]:
        """Get user information"""
        if user_id not in self.users:
            logger.error(f"User {user_id} not found")
            return None
            
        user = self.users[user_id]
        return {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "points": user.points,
            "tier": user.tier.name,
            "join_date": user.join_date.isoformat(),
            "last_activity": user.last_activity.isoformat()
        }

# Example usage
if __name__ == "__main__":
    # Initialize the VIP Club system
    vip_club = VIPClubAPI()
    
    # Register a new user
    user = vip_club.register_user("John Doe", "john@example.com")
    
    # Add some points
    vip_club.add_points(user.user_id, 1500)
    
    # Create and add a reward
    reward = Reward(
        reward_id=str(uuid.uuid4()),
        name="Free Drink",
        description="Complimentary beverage",
        points_cost=500,
        tier_requirement=TierLevel.SILVER
    )
    vip_club.reward_system.add_reward(reward)
    
    # Claim the reward
    if vip_club.claim_reward(user.user_id, reward.reward_id):
        print("Reward claimed successfully!")
    else:
        print("Failed to claim reward")
    
    # Get user info
    user_info = vip_club.get_user_info(user.user_id)
    print(json.dumps(user_info, indent=2))
```
