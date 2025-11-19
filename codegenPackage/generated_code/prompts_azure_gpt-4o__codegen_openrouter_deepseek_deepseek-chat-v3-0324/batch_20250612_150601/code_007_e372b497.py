"""
Generated Code Metadata:
========================
Original URL: https://minthidden.web.app
Prompt: Write code to implement dynamic rewards based on user activity or level status, as referenced in the "My rewards" section of the website.
Generated: DETERMINISTIC_e372b497d5b67d48
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RewardType(Enum):
    """Enumeration of reward types."""
    DISCOUNT = "discount"
    FREE_SHIPPING = "free_shipping"
    GIFT_CARD = "gift_card"
    EARLY_ACCESS = "early_access"
    EXCLUSIVE_CONTENT = "exclusive_content"


class UserLevel(Enum):
    """Enumeration of user levels."""
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    PLATINUM = "platinum"


class Reward:
    """Class representing a reward."""
    
    def __init__(
        self,
        reward_id: str,
        reward_type: RewardType,
        name: str,
        description: str,
        value: float,
        expiry_days: int = 30,
        min_level: Optional[UserLevel] = None,
        required_activity: Optional[int] = None
    ):
        self.reward_id = reward_id
        self.reward_type = reward_type
        self.name = name
        self.description = description
        self.value = value
        self.expiry_date = datetime.now() + timedelta(days=expiry_days)
        self.min_level = min_level
        self.required_activity = required_activity
    
    def is_eligible(self, user_level: UserLevel, user_activity: int) -> bool:
        """Check if user is eligible for this reward."""
        level_ok = (self.min_level is None or user_level.value >= self.min_level.value)
        activity_ok = (self.required_activity is None or user_activity >= self.required_activity)
        return level_ok and activity_ok
    
    def to_dict(self) -> Dict:
        """Convert reward to dictionary for API response."""
        return {
            "reward_id": self.reward_id,
            "type": self.reward_type.value,
            "name": self.name,
            "description": self.description,
            "value": self.value,
            "expiry_date": self.expiry_date.isoformat(),
            "min_level": self.min_level.value if self.min_level else None,
            "required_activity": self.required_activity
        }


class RewardSystem:
    """Class managing the reward system."""
    
    def __init__(self):
        self.rewards: List[Reward] = []
        self._initialize_rewards()
    
    def _initialize_rewards(self):
        """Initialize the available rewards."""
        self.rewards = [
            Reward(
                reward_id="r1",
                reward_type=RewardType.DISCOUNT,
                name="10% Off",
                description="10% discount on your next purchase",
                value=10.0,
                min_level=UserLevel.BRONZE
            ),
            Reward(
                reward_id="r2",
                reward_type=RewardType.FREE_SHIPPING,
                name="Free Shipping",
                description="Free shipping on your next order",
                value=5.99,
                min_level=UserLevel.SILVER,
                required_activity=5
            ),
            Reward(
                reward_id="r3",
                reward_type=RewardType.GIFT_CARD,
                name="$20 Gift Card",
                description="$20 gift card for your next purchase",
                value=20.0,
                min_level=UserLevel.GOLD,
                required_activity=15
            ),
            Reward(
                reward_id="r4",
                reward_type=RewardType.EARLY_ACCESS,
                name="Early Access",
                description="Early access to new products",
                value=0.0,
                min_level=UserLevel.PLATINUM,
                required_activity=30
            )
        ]
    
    def get_available_rewards(
        self,
        user_level: UserLevel,
        user_activity: int
    ) -> List[Dict]:
        """Get available rewards for a user based on level and activity."""
        try:
            available_rewards = [
                reward.to_dict()
                for reward in self.rewards
                if reward.is_eligible(user_level, user_activity)
                and datetime.now() < reward.expiry_date
            ]
            return available_rewards
        except Exception as e:
            logger.error(f"Error getting available rewards: {e}")
            return []
    
    def add_reward(self, reward: Reward) -> bool:
        """Add a new reward to the system."""
        try:
            self.rewards.append(reward)
            return True
        except Exception as e:
            logger.error(f"Error adding reward: {e}")
            return False
    
    def remove_expired_rewards(self) -> int:
        """Remove expired rewards and return count of removed rewards."""
        try:
            initial_count = len(self.rewards)
            self.rewards = [
                reward for reward in self.rewards
                if datetime.now() < reward.expiry_date
            ]
            return initial_count - len(self.rewards)
        except Exception as e:
            logger.error(f"Error removing expired rewards: {e}")
            return 0


# Example usage
if __name__ == "__main__":
    reward_system = RewardSystem()
    
    # Get rewards for a silver user with 10 activities
    user_level = UserLevel.SILVER
    user_activity = 10
    rewards = reward_system.get_available_rewards(user_level, user_activity)
    
    print(f"Available rewards for {user_level.value} level with {user_activity} activities:")
    for reward in rewards:
        print(f"- {reward['name']} ({reward['type']}): {reward['description']}")
```
