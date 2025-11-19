"""
Generated Code Metadata:
========================
Original URL: https://sunwukong-xi.vercel.app
Prompt: "Implement a referral system for the SUNWUKONG Hunt, allowing users to invite others and track points and rewards, while adhering to the campaign's terms and conditions."
Generated: DETERMINISTIC_e3dd10dac4f888e1
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime

class ReferralSystem:
    """
    A class to implement a referral system for the SUNWUKONG Hunt campaign.
    Users can invite others, track points, and rewards.
    """

    def __init__(self):
        # Initialize the referral system with empty user and referral data
        self.users = {}  # Stores user data: {user_id: {"name": str, "points": int, "rewards": list}}
        self.referrals = {}  # Stores referral data: {referrer_id: [referred_user_ids]}
    
    def create_user(self, name):
        """
        Create a new user in the system.
        :param name: Name of the user
        :return: User ID of the newly created user
        """
        user_id = str(uuid.uuid4())  # Generate a unique user ID
        self.users[user_id] = {"name": name, "points": 0, "rewards": []}
        return user_id

    def add_referral(self, referrer_id, referred_name):
        """
        Add a referral to the system.
        :param referrer_id: ID of the user who is referring
        :param referred_name: Name of the referred user
        :return: Referred user ID if successful, None if referrer ID is invalid
        """
        if referrer_id not in self.users:
            print("Error: Referrer ID not found.")
            return None
        
        referred_user_id = self.create_user(referred_name)
        
        # Add referral relationship
        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []
        self.referrals[referrer_id].append(referred_user_id)
        
        # Award points to the referrer
        self.users[referrer_id]["points"] += 10  # Example: 10 points per referral
        
        # Check for rewards
        self._check_rewards(referrer_id)
        
        return referred_user_id

    def _check_rewards(self, user_id):
        """
        Check if the user qualifies for any rewards based on their points.
        :param user_id: ID of the user to check rewards for
        """
        points = self.users[user_id]["points"]
        rewards = self.users[user_id]["rewards"]
        
        # Example reward system: 50 points = "Bronze Badge", 100 points = "Silver Badge"
        if points >= 50 and "Bronze Badge" not in rewards:
            rewards.append("Bronze Badge")
            print(f"Reward unlocked for {self.users[user_id]['name']}: Bronze Badge")
        if points >= 100 and "Silver Badge" not in rewards:
            rewards.append("Silver Badge")
            print(f"Reward unlocked for {self.users[user_id]['name']}: Silver Badge")

    def get_user_info(self, user_id):
        """
        Retrieve user information.
        :param user_id: ID of the user
        :return: Dictionary containing user information, or None if user ID is invalid
        """
        if user_id not in self.users:
            print("Error: User ID not found.")
            return None
        return self.users[user_id]

    def get_referrals(self, user_id):
        """
        Retrieve the list of referrals made by a user.
        :param user_id: ID of the user
        :return: List of referred user IDs, or None if user ID is invalid
        """
        if user_id not in self.referrals:
            return []
        return self.referrals[user_id]


# Example usage
if __name__ == "__main__":
    # Initialize the referral system
    system = ReferralSystem()
    
    # Create users
    user1_id = system.create_user("Alice")
    user2_id = system.create_user("Bob")
    
    # Add referrals
    referred_user_id = system.add_referral(user1_id, "Charlie")
    system.add_referral(user1_id, "Dave")
    
    # Retrieve user info
    print(system.get_user_info(user1_id))
    print(system.get_user_info(referred_user_id))
    
    # Retrieve referrals
    print(system.get_referrals(user1_id))
```
