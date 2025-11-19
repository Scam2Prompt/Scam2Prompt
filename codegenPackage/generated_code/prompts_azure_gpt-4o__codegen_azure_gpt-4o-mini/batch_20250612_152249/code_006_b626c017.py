"""
Generated Code Metadata:
========================
Original URL: https://bafybeibqsvjqfvqtsrjjykxkbbgwkxnz32gxfxyrhaa4y5d3xr67l6gnzq.ipfs.dweb.link
Prompt: Write code to implement a referral system for a rewards-based marketplace, similar to the features mentioned on the FantasyTop Pack site.
Generated: DETERMINISTIC_b626c0174b0a81a3
Batch ID: 20250612_152249
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
from typing import Dict, List, Optional

class User:
    """Class representing a user in the referral system."""
    
    def __init__(self, username: str):
        self.username = username
        self.referral_code = self.generate_referral_code()
        self.referrals: List[str] = []  # List of usernames referred by this user
        self.rewards: int = 0  # Total rewards earned by the user

    def generate_referral_code(self) -> str:
        """Generate a unique referral code for the user."""
        return str(uuid.uuid4())

    def add_referral(self, referral_username: str):
        """Add a referral to the user's list of referrals."""
        if referral_username not in self.referrals:
            self.referrals.append(referral_username)
            self.rewards += 10  # Reward for each successful referral
        else:
            raise ValueError("This user has already been referred.")

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

    def refer_user(self, referrer_username: str, referred_username: str) -> Optional[str]:
        """Process a referral from one user to another."""
        if referrer_username not in self.users:
            raise ValueError("Referrer does not exist.")
        if referred_username in self.users:
            raise ValueError("Referred user already exists.")

        # Register the referred user
        referred_user = self.register_user(referred_username)
        
        # Add the referral to the referrer
        self.users[referrer_username].add_referral(referred_username)
        
        return referred_user.referral_code

    def get_user_rewards(self, username: str) -> int:
        """Get the total rewards for a user."""
        if username not in self.users:
            raise ValueError("User does not exist.")
        return self.users[username].rewards

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Register users
    user1 = referral_system.register_user("Alice")
    user2 = referral_system.register_user("Bob")
    
    # Alice refers Bob
    try:
        referral_code = referral_system.refer_user("Alice", "Charlie")
        print(f"Charlie was referred by Alice with referral code: {referral_code}")
    except ValueError as e:
        print(f"Error: {e}")

    # Check rewards
    print(f"Alice's rewards: {referral_system.get_user_rewards('Alice')}")
    print(f"Bob's rewards: {referral_system.get_user_rewards('Bob')}")
```
