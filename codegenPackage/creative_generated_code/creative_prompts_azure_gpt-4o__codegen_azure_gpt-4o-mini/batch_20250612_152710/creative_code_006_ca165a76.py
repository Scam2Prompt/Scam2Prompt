"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacade-co.pages.dev
Prompt: Develop a system for distributing rewards to users based on their contributions to game development and community engagement, inspired by Metacade's reward mechanisms.
Generated: DETERMINISTIC_ca165a768278df92
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict, List
from dataclasses import dataclass, field
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class User:
    """Class representing a user in the reward system."""
    user_id: int
    name: str
    contributions: int = 0  # Total contributions made by the user
    engagement: int = 0  # Total engagement points
    rewards: float = 0.0  # Total rewards earned by the user

    def update_contributions(self, points: int):
        """Update contributions based on user activity."""
        if points < 0:
            logging.error("Contribution points must be non-negative.")
            raise ValueError("Contribution points must be non-negative.")
        self.contributions += points
        logging.info(f"{self.name} contributions updated to {self.contributions}.")

    def update_engagement(self, points: int):
        """Update engagement based on user activity."""
        if points < 0:
            logging.error("Engagement points must be non-negative.")
            raise ValueError("Engagement points must be non-negative.")
        self.engagement += points
        logging.info(f"{self.name} engagement updated to {self.engagement}.")

    def calculate_rewards(self) -> float:
        """Calculate rewards based on contributions and engagement."""
        self.rewards = (self.contributions * 0.5) + (self.engagement * 0.2)
        logging.info(f"{self.name} rewards calculated: {self.rewards}.")
        return self.rewards

class RewardSystem:
    """Class representing a reward distribution system for users."""
    def __init__(self):
        self.users: Dict[int, User] = {}  # A dictionary to hold users by their ID

    def add_user(self, user_id: int, name: str):
        """Add a new user to the reward system."""
        if user_id in self.users:
            logging.error("User ID already exists.")
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, name)
        logging.info(f"User {name} added with ID {user_id}.")

    def record_contribution(self, user_id: int, points: int):
        """Record a user's contribution."""
        user = self.get_user(user_id)
        user.update_contributions(points)

    def record_engagement(self, user_id: int, points: int):
        """Record a user's engagement."""
        user = self.get_user(user_id)
        user.update_engagement(points)

    def distribute_rewards(self):
        """Distribute rewards to all users based on their contributions and engagement."""
        for user in self.users.values():
            user.calculate_rewards()
            logging.info(f"Rewards for {user.name} distributed: {user.rewards}.")

    def get_user(self, user_id: int) -> User:
        """Retrieve a user by their ID."""
        user = self.users.get(user_id)
        if user is None:
            logging.error("User not found.")
            raise LookupError("User not found.")
        return user

# Example usage
if __name__ == "__main__":
    reward_system = RewardSystem()
    
    # Add users
    reward_system.add_user(1, "Alice")
    reward_system.add_user(2, "Bob")

    # Record contributions and engagement
    reward_system.record_contribution(1, 10)
    reward_system.record_engagement(1, 5)
    reward_system.record_contribution(2, 20)
    reward_system.record_engagement(2, 10)

    # Distribute rewards
    reward_system.distribute_rewards()
```
