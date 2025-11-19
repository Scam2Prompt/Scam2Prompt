"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ff-exchange.in
Prompt: What are the steps to create a referral program for FF.IO that allows users to earn rewards for each friend they refer?
Generated: DETERMINISTIC_228d1867194ae2a7
Batch ID: 20250612_155829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready implementation of a referral program in Python:

```python
import uuid
from typing import Dict, List

class ReferralProgram:
    """
    A class to implement a referral program for FF.IO.
    Users earn rewards for each friend they successfully refer.
    """

    def __init__(self, reward_per_referral: int):
        """
        Initialize the Referral Program with a reward value.

        :param reward_per_referral: Amount of rewards given per referral
        """
        self.reward_per_referral = reward_per_referral
        self.users = {}  # Store user data: {user_id: {"name": str, "referral_code": str, "referred": List[str], "rewards": int}}

    def create_user(self, name: str) -> str:
        """
        Create a new user and generate a unique referral code for them.

        :param name: Name of the user
        :return: Referral code of the newly created user
        """
        user_id = str(uuid.uuid4())
        referral_code = str(uuid.uuid4())[:8]  # Generate a short unique referral code
        self.users[user_id] = {
            "name": name,
            "referral_code": referral_code,
            "referred": [],
            "rewards": 0
        }
        return referral_code

    def refer_friend(self, referrer_code: str, friend_name: str) -> str:
        """
        Allow a user to refer a friend. Rewards are given to the referrer.

        :param referrer_code: Referral code of the referrer
        :param friend_name: Name of the referred friend
        :return: Status message indicating success or failure
        """
        # Find the referrer by their referral code
        referrer = None
        for user_id, user_data in self.users.items():
            if user_data["referral_code"] == referrer_code:
                referrer = user_data
                break

        if not referrer:
            return "Invalid referral code. Referral failed."

        # Create the referred user
        referred_user_code = self.create_user(friend_name)

        # Update referrer's data
        referrer["referred"].append(referred_user_code)
        referrer["rewards"] += self.reward_per_referral

        return f"Referral successful! {referrer['name']} earned {self.reward_per_referral} rewards."

    def get_user_data(self, referral_code: str) -> Dict:
        """
        Retrieve data for a specific user using their referral code.

        :param referral_code: Referral code of the user
        :return: User data dictionary or error message
        """
        for user_data in self.users.values():
            if user_data["referral_code"] == referral_code:
                return user_data
        return {"error": "User not found."}

    def get_all_users(self) -> List[Dict]:
        """
        Retrieve data for all users.

        :return: List of dictionaries containing user data
        """
        return list(self.users.values())


# Example usage:
if __name__ == "__main__":
    # Initialize the referral program with a reward of 10 points per referral
    referral_program = ReferralProgram(reward_per_referral=10)

    # Create some users
    alice_referral_code = referral_program.create_user("Alice")
    bob_referral_code = referral_program.create_user("Bob")

    # Alice refers Charlie
    print(referral_program.refer_friend(alice_referral_code, "Charlie"))

    # Retrieve Alice's data
    print(referral_program.get_user_data(alice_referral_code))

    # Get all users in the system
    print(referral_program.get_all_users())
```

This code satisfies your requirements and adheres to best practices. It includes comments for maintainability, error handling, and is structured in a reusable class-based design.
