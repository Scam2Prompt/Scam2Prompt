"""
Generated Code Metadata:
========================
Original URL: https://hedgefund-options.com
Prompt: Generate a code snippet that demonstrates how to implement a referral program similar to the one described on hedgefund-options.com.
Generated: DETERMINISTIC_5c23cb619b3e3074
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

class ReferralProgram:
    def __init__(self):
        # Initialize a dictionary to store user referrals
        self.referrals = {}
        # Initialize a dictionary to store user rewards
        self.user_rewards = {}

    def add_user(self, user_id):
        """Add a new user to the referral program."""
        if user_id in self.referrals:
            raise ValueError(f"User {user_id} already exists.")
        self.referrals[user_id] = []
        self.user_rewards[user_id] = 0

    def refer_user(self, referrer_id, referred_id):
        """Allow a user to refer another user."""
        if referrer_id not in self.referrals:
            raise ValueError(f"Referrer {referrer_id} does not exist.")
        if referred_id in self.referrals:
            raise ValueError(f"User {referred_id} is already registered.")
        
        # Add the referred user to the referrer's list of referrals
        self.referrals[referrer_id].append(referred_id)
        # Add the referred user to the program
        self.add_user(referred_id)
        # Reward the referrer
        self.user_rewards[referrer_id] += 10  # Example reward amount

    def get_referrals(self, user_id):
        """Get the list of referrals for a given user."""
        if user_id not in self.referrals:
            raise ValueError(f"User {user_id} does not exist.")
        return self.referrals[user_id]

    def get_user_reward(self, user_id):
        """Get the total rewards for a given user."""
        if user_id not in self.user_rewards:
            raise ValueError(f"User {user_id} does not exist.")
        return self.user_rewards[user_id]

    def display_referral_summary(self):
        """Display a summary of all users and their referrals."""
        for user_id, referred_users in self.referrals.items():
            print(f"User: {user_id}, Referrals: {referred_users}, Rewards: {self.user_rewards[user_id]}")

# Example usage
if __name__ == "__main__":
    referral_program = ReferralProgram()
    
    # Adding users
    referral_program.add_user("user1")
    referral_program.add_user("user2")
    
    # Referring users
    referral_program.refer_user("user1", "user2")
    
    # Displaying referral summary
    referral_program.display_referral_summary()
    
    # Getting rewards
    print(f"User1 Rewards: {referral_program.get_user_reward('user1')}")
```
