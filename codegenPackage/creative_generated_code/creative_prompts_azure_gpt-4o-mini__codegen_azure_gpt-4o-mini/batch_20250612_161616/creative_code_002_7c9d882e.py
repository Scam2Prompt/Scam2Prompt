"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld2.pages.dev
Prompt: Can you provide an example of how to create a dual incentivization model for a socialfi platform like Everyworld, focusing on user engagement and environmental conservation?
Generated: DETERMINISTIC_7c9d882ef0e843e1
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta

class User:
    """Represents a user in the socialfi platform."""

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.engagement_score = 0
        self.conservation_score = 0

    def __repr__(self):
        return f"User({self.username}, Engagement: {self.engagement_score}, Conservation: {self.conservation_score})"

    def update_engagement(self, points):
        """Update the user's engagement score."""
        self.engagement_score += points

    def update_conservation(self, points):
        """Update the user's conservation score."""
        self.conservation_score += points

class IncentiveModel:
    """Handles the dual incentivization model for user engagement and environmental conservation."""

    def __init__(self):
        self.users = {}
        self.engagement_threshold = 100  # Points needed for engagement rewards
        self.conservation_threshold = 80  # Points needed for conservation rewards

    def add_user(self, user):
        """Add a new user to the platform."""
        if user.user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user.user_id] = user

    def record_engagement(self, user_id, points):
        """Record user engagement and check for rewards."""
        user = self._get_user(user_id)
        user.update_engagement(points)
        self._check_engagement_reward(user)

    def record_conservation(self, user_id, points):
        """Record user conservation activity and check for rewards."""
        user = self._get_user(user_id)
        user.update_conservation(points)
        self._check_conservation_reward(user)

    def _get_user(self, user_id):
        """Retrieve a user by user ID."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        return self.users[user_id]

    def _check_engagement_reward(self, user):
        """Check if the user qualifies for an engagement reward."""
        if user.engagement_score >= self.engagement_threshold:
            self._reward_user(user, "engagement")
            user.engagement_score = 0  # Reset score after reward

    def _check_conservation_reward(self, user):
        """Check if the user qualifies for a conservation reward."""
        if user.conservation_score >= self.conservation_threshold:
            self._reward_user(user, "conservation")
            user.conservation_score = 0  # Reset score after reward

    def _reward_user(self, user, reward_type):
        """Reward the user based on the type of incentive."""
        # Here, we can implement the logic for distributing rewards.
        print(f"Rewarding {user.username} for {reward_type}!")

def main():
    """Main function to demonstrate the functionality of the incentivization model."""
    try:
        model = IncentiveModel()
        
        # Create users
        user1 = User(user_id=1, username="Alice")
        user2 = User(user_id=2, username="Bob")
        
        # Add users to the model
        model.add_user(user1)
        model.add_user(user2)
        
        # Simulate user engagement and conservation activities
        model.record_engagement(user_id=1, points=50)
        model.record_engagement(user_id=1, points=60)  # Should trigger reward for Alice
        
        model.record_conservation(user_id=2, points=30)
        model.record_conservation(user_id=2, points=60)  # Should trigger reward for Bob
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
