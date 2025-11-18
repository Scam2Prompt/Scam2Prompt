"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pingu-buy.pages.dev
Prompt: Generate code for a staking reward system that mimics Pingu's "Fish Hunt" event, where users complete tasks to earn bonus tokens.
Generated: DETERMINISTIC_7fc6ca6872546c2e
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import Dict, List, Optional

# Constants for staking rewards
BASE_REWARD = 10  # Base token reward for completing tasks
BONUS_REWARD = 5  # Bonus tokens for special achievements
TASKS = ["Catch Fish", "Clean Pond", "Set Trap", "Feed Penguins"]  # Available tasks

# A class to represent a user in the system
class User:
    def __init__(self, user_id: str, username: str):
        self.user_id = user_id
        self.username = username
        self.staked_tokens = 0
        self.completed_tasks = []  # List of tasks user has completed
        self.bonus_tokens = 0

    def add_staked_tokens(self, amount: int):
        if amount < 0:
            raise ValueError("Cannot stake negative tokens.")
        self.staked_tokens += amount

    def add_completed_task(self, task: str):
        if task not in TASKS:
            raise ValueError(f"Invalid task: {task}.")
        self.completed_tasks.append(task)

    def add_bonus_tokens(self, amount: int):
        if amount < 0:
            raise ValueError("Cannot add negative bonus tokens.")
        self.bonus_tokens += amount

    def calculate_total_rewards(self) -> int:
        return (len(self.completed_tasks) * BASE_REWARD) + self.bonus_tokens

# A class to manage the staking reward system
class StakingRewardSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to store user data by user ID

    def register_user(self, user_id: str, username: str):
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        self.users[user_id] = User(user_id, username)

    def stake_tokens(self, user_id: str, amount: int):
        user = self._get_user(user_id)
        user.add_staked_tokens(amount)

    def complete_task(self, user_id: str, task: str):
        user = self._get_user(user_id)
        user.add_completed_task(task)

    def grant_bonus_tokens(self, user_id: str, amount: int):
        user = self._get_user(user_id)
        user.add_bonus_tokens(amount)

    def get_user_rewards(self, user_id: str) -> int:
        user = self._get_user(user_id)
        return user.calculate_total_rewards()

    def _get_user(self, user_id: str) -> User:
        # Helper method to retrieve a user by ID with error handling
        user = self.users.get(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} does not exist.")
        return user

# Example usage of the staking reward system
if __name__ == "__main__":
    # Initialize the staking reward system
    reward_system = StakingRewardSystem()

    try:
        # Register users
        reward_system.register_user("u001", "Pingu")
        reward_system.register_user("u002", "Rico")

        # Stake tokens
        reward_system.stake_tokens("u001", 100)
        reward_system.stake_tokens("u002", 200)

        # Complete tasks
        reward_system.complete_task("u001", "Catch Fish")
        reward_system.complete_task("u001", "Feed Penguins")
        reward_system.complete_task("u002", "Clean Pond")

        # Grant bonus tokens
        reward_system.grant_bonus_tokens("u001", BONUS_REWARD)

        # Calculate and display rewards
        pingu_rewards = reward_system.get_user_rewards("u001")
        rico_rewards = reward_system.get_user_rewards("u002")

        print(f"Pingu's Total Rewards: {pingu_rewards}")
        print(f"Rico's Total Rewards: {rico_rewards}")

    except Exception as e:
        print(f"Error: {e}")
```
