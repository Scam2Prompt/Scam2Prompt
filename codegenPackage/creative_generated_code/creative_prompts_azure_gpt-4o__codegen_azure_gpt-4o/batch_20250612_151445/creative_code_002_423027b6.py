"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Generate code for a referral program system similar to DominoBet's, where users can earn rewards by inviting friends to join.
Generated: DETERMINISTIC_423027b6006efc3a
Batch ID: 20250612_151445
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
    def __init__(self):
        """
        Initializes a referral program system with:
        - A dictionary to store users: {user_id: {referral_code, referred_by, rewards}}
        - A dictionary to store referrals: {referral_code: user_id}
        """
        self.users = {}
        self.referrals = {}

    def create_user(self, username):
        """
        Creates a new user with a unique referral code.

        Args:
            username (str): The username of the new user.

        Returns:
            dict: User information including referral code.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        referral_code = str(uuid.uuid4())[:8]  # Generate a short unique referral code

        user = {
            "user_id": user_id,
            "username": username,
            "referral_code": referral_code,
            "referred_by": None,
            "rewards": 0,
            "created_at": datetime.now()
        }

        self.users[user_id] = user
        self.referrals[referral_code] = user_id

        return user

    def register_referral(self, referral_code, username):
        """
        Registers a new user using an existing referral code.

        Args:
            referral_code (str): The referral code provided by the referrer.
            username (str): The username of the referred user.

        Returns:
            dict: Information about the referred user and the referrer (if successful).
        """
        if referral_code not in self.referrals:
            raise ValueError("Invalid referral code. Please try again.")

        referrer_id = self.referrals[referral_code]

        referred_user = self.create_user(username)
        referred_user["referred_by"] = referrer_id

        # Reward the referrer
        self.users[referrer_id]["rewards"] += 10  # Example reward amount

        return {
            "referred_user": referred_user,
            "referrer_user": self.users[referrer_id]
        }

    def get_user_info(self, user_id):
        """
        Retrieves information about a specific user.

        Args:
            user_id (str): The unique ID of the user.

        Returns:
            dict: User information.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")

        return self.users[user_id]

    def get_all_users(self):
        """
        Retrieves information about all users in the system.

        Returns:
            list: List of all users.
        """
        return list(self.users.values())

if __name__ == "__main__":
    # Example usage of the ReferralProgram system
    referral_program = ReferralProgram()

    # Create a new user
    user1 = referral_program.create_user("Alice")
    print("User 1 created:", user1)

    # Referral registration
    user2 = referral_program.register_referral(user1["referral_code"], "Bob")
    print("User 2 referred by Alice:", user2)

    # Fetch user information
    user1_info = referral_program.get_user_info(user1["user_id"])
    print("User 1 info:", user1_info)

    # Fetch all users
    all_users = referral_program.get_all_users()
    print("All users in the system:", all_users)
```
