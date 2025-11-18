"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappbay-bnbchain-org.pages.dev
Prompt: Generate code to track user participation in BNB Chain's anniversary campaigns and calculate rewards earned across multiple weeks.
Generated: DETERMINISTIC_dce7b4d6b0bae518
Batch ID: 20250612_145823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from collections import defaultdict

class UserParticipationTracker:
    def __init__(self):
        """Initialize the tracker with a dictionary to store user participation."""
        self.participation_data = defaultdict(lambda: {'weeks': {}, 'total_rewards': 0})

    def record_participation(self, user_id: str, week_number: int, rewards: float):
        """
        Record a user's participation and the rewards they earned for a specific week.

        Args:
            user_id (str): The ID of the user participating.
            week_number (int): The week number of the participation.
            rewards (float): The amount of rewards earned.

        Raises:
            ValueError: If the week number is invalid or rewards are negative.
        """
        if week_number < 1:
            raise ValueError("Week number must be greater than 0.")
        if rewards < 0:
            raise ValueError("Rewards must be a non-negative value.")

        # Record the participation
        self.participation_data[user_id]['weeks'][week_number] = rewards
        self.participation_data[user_id]['total_rewards'] += rewards

    def get_user_rewards(self, user_id: str):
        """
        Retrieve the total rewards earned by a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: A dictionary containing user's week-wise rewards and total rewards.
        """
        return self.participation_data.get(user_id, {'weeks': {}, 'total_rewards': 0})

    def get_all_users_rewards(self):
        """
        Retrieve the rewards earned by all users.

        Returns:
            dict: A dictionary with user IDs as keys and their rewards data as values.
        """
        return dict(self.participation_data)

if __name__ == "__main__":
    # Example usage of UserParticipationTracker
    tracker = UserParticipationTracker()

    try:
        # Recording user participations
        tracker.record_participation("user_1", 1, 10.5)
        tracker.record_participation("user_1", 2, 15.0)
        tracker.record_participation("user_2", 1, 12.0)
        tracker.record_participation("user_2", 3, 8.5)

        # Retrieve and print rewards
        user_1_rewards = tracker.get_user_rewards("user_1")
        user_2_rewards = tracker.get_user_rewards("user_2")
        print(f"User 1 Rewards: {user_1_rewards}")
        print(f"User 2 Rewards: {user_2_rewards}")

        # Print all users' rewards
        all_rewards = tracker.get_all_users_rewards()
        print(f"All Users Rewards: {all_rewards}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
