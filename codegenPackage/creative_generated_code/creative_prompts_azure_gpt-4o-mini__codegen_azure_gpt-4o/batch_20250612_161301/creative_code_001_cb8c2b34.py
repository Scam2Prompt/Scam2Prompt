"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betpandaofficial.com
Prompt: How can I implement a system to track and manage user bonuses and VIP rewards in a gaming application like Betpanda?
Generated: DETERMINISTIC_cb8c2b3499103d19
Batch ID: 20250612_161301
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


class User:
    """
    Represents a user in the gaming application with bonuses and VIP rewards.
    """
    def __init__(self, user_id: str, username: str):
        self.user_id = user_id
        self.username = username
        self.bonuses = []
        self.vip_rewards = []

    def add_bonus(self, bonus):
        """
        Adds a bonus to the user's account.
        """
        self.bonuses.append(bonus)

    def add_vip_reward(self, reward):
        """
        Adds a VIP reward to the user's account.
        """
        self.vip_rewards.append(reward)


class Bonus:
    """
    Represents a bonus in the system.
    """
    def __init__(self, description: str, amount: float, expiration_date: datetime):
        self.bonus_id = str(uuid.uuid4())  # Generate a unique ID for the bonus
        self.description = description
        self.amount = amount
        self.expiration_date = expiration_date

    def is_expired(self):
        """
        Checks if the bonus has expired.
        """
        return datetime.now() > self.expiration_date


class VIPReward:
    """
    Represents a VIP reward in the system.
    """
    def __init__(self, description: str, reward_points: int):
        self.reward_id = str(uuid.uuid4())  # Generate a unique ID for the reward
        self.description = description
        self.reward_points = reward_points
        self.created_at = datetime.now()


class RewardManager:
    """
    Manages bonuses and VIP rewards for users in the gaming application.
    """
    def __init__(self):
        self.users = {}

    def add_user(self, username: str):
        """
        Adds a new user to the system.
        """
        user_id = str(uuid.uuid4())  # Generate a unique ID for the user
        user = User(user_id, username)
        self.users[user_id] = user
        return user_id

    def assign_bonus(self, user_id: str, description: str, amount: float, duration_days: int):
        """
        Assigns a bonus to a user.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        expiration_date = datetime.now() + timedelta(days=duration_days)
        bonus = Bonus(description, amount, expiration_date)
        self.users[user_id].add_bonus(bonus)

    def assign_vip_reward(self, user_id: str, description: str, reward_points: int):
        """
        Assigns a VIP reward to a user.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        reward = VIPReward(description, reward_points)
        self.users[user_id].add_vip_reward(reward)

    def get_active_bonuses(self, user_id: str):
        """
        Returns all active bonuses for a user.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        user = self.users[user_id]
        return [bonus for bonus in user.bonuses if not bonus.is_expired()]

    def get_vip_rewards(self, user_id: str):
        """
        Returns all VIP rewards for a user.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        user = self.users[user_id]
        return user.vip_rewards


if __name__ == "__main__":
    # Example usage of the RewardManager system:
    reward_manager = RewardManager()

    # Add a user
    user_id = reward_manager.add_user("player1")

    # Assign bonuses and VIP rewards
    reward_manager.assign_bonus(user_id, "Welcome Bonus", 100.0, 7)
    reward_manager.assign_vip_reward(user_id, "VIP Level 1", 200)

    # Get active bonuses and VIP rewards for the user
    active_bonuses = reward_manager.get_active_bonuses(user_id)
    vip_rewards = reward_manager.get_vip_rewards(user_id)

    # Print results
    print("Active Bonuses:")
    for bonus in active_bonuses:
        print(f"ID: {bonus.bonus_id}, Description: {bonus.description}, Amount: {bonus.amount}, Expiration: {bonus.expiration_date}")

    print("\nVIP Rewards:")
    for reward in vip_rewards:
        print(f"ID: {reward.reward_id}, Description: {reward.description}, Points: {reward.reward_points}")
```
