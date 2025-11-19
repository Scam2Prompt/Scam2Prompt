"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cd-eocse.sbs
Prompt: Generate code to create a referral system for a BTC mining platform, inspired by the features on the ECOS site.
Generated: DETERMINISTIC_c1f3ed29a99cbbfb
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import uuid
from datetime import datetime
from typing import Dict, Optional


class ReferralSystem:
    """
    Referral System for BTC Mining Platform.
    Allows users to generate referral codes, track referrals, and reward users based on referrals.
    """

    def __init__(self):
        self.users = {}  # Stores user data, including referral codes and earnings
        self.referrals = {}  # Tracks referrals made using referral codes

    def create_user(self, username: str) -> str:
        """
        Create a new user with a unique referral code.

        Args:
            username (str): The username of the new user.

        Returns:
            str: The referral code generated for the user.
        """
        if username in self.users:
            raise ValueError("Username already exists.")

        # Generate unique referral code using UUID and username hash
        referral_code = self._generate_referral_code(username)
        self.users[username] = {
            "referral_code": referral_code,
            "referred_users": [],
            "earnings": 0.0,  # Earnings from referrals
        }

        return referral_code

    def _generate_referral_code(self, username: str) -> str:
        """
        Internal method to generate a unique referral code.

        Args:
            username (str): The username for which to generate the referral code.

        Returns:
            str: A unique referral code.
        """
        unique_str = f"{username}-{uuid.uuid4()}"
        return hashlib.sha256(unique_str.encode()).hexdigest()[:10]

    def apply_referral_code(self, referrer_code: str, new_user: str) -> None:
        """
        Apply a referral code for a new user, linking the referrer and the new user.

        Args:
            referrer_code (str): The referral code of the referrer.
            new_user (str): The username of the new user.

        Raises:
            ValueError: If the referral code is invalid or the new user already exists.
        """
        if new_user in self.users:
            raise ValueError("New user already exists.")
        if referrer_code not in [user["referral_code"] for user in self.users.values()]:
            raise ValueError("Invalid referral code.")

        # Link referrer and new user
        referrer = self._find_user_by_referral_code(referrer_code)
        self.users[new_user] = {
            "referral_code": self._generate_referral_code(new_user),
            "referred_users": [],
            "earnings": 0.0,
        }
        self.users[referrer]["referred_users"].append(new_user)

        # Update referral tracking
        self.referrals[new_user] = {
            "referrer": referrer,
            "timestamp": datetime.now(),
        }

    def _find_user_by_referral_code(self, referral_code: str) -> str:
        """
        Internal method to find a user by their referral code.

        Args:
            referral_code (str): The referral code to search for.

        Returns:
            str: The username of the user with the given referral code.

        Raises:
            ValueError: If no user is found with the given referral code.
        """
        for username, user_data in self.users.items():
            if user_data["referral_code"] == referral_code:
                return username
        raise ValueError("No user found with the given referral code.")

    def get_user_details(self, username: str) -> Optional[Dict]:
        """
        Retrieve details about a specific user.

        Args:
            username (str): The username of the user.

        Returns:
            Optional[Dict]: A dictionary containing user details if found, otherwise None.
        """
        return self.users.get(username)

    def calculate_rewards(self, referrer: str, reward_per_referral: float) -> None:
        """
        Calculate and update the earnings of a referrer based on the number of referrals.

        Args:
            referrer (str): The username of the referrer.
            reward_per_referral (float): The reward amount for each referral.

        Raises:
            ValueError: If the referrer does not exist.
        """
        if referrer not in self.users:
            raise ValueError("Referrer does not exist.")

        num_referrals = len(self.users[referrer]["referred_users"])
        self.users[referrer]["earnings"] += num_referrals * reward_per_referral

    def display_summary(self) -> None:
        """
        Display a summary of all users and their referral activity.
        """
        print("Referral System Summary:")
        for username, user_data in self.users.items():
            print(f"Username: {username}")
            print(f"  Referral Code: {user_data['referral_code']}")
            print(f"  Referred Users: {user_data['referred_users']}")
            print(f"  Earnings: {user_data['earnings']:.2f}")
            print()


# Example usage:
if __name__ == "__main__":
    referral_system = ReferralSystem()

    # Creating users
    alice_code = referral_system.create_user("Alice")
    bob_code = referral_system.create_user("Bob")

    # Applying referral codes
    referral_system.apply_referral_code(alice_code, "Charlie")
    referral_system.apply_referral_code(bob_code, "Dave")

    # Calculate rewards
    referral_system.calculate_rewards("Alice", reward_per_referral=10.0)
    referral_system.calculate_rewards("Bob", reward_per_referral=10.0)

    # Display summary
    referral_system.display_summary()
```
