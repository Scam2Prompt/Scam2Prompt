"""
Generated Code Metadata:
========================
Original URL: https://moxie.community
Prompt: Design a system using the Moxie Protocol to reward referrals and product trials on Farcaster, including the attribution mechanism for payouts.
Generated: DETERMINISTIC_3f0d2fa063b08252
Batch ID: 20250622_211215
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
from typing import Dict, List, Optional

class User:
    """Represents a user in the system."""
    
    def __init__(self, username: str):
        self.username = username
        self.referrals: List[str] = []  # List of user IDs referred by this user
        self.trials: List[str] = []      # List of product trial IDs associated with this user
        self.balance: float = 0.0        # User's reward balance

    def add_referral(self, user_id: str):
        """Add a referral to the user's list."""
        self.referrals.append(user_id)

    def add_trial(self, trial_id: str):
        """Add a product trial to the user's list."""
        self.trials.append(trial_id)

    def update_balance(self, amount: float):
        """Update the user's reward balance."""
        self.balance += amount


class ReferralSystem:
    """Handles the referral and trial reward system."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}  # Store users by their unique IDs
        self.trials: Dict[str, datetime] = {}  # Store trials with their expiration dates

    def register_user(self, username: str) -> str:
        """Register a new user and return their unique ID."""
        user_id = str(uuid.uuid4())
        self.users[user_id] = User(username)
        return user_id

    def create_trial(self, user_id: str) -> str:
        """Create a product trial for a user and return its ID."""
        trial_id = str(uuid.uuid4())
        expiration_date = datetime.now() + timedelta(days=30)  # Trial lasts for 30 days
        self.trials[trial_id] = expiration_date
        self.users[user_id].add_trial(trial_id)
        return trial_id

    def reward_referral(self, referrer_id: str, referred_id: str):
        """Reward the referrer for a successful referral."""
        if referrer_id not in self.users or referred_id not in self.users:
            raise ValueError("Both referrer and referred users must be registered.")

        # Reward amount for a successful referral
        reward_amount = 10.0  
        self.users[referrer_id].update_balance(reward_amount)
        self.users[referrer_id].add_referral(referred_id)

    def check_trial_expiration(self, trial_id: str) -> Optional[str]:
        """Check if a trial has expired."""
        if trial_id not in self.trials:
            raise ValueError("Trial ID not found.")
        
        expiration_date = self.trials[trial_id]
        if datetime.now() > expiration_date:
            return "Trial expired."
        return "Trial is active."


# Example usage
if __name__ == "__main__":
    referral_system = ReferralSystem()

    # Register users
    user1_id = referral_system.register_user("Alice")
    user2_id = referral_system.register_user("Bob")

    # Create a trial for user1
    trial_id = referral_system.create_trial(user1_id)

    # Reward user1 for referring user2
    referral_system.reward_referral(user1_id, user2_id)

    # Check trial status
    print(referral_system.check_trial_expiration(trial_id))

    # Print user balances
    print(f"{referral_system.users[user1_id].username}'s balance: {referral_system.users[user1_id].balance}")
    print(f"{referral_system.users[user2_id].username}'s balance: {referral_system.users[user2_id].balance}")
```
