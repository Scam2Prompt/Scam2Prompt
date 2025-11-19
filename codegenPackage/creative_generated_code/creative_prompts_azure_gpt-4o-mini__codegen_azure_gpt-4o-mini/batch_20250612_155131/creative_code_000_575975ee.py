"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterkom-com.pages.dev
Prompt: Generate code to implement a referral system for a gaming platform similar to Hamster Kombat, focusing on user levels and daily rewards.
Generated: DETERMINISTIC_575975eedc303af2
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class User:
    """Class representing a user in the gaming platform."""
    
    def __init__(self, username):
        self.username = username
        self.level = 1
        self.referrals = []
        self.daily_rewards_claimed = {}
    
    def refer_user(self, referred_username):
        """Refer a new user and add them to the referrals list."""
        if referred_username not in self.referrals:
            self.referrals.append(referred_username)
            print(f"{self.username} referred {referred_username}.")
        else:
            print(f"{referred_username} has already been referred by {self.username}.")

    def claim_daily_reward(self):
        """Claim the daily reward for the user if not already claimed today."""
        today = datetime.now().date()
        if today in self.daily_rewards_claimed:
            print("Daily reward already claimed for today.")
            return False
        
        # Simulate reward based on the user's level
        reward = self.level * 10
        self.daily_rewards_claimed[today] = reward
        print(f"{self.username} claimed a daily reward of {reward} points.")
        return reward

    def level_up(self):
        """Level up the user based on the referrals."""
        if len(self.referrals) >= 5:  # Example threshold for leveling up
            self.level += 1
            print(f"{self.username} leveled up to level {self.level}!")

class ReferralSystem:
    """Class to manage the referral system for all users."""
    
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        """Add a new user to the system."""
        if username in self.users:
            print(f"User {username} already exists.")
            return False
        
        self.users[username] = User(username)
        print(f"User {username} added to the system.")
        return True

    def refer(self, username, referred_username):
        """Handle the referral process between users."""
        if username not in self.users or referred_username in self.users:
            print("Referral action failed: invalid users.")
            return False
        
        self.users[username].refer_user(referred_username)
        self.users[username].level_up()  # Check if the referral leads to a level-up
        return True

    def claim_reward(self, username):
        """Allow a user to claim their daily reward."""
        if username not in self.users:
            print("Claim action failed: user does not exist.")
            return False
        
        return self.users[username].claim_daily_reward()

# Example Usage
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    # Adding users
    referral_system.add_user("Player1")
    referral_system.add_user("Player2")
    
    # Players referring each other
    referral_system.refer("Player1", "Player2")
    referral_system.refer("Player1", "Player3")  # Player3 doesn't exist yet
    
    # Claiming daily rewards
    referral_system.claim_reward("Player1")
    referral_system.claim_reward("Player2")
    
    # Trying to claim again
    referral_system.claim_reward("Player1")
```

This code implements a basic referral system for a gaming platform, allowing users to refer others, level up based on referrals, and claim daily rewards. Each class and method is documented for clarity, and basic error handling is included.
