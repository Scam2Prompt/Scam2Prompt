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
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class User:
    """Class representing a user in the referral system."""
    
    def __init__(self, username: str):
        self.username = username
        self.referral_code = str(uuid.uuid4())  # Unique referral code for the user
        self.referrals: List['User'] = []  # List to store referred users
        self.reward_points: int = 0  # Points earned through referrals

    def refer(self, user: 'User'):
        """Add a referred user to the user's referral list."""
        self.referrals.append(user)

    def add_reward_points(self, points: int):
        """Add reward points to the user's account."""
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.reward_points += points

class ReferralSystem:
    """Class to manage the referral system."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to store users by username

    def register_user(self, username: str) -> User:
        """Register a new user in the system."""
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[username] = user
        return user

    def process_referral(self, referrer_username: str, referred_username: str) -> Optional[str]:
        """Process a referral from one user to another."""
        if referrer_username not in self.users:
            return "Referrer does not exist."
        if referred_username in self.users:
            return "Referred user already exists."

        referrer = self.users[referrer_username]
        referred_user = self.register_user(referred_username)
        referrer.refer(referred_user)

        # Reward the referrer
        referrer.add_reward_points(10)  # Reward 10 points for each referral
        return f"Referral successful! {referrer_username} has earned 10 points."

    def get_user_info(self, username: str) -> Optional[Dict]:
        """Retrieve user information including referrals and reward points."""
        user = self.users.get(username)
        if not user:
            return None
        return {
            "username": user.username,
            "referral_code": user.referral_code,
            "referrals": [referral.username for referral in user.referrals],
            "reward_points": user.reward_points
        }

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Register users
    user1 = referral_system.register_user("Alice")
    user2 = referral_system.register_user("Bob")
    
    # Process a referral
    result = referral_system.process_referral("Alice", "Charlie")
    print(result)  # Output: Referral successful! Alice has earned 10 points.

    # Get user info
    user_info = referral_system.get_user_info("Alice")
    print(user_info)  # Output: User information including referrals and points
```
