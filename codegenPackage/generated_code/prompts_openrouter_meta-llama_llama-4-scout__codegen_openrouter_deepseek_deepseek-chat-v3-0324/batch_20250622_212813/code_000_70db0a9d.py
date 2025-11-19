"""
Generated Code Metadata:
========================
Original URL: https://staylodu.io
Prompt: Explain how the Loud platform's reward system works, including how mindshare is calculated and how rewards are distributed to top contributors.
Generated: DETERMINISTIC_70db0a9d0c7767c4
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Loud Platform Reward System Implementation

This module handles the calculation of mindshare and distribution of rewards
to top contributors based on their engagement and contributions.
"""

from typing import List, Dict
from datetime import datetime, timedelta
import math

class Contribution:
    """Represents a single contribution by a user"""
    def __init__(self, user_id: str, contribution_type: str, value: float, timestamp: datetime):
        self.user_id = user_id
        self.type = contribution_type  # e.g., 'post', 'comment', 'vote', 'share'
        self.value = value  # Contribution weight/quality score
        self.timestamp = timestamp

class User:
    """Represents a user and their contributions"""
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.contributions: List[Contribution] = []
        self.mindshare = 0.0

    def add_contribution(self, contribution: Contribution):
        """Add a new contribution to the user's record"""
        self.contributions.append(contribution)

class RewardSystem:
    """Handles mindshare calculation and reward distribution"""
    
    # Contribution type weights
    CONTRIBUTION_WEIGHTS = {
        'post': 1.0,
        'comment': 0.7,
        'vote': 0.3,
        'share': 0.5
    }
    
    # Time decay factor (daily)
    TIME_DECAY = 0.95
    
    def __init__(self, total_reward_pool: float):
        self.total_reward_pool = total_reward_pool
        self.users: Dict[str, User] = {}
    
    def register_contribution(self, user_id: str, contribution_type: str, value: float, timestamp: datetime):
        """Record a new contribution from a user"""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
        
        contribution = Contribution(user_id, contribution_type, value, timestamp)
        self.users[user_id].add_contribution(contribution)
    
    def calculate_mindshare(self, current_time: datetime):
        """
        Calculate mindshare for all users based on their contributions.
        Mindshare decays over time and is weighted by contribution type.
        """
        for user in self.users.values():
            total = 0.0
            for contrib in user.contributions:
                # Calculate time decay
                days_old = (current_time - contrib.timestamp).days
                decay_factor = math.pow(self.TIME_DECAY, days_old)
                
                # Apply contribution type weight and value
                weight = self.CONTRIBUTION_WEIGHTS.get(contrib.type, 0.5)
                total += contrib.value * weight * decay_factor
            
            user.mindshare = total
    
    def distribute_rewards(self) -> Dict[str, float]:
        """
        Distribute rewards from the pool to top contributors based on mindshare.
        Returns a dictionary of user_id to reward amount.
        """
        if not self.users:
            return {}
        
        # Calculate total mindshare across all users
        total_mindshare = sum(user.mindshare for user in self.users.values())
        if total_mindshare <= 0:
            return {}
        
        # Calculate rewards proportionally
        rewards = {}
        for user_id, user in self.users.items():
            share = user.mindshare / total_mindshare
            rewards[user_id] = share * self.total_reward_pool
        
        return rewards
    
    def get_top_contributors(self, count: int = 10) -> List[User]:
        """Get top contributors sorted by mindshare"""
        sorted_users = sorted(
            self.users.values(),
            key=lambda u: u.mindshare,
            reverse=True
        )
        return sorted_users[:count]
```
