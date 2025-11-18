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
import datetime
from typing import Dict, List, Optional

class User:
    """
    A class representing a user in the referral system.
    """
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.referrals: List[User] = []
        self.referral_count = 0
        self.level = 0
        self.last_reward_claim: Optional[datetime.date] = None

    def add_referral(self, referral: 'User'):
        """
        Add a user as a referral and update referral count.
        """
        self.referrals.append(referral)
        self.referral_count += 1
        self.update_level()

    def update_level(self):
        """
        Update the user's level based on referral count.
        """
        if self.referral_count >= 20:
            self.level = 3
        elif self.referral_count >= 10:
            self.level = 2
        elif self.referral_count >= 5:
            self.level = 1
        else:
            self.level = 0

    def claim_daily_reward(self):
        """
        Allow the user to claim a daily reward based on their level.
        """
        today = datetime.date.today()
        if self.last_reward_claim == today:
            raise Exception("Reward already claimed for today.")
        
        rewards = {0: 0, 1: 10, 2: 20, 3: 50}  # Rewards based on level
        reward = rewards.get(self.level, 0)
        self.last_reward_claim = today
        return f"{self.name} has claimed {reward} coins for their daily reward."

class ReferralSystem:
    """
    A class to manage the referral system.
    """
    def __init__(self):
        self.users: Dict[str, User] = {}

    def register_user(self, user_id: str, name: str):
        """
        Register a new user in the system.
        """
        if user_id in self.users:
            raise Exception("User ID already exists.")
        self.users[user_id] = User(user_id, name)

    def add_referral(self, referrer_id: str, referral_id: str, referral_name: str):
        """
        Add a referral to a referrer.
        """
        if referrer_id not in self.users:
            raise Exception("Referrer does not exist.")
        if referral_id in self.users:
            raise Exception("Referral ID already exists.")
        
        referral = User(referral_id, referral_name)
        self.users[referral_id] = referral
        self.users[referrer_id].add_referral(referral)

    def claim_reward(self, user_id: str):
        """
        Let a user claim their daily reward.
        """
        if user_id not in self.users:
            raise Exception("User does not exist.")
        return self.users[user_id].claim_daily_reward()

# Example usage
if __name__ == "__main__":
    system = ReferralSystem()

    # Register users
    system.register_user("001", "Alice")
    system.register_user("002", "Bob")

    # Add referrals
    system.add_referral("001", "003", "Charlie")
    system.add_referral("001", "004", "Diana")
    system.add_referral("002", "005", "Eve")

    # Claim rewards
    try:
        print(system.claim_reward("001"))  # Should provide a reward based on level
        print(system.claim_reward("002"))  # Should provide a reward based on level
    except Exception as e:
        print(f"Error: {e}")
```
