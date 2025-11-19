"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: What are the best practices for integrating a referral system in a mobile game that rewards users for inviting friends?
Generated: DETERMINISTIC_3c1a917297a5be73
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
from datetime import datetime, timedelta
from collections import defaultdict

class ReferralSystem:
    def __init__(self):
        # Dictionary to store user data
        self.users = {}
        # Dictionary to store referral rewards
        self.referral_rewards = defaultdict(int)

    def generate_user_id(self):
        """Generate a unique user ID."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    def register_user(self, username, referrer_id=None):
        """Register a new user in the system."""
        user_id = self.generate_user_id()
        if referrer_id and referrer_id in self.users:
            self.users[user_id] = {
                'username': username,
                'referrer_id': referrer_id,
                'referral_date': datetime.now()
            }
            # Reward the referrer
            self.referral_rewards[referrer_id] += 1
        else:
            self.users[user_id] = {
                'username': username,
                'referrer_id': None,
                'referral_date': datetime.now()
            }
        return user_id

    def get_user_info(self, user_id):
        """Retrieve information about a specific user."""
        return self.users.get(user_id, "User not found.")

    def get_referral_rewards(self, user_id):
        """Get the number of referral rewards for a user."""
        return self.referral_rewards.get(user_id, 0)

    def redeem_rewards(self, user_id, points):
        """Redeem rewards for a user. Ensures enough points are available."""
        if self.referral_rewards[user_id] >= points:
            self.referral_rewards[user_id] -= points
            return f"{points} rewards redeemed."
        else:
            raise ValueError("Insufficient referral rewards to redeem.")

    def clean_up_inactive_referrals(self):
        """Remove users who haven't referred anyone in the last 30 days."""
        cutoff_date = datetime.now() - timedelta(days=30)
        inactive_users = [user_id for user_id, info in self.users.items() 
                          if info['referrer_id'] is None and info['referral_date'] < cutoff_date]

        for user_id in inactive_users:
            del self.users[user_id]

# Example Usage:
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Register users
    user1_id = referral_system.register_user("Alice")
    user2_id = referral_system.register_user("Bob", user1_id)
    
    # Check user info
    print(referral_system.get_user_info(user1_id))
    print(referral_system.get_user_info(user2_id))
    
    # Check rewards
    print(referral_system.get_referral_rewards(user1_id))
    
    # Redeem rewards
    try:
        print(referral_system.redeem_rewards(user1_id, 1))
    except ValueError as e:
        print(e)

    # Clean up inactive referrals
    referral_system.clean_up_inactive_referrals()
```
