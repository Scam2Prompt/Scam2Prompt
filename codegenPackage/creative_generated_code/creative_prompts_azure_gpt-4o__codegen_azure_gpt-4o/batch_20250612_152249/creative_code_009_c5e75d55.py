"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://828768840-96b.pages.dev
Prompt: Provide code to implement a leaderboard system that tracks user performance and rewards points based on trading activity, as described on Blum.
Generated: DETERMINISTIC_c5e75d55000d7dc8
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Leaderboard:
    """
    A class to represent a leaderboard system that tracks user performance and rewards points based on trading activity.
    """

    def __init__(self):
        """
        Initialize the leaderboard with an empty user list.
        """
        self.users = {}

    def add_user(self, user_id: str, username: str):
        """
        Add a new user to the leaderboard.
        
        :param user_id: Unique identifier for the user.
        :param username: Display name of the user.
        """
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        self.users[user_id] = {
            "username": username,
            "points": 0,
            "last_updated": datetime.datetime.now()
        }

    def record_trade(self, user_id: str, trade_value: float):
        """
        Record a trading activity and reward points based on the trade value.
        
        :param user_id: Unique identifier for the user.
        :param trade_value: The monetary value of the trade.
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        if trade_value <= 0:
            raise ValueError("Trade value must be greater than 0.")

        # Reward points (e.g., 1 point per $100 traded)
        points_rewarded = int(trade_value / 100)
        self.users[user_id]['points'] += points_rewarded
        self.users[user_id]['last_updated'] = datetime.datetime.now()

    def get_leaderboard(self):
        """
        Get the current leaderboard sorted by points (descending).
        
        :return: A sorted list of users based on points.
        """
        sorted_users = sorted(
            self.users.items(),
            key=lambda x: x[1]['points'],
            reverse=True
        )
        return [
            {
                "user_id": user_id,
                "username": user_data['username'],
                "points": user_data['points'],
                "last_updated": user_data['last_updated']
            }
            for user_id, user_data in sorted_users
        ]

    def display_leaderboard(self):
        """
        Print the leaderboard in a readable format.
        """
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        print("------------------------------")
        for rank, user in enumerate(leaderboard, start=1):
            print(
                f"Rank {rank}: {user['username']} (User ID: {user['user_id']}) - Points: {user['points']} - Last Updated: {user['last_updated']}"
            )
        print("------------------------------")


# Example Usage
if __name__ == "__main__":
    try:
        # Create leaderboard instance
        lb = Leaderboard()

        # Add users to leaderboard
        lb.add_user("u1", "Alice")
        lb.add_user("u2", "Bob")
        lb.add_user("u3", "Charlie")

        # Record trades
        lb.record_trade("u1", 1500)  # Alice earns 15 points
        lb.record_trade("u2", 700)   # Bob earns 7 points
        lb.record_trade("u3", 2000)  # Charlie earns 20 points

        # Display leaderboard
        lb.display_leaderboard()

    except Exception as e:
        print(f"Error: {e}")
```
