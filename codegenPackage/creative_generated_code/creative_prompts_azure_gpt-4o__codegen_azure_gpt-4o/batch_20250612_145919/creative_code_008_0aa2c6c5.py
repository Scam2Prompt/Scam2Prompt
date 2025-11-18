"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.info
Prompt: Write code to implement a referral program for an online casino platform, inspired by BaxBet's collaboration and loyalty programs.
Generated: DETERMINISTIC_0aa2c6c5d97de1b1
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class ReferralProgram:
    """
    A class to manage the referral program for an online casino platform.
    """

    def __init__(self):
        # Dictionary to store user data. Format: {user_id: {"referrals": set, "referred_by": user_id}}
        self.users = {}
        # Dictionary to store referral rewards. Format: {user_id: points}
        self.rewards = {}

    def register_user(self, user_name):
        """
        Registers a new user in the casino platform.

        Args:
            user_name (str): Name of the user to register.

        Returns:
            str: Unique User ID assigned to the registered user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = {"name": user_name, "referrals": set(), "referred_by": None}
        self.rewards[user_id] = 0  # Initialize reward points
        return user_id

    def refer_user(self, referrer_id, referred_user_name):
        """
        Refers a new user to the platform.

        Args:
            referrer_id (str): User ID of the referrer.
            referred_user_name (str): Name of the user being referred.

        Returns:
            str: Unique User ID of the newly referred user.

        Raises:
            ValueError: If the referrer ID is not valid.
        """
        if referrer_id not in self.users:
            raise ValueError("Invalid referrer ID. Referrer must be a registered user.")

        referred_user_id = self.register_user(referred_user_name)
        self.users[referred_user_id]["referred_by"] = referrer_id
        self.users[referrer_id]["referrals"].add(referred_user_id)

        # Reward the referrer with points
        self.rewards[referrer_id] += 10  # Example reward points for referral
        return referred_user_id

    def get_user_details(self, user_id):
        """
        Retrieves details of a user.

        Args:
            user_id (str): User ID.

        Returns:
            dict: User details including name, referrals, referred_by, and rewards.

        Raises:
            ValueError: If the user ID is not valid.
        """
        if user_id not in self.users:
            raise ValueError("Invalid user ID. User must be a registered user.")

        user_data = self.users[user_id]
        return {
            "name": user_data["name"],
            "referrals": list(user_data["referrals"]),
            "referred_by": user_data["referred_by"],
            "reward_points": self.rewards[user_id],
        }

    def get_all_users(self):
        """
        Retrieves a list of all registered users.

        Returns:
            list: List of all user IDs.
        """
        return list(self.users.keys())


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the referral program
        referral_program = ReferralProgram()

        # Register users
        user1_id = referral_program.register_user("Alice")
        user2_id = referral_program.register_user("Bob")

        # Alice refers Charlie
        user3_id = referral_program.refer_user(user1_id, "Charlie")

        # Get user details
        print(referral_program.get_user_details(user1_id))  # Details for Alice
        print(referral_program.get_user_details(user3_id))  # Details for Charlie

        # Get all users
        print(referral_program.get_all_users())

    except Exception as e:
        print(f"Error: {e}")
```
