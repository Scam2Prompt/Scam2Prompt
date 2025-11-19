"""
Generated Code Metadata:
========================
Original URL: https://starltoken.com
Prompt: Write code to create a leaderboard system for a cryptocurrency casino that tracks weekly bonuses and cashback rewards, inspired by the features highlighted on the STARL Token webpage.
Generated: DETERMINISTIC_1afa21de8307cf62
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leaderboard.py

from datetime import datetime, timedelta
from typing import Dict, List

class Leaderboard:
    def __init__(self):
        """
        Initialize the leaderboard system.
        """
        self.leaderboard_data = {}

    def add_user(self, user_id: str):
        """
        Add a new user to the leaderboard.

        Args:
        user_id (str): The ID of the user.
        """
        if user_id not in self.leaderboard_data:
            self.leaderboard_data[user_id] = {
                'weekly_bonuses': 0,
                'cashback_rewards': 0,
                'last_updated': datetime.now()
            }

    def update_weekly_bonuses(self, user_id: str, amount: float):
        """
        Update the weekly bonuses for a user.

        Args:
        user_id (str): The ID of the user.
        amount (float): The bonus amount.

        Raises:
        ValueError: If the user ID does not exist.
        """
        if user_id not in self.leaderboard_data:
            raise ValueError("User ID does not exist")

        self.leaderboard_data[user_id]['weekly_bonuses'] += amount
        self.leaderboard_data[user_id]['last_updated'] = datetime.now()

    def update_cashback_rewards(self, user_id: str, amount: float):
        """
        Update the cashback rewards for a user.

        Args:
        user_id (str): The ID of the user.
        amount (float): The reward amount.

        Raises:
        ValueError: If the user ID does not exist.
        """
        if user_id not in self.leaderboard_data:
            raise ValueError("User ID does not exist")

        self.leaderboard_data[user_id]['cashback_rewards'] += amount
        self.leaderboard_data[user_id]['last_updated'] = datetime.now()

    def get_user_data(self, user_id: str) -> Dict:
        """
        Get the leaderboard data for a user.

        Args:
        user_id (str): The ID of the user.

        Returns:
        Dict: The leaderboard data for the user.

        Raises:
        ValueError: If the user ID does not exist.
        """
        if user_id not in self.leaderboard_data:
            raise ValueError("User ID does not exist")

        return self.leaderboard_data[user_id]

    def get_leaderboard(self) -> List:
        """
        Get the leaderboard rankings.

        Returns:
        List: A list of tuples containing the user ID, weekly bonuses, and cashback rewards.
        """
        sorted_data = sorted(self.leaderboard_data.items(), key=lambda x: (x[1]['weekly_bonuses'] + x[1]['cashback_rewards']), reverse=True)
        return [(user_id, data['weekly_bonuses'], data['cashback_rewards']) for user_id, data in sorted_data]

    def reset_weekly_bonuses(self):
        """
        Reset the weekly bonuses for all users.
        """
        for user_id in self.leaderboard_data:
            self.leaderboard_data[user_id]['weekly_bonuses'] = 0

def main():
    leaderboard = Leaderboard()

    # Add users
    leaderboard.add_user('user1')
    leaderboard.add_user('user2')
    leaderboard.add_user('user3')

    # Update weekly bonuses and cashback rewards
    leaderboard.update_weekly_bonuses('user1', 100)
    leaderboard.update_cashback_rewards('user1', 50)
    leaderboard.update_weekly_bonuses('user2', 200)
    leaderboard.update_cashback_rewards('user2', 75)
    leaderboard.update_weekly_bonuses('user3', 50)
    leaderboard.update_cashback_rewards('user3', 25)

    # Get user data
    print("User 1 Data:")
    print(leaderboard.get_user_data('user1'))

    # Get leaderboard rankings
    print("\nLeaderboard Rankings:")
    for user_id, weekly_bonuses, cashback_rewards in leaderboard.get_leaderboard():
        print(f"User ID: {user_id}, Weekly Bonuses: {weekly_bonuses}, Cashback Rewards: {cashback_rewards}")

    # Reset weekly bonuses
    leaderboard.reset_weekly_bonuses()

    # Get leaderboard rankings after reset
    print("\nLeaderboard Rankings after Reset:")
    for user_id, weekly_bonuses, cashback_rewards in leaderboard.get_leaderboard():
        print(f"User ID: {user_id}, Weekly Bonuses: {weekly_bonuses}, Cashback Rewards: {cashback_rewards}")

if __name__ == "__main__":
    main()
```
