"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Create a function to implement a loyalty rewards program for users, inspired by the features mentioned on the BaxBet platform.
Generated: DETERMINISTIC_76c32c2b4076400b
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_rewards.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict

class RewardType(Enum):
    """Types of rewards that can be earned by users."""
    FREE_BET = 1
    BONUS_CREDITS = 2
    EXCLUSIVE_OFFER = 3

class User:
    """Represents a user in the loyalty rewards program."""
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.rewards = []
        self.last_active = datetime.now()

    def earn_reward(self, reward_type: RewardType, amount: float):
        """Earns a reward for the user."""
        reward = {
            "type": reward_type,
            "amount": amount,
            "earned_at": datetime.now()
        }
        self.rewards.append(reward)

    def redeem_reward(self, reward_type: RewardType):
        """Redeems a reward for the user."""
        for reward in self.rewards:
            if reward["type"] == reward_type:
                self.rewards.remove(reward)
                return f"Reward of type {reward_type} redeemed successfully."
        return f"No reward of type {reward_type} found."

class LoyaltyProgram:
    """Manages the loyalty rewards program for users."""
    def __init__(self):
        self.users: Dict[int, User] = {}

    def add_user(self, user_id: int):
        """Adds a new user to the loyalty program."""
        if user_id not in self.users:
            self.users[user_id] = User(user_id)
            return f"User {user_id} added to the loyalty program."
        return f"User {user_id} already exists in the loyalty program."

    def earn_reward(self, user_id: int, reward_type: RewardType, amount: float):
        """Earns a reward for a user."""
        try:
            user = self.users[user_id]
            user.earn_reward(reward_type, amount)
            return f"User {user_id} earned a reward of type {reward_type} with amount {amount}."
        except KeyError:
            return f"User {user_id} not found in the loyalty program."

    def redeem_reward(self, user_id: int, reward_type: RewardType):
        """Redeems a reward for a user."""
        try:
            user = self.users[user_id]
            return user.redeem_reward(reward_type)
        except KeyError:
            return f"User {user_id} not found in the loyalty program."

    def get_user_rewards(self, user_id: int):
        """Gets the rewards earned by a user."""
        try:
            user = self.users[user_id]
            return user.rewards
        except KeyError:
            return f"User {user_id} not found in the loyalty program."

def main():
    loyalty_program = LoyaltyProgram()

    # Add users to the loyalty program
    print(loyalty_program.add_user(1))
    print(loyalty_program.add_user(2))

    # Earn rewards for users
    print(loyalty_program.earn_reward(1, RewardType.FREE_BET, 10.0))
    print(loyalty_program.earn_reward(1, RewardType.BONUS_CREDITS, 50.0))
    print(loyalty_program.earn_reward(2, RewardType.EXCLUSIVE_OFFER, 100.0))

    # Redeem rewards for users
    print(loyalty_program.redeem_reward(1, RewardType.FREE_BET))
    print(loyalty_program.redeem_reward(2, RewardType.EXCLUSIVE_OFFER))

    # Get user rewards
    print(loyalty_program.get_user_rewards(1))
    print(loyalty_program.get_user_rewards(2))

if __name__ == "__main__":
    main()
```
