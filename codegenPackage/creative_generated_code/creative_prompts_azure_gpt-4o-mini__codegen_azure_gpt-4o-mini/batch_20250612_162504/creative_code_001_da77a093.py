"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://desol.pages.dev
Prompt: How can I implement a referral code system for an airdrop similar to the one used in The Desolation?
Generated: DETERMINISTIC_da77a0934c7c93f8
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class ReferralSystem:
    def __init__(self):
        # A dictionary to store user information and their referral codes
        self.users: Dict[str, Dict] = {}
        # A dictionary to store referral statistics
        self.referral_stats: Dict[str, List[str]] = {}

    def generate_referral_code(self) -> str:
        """
        Generate a unique referral code using UUID.
        """
        return str(uuid.uuid4())

    def register_user(self, username: str) -> str:
        """
        Register a new user and generate a referral code for them.
        
        :param username: The username of the user
        :return: The referral code of the user
        """
        if username in self.users:
            raise ValueError("Username already exists.")

        referral_code = self.generate_referral_code()
        self.users[username] = {
            "referral_code": referral_code,
            "referred_users": [],
            "rewards": 0
        }
        self.referral_stats[referral_code] = []

        return referral_code

    def refer_user(self, referring_username: str, new_username: str) -> Optional[str]:
        """
        Allow a user to refer another user using their referral code.
        
        :param referring_username: The username of the person referring
        :param new_username: The username of the new user being referred
        :return: The referral code of the referring user or None if the referral fails
        """
        if new_username in self.users:
            raise ValueError("User already registered.")

        if referring_username not in self.users:
            raise ValueError("Referring user does not exist.")

        referral_code = self.users[referring_username]["referral_code"]
        self.users[referring_username]["referred_users"].append(new_username)
        self.referral_stats[referral_code].append(new_username)

        # Register the new user
        return self.register_user(new_username)

    def get_referral_rewards(self, username: str) -> int:
        """
        Calculate the rewards for a user based on their referred users.
        
        :param username: The username of the user
        :return: The total rewards
        """
        if username not in self.users:
            raise ValueError("User does not exist.")

        referred_count = len(self.users[username]["referred_users"])
        return referred_count * 10  # Example: $10 reward per referred user

    def display_user_info(self, username: str) -> Dict:
        """
        Display user information including referral code and referred users.
        
        :param username: The username of the user
        :return: User information
        """
        if username not in self.users:
            raise ValueError("User does not exist.")

        return {
            "username": username,
            "referral_code": self.users[username]["referral_code"],
            "referred_users": self.users[username]["referred_users"],
            "rewards": self.get_referral_rewards(username)
        }

# Example usage:
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    try:
        alice_code = referral_system.register_user("Alice")
        print(f"Alice's referral code: {alice_code}")

        bob_code = referral_system.refer_user("Alice", "Bob")
        print(f"Bob's referral code: {bob_code}")

        # Display user information
        user_info = referral_system.display_user_info("Alice")
        print(user_info)
    except ValueError as e:
        print(f"Error: {e}")
```
