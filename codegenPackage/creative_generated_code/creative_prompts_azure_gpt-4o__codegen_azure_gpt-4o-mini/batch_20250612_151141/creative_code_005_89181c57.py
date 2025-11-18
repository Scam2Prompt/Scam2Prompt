"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananarewards.pages.dev
Prompt: Create a reward history tracker that displays claimed rewards and calculates total earned ETH and SOL for users on the Bananagun Rewards platform.
Generated: DETERMINISTIC_89181c5785406853
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Union

class Reward:
    """Class representing a reward entry."""
    def __init__(self, reward_id: str, amount: float, currency: str, claimed: bool):
        """
        Initializes a Reward object.

        :param reward_id: Unique identifier for the reward
        :param amount: Amount of the reward
        :param currency: Currency of the reward (ETH or SOL)
        :param claimed: Status of the reward (True if claimed, False otherwise)
        """
        self.reward_id = reward_id
        self.amount = amount
        self.currency = currency
        self.claimed = claimed

class RewardHistoryTracker:
    """Class to track reward history of users."""
    
    def __init__(self):
        """Initializes the RewardHistoryTracker with an empty reward history."""
        self.rewards: List[Reward] = []

    def add_reward(self, reward: Reward) -> None:
        """
        Adds a reward to the tracker.

        :param reward: A Reward object to add to the history
        """
        self.rewards.append(reward)

    def get_claimed_rewards(self) -> List[Reward]:
        """
        Returns a list of claimed rewards.

        :return: List of Reward objects that have been claimed
        """
        return [reward for reward in self.rewards if reward.claimed]

    def calculate_total_earned(self, currency: str) -> float:
        """
        Calculates total earned amount for a given currency.

        :param currency: Currency to calculate total earned (ETH or SOL)
        :return: Total earned amount in the specified currency
        """
        total = sum(reward.amount for reward in self.rewards if reward.currency == currency and reward.claimed)
        return total

    def export_history(self, file_path: str) -> None:
        """
        Exports the reward history to a JSON file.

        :param file_path: Path to the file where the history will be exported
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([reward.__dict__ for reward in self.rewards], file, indent=4)
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")

    def import_history(self, file_path: str) -> None:
        """
        Imports reward history from a JSON file.

        :param file_path: Path to the file from which the history will be imported
        """
        try:
            with open(file_path, 'r') as file:
                rewards_data = json.load(file)
                for data in rewards_data:
                    reward = Reward(**data)
                    self.add_reward(reward)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error reading from file {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    tracker = RewardHistoryTracker()
    
    # Adding rewards
    tracker.add_reward(Reward("1", 0.5, "ETH", True))
    tracker.add_reward(Reward("2", 1.0, "SOL", True))
    tracker.add_reward(Reward("3", 0.3, "ETH", False))
    
    # Display claimed rewards
    claimed_rewards = tracker.get_claimed_rewards()
    print("Claimed Rewards:")
    for reward in claimed_rewards:
        print(f"ID: {reward.reward_id}, Amount: {reward.amount} {reward.currency}")

    # Calculate total earned ETH and SOL
    total_earned_eth = tracker.calculate_total_earned("ETH")
    total_earned_sol = tracker.calculate_total_earned("SOL")
    
    print(f"Total Earned ETH: {total_earned_eth}")
    print(f"Total Earned SOL: {total_earned_sol}")

    # Exporting history to a file
    tracker.export_history("reward_history.json")
    
    # Importing history from a file
    new_tracker = RewardHistoryTracker()
    new_tracker.import_history("reward_history.json")
```
