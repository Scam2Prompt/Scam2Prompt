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
# File: staking_rewards.py
# Description: Script to track and distribute staking rewards across multiple users in a DeFi platform.
# Author: [Your Name]
# Created: [Date]

from typing import Dict, List
import json


class StakingRewardsDistributor:
    """
    A class to manage the distribution of staking rewards across multiple users.
    """
    
    def __init__(self):
        """
        Initializes the StakingRewardsDistributor instance.
        """
        self.total_rewards = 0.0  # Total rewards available for distribution
        self.user_balances = {}  # Dictionary to store user balances
        self.user_stakes = {}  # Dictionary to store user stakes

    def add_user(self, user_id: str, stake_amount: float):
        """
        Adds a user to the system with their staking amount.
        
        :param user_id: Unique identifier for the user.
        :param stake_amount: Amount the user has staked.
        """
        if user_id in self.user_stakes:
            raise ValueError(f"User {user_id} already exists.")
        self.user_stakes[user_id] = stake_amount
        self.user_balances[user_id] = 0.0
        print(f"Added user {user_id} with stake: {stake_amount}")

    def update_rewards(self, new_rewards: float):
        """
        Updates the total rewards available for distribution.
        
        :param new_rewards: New rewards to be added to the pool.
        """
        if new_rewards <= 0:
            raise ValueError("Rewards must be greater than zero.")
        self.total_rewards += new_rewards
        print(f"Updated total rewards pool: {self.total_rewards}")

    def distribute_rewards(self):
        """
        Distributes the rewards among users based on their stakes.
        """
        total_stake = sum(self.user_stakes.values())
        if total_stake == 0:
            raise ValueError("Total stake must be greater than zero.")

        print(f"Distributing rewards... Total stake: {total_stake}")
        
        # Calculate rewards for each user
        for user_id, stake in self.user_stakes.items():
            user_reward = (stake / total_stake) * self.total_rewards
            self.user_balances[user_id] += user_reward
            print(f"Distributed {user_reward:.2f} rewards to user {user_id}")

        # Reset total rewards after distribution
        self.total_rewards = 0.0
        print("Rewards distributed successfully.")

    def get_user_balance(self, user_id: str) -> float:
        """
        Returns the balance of a specific user.
        
        :param user_id: Unique identifier for the user.
        :return: User's balance.
        """
        if user_id not in self.user_balances:
            raise ValueError(f"User {user_id} does not exist.")
        return self.user_balances[user_id]

    def export_user_balances(self, file_path: str):
        """
        Exports user balances to a JSON file.
        
        :param file_path: Path to the file where balances will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.user_balances, file, indent=4)
            print(f"User balances exported to {file_path}")
        except IOError as e:
            print(f"Error exporting user balances: {e}")


def main():
    """
    Main function to demonstrate the usage of StakingRewardsDistributor.
    """
    distributor = StakingRewardsDistributor()

    # Add users
    distributor.add_user("user1", 100)
    distributor.add_user("user2", 200)
    distributor.add_user("user3", 300)

    # Update rewards pool
    distributor.update_rewards(600)

    # Distribute rewards
    distributor.distribute_rewards()

    # Print user balances
    for user_id in distributor.user_balances:
        balance = distributor.get_user_balance(user_id)
        print(f"User {user_id} balance: {balance:.2f}")

    # Export balances to a file
    distributor.export_user_balances("user_balances.json")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
