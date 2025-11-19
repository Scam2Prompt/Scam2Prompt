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
import uuid
from datetime import datetime
from collections import defaultdict

class User:
    """
    Represents a user in the referral system.
    
    Attributes:
        user_id (str): Unique identifier for the user.
        username (str): The username of the user.
        referrals (list): List of User objects referred by this user.
        referral_code (str): Unique referral code for the user.
        created_at (datetime): Timestamp when the user was created.
    """
    
    def __init__(self, username):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.referrals = []
        self.referral_code = str(uuid.uuid4())[:8]  # Shortened referral code
        self.created_at = datetime.now()

    def add_referral(self, user):
        """Add a new referral to the user's referrals list."""
        self.referrals.append(user)

class ReferralSystem:
    """
    Represents the referral system for the BTC mining platform.
    
    Attributes:
        users (dict): Dictionary of users indexed by their user_id.
    """
    
    def __init__(self):
        self.users = {}

    def register_user(self, username):
        """Register a new user."""
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username)
        self.users[user.user_id] = user
        return user

    def refer_user(self, referrer_id, username):
        """Refer a new user through an existing user."""
        if referrer_id not in self.users:
            raise ValueError("Referrer not found.")
        referrer = self.users[referrer_id]
        new_user = self.register_user(username)
        referrer.add_referral(new_user)
        return new_user

    def get_referral_info(self, user_id):
        """Get the referral details for a specific user."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        user = self.users[user_id]
        return {
            "username": user.username,
            "referral_code": user.referral_code,
            "referrals": [referral.username for referral in user.referrals]
        }

    def get_all_users(self):
        """Get a list of all registered users."""
        return [user.username for user in self.users.values()]

# Example usage:
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Register initial users
    user1 = referral_system.register_user("Alice")
    user2 = referral_system.register_user("Bob")
    
    # User1 refers User3
    user3 = referral_system.refer_user(user1.user_id, "Charlie")
    
    # Fetch referral information
    referral_info = referral_system.get_referral_info(user1.user_id)
    print(referral_info)

    # List all registered users
    print(referral_system.get_all_users())
```
