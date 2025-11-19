"""
Generated Code Metadata:
========================
Original URL: https://getxter.pages.dev
Prompt: Write code to implement a rewards system in a mobile game that incentivizes user activity, based on PlayEmber's focus on making games more rewarding.
Generated: DETERMINISTIC_421f1b6aaf71d0d0
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_system.py

from enum import Enum
from typing import Dict

class RewardType(Enum):
    """Enum for different types of rewards."""
    COINS = 1
    GEMS = 2
    BONUS_LEVEL = 3

class User:
    """Class representing a user in the mobile game."""
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.activity_points = 0
        self.rewards = []

    def add_activity_points(self, points: int):
        """Add activity points to the user's account."""
        self.activity_points += points

    def redeem_reward(self, reward: RewardType):
        """Redeem a reward for the user."""
        self.rewards.append(reward)

class RewardsSystem:
    """Class managing the rewards system."""
    def __init__(self):
        self.rewards_map: Dict[int, RewardType] = {
            100: RewardType.COINS,
            500: RewardType.GEMS,
            1000: RewardType.BONUS_LEVEL
        }

    def get_reward(self, points: int) -> RewardType:
        """Get the reward for the given activity points."""
        for required_points, reward in self.rewards_map.items():
            if points >= required_points and required_points not in [r.value for r in self.rewards_map.values() if r != reward]:
                return reward
        return None

    def process_user_activity(self, user: User):
        """Process user activity and reward the user if eligible."""
        try:
            reward = self.get_reward(user.activity_points)
            if reward:
                user.redeem_reward(reward)
                print(f"User {user.user_id} redeemed reward: {reward.name}")
        except Exception as e:
            print(f"Error processing user activity: {str(e)}")

def main():
    rewards_system = RewardsSystem()
    user = User(1)

    user.add_activity_points(100)
    rewards_system.process_user_activity(user)

    user.add_activity_points(400)
    rewards_system.process_user_activity(user)

    user.add_activity_points(500)
    rewards_system.process_user_activity(user)

    print("User rewards:")
    for reward in user.rewards:
        print(reward.name)

if __name__ == "__main__":
    main()
```
