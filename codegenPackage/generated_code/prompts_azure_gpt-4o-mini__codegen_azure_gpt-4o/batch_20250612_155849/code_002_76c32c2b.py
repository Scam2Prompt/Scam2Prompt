"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Create a function to implement a loyalty rewards program for users, inspired by the features mentioned on the BaxBet platform.
Generated: DETERMINISTIC_76c32c2b4076400b
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class LoyaltyRewardsProgram:
    """
    A class to manage a loyalty rewards program for users.
    Inspired by features from the BaxBet platform.
    """

    def __init__(self):
        """
        Initialize the loyalty rewards program with an empty user database.
        """
        self.users = {}  # Dictionary to store user data: {user_id: {"points": int, "last_activity": datetime}}

    def add_user(self, user_id):
        """
        Add a new user to the loyalty program.

        :param user_id: Unique identifier for the user.
        """
        if user_id in self.users:
            raise ValueError("User already exists in the program.")
        self.users[user_id] = {"points": 0, "last_activity": datetime.datetime.now()}

    def add_points(self, user_id, points):
        """
        Add loyalty points to a user's account.

        :param user_id: Unique identifier for the user.
        :param points: Number of points to add.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist in the program.")
        if points < 0:
            raise ValueError("Points to add must be a positive value.")
        self.users[user_id]["points"] += points
        self.users[user_id]["last_activity"] = datetime.datetime.now()

    def redeem_points(self, user_id, points):
        """
        Redeem loyalty points from a user's account.

        :param user_id: Unique identifier for the user.
        :param points: Number of points to redeem.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist in the program.")
        if points < 0:
            raise ValueError("Points to redeem must be a positive value.")
        if self.users[user_id]["points"] < points:
            raise ValueError("Insufficient points to redeem.")
        self.users[user_id]["points"] -= points
        self.users[user_id]["last_activity"] = datetime.datetime.now()

    def get_user_points(self, user_id):
        """
        Retrieve the current points balance for a user.

        :param user_id: Unique identifier for the user.
        :return: Current points balance.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist in the program.")
        return self.users[user_id]["points"]

    def get_user_last_activity(self, user_id):
        """
        Retrieve the last activity timestamp for a user.

        :param user_id: Unique identifier for the user.
        :return: Last activity timestamp.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist in the program.")
        return self.users[user_id]["last_activity"]

    def remove_inactive_users(self, inactivity_threshold_days):
        """
        Remove users who have been inactive for a specified number of days.

        :param inactivity_threshold_days: Number of days of inactivity before removal.
        """
        if inactivity_threshold_days < 0:
            raise ValueError("Inactivity threshold must be a positive value.")
        current_time = datetime.datetime.now()
        inactive_users = [
            user_id for user_id, data in self.users.items()
            if (current_time - data["last_activity"]).days > inactivity_threshold_days
        ]
        for user_id in inactive_users:
            del self.users[user_id]

# Example usage:
if __name__ == "__main__":
    program = LoyaltyRewardsProgram()
    program.add_user("user123")
    program.add_points("user123", 100)
    print(f"User Points: {program.get_user_points('user123')}")
    program.redeem_points("user123", 50)
    print(f"User Points after redemption: {program.get_user_points('user123')}")
    print(f"Last Activity: {program.get_user_last_activity('user123')}")
    program.remove_inactive_users(30)  # Remove users inactive for more than 30 days
```
