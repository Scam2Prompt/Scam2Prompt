"""
Generated Code Metadata:
========================
Original URL: https://smartnetrewardls.pages.dev
Prompt: Design a system to track and manage token rewards for community members, including user eligibility and reward claiming functionality.
Generated: DETERMINISTIC_73208e7c4400ece4
Batch ID: 20250622_204712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_reward_system.py

from datetime import datetime
from typing import Dict, List

class TokenRewardSystem:
    def __init__(self):
        """
        Initialize the token reward system.

        Attributes:
            users (Dict): A dictionary to store user information.
            rewards (Dict): A dictionary to store reward information.
        """
        self.users = {}
        self.rewards = {}

    def add_user(self, user_id: str, eligibility_criteria: Dict):
        """
        Add a user to the system.

        Args:
            user_id (str): The unique ID of the user.
            eligibility_criteria (Dict): A dictionary containing eligibility criteria.

        Raises:
            ValueError: If the user ID already exists.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists")

        self.users[user_id] = {
            "eligibility_criteria": eligibility_criteria,
            "claimed_rewards": []
        }

    def add_reward(self, reward_id: str, reward_details: Dict):
        """
        Add a reward to the system.

        Args:
            reward_id (str): The unique ID of the reward.
            reward_details (Dict): A dictionary containing reward details.

        Raises:
            ValueError: If the reward ID already exists.
        """
        if reward_id in self.rewards:
            raise ValueError("Reward ID already exists")

        self.rewards[reward_id] = reward_details

    def check_eligibility(self, user_id: str, reward_id: str) -> bool:
        """
        Check if a user is eligible for a reward.

        Args:
            user_id (str): The unique ID of the user.
            reward_id (str): The unique ID of the reward.

        Returns:
            bool: True if the user is eligible, False otherwise.

        Raises:
            ValueError: If the user ID or reward ID does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist")
        if reward_id not in self.rewards:
            raise ValueError("Reward ID does not exist")

        user_eligibility = self.users[user_id]["eligibility_criteria"]
        reward_requirements = self.rewards[reward_id].get("requirements", {})

        for requirement, value in reward_requirements.items():
            if user_eligibility.get(requirement) < value:
                return False

        return True

    def claim_reward(self, user_id: str, reward_id: str):
        """
        Claim a reward for a user.

        Args:
            user_id (str): The unique ID of the user.
            reward_id (str): The unique ID of the reward.

        Raises:
            ValueError: If the user ID or reward ID does not exist.
            Exception: If the user is not eligible for the reward.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist")
        if reward_id not in self.rewards:
            raise ValueError("Reward ID does not exist")

        if not self.check_eligibility(user_id, reward_id):
            raise Exception("User is not eligible for the reward")

        self.users[user_id]["claimed_rewards"].append(reward_id)

    def get_user_rewards(self, user_id: str) -> List:
        """
        Get the rewards claimed by a user.

        Args:
            user_id (str): The unique ID of the user.

        Returns:
            List: A list of reward IDs claimed by the user.

        Raises:
            ValueError: If the user ID does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist")

        return self.users[user_id]["claimed_rewards"]


def main():
    # Example usage
    token_reward_system = TokenRewardSystem()

    # Add users
    token_reward_system.add_user("user1", {"points": 100, "level": 2})
    token_reward_system.add_user("user2", {"points": 50, "level": 1})

    # Add rewards
    token_reward_system.add_reward("reward1", {"name": "Reward 1", "requirements": {"points": 50, "level": 1}})
    token_reward_system.add_reward("reward2", {"name": "Reward 2", "requirements": {"points": 100, "level": 2}})

    # Claim rewards
    token_reward_system.claim_reward("user1", "reward1")
    token_reward_system.claim_reward("user1", "reward2")
    try:
        token_reward_system.claim_reward("user2", "reward2")
    except Exception as e:
        print(e)

    # Get user rewards
    print(token_reward_system.get_user_rewards("user1"))  # Output: ['reward1', 'reward2']
    print(token_reward_system.get_user_rewards("user2"))  # Output: []


if __name__ == "__main__":
    main()
```
