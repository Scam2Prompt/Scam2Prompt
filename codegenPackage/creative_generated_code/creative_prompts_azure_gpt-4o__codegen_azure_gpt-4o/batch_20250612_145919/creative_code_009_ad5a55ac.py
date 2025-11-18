"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.bet
Prompt: Write code to implement a referral program for an online casino platform, including tracking referrals and calculating rewards, inspired by BaxBet's collaboration programs.
Generated: DETERMINISTIC_ad5a55ac3bd08b21
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
from typing import Dict, List

class ReferralProgram:
    """
    Referral Program Class to track referrals and calculate rewards for an online casino platform.
    """

    def __init__(self, reward_per_referral: float, max_referrals_per_user: int):
        """
        Initialize the Referral Program.

        :param reward_per_referral: Reward amount for each valid referral.
        :param max_referrals_per_user: Maximum number of referrals allowed per user.
        """
        self.users = {}  # Dictionary to store user data (user_id -> user details)
        self.referrals = {}  # Dictionary to track referrals (referrer_id -> List of referred user_id)
        self.reward_per_referral = reward_per_referral
        self.max_referrals_per_user = max_referrals_per_user

    def register_user(self, username: str) -> str:
        """
        Register a new user on the platform.

        :param username: Username of the new user.
        :return: Unique user ID of the registered user.
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = {
            "username": username,
            "balance": 0.0,
            "referred_by": None
        }
        return user_id

    def refer_user(self, referrer_id: str, referred_username: str) -> Dict[str, str]:
        """
        Refer a new user to the platform.

        :param referrer_id: User ID of the referrer.
        :param referred_username: Username of the user being referred.
        :return: Dictionary indicating success or error message.
        """
        if referrer_id not in self.users:
            return {"error": "Referrer does not exist."}

        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []

        if len(self.referrals[referrer_id]) >= self.max_referrals_per_user:
            return {"error": "Maximum referral limit reached."}

        # Register the referred user and assign the referrer
        referred_user_id = self.register_user(referred_username)
        self.users[referred_user_id]["referred_by"] = referrer_id
        self.referrals[referrer_id].append(referred_user_id)

        # Add reward to referrer
        self.users[referrer_id]["balance"] += self.reward_per_referral

        return {"success": f"User '{referred_username}' referred successfully.", "referred_user_id": referred_user_id}

    def get_user_details(self, user_id: str) -> Dict[str, any]:
        """
        Get details of a specific user.

        :param user_id: User ID to fetch details for.
        :return: Dictionary containing user details or an error message.
        """
        if user_id not in self.users:
            return {"error": "User does not exist."}
        return {"user_details": self.users[user_id]}

    def get_referrer_details(self, referrer_id: str) -> Dict[str, any]:
        """
        Get details of a referrer and their referrals.

        :param referrer_id: User ID of the referrer.
        :return: Dictionary containing referrer details or an error message.
        """
        if referrer_id not in self.users:
            return {"error": "User does not exist."}

        referrals = self.referrals.get(referrer_id, [])
        return {
            "referrer_details": self.users[referrer_id],
            "referrals": [self.users[user_id]["username"] for user_id in referrals]
        }


# Example Usage
if __name__ == "__main__":
    # Initialize the referral program
    referral_program = ReferralProgram(reward_per_referral=10.0, max_referrals_per_user=5)

    # Register users
    john_id = referral_program.register_user("JohnDoe")
    jane_id = referral_program.register_user("JaneSmith")

    # Refer users
    result1 = referral_program.refer_user(john_id, "AliceJones")
    print(result1)  # Success

    result2 = referral_program.refer_user(john_id, "BobBrown")
    print(result2)  # Success

    result3 = referral_program.refer_user(jane_id, "CharlieWhite")
    print(result3)  # Success

    # Fetch user details
    print(referral_program.get_user_details(john_id))
    print(referral_program.get_referrer_details(john_id))
```
