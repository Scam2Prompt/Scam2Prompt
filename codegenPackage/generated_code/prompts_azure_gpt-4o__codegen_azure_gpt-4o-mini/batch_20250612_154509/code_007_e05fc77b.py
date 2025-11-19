"""
Generated Code Metadata:
========================
Original URL: https://gamees.org
Prompt: Write code to implement a referral system for "3 Patti Bounty" apps, allowing users to earn rewards for inviting others, as mentioned on https://gamees.org.
Generated: DETERMINISTIC_e05fc77b44bf941b
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_system.py

class ReferralSystem:
    def __init__(self):
        # Initialize a dictionary to store user data
        self.users = {}
        self.referral_rewards = 10  # Reward for each successful referral

    def add_user(self, user_id, referrer_id=None):
        """
        Add a new user to the system.
        
        :param user_id: Unique identifier for the new user
        :param referrer_id: Unique identifier for the user who referred the new user
        :raises ValueError: If the user_id already exists
        """
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        
        # Create a new user entry
        self.users[user_id] = {
            'referrer_id': referrer_id,
            'reward_points': 0
        }
        
        # If the user has a referrer, reward the referrer
        if referrer_id and referrer_id in self.users:
            self.users[referrer_id]['reward_points'] += self.referral_rewards

    def get_user_reward(self, user_id):
        """
        Get the total reward points for a user.
        
        :param user_id: Unique identifier for the user
        :return: Total reward points for the user
        :raises ValueError: If the user_id does not exist
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        
        return self.users[user_id]['reward_points']

    def get_referrer(self, user_id):
        """
        Get the referrer of a user.
        
        :param user_id: Unique identifier for the user
        :return: Referrer ID or None if no referrer exists
        :raises ValueError: If the user_id does not exist
        """
        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        
        return self.users[user_id]['referrer_id']

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Adding users and handling potential errors
    try:
        referral_system.add_user("user1")
        referral_system.add_user("user2", "user1")  # user1 refers user2
        referral_system.add_user("user3", "user1")  # user1 refers user3
        
        print(f"User1 Reward Points: {referral_system.get_user_reward('user1')}")
        print(f"User2 Reward Points: {referral_system.get_user_reward('user2')}")
        print(f"User3 Reward Points: {referral_system.get_user_reward('user3')}")
        
        # Attempting to add a user with an existing ID
        referral_system.add_user("user1")  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")
```
