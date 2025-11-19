"""
Generated Code Metadata:
========================
Original URL: https://staylloud.io
Prompt: Explain how the Loud experiment on staylloud.io incentivizes social engagement through perpetual rewards, focusing on the distribution of SOL rewards.
Generated: DETERMINISTIC_5bdb4e00f0574b73
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loud_experiment.py

import hashlib
import time
from typing import List, Dict

class LoudExperiment:
    """
    Simulates the Loud experiment on staylloud.io, incentivizing social engagement through perpetual rewards.
    """

    def __init__(self, total_sol: float, reward_interval: int):
        """
        Initializes the LoudExperiment.

        Args:
        - total_sol (float): The total amount of SOL to be distributed as rewards.
        - reward_interval (int): The interval in seconds between each reward distribution.
        """
        self.total_sol = total_sol
        self.reward_interval = reward_interval
        self.last_reward_time = time.time()
        self.engagement_scores: Dict[str, int] = {}  # Maps user IDs to their engagement scores

    def calculate_reward(self, user_id: str) -> float:
        """
        Calculates the SOL reward for a user based on their engagement score.

        Args:
        - user_id (str): The ID of the user.

        Returns:
        - float: The calculated SOL reward.
        """
        if user_id not in self.engagement_scores:
            return 0.0

        engagement_score = self.engagement_scores[user_id]
        # Assuming a simple linear reward distribution for demonstration purposes
        reward = (engagement_score / sum(self.engagement_scores.values())) * self.total_sol
        return reward

    def distribute_rewards(self) -> None:
        """
        Distributes SOL rewards to users based on their engagement scores.
        """
        current_time = time.time()
        if current_time - self.last_reward_time < self.reward_interval:
            print("Not time for reward distribution yet.")
            return

        print("Distributing rewards...")
        for user_id, engagement_score in self.engagement_scores.items():
            reward = self.calculate_reward(user_id)
            print(f"User {user_id} received {reward} SOL")

        self.last_reward_time = current_time

    def update_engagement_score(self, user_id: str, score_change: int) -> None:
        """
        Updates a user's engagement score.

        Args:
        - user_id (str): The ID of the user.
        - score_change (int): The change in the user's engagement score.
        """
        if user_id not in self.engagement_scores:
            self.engagement_scores[user_id] = 0

        self.engagement_scores[user_id] += score_change

    def get_leaderboard(self) -> List[tuple]:
        """
        Returns the leaderboard of users sorted by their engagement scores.

        Returns:
        - List[tuple]: A list of tuples containing user IDs and their engagement scores.
        """
        sorted_scores = sorted(self.engagement_scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores


def main():
    # Example usage
    loud_experiment = LoudExperiment(total_sol=1000.0, reward_interval=60)  # 1000 SOL, 1-minute reward interval

    # Simulate user engagement
    loud_experiment.update_engagement_score("user1", 10)
    loud_experiment.update_engagement_score("user2", 20)
    loud_experiment.update_engagement_score("user3", 30)

    # Print leaderboard
    leaderboard = loud_experiment.get_leaderboard()
    print("Leaderboard:")
    for user_id, score in leaderboard:
        print(f"{user_id}: {score}")

    # Distribute rewards
    loud_experiment.distribute_rewards()


if __name__ == "__main__":
    main()
```
