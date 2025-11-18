"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assetdash-staking.vercel.app
Prompt: Suggest tools or frameworks to gamify staking rewards, similar to the "Games" section mentioned on the AssetDash staking site.
Generated: DETERMINISTIC_8c5277bf91e9b8b3
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO)

class StakingRewardGame:
    """
    A class to represent a gamified staking rewards system.
    
    Attributes:
        user_rewards (Dict[str, int]): A dictionary to track rewards for each user.
    """
    
    def __init__(self):
        """Initialize the game with an empty rewards dictionary."""
        self.user_rewards = {}

    def register_user(self, user_id: str) -> None:
        """
        Register a new user into the rewards system.
        
        Args:
            user_id (str): The unique identifier for the user.
        
        Raises:
            ValueError: If the user_id is already registered.
        """
        if user_id in self.user_rewards:
            logging.error(f"User {user_id} is already registered.")
            raise ValueError("User already registered.")
        
        self.user_rewards[user_id] = 0  # Initialize user reward to 0
        logging.info(f"User {user_id} registered successfully.")

    def stake(self, user_id: str, amount: int) -> None:
        """
        Simulate staking an amount for a user.
        
        Args:
            user_id (str): The unique identifier for the user.
            amount (int): The amount to stake.
        
        Raises:
            ValueError: If the user_id is not registered or the amount is non-positive.
        """
        if user_id not in self.user_rewards:
            logging.error(f"User {user_id} is not registered.")
            raise ValueError("User not registered.")
        
        if amount <= 0:
            logging.error("Stake amount must be positive.")
            raise ValueError("Stake amount must be positive.")

        # Randomly reward the user for staking
        reward = self._gamify_reward(amount)
        self.user_rewards[user_id] += reward
        logging.info(f"User {user_id} staked {amount} and earned {reward} rewards.")

    def _gamify_reward(self, amount: int) -> int:
        """
        Determine the reward based on the staked amount using a randomized factor.
        
        Args:
            amount (int): The amount staked by the user.
        
        Returns:
            int: The calculated reward.
        """
        # Simple reward mechanism: reward is between 10% to 50% of the staked amount
        reward_multiplier = random.uniform(0.1, 0.5)
        return int(amount * reward_multiplier)

    def get_rewards(self, user_id: str) -> int:
        """
        Retrieve the total rewards for a user.
        
        Args:
            user_id (str): The unique identifier for the user.
        
        Returns:
            int: Total rewards for the user.
        
        Raises:
            ValueError: If the user_id is not registered.
        """
        if user_id not in self.user_rewards:
            logging.error(f"User {user_id} is not registered.")
            raise ValueError("User not registered.")

        return self.user_rewards[user_id]

def main():
    """Main function to demonstrate the staking reward game."""
    game = StakingRewardGame()

    # Register users
    try:
        game.register_user("user1")
        game.register_user("user2")

        # Stake rewards
        game.stake("user1", 100)
        game.stake("user2", 200)

        # Retrieve and print rewards
        user1_rewards = game.get_rewards("user1")
        user2_rewards = game.get_rewards("user2")
        print(f"User1 Rewards: {user1_rewards}")
        print(f"User2 Rewards: {user2_rewards}")

    except ValueError as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
```
