"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenderize.xyz
Prompt: Generate code for tracking staking rewards distribution across multiple users in a DeFi platform, ensuring transparency as described in Tenderize's operations.
Generated: DETERMINISTIC_45ae9bdae9517f49
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List

class StakingRewardTracker:
    def __init__(self):
        """Initialize the reward tracker with an empty rewards dictionary."""
        self.rewards: Dict[str, float] = {}
    
    def stake(self, user_id: str, amount: float) -> None:
        """
        Record a staking action for a user.
        
        Args:
            user_id (str): The unique identifier for the user.
            amount (float): The amount being staked by the user.
        
        Raises:
            ValueError: If the staking amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Staking amount must be positive.")
        
        if user_id not in self.rewards:
            self.rewards[user_id] = 0.0
        
        # Update the user's staked amount
        self.rewards[user_id] += amount
        print(f"User {user_id} has staked {amount}. Total staked: {self.rewards[user_id]}")

    def distribute_rewards(self, total_rewards: float) -> None:
        """
        Distribute staking rewards proportionally to staked amounts.
        
        Args:
            total_rewards (float): The total rewards to distribute.
        
        Raises:
            ValueError: If total rewards are non-positive or there are no stakers.
        """
        if total_rewards <= 0:
            raise ValueError("Total rewards must be positive.")
        if not self.rewards:
            raise ValueError("No users to distribute rewards to.")

        total_staked = sum(self.rewards.values())
        
        for user_id, amount in self.rewards.items():
            # Calculate individual rewards
            user_reward = (amount / total_staked) * total_rewards
            self.rewards[user_id] += user_reward
            print(f"Distributed {user_reward} rewards to user {user_id}. Total rewards: {self.rewards[user_id]}")

    def get_reward_summary(self) -> Dict[str, float]:
        """
        Get the summary of rewards for all users.
        
        Returns:
            Dict[str, float]: A dictionary containing user IDs and their total rewards.
        """
        return self.rewards.copy()

    def save_rewards_to_file(self, file_path: str) -> None:
        """
        Save the current state of rewards to a JSON file.
        
        Args:
            file_path (str): The path to the file where rewards will be saved.
        
        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.rewards, file)
            print(f"Rewards saved to {file_path}.")
        except IOError as e:
            print(f"Error saving rewards to file: {e}")

    def load_rewards_from_file(self, file_path: str) -> None:
        """
        Load rewards from a JSON file into the tracker.
        
        Args:
            file_path (str): The path to the file from which rewards will be loaded.
        
        Raises:
            IOError: If there is an error reading the file.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.rewards = json.load(file)
            print(f"Rewards loaded from {file_path}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading rewards from file: {e}")

# Example usage
if __name__ == "__main__":
    tracker = StakingRewardTracker()
    
    # Users staking amounts
    tracker.stake('user1', 100.0)
    tracker.stake('user2', 200.0)
    
    # Distributing rewards
    tracker.distribute_rewards(30.0)
    
    # Get summary of rewards
    print(tracker.get_reward_summary())
    
    # Save to file
    tracker.save_rewards_to_file('rewards.json')
    
    # Load from file
    tracker.load_rewards_from_file('rewards.json')
```
