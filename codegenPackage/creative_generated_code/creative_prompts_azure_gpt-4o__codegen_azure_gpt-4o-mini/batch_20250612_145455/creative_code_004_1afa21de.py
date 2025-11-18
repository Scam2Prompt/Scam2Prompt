"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starltoken.com
Prompt: Write code to create a leaderboard system for a cryptocurrency casino that tracks weekly bonuses and cashback rewards, inspired by the features highlighted on the STARL Token webpage.
Generated: DETERMINISTIC_1afa21de8307cf62
Batch ID: 20250612_145455
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

class Leaderboard:
    def __init__(self):
        """
        Initializes the leaderboard with a dictionary to track users' bonuses
        and cashback rewards, as well as the start date for the weekly cycle.
        """
        self.user_data = defaultdict(lambda: {'bonus': 0.0, 'cashback': 0.0})
        self.start_date = datetime.datetime.now()
        self.current_week = self.get_current_week()

    def get_current_week(self):
        """
        Returns the current week number of the year.
        """
        return datetime.datetime.now().isocalendar()[1]

    def update_leaderboard(self, user_id, bonus=0.0, cashback=0.0):
        """
        Updates the leaderboard for a given user with the specified bonus and cashback.

        Args:
            user_id (str): The unique identifier for the user.
            bonus (float): The weekly bonus to be added to the user's total.
            cashback (float): The weekly cashback to be added to the user's total.
        """
        if bonus < 0 or cashback < 0:
            raise ValueError("Bonus and cashback values must be non-negative.")

        current_week = self.get_current_week()

        # Reset user data if we are in a new week
        if current_week != self.current_week:
            self.user_data.clear()
            self.start_date = datetime.datetime.now()
            self.current_week = current_week

        self.user_data[user_id]['bonus'] += bonus
        self.user_data[user_id]['cashback'] += cashback

    def get_leaderboard(self):
        """
        Returns a sorted list of users based on their total bonuses and cashback rewards.

        Returns:
            list: A list of tuples containing user_id, total_bonus, and total_cashback.
        """
        leaderboard = [
            (user_id, data['bonus'], data['cashback'])
            for user_id, data in self.user_data.items()
        ]
        # Sort primarily by bonus, and secondarily by cashback
        return sorted(leaderboard, key=lambda x: (-x[1], -x[2]))

    def display_leaderboard(self):
        """
        Displays the leaderboard in a formatted manner.
        """
        print("Leaderboard:")
        for rank, (user_id, bonus, cashback) in enumerate(self.get_leaderboard(), start=1):
            print(f"{rank}. User: {user_id}, Bonus: {bonus:.2f}, Cashback: {cashback:.2f}")

# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    try:
        leaderboard.update_leaderboard("user_1", bonus=100.0, cashback=10.0)
        leaderboard.update_leaderboard("user_2", bonus=150.0, cashback=15.0)
        leaderboard.update_leaderboard("user_1", bonus=50.0, cashback=5.0)

        leaderboard.display_leaderboard()
        
    except ValueError as e:
        print(f"Error: {e}")
```
