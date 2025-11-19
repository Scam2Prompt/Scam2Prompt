"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cosmicrewards.com
Prompt: How can I implement an affiliate program similar to Cosmic Rewards that allows users to earn gift cards through gameplay?
Generated: DETERMINISTIC_9e63154e679a5c03
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta
from collections import defaultdict

class User:
    """
    Represents a user in the affiliate program.
    """
    def __init__(self, username):
        self.username = username
        self.id = str(uuid.uuid4())
        self.points = 0
        self.rewards = []

    def add_points(self, points):
        """
        Adds points to the user's account.
        :param points: int - The number of points to add.
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.points += points

    def redeem_reward(self, reward):
        """
        Redeems a reward if enough points are available.
        :param reward: Reward - The reward to redeem.
        """
        if reward.points_required > self.points:
            raise ValueError("Not enough points to redeem this reward.")
        self.points -= reward.points_required
        self.rewards.append(reward)
        return reward

class Reward:
    """
    Represents a reward that can be redeemed by users.
    """
    def __init__(self, name, points_required):
        self.name = name
        self.points_required = points_required
        self.created_at = datetime.now()

class AffiliateProgram:
    """
    Manages the affiliate program, user registrations, point allocations, and rewards.
    """
    def __init__(self):
        self.users = {}
        self.rewards = []

    def register_user(self, username):
        """
        Registers a new user in the affiliate program.
        :param username: str - The username of the new user.
        :return: User - The registered user.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[username] = user
        return user

    def create_reward(self, name, points_required):
        """
        Creates a new reward that users can redeem.
        :param name: str - The name of the reward.
        :param points_required: int - The points required to redeem the reward.
        """
        if points_required <= 0:
            raise ValueError("Points required must be positive.")
        reward = Reward(name, points_required)
        self.rewards.append(reward)
        return reward

    def allocate_points(self, username, points):
        """
        Allocates points to a user for gameplay achievements.
        :param username: str - The username of the user.
        :param points: int - The number of points to allocate.
        """
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found.")
        user.add_points(points)

    def redeem_reward(self, username, reward_name):
        """
        Allows a user to redeem a reward.
        :param username: str - The username of the user redeeming the reward.
        :param reward_name: str - The name of the reward to redeem.
        :return: Reward - The redeemed reward.
        """
        user = self.users.get(username)
        if not user:
            raise ValueError("User not found.")
        
        reward = next((r for r in self.rewards if r.name == reward_name), None)
        if not reward:
            raise ValueError("Reward not found.")
        
        return user.redeem_reward(reward)

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the affiliate program
        program = AffiliateProgram()

        # Register users
        user1 = program.register_user("player1")
        user2 = program.register_user("player2")

        # Create rewards
        reward1 = program.create_reward("Amazon Gift Card", 100)
        reward2 = program.create_reward("Starbucks Gift Card", 50)

        # Allocate points to users
        program.allocate_points("player1", 150)
        program.allocate_points("player2", 30)

        # Redeem rewards
        redeemed_reward = program.redeem_reward("player1", "Amazon Gift Card")
        print(f"{user1.username} redeemed {redeemed_reward.name}!")

    except ValueError as e:
        print(f"Error: {e}")
```
