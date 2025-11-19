"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anylimitedcentralize.pages.dev
Prompt: Write code to create a referral system that rewards users with $RIFT for inviting others on a decentralized platform.
Generated: DETERMINISTIC_04d657810ce2df67
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral System for Decentralized Platform
Rewards users with tokens ($RIFT) for successfully inviting others.
"""

from typing import Dict

class ReferralSystem:
    def __init__(self, reward_amount: float):
        """
        Initializes the referral system.
        
        :param reward_amount: The amount of $RIFT tokens rewarded per successful referral.
        """
        self.reward_amount = reward_amount
        self.user_referrals: Dict[str, Dict[str, int]] = {}  # {user_id: {"balance": float, "referrals": int}}

    def register_user(self, user_id: str) -> None:
        """
        Registers a new user in the system.
        
        :param user_id: Unique identifier for the user.
        :raises ValueError: If the user_id already exists in the system.
        """
        if user_id in self.user_referrals:
            raise ValueError(f"User {user_id} is already registered.")
        self.user_referrals[user_id] = {"balance": 0.0, "referrals": 0}

    def invite_user(self, referrer_id: str, new_user_id: str) -> None:
        """
        Handles inviting a new user to the system.
        
        :param referrer_id: ID of the user making the referral.
        :param new_user_id: ID of the new user being invited.
        :raises ValueError: If the referrer or new user ID is invalid.
        """
        if referrer_id not in self.user_referrals:
            raise ValueError(f"Referrer {referrer_id} does not exist.")
        if new_user_id in self.user_referrals:
            raise ValueError(f"User {new_user_id} is already registered.")
        
        # Register the new user
        self.register_user(new_user_id)
        
        # Reward the referrer
        self.user_referrals[referrer_id]["balance"] += self.reward_amount
        self.user_referrals[referrer_id]["referrals"] += 1

    def get_user_balance(self, user_id: str) -> float:
        """
        Retrieves the token balance for a specific user.
        
        :param user_id: The ID of the user.
        :raises ValueError: If the user ID is invalid.
        :return: The $RIFT token balance of the user.
        """
        if user_id not in self.user_referrals:
            raise ValueError(f"User {user_id} does not exist.")
        return self.user_referrals[user_id]["balance"]

    def get_user_referrals(self, user_id: str) -> int:
        """
        Retrieves the number of successful referrals for a specific user.
        
        :param user_id: The ID of the user.
        :raises ValueError: If the user ID is invalid.
        :return: The number of successful referrals made by the user.
        """
        if user_id not in self.user_referrals:
            raise ValueError(f"User {user_id} does not exist.")
        return self.user_referrals[user_id]["referrals"]

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the referral system with $RIFT reward amount
        referral_system = ReferralSystem(reward_amount=10.0)

        # Register users and process referrals
        referral_system.register_user("alice")
        referral_system.register_user("bob")

        referral_system.invite_user("alice", "charlie")  # Alice invites Charlie
        referral_system.invite_user("bob", "dave")      # Bob invites Dave

        # Retrieve data for Alice
        print(f"Alice's Balance: {referral_system.get_user_balance('alice')} $RIFT")
        print(f"Alice's Referrals: {referral_system.get_user_referrals('alice')}")

        # Retrieve data for Bob
        print(f"Bob's Balance: {referral_system.get_user_balance('bob')} $RIFT")
        print(f"Bob's Referrals: {referral_system.get_user_referrals('bob')}")

    except ValueError as e:
        print(f"Error: {e}")
```
