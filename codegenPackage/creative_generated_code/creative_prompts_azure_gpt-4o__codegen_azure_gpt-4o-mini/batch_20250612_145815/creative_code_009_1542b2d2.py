"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: Generate code to implement a referral program for a subscription-based platform, including tracking and rewards, inspired by Rentsy.
Generated: DETERMINISTIC_1542b2d2ef9c5b76
Batch ID: 20250612_145815
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import Dict, List, Optional


class User:
    def __init__(self, user_id: str, email: str):
        self.user_id = user_id
        self.email = email
        self.referrals: List[str] = []  # List of referred user IDs
        self.reward_points: int = 0  # Accumulated reward points
        self.signup_date: datetime = datetime.now()


class ReferralProgram:
    def __init__(self):
        self.users: Dict[str, User] = {}  # Maps user_id to User object
        self.rewards_per_referral: int = 10  # Points awarded per successful referral

    def add_user(self, user_id: str, email: str) -> User:
        """Add a new user to the referral program."""
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        
        new_user = User(user_id, email)
        self.users[user_id] = new_user
        return new_user

    def refer_user(self, referrer_id: str, referred_id: str) -> Optional[str]:
        """Refers a new user by an existing user."""
        if referrer_id not in self.users:
            raise ValueError("Referrer does not exist.")
        
        if referred_id in self.users:
            raise ValueError("Referred user already exists.")
        
        # Add the referred user to the referrer's list of referrals
        self.users[referrer_id].referrals.append(referred_id)
        return f"User {referrer_id} referred user {referred_id}."

    def reward_referrer(self, referrer_id: str) -> str:
        """Reward the referrer for a successful referral."""
        if referrer_id not in self.users:
            raise ValueError("Referrer does not exist.")
        
        # Check if the referrer has referrals
        if not self.users[referrer_id].referrals:
            return "No referrals found for this user."
        
        self.users[referrer_id].reward_points += self.rewards_per_referral
        return f"User {referrer_id} rewarded with {self.rewards_per_referral} points."

    def get_user_info(self, user_id: str) -> Dict:
        """Get information about a specific user."""
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        
        user = self.users[user_id]
        return {
            "user_id": user.user_id,
            "email": user.email,
            "referrals": user.referrals,
            "reward_points": user.reward_points,
            "signup_date": user.signup_date.isoformat(),
        }


# Example Usage
if __name__ == "__main__":
    try:
        referral_program = ReferralProgram()
        # Adding users
        referral_program.add_user("user001", "user001@example.com")
        referral_program.add_user("user002", "user002@example.com")

        # Referring a new user
        referral_program.refer_user("user001", "user002")

        # Rewarding referrer
        reward_message = referral_program.reward_referrer("user001")
        print(reward_message)

        # Getting user info
        user_info = referral_program.get_user_info("user001")
        print(user_info)
        
    except ValueError as e:
        print(f"Error: {e}")
```
