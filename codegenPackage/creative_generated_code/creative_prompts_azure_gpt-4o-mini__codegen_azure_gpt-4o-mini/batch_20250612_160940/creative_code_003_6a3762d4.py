"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://websea-login.com
Prompt: How can I implement a referral system in my app that rewards users with 10WBS for inviting friends, similar to Websea's model?
Generated: DETERMINISTIC_6a3762d47df54502
Batch ID: 20250612_160940
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

class User:
    """Represents a user in the referral system."""
    
    def __init__(self, username: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the user
        self.username = username
        self.referral_code = str(uuid.uuid4())[:8]  # Generate a unique referral code
        self.referrals = []  # List to store referrals
        self.reward_balance = 0  # User's reward balance

    def add_referral(self, referral_code: str):
        """Adds a referral to the user's list of referrals if valid."""
        if referral_code in ReferralSystem.referral_codes:
            self.referrals.append(referral_code)
            self.reward_balance += 10  # Award 10WBS for each successful referral
            print(f"{self.username} has successfully referred a user! New balance: {self.reward_balance} WBS.")
        else:
            print(f"Failed to add referral: {referral_code} is invalid.")

class ReferralSystem:
    """Handles the referral logic."""
    
    referral_codes: List[str] = []  # Store valid referral codes

    @classmethod
    def register_user(cls, username: str) -> User:
        """Registers a new user and stores their referral code."""
        user = User(username)
        cls.referral_codes.append(user.referral_code)  # Store the user’s referral code
        print(f"User {username} registered with referral code: {user.referral_code}")
        return user

    @classmethod
    def refer_user(cls, referrer: User, referral_code: str) -> None:
        """Processes a new user referral using the referrer’s referral code."""
        try:
            referrer.add_referral(referral_code)
        except Exception as e:
            print(f"An error occurred during referral process: {e}")

# Example usage
if __name__ == "__main__":
    # Register users
    user1 = ReferralSystem.register_user("Alice")
    user2 = ReferralSystem.register_user("Bob")

    # User 1 refers User 2 using their referral code
    ReferralSystem.refer_user(user1, user1.referral_code)  # Successful referral
    ReferralSystem.refer_user(user2, "INVALIDCODE")  # Unsuccessful referral
```
