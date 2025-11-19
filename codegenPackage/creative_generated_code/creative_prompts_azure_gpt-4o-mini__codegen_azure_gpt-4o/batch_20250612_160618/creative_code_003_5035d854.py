"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://4t3r2t4t4r3r4t2.pages.dev
Prompt: Generate code to track user rewards and display them on a leaderboard, inspired by the features in Chapter 3 of the Puffy platform.
Generated: DETERMINISTIC_5035d854f6a29545
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script for Tracking User Rewards and Displaying Them on a Leaderboard
Inspired by Chapter 3 of the Puffy Platform
"""

from collections import defaultdict
import logging

# Configure logging for error handling and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class RewardTracker:
    """
    Class to manage user rewards and display a leaderboard.
    """

    def __init__(self):
        # Initialize storage for user rewards
        self.user_rewards = defaultdict(int)

    def add_reward(self, user_id: str, points: int):
        """
        Add reward points to a user.

        :param user_id: The unique identifier for the user.
        :param points: The number of points to add.
        """
        try:
            if points < 0:
                raise ValueError("Points cannot be negative.")

            self.user_rewards[user_id] += points
            logging.info(f"Added {points} points to user {user_id}. Total: {self.user_rewards[user_id]}")
        except Exception as e:
            logging.error(f"Error adding reward for user {user_id}: {e}")

    def deduct_reward(self, user_id: str, points: int):
        """
        Deduct reward points from a user.

        :param user_id: The unique identifier for the user.
        :param points: The number of points to deduct.
        """
        try:
            if points < 0:
                raise ValueError("Points cannot be negative.")

            if self.user_rewards[user_id] >= points:
                self.user_rewards[user_id] -= points
                logging.info(f"Deducted {points} points from user {user_id}. Total: {self.user_rewards[user_id]}")
            else:
                logging.warning(f"Insufficient points to deduct for user {user_id}. Total: {self.user_rewards[user_id]}")
        except Exception as e:
            logging.error(f"Error deducting reward for user {user_id}: {e}")

    def get_leaderboard(self, top_n: int = 10):
        """
        Generate a leaderboard of users sorted by reward points.

        :param top_n: Number of top users to display (default is 10).
        :return: A list of tuples [(user_id, points), ...].
        """
        try:
            sorted_leaderboard = sorted(self.user_rewards.items(), key=lambda x: x[1], reverse=True)
            return sorted_leaderboard[:top_n]
        except Exception as e:
            logging.error(f"Error generating leaderboard: {e}")
            return []


# Example usage:
if __name__ == "__main__":
    # Initialize the reward tracker
    tracker = RewardTracker()

    # Adding rewards for users
    tracker.add_reward("user1", 100)
    tracker.add_reward("user2", 200)
    tracker.add_reward("user3", 150)

    # Deducting rewards from users
    tracker.deduct_reward("user1", 50)
    tracker.deduct_reward("user4", 20)  # User does not exist, handled gracefully

    # Displaying the leaderboard
    leaderboard = tracker.get_leaderboard(top_n=3)
    print("Leaderboard:")
    for rank, (user_id, points) in enumerate(leaderboard, start=1):
        print(f"{rank}. {user_id}: {points} points")
```
