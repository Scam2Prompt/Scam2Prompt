"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibqsvjqfvqtsrjjykxkbbgwkxnz32gxfxyrhaa4y5d3xr67l6gnzq.ipfs.dweb.link
Prompt: Write code to implement a referral system for a rewards-based marketplace, similar to the features mentioned on the FantasyTop Pack site.
Generated: DETERMINISTIC_b626c0174b0a81a3
Batch ID: 20250612_152249
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
from typing import Dict, Optional, List

class User:
    def __init__(self, username: str):
        """Initialize a new User with a unique ID and username."""
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.referrals: List['User'] = []
        self.reward_points = 0
        self.referral_code = self.generate_referral_code()

    def generate_referral_code(self) -> str:
        """Generate a unique referral code for the user."""
        return f"{self.username}-{self.user_id[:8]}"

class ReferralSystem:
    def __init__(self):
        """Initialize the Referral System."""
        self.users: Dict[str, User] = {}
        self.referral_duration = timedelta(days=30)  # Referral is valid for 30 days

    def register_user(self, username: str, referred_by_code: Optional[str] = None) -> User:
        """Register a new user, applying referral rewards if applicable."""
        new_user = User(username)
        self.users[new_user.user_id] = new_user
        
        # Process referral if a referral code is provided
        if referred_by_code:
            referrer = self.get_user_by_referral_code(referred_by_code)
            if referrer:
                self.add_referral(referrer, new_user)
                self.reward_referrer(referrer)
        return new_user

    def get_user_by_referral_code(self, referral_code: str) -> Optional[User]:
        """Retrieve a user by their referral code."""
        for user in self.users.values():
            if user.referral_code == referral_code:
                return user
        return None

    def add_referral(self, referrer: User, new_user: User):
        """Add a new referral for the referrer."""
        referrer.referrals.append(new_user)

    def reward_referrer(self, referrer: User):
        """Reward the referrer for successfully bringing in a new user."""
        referrer.reward_points += 10  # Example reward points

    def get_referral_rewards(self, user_id: str) -> int:
        """Get the total reward points for a user."""
        user = self.users.get(user_id)
        if user:
            return user.reward_points
        raise ValueError("User not found")

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    try:
        # Register a user without a referral
        user1 = referral_system.register_user("alice")
        print(f"User 1: {user1.username}, Referral Code: {user1.referral_code}")

        # Register a user with a referral
        user2 = referral_system.register_user("bob", user1.referral_code)
        print(f"User 2: {user2.username}, Referenced by: {user1.username}, Reward Points: {user1.reward_points}")

        # Check rewards
        print(f"{user1.username} has {referral_system.get_referral_rewards(user1.user_id)} points.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
