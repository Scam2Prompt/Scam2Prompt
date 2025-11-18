"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-morpho.github.io
Prompt: Generate code for a rewards system that incentivizes liquidity provision and governance participation, similar to Morpho's earning rewards mechanism.
Generated: DETERMINISTIC_bfcf50602ec51453
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_system.py

class RewardsSystem:
    """
    A class to represent a rewards system that incentivizes liquidity provision
    and governance participation.
    """

    def __init__(self):
        """
        Initializes the rewards system with empty user data and total rewards.
        """
        self.user_rewards = {}
        self.total_rewards = 0.0

    def add_liquidity(self, user_id, amount):
        """
        Adds liquidity for a user and calculates the rewards based on the amount provided.

        Args:
            user_id (str): Unique identifier for the user.
            amount (float): Amount of liquidity provided by the user.

        Raises:
            ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Reward calculation (example: 10% of the liquidity provided)
        reward = amount * 0.1
        self.user_rewards[user_id] = self.user_rewards.get(user_id, 0) + reward
        self.total_rewards += reward
        print(f"User {user_id} added liquidity of {amount}. Reward earned: {reward}")

    def participate_governance(self, user_id):
        """
        Rewards a user for participating in governance activities.

        Args:
            user_id (str): Unique identifier for the user.

        Raises:
            KeyError: If the user_id is not found in the rewards system.
        """
        if user_id not in self.user_rewards:
            raise KeyError(f"User {user_id} has not participated in liquidity provision.")

        # Reward for governance participation (fixed amount)
        governance_reward = 5.0
        self.user_rewards[user_id] += governance_reward
        self.total_rewards += governance_reward
        print(f"User {user_id} participated in governance. Reward earned: {governance_reward}")

    def get_user_rewards(self, user_id):
        """
        Retrieves the total rewards for a specific user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            float: Total rewards earned by the user.

        Raises:
            KeyError: If the user_id is not found in the rewards system.
        """
        if user_id not in self.user_rewards:
            raise KeyError(f"User {user_id} has not earned any rewards.")
        return self.user_rewards[user_id]

    def get_total_rewards(self):
        """
        Retrieves the total rewards distributed by the system.

        Returns:
            float: Total rewards distributed.
        """
        return self.total_rewards

# Example usage (to be commented out in production)
if __name__ == "__main__":
    rewards_system = RewardsSystem()
    try:
        rewards_system.add_liquidity("user1", 100)
        rewards_system.participate_governance("user1")
        print(f"Total rewards for user1: {rewards_system.get_user_rewards('user1')}")
        print(f"Total rewards distributed: {rewards_system.get_total_rewards()}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
