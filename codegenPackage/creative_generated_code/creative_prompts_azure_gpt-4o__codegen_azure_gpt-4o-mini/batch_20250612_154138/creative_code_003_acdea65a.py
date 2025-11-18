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
import json
from datetime import datetime, timedelta

class User:
    """
    Represents a user in the loyalty program.
    """

    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.points = 0
        self.activities = []  # List to track user activities

    def add_activity(self, activity: str, points: int):
        """
        Adds an activity to the user's record and awards points.
        """
        self.activities.append({
            "activity": activity,
            "points": points,
            "timestamp": datetime.now()
        })
        self.points += points

    def redeem_points(self, points: int) -> bool:
        """
        Redeems points if the user has enough.
        Returns True if points are successfully redeemed, else False.
        """
        if points <= self.points:
            self.points -= points
            return True
        else:
            return False

class LoyaltyProgram:
    """
    Represents the loyalty program that manages users and their activities.
    """

    def __init__(self):
        self.users = {}  # Dictionary to hold user records

    def register_user(self, user_id: str, name: str) -> User:
        """
        Registers a new user in the loyalty program.
        Returns the User object created.
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        user = User(user_id, name)
        self.users[user_id] = user
        return user

    def record_activity(self, user_id: str, activity: str, points: int):
        """
        Records an activity for the specified user and awards points.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} not found.")
        user = self.users[user_id]
        user.add_activity(activity, points)

    def get_user_info(self, user_id: str) -> dict:
        """
        Returns user information including activities and points.
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} not found.")
        user = self.users[user_id]
        return {
            "user_id": user.user_id,
            "name": user.name,
            "points": user.points,
            "activities": user.activities
        }

    def save_to_file(self, filename: str):
        """
        Saves the current state of the loyalty program to a JSON file.
        """
        data = {user_id: user.__dict__ for user_id, user in self.users.items()}
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, default=str)  # Use default=str to serialize datetime

    def load_from_file(self, filename: str):
        """
        Loads user data from a JSON file into the loyalty program.
        """
        try:
            with open(filename, 'r') as json_file:
                data = json.load(json_file)
                for user_id, user_data in data.items():
                    user = User(user_id, user_data['name'])
                    user.points = user_data['points']
                    user.activities = user_data['activities']
                    self.users[user_id] = user
        except FileNotFoundError:
            print(f"File {filename} not found. Loading default state.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the file. Please check the file format.")

# Example usage:
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()

    # Register a user
    user = loyalty_program.register_user("001", "John Doe")

    # Record activities
    loyalty_program.record_activity("001", "Purchase", 100)
    loyalty_program.record_activity("001", "Referral", 50)

    # Redeem points
    if loyalty_program.users["001"].redeem_points(80):
        print("Points redeemed successfully.")
    else:
        print("Not enough points to redeem.")

    # Get user info
    user_info = loyalty_program.get_user_info("001")
    print(user_info)

    # Save and load state
    loyalty_program.save_to_file("loyalty_program.json")
    loyalty_program.load_from_file("loyalty_program.json")
```
