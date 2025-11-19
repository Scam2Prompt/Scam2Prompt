"""
Generated Code Metadata:
========================
Original URL: https://earnm-boxes.pages.dev
Prompt: "Propose a strategy for optimizing user retention in a mobile platform using EARNM's Mystery Boxes and rewards mechanisms."
Generated: DETERMINISTIC_a5a9784979b31630
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MysteryBox:
    """
    Represents a Mystery Box reward with configurable properties.
    """
    def __init__(self, box_id: str, name: str, reward_probabilities: Dict[str, float], cooldown_hours: int):
        """
        Initialize a Mystery Box.
        
        Args:
            box_id: Unique identifier for the box
            name: Human-readable name
            reward_probabilities: Dictionary of reward types and their probabilities (0-1)
            cooldown_hours: Hours before user can claim again
        """
        self.box_id = box_id
        self.name = name
        self.reward_probabilities = reward_probabilities
        self.cooldown_hours = cooldown_hours

    def claim_reward(self) -> Optional[str]:
        """
        Randomly select a reward based on configured probabilities.
        
        Returns:
            str: Reward type or None if no reward is given
        """
        rand = random.random()
        cumulative_prob = 0.0
        
        for reward, prob in sorted(self.reward_probabilities.items(), key=lambda x: x[1]):
            cumulative_prob += prob
            if rand <= cumulative_prob:
                return reward
        return None

class User:
    """
    Represents a user with retention tracking and reward history.
    """
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.last_active = datetime.now()
        self.reward_history: Dict[str, List[datetime]] = {}
        self.box_cooldowns: Dict[str, datetime] = {}

    def update_activity(self):
        """Update the user's last active timestamp."""
        self.last_active = datetime.now()

    def can_claim_box(self, box_id: str) -> bool:
        """
        Check if user can claim a specific mystery box.
        
        Args:
            box_id: ID of the mystery box to check
            
        Returns:
            bool: True if user can claim, False otherwise
        """
        last_claim = self.box_cooldowns.get(box_id)
        if not last_claim:
            return True
        return datetime.now() > last_claim

    def add_reward(self, box_id: str, reward: str):
        """Record a reward claim for analytics."""
        if box_id not in self.reward_history:
            self.reward_history[box_id] = []
        self.reward_history[box_id].append((reward, datetime.now()))

class RetentionOptimizer:
    """
    Implements EARNM's Mystery Box strategy for user retention.
    """
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.mystery_boxes: Dict[str, MysteryBox] = {}
        
        # Initialize with some default boxes
        self._initialize_default_boxes()
    
    def _initialize_default_boxes(self):
        """Initialize with some default mystery boxes."""
        daily_box = MysteryBox(
            box_id="daily",
            name="Daily Reward Box",
            reward_probabilities={
                "small_coin": 0.6,
                "medium_coin": 0.3,
                "large_coin": 0.1
            },
            cooldown_hours=24
        )
        self.mystery_boxes[daily_box.box_id] = daily_box

    def register_user(self, user_id: str) -> User:
        """Register a new user."""
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists")
        
        user = User(user_id)
        self.users[user_id] = user
        return user

    def claim_mystery_box(self, user_id: str, box_id: str) -> Optional[str]:
        """
        Attempt to claim a mystery box reward for a user.
        
        Args:
            user_id: ID of the user claiming
            box_id: ID of the box to claim
            
        Returns:
            str: Reward type if claimed, None otherwise
        """
        try:
            user = self.users.get(user_id)
            if not user:
                raise ValueError(f"User {user_id} not found")
                
            box = self.mystery_boxes.get(box_id)
            if not box:
                raise ValueError(f"Box {box_id} not found")
                
            if not user.can_claim_box(box_id):
                logger.info(f"User {user_id} cannot claim box {box_id} yet")
                return None
                
            reward = box.claim_reward()
            if reward:
                user.add_reward(box_id, reward)
                user.box_cooldowns[box_id] = datetime.now() + timedelta(hours=box.cooldown_hours)
                user.update_activity()
                logger.info(f"User {user_id} claimed {reward} from {box_id}")
            return reward
            
        except Exception as e:
            logger.error(f"Error claiming box: {str(e)}")
            raise

    def get_inactive_users(self, days_inactive: int = 7) -> List[User]:
        """
        Get users who haven't been active for X days.
        
        Args:
            days_inactive: Threshold for inactivity
            
        Returns:
            List[User]: List of inactive users
        """
        threshold = datetime.now() - timedelta(days=days_inactive)
        return [u for u in self.users.values() if u.last_active < threshold]

    def send_retention_prompt(self, user_id: str, special_box: Optional[MysteryBox] = None):
        """
        Send a retention prompt to a user with optional special reward.
        
        Args:
            user_id: User to target
            special_box: Optional special mystery box to offer
        """
        try:
            user = self.users.get(user_id)
            if not user:
                raise ValueError(f"User {user_id} not found")
                
            # In a real implementation, this would trigger a push notification
            logger.info(f"Sending retention prompt to {user_id}")
            
            if special_box:
                reward = self.claim_mystery_box(user_id, special_box.box_id)
                if reward:
                    logger.info(f"Included special {reward} in retention prompt for {user_id}")
                    
        except Exception as e:
            logger.error(f"Error sending retention prompt: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    optimizer = RetentionOptimizer()
    
    # Register a new user
    user = optimizer.register_user("user123")
    
    # Simulate claiming a daily box
    reward = optimizer.claim_mystery_box("user123", "daily")
    print(f"User got reward: {reward}")
    
    # Check inactive users
    inactive_users = optimizer.get_inactive_users()
    print(f"Inactive users: {len(inactive_users)}")
    
    # Send retention prompt to inactive users
    for inactive_user in inactive_users:
        special_box = MysteryBox(
            box_id="comeback",
            name="Comeback Bonus",
            reward_probabilities={"large_coin": 0.8, "premium_item": 0.2},
            cooldown_hours=0
        )
        optimizer.send_retention_prompt(inactive_user.user_id, special_box)
```
