"""
Generated Code Metadata:
========================
Original URL: https://kayen.pages.dev
Prompt: Generate code to facilitate a referral mission system that rewards users for inviting others, inspired by KAYEN's community engagement strategies.
Generated: DETERMINISTIC_ee0bfef9efd6ed15
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime

class ReferralSystem:
    """
    A class to manage a referral mission system that rewards users for inviting others.
    """

    def __init__(self):
        # Dictionary to store user data: {user_id: {"referrals": [], "reward_points": int}}
        self.users = {}

    def create_user(self, username):
        """
        Creates a new user in the system.

        Args:
            username (str): The username of the new user.

        Returns:
            str: The unique user ID of the created user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = {
            "username": username,
            "referrals": [],
            "reward_points": 0,
            "created_at": datetime.now()
        }
        return user_id

    def refer_user(self, referrer_id, referred_username):
        """
        Allows a user to refer another user.

        Args:
            referrer_id (str): The user ID of the referrer.
            referred_username (str): The username of the referred user.

        Returns:
            str: The user ID of the referred user if successful.
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer ID does not exist.")

        referred_user_id = self.create_user(referred_username)
        self.users[referrer_id]["referrals"].append(referred_user_id)
        self._reward_user(referrer_id)
        return referred_user_id

    def _reward_user(self, user_id):
        """
        Rewards a user for successful referrals.

        Args:
            user_id (str): The user ID of the user to reward.
        """
        self.users[user_id]["reward_points"] += 10  # Example: 10 points per referral

    def get_user_info(self, user_id):
        """
        Retrieves information about a user.

        Args:
            user_id (str): The user ID of the user.

        Returns:
            dict: A dictionary containing user information.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        return self.users[user_id]

    def get_leaderboard(self):
        """
        Generates a leaderboard based on reward points.

        Returns:
            list: A sorted list of users by reward points in descending order.
        """
        return sorted(
            self.users.items(),
            key=lambda x: x[1]["reward_points"],
            reverse=True
        )


# Example usage:
if __name__ == "__main__":
    try:
        system = ReferralSystem()

        # Create initial users
        user1_id = system.create_user("Alice")
        user2_id = system.create_user("Bob")

        # Alice refers Charlie
        charlie_id = system.refer_user(user1_id, "Charlie")

        # Bob refers Dave
        dave_id = system.refer_user(user2_id, "Dave")

        # Print user info
        print("Alice Info:", system.get_user_info(user1_id))
        print("Bob Info:", system.get_user_info(user2_id))

        # Print leaderboard
        print("Leaderboard:", system.get_leaderboard())

    except Exception as e:
        print(f"Error: {e}")
```
