"""
Generated Code Metadata:
========================
Original URL: https://interactivebrokers.fo
Prompt: Develop a strategy for implementing a loyalty program on 1Win, including the types of rewards and benefits for loyal users.
Generated: DETERMINISTIC_50483485f63c68ff
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_program.py

from enum import Enum
from typing import Dict, List

class RewardType(Enum):
    """Types of rewards in the loyalty program."""
    BONUS_CREDITS = 1
    FREE_BETS = 2
    EXCLUSIVE_ACCESS = 3

class LoyaltyProgram:
    """Manages the loyalty program for 1Win users."""

    def __init__(self):
        self.users: Dict[int, User] = {}
        self.rewards: Dict[RewardType, Reward] = {}

    def add_user(self, user_id: int, username: str):
        """Adds a new user to the loyalty program."""
        if user_id in self.users:
            raise ValueError("User already exists in the loyalty program.")
        self.users[user_id] = User(user_id, username)

    def add_reward(self, reward_type: RewardType, name: str, description: str, value: int):
        """Adds a new reward to the loyalty program."""
        if reward_type in self.rewards:
            raise ValueError("Reward already exists in the loyalty program.")
        self.rewards[reward_type] = Reward(reward_type, name, description, value)

    def assign_reward(self, user_id: int, reward_type: RewardType):
        """Assigns a reward to a user."""
        if user_id not in self.users:
            raise ValueError("User does not exist in the loyalty program.")
        if reward_type not in self.rewards:
            raise ValueError("Reward does not exist in the loyalty program.")
        self.users[user_id].rewards.append(self.rewards[reward_type])

class User:
    """Represents a user in the loyalty program."""

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.rewards: List[Reward] = []
        self.balance: int = 0

    def update_balance(self, amount: int):
        """Updates the user's balance."""
        self.balance += amount

class Reward:
    """Represents a reward in the loyalty program."""

    def __init__(self, reward_type: RewardType, name: str, description: str, value: int):
        self.reward_type = reward_type
        self.name = name
        self.description = description
        self.value = value

def main():
    loyalty_program = LoyaltyProgram()

    # Add rewards
    loyalty_program.add_reward(RewardType.BONUS_CREDITS, "Bonus Credits", "Get 100 bonus credits", 100)
    loyalty_program.add_reward(RewardType.FREE_BETS, "Free Bets", "Get 5 free bets", 5)
    loyalty_program.add_reward(RewardType.EXCLUSIVE_ACCESS, "Exclusive Access", "Get exclusive access to premium content", 1)

    # Add users
    loyalty_program.add_user(1, "user1")
    loyalty_program.add_user(2, "user2")

    # Assign rewards
    loyalty_program.assign_reward(1, RewardType.BONUS_CREDITS)
    loyalty_program.assign_reward(2, RewardType.FREE_BETS)

    # Update user balance
    loyalty_program.users[1].update_balance(1000)

    # Print user information
    for user_id, user in loyalty_program.users.items():
        print(f"User ID: {user.user_id}")
        print(f"Username: {user.username}")
        print(f"Balance: {user.balance}")
        print("Rewards:")
        for reward in user.rewards:
            print(f"- {reward.name}: {reward.description} ({reward.value})")
        print()

if __name__ == "__main__":
    main()
```
