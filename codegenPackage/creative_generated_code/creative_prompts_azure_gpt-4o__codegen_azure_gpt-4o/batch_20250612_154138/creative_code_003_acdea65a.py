"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venez888.vip
Prompt: Provide a Python implementation for a loyalty program system that tracks user activity and awards points, which can be redeemed for "เครดิตฟรี" as described on venez888.vip.
Generated: DETERMINISTIC_acdea65a29c28d9e
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import datetime


class User:
    """
    Represents a user in the loyalty program.
    Each user has a unique ID, name, points balance, and activity log.
    """
    def __init__(self, name: str):
        self.user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.name = name
        self.points = 0  # User's points balance
        self.activity_log = []  # List of activities performed by the user

    def add_points(self, points: int):
        """
        Add points to the user's balance.

        :param points: Number of points to add.
        """
        if points <= 0:
            raise ValueError("Points to add must be greater than zero.")
        self.points += points
        self.log_activity(f"Added {points} points. Current balance: {self.points}.")

    def redeem_points(self, points: int):
        """
        Redeem points for rewards (e.g., 'เครดิตฟรี').

        :param points: Number of points to redeem.
        """
        if points <= 0:
            raise ValueError("Points to redeem must be greater than zero.")
        if points > self.points:
            raise ValueError("Insufficient points to redeem.")
        self.points -= points
        self.log_activity(f"Redeemed {points} points. Current balance: {self.points}.")

    def log_activity(self, activity: str):
        """
        Log user activity with a timestamp.

        :param activity: Activity description.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.activity_log.append(f"[{timestamp}] {activity}")

    def get_activity_log(self):
        """
        Retrieve the user's activity log.

        :return: List of activity log entries.
        """
        return self.activity_log


class LoyaltyProgram:
    """
    Represents the loyalty program system.
    Manages users, tracks points, and facilitates rewards redemption.
    """
    def __init__(self):
        self.users = {}  # Dictionary to store users by their ID

    def register_user(self, name: str) -> User:
        """
        Register a new user in the loyalty program.

        :param name: Name of the user.
        :return: The registered User object.
        """
        if not name:
            raise ValueError("User name cannot be empty.")
        user = User(name)
        self.users[user.user_id] = user
        return user

    def find_user(self, user_id: str) -> User:
        """
        Find a user by their unique ID.

        :param user_id: User ID to search for.
        :return: The User object if found.
        """
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User not found.")
        return user

    def award_points(self, user_id: str, points: int):
        """
        Award points to a user.

        :param user_id: ID of the user to award points to.
        :param points: Number of points to award.
        """
        user = self.find_user(user_id)
        user.add_points(points)

    def redeem_points(self, user_id: str, points: int):
        """
        Redeem points for rewards for a user.

        :param user_id: ID of the user redeeming points.
        :param points: Number of points to redeem.
        """
        user = self.find_user(user_id)
        user.redeem_points(points)

    def get_user_activity_log(self, user_id: str):
        """
        Retrieve the activity log of a specific user.

        :param user_id: ID of the user whose activity log is requested.
        :return: List of activity log entries.
        """
        user = self.find_user(user_id)
        return user.get_activity_log()


# Example Usage:
# loyalty_program = LoyaltyProgram()
# user = loyalty_program.register_user("Alice")
# loyalty_program.award_points(user.user_id, 100)
# loyalty_program.redeem_points(user.user_id, 50)
# print(loyalty_program.get_user_activity_log(user.user_id))
```
