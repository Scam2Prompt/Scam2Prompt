"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staylloud.io
Prompt: How can I implement a reward system for social engagement similar to Loud's model, where users earn rewards based on their contributions?
Generated: DETERMINISTIC_098ce8b7b5764fd5
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import random

class User:
    def __init__(self, user_id, username):
        """Initialize a user with a unique ID and username."""
        self.user_id = user_id
        self.username = username
        self.reward_points = 0
        self.contributions = []

    def add_contribution(self, contribution):
        """Add a contribution to the user's account and update their reward points."""
        self.contributions.append(contribution)
        self.reward_points += contribution.get_reward_points()

class Contribution:
    def __init__(self, content, timestamp=None):
        """Initialize a contribution with content and optional timestamp."""
        self.content = content
        self.timestamp = timestamp if timestamp else datetime.now()

    def get_reward_points(self):
        """Calculate reward points based on the contribution content length."""
        # Reward points based on content length; can be customized further
        return max(1, len(self.content) // 50)  # 1 point for every 50 characters

class RewardSystem:
    def __init__(self):
        """Initialize the reward system for managing users and their rewards."""
        self.users = {}

    def register_user(self, user_id, username):
        """Register a new user with a unique ID and username."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = User(user_id, username)

    def record_contribution(self, user_id, content):
        """Record a contribution for a registered user."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        contribution = Contribution(content)
        self.users[user_id].add_contribution(contribution)

    def get_user_rewards(self, user_id):
        """Retrieve the total reward points for a user."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        return self.users[user_id].reward_points

    def display_user_contributions(self, user_id):
        """Display all contributions made by a user."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        return [contribution.content for contribution in self.users[user_id].contributions]

# Example usage of the RewardSystem
if __name__ == "__main__":
    reward_system = RewardSystem()
    
    # Register users
    try:
        reward_system.register_user(1, 'Alice')
        reward_system.register_user(2, 'Bob')
    except ValueError as e:
        print(f"Error: {e}")

    # Record contributions
    try:
        reward_system.record_contribution(1, "This is Alice's first contribution.")
        reward_system.record_contribution(2, "Bob is sharing his thoughts on the topic.")
        reward_system.record_contribution(1, "Alice loves programming and sharing knowledge!")
    except ValueError as e:
        print(f"Error: {e}")

    # Get user rewards
    try:
        print(f"Alice's rewards: {reward_system.get_user_rewards(1)}")
        print(f"Bob's rewards: {reward_system.get_user_rewards(2)}")
    except ValueError as e:
        print(f"Error: {e}")

    # Display contributions
    try:
        print("Alice's contributions:", reward_system.display_user_contributions(1))
        print("Bob's contributions:", reward_system.display_user_contributions(2))
    except ValueError as e:
        print(f"Error: {e}")
```
