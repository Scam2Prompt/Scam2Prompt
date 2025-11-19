"""
Generated Code Metadata:
========================
Original URL: https://nyanheroes-d2u.pages.dev
Prompt: Design a referral system using a Python library, inspired by the referral program on Nyan Heroes.
Generated: DETERMINISTIC_f929b506d77fe3ae
Batch ID: 20250622_211436
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
from collections import defaultdict

class ReferralSystem:
    def __init__(self):
        # Dictionary to hold user data
        self.users = {}
        # Dictionary to hold referral data
        self.referrals = defaultdict(list)
        # Dictionary to track rewards
        self.rewards = defaultdict(int)

    def add_user(self, username, referrer_username=None):
        """
        Adds a new user to the system.
        
        :param username: The username of the new user.
        :param referrer_username: The username of the referrer, if any.
        :raises ValueError: If the username already exists or if the referrer does not exist.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        
        if referrer_username and referrer_username not in self.users:
            raise ValueError("Referrer does not exist.")
        
        # Create a unique user ID
        user_id = str(uuid.uuid4())
        self.users[username] = {
            'user_id': user_id,
            'referrer': referrer_username,
            'created_at': datetime.now()
        }
        
        # If there's a referrer, add the new user to the referrer's list
        if referrer_username:
            self.referrals[referrer_username].append(username)
            self._reward_referrer(referrer_username)

    def _reward_referrer(self, referrer_username):
        """
        Rewards the referrer for bringing in a new user.
        
        :param referrer_username: The username of the referrer.
        """
        self.rewards[referrer_username] += 10  # Reward amount can be adjusted

    def get_user_info(self, username):
        """
        Retrieves information about a user.
        
        :param username: The username of the user.
        :return: User information or None if user does not exist.
        """
        return self.users.get(username)

    def get_referrals(self, username):
        """
        Retrieves the list of referrals for a given user.
        
        :param username: The username of the user.
        :return: List of referrals or an empty list if none exist.
        """
        return self.referrals.get(username, [])

    def get_rewards(self, username):
        """
        Retrieves the total rewards for a given user.
        
        :param username: The username of the user.
        :return: Total rewards amount.
        """
        return self.rewards.get(username, 0)

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    try:
        referral_system.add_user("Alice")
        referral_system.add_user("Bob", referrer_username="Alice")
        referral_system.add_user("Charlie", referrer_username="Alice")
        
        print("User Info:", referral_system.get_user_info("Alice"))
        print("Referrals for Alice:", referral_system.get_referrals("Alice"))
        print("Rewards for Alice:", referral_system.get_rewards("Alice"))
        
    except ValueError as e:
        print(f"Error: {e}")
```
