"""
Generated Code Metadata:
========================
Original URL: https://halo-social.pages.dev
Prompt: How can I implement a system to track social influence and reward users with Halo XP based on their contributions, following the guidelines provided by halo.social?
Generated: DETERMINISTIC_2fbf64e838007754
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, List, Optional
from datetime import datetime
from enum import Enum
import uuid

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContributionType(Enum):
    """Enum representing different types of contributions."""
    POST = "post"
    COMMENT = "comment"
    LIKE = "like"
    SHARE = "share"
    FOLLOW = "follow"

class User:
    """Class representing a user in the system."""
    def __init__(self, user_id: str, username: str):
        self.user_id = user_id
        self.username = username
        self.xp = 0
        self.contributions: List['Contribution'] = []

    def add_xp(self, amount: int) -> None:
        """Add XP to the user's total."""
        if amount <= 0:
            raise ValueError("XP amount must be positive")
        self.xp += amount
        logger.info(f"Added {amount} XP to user {self.username}. Total XP: {self.xp}")

class Contribution:
    """Class representing a user contribution."""
    def __init__(self, contribution_id: str, user: User, contribution_type: ContributionType, content: Optional[str] = None):
        self.contribution_id = contribution_id
        self.user = user
        self.type = contribution_type
        self.content = content
        self.timestamp = datetime.utcnow()
        self.xp_rewarded = 0

class XPCalculator:
    """Class responsible for calculating XP rewards based on contribution type."""
    _XP_VALUES = {
        ContributionType.POST: 10,
        ContributionType.COMMENT: 5,
        ContributionType.LIKE: 1,
        ContributionType.SHARE: 3,
        ContributionType.FOLLOW: 2
    }

    @classmethod
    def calculate_xp(cls, contribution: Contribution) -> int:
        """Calculate XP for a given contribution."""
        return cls._XP_VALUES.get(contribution.type, 0)

class InfluenceTracker:
    """Main class for tracking social influence and rewarding XP."""
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.contributions: Dict[str, Contribution] = {}

    def register_user(self, username: str) -> User:
        """Register a new user."""
        if not username:
            raise ValueError("Username cannot be empty")
        
        user_id = str(uuid.uuid4())
        user = User(user_id, username)
        self.users[user_id] = user
        logger.info(f"Registered new user: {username}")
        return user

    def add_contribution(self, user: User, contribution_type: ContributionType, content: Optional[str] = None) -> Contribution:
        """Record a new contribution from a user."""
        if user.user_id not in self.users:
            raise ValueError("User not registered")
        
        contribution_id = str(uuid.uuid4())
        contribution = Contribution(contribution_id, user, contribution_type, content)
        self.contributions[contribution_id] = contribution
        user.contributions.append(contribution)
        
        xp_reward = XPCalculator.calculate_xp(contribution)
        user.add_xp(xp_reward)
        contribution.xp_rewarded = xp_reward
        
        logger.info(f"Recorded {contribution_type.value} contribution from {user.username}")
        return contribution

    def get_user_xp(self, user_id: str) -> int:
        """Get a user's total XP."""
        if user_id not in self.users:
            raise ValueError("User not found")
        return self.users[user_id].xp

    def get_user_contributions(self, user_id: str) -> List[Contribution]:
        """Get all contributions for a user."""
        if user_id not in self.users:
            raise ValueError("User not found")
        return self.users[user_id].contributions

# Example usage
if __name__ == "__main__":
    tracker = InfluenceTracker()
    
    try:
        # Register users
        user1 = tracker.register_user("alice")
        user2 = tracker.register_user("bob")
        
        # Add contributions
        tracker.add_contribution(user1, ContributionType.POST, "Hello world!")
        tracker.add_contribution(user2, ContributionType.COMMENT, "Nice post!")
        tracker.add_contribution(user1, ContributionType.LIKE)
        
        # Check XP
        print(f"{user1.username} has {tracker.get_user_xp(user1.user_id)} XP")
        print(f"{user2.username} has {tracker.get_user_xp(user2.user_id)} XP")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
```
