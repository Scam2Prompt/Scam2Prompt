"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamstercombat.hk
Prompt: Generate code for implementing a referral system with level ratings and daily rewards, as outlined in the Hamster Kombat roadmap for April 2024.
Generated: DETERMINISTIC_0b5d9f9a31caf6e7
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from collections import defaultdict
import random

class ReferralSystem:
    def __init__(self):
        # Dictionary to hold user information
        self.users = defaultdict(lambda: {'level': 1, 'referrals': [], 'daily_reward_claimed': False})
        # Daily reward points
        self.daily_reward_points = 10
        # Reward levels based on referrals
        self.level_rewards = {
            1: 0,
            2: 20,
            3: 50,
            4: 100
        }
        
    def add_user(self, user_id):
        """Add a new user to the referral system."""
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id]  # Initialize user entry

    def refer(self, referrer_id, referee_id):
        """Allow a user to refer another user."""
        if referrer_id not in self.users:
            raise ValueError("Referrer does not exist.")
        if referee_id in self.users:
            raise ValueError("Referee already exists.")

        self.users[referrer_id]['referrals'].append(referee_id)
        self.add_user(referee_id)

        # Update referrer's level if necessary
        self.update_level(referrer_id)

    def update_level(self, user_id):
        """Update user's level based on the number of referrals."""
        referral_count = len(self.users[user_id]['referrals'])
        new_level = min(referral_count // 5 + 1, len(self.level_rewards))  # Every 5 referrals increase level
        if new_level != self.users[user_id]['level']:
            self.users[user_id]['level'] = new_level

    def claim_daily_reward(self, user_id):
        """Allow a user to claim their daily reward."""
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        user = self.users[user_id]
        
        # Check if the user has already claimed the reward today
        if user['daily_reward_claimed']:
            raise Exception("Daily reward already claimed.")
        
        # Mark the daily reward as claimed
        user['daily_reward_claimed'] = True

        # Calculate the reward amount based on the user's level
        reward_amount = self.level_rewards[user['level']]
        return reward_amount

    def reset_daily_rewards(self):
        """Reset daily rewards for all users at midnight."""
        for user in self.users:
            self.users[user]['daily_reward_claimed'] = False

    def simulate_day(self):
        """Simulate a day passing, calling reset_daily_rewards."""
        self.reset_daily_rewards()
        print("Daily rewards reset.")

# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Adding users
    referral_system.add_user("user1")
    referral_system.add_user("user2")
    
    # Referring users
    referral_system.refer("user1", "user2")
    
    # Claim daily reward
    try:
        reward = referral_system.claim_daily_reward("user1")
        print(f"User1 claimed daily reward: {reward} points")
    except Exception as e:
        print(f"Error: {e}")
    
    # Simulate a day passing
    referral_system.simulate_day()
```
