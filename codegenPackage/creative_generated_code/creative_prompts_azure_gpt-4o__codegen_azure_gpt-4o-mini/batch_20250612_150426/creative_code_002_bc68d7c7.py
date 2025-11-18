"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ff-exchange.at
Prompt: Generate code to integrate a referral system that tracks rewards for users referring friends to FF.IO, following the platform's reward structure.
Generated: DETERMINISTIC_bc68d7c772f7b760
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import datetime
from typing import List, Dict, Optional

class User:
    """Class representing a user in the referral system."""
    
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.referrals: List[str] = []  # List to store IDs of referred users
        self.reward_points: int = 0      # User's total reward points

    def refer(self, friend: 'User'):
        """Refer a friend and add them to the user's referrals."""
        if friend.user_id in self.referrals:
            raise ValueError(f"{friend.name} is already referred.")
        self.referrals.append(friend.user_id)
        return self

    def earn_reward(self, points: int):
        """Increase the user's reward points."""
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.reward_points += points

    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.reward_points} points)"

class ReferralSystem:
    """Class for managing the referral system."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to store user objects by user_id

    def add_user(self, name: str) -> User:
        """Add a new user to the referral system."""
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        user = User(user_id, name)
        self.users[user_id] = user
        return user

    def process_referral(self, referrer_id: str, friend_id: str, reward_points: int):
        """Process a referral and award points to the referrer."""
        referrer = self.users.get(referrer_id)
        friend = self.users.get(friend_id)

        if not referrer or not friend:
            raise ValueError("Both referrer and friend must be valid users.")
        
        try:
            referrer.refer(friend)
            referrer.earn_reward(reward_points)
            print(f"Referral successful: {referrer.name} referred {friend.name}. Rewarded {reward_points} points.")
        except ValueError as e:
            print(f"Error processing referral: {e}")

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()

    # Create users
    alice = referral_system.add_user("Alice")
    bob = referral_system.add_user("Bob")
    charlie = referral_system.add_user("Charlie")

    # Process referrals
    referral_system.process_referral(alice.user_id, bob.user_id, 10)  # Alice refers Bob
    referral_system.process_referral(alice.user_id, charlie.user_id, 15)  # Alice refers Charlie

    # Attempting to refer Bob again
    try:
        referral_system.process_referral(alice.user_id, bob.user_id, 10)  # Should raise an error
    except ValueError as e:
        print(f"Handled error: {e}")

    # Display users and their rewards
    for user in referral_system.users.values():
        print(user)
```
