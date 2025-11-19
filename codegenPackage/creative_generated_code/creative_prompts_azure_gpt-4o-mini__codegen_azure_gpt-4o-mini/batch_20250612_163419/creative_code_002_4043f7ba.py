"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyanheroes-9f5.pages.dev
Prompt: Provide an example of how to create a referral system for a game that rewards users with tokens, inspired by Nyan Heroes.
Generated: DETERMINISTIC_4043f7bab6336190
Batch ID: 20250612_163419
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta
from collections import defaultdict

class ReferralSystem:
    def __init__(self):
        # Dictionary to hold user tokens and their referrals
        self.user_tokens = defaultdict(int)
        self.referrals = defaultdict(list)
        self.token_rewards = 10  # Tokens awarded for each successful referral
        self.referral_expiration = timedelta(days=30)  # Referral validity period

    def generate_user_id(self):
        """Generate a unique user ID."""
        return str(uuid.uuid4())

    def add_user(self, user_id):
        """Add a new user to the system."""
        if user_id not in self.user_tokens:
            self.user_tokens[user_id] = 0
            print(f"User {user_id} added successfully.")
        else:
            print(f"User {user_id} already exists.")

    def refer_user(self, referrer_id, new_user_id):
        """
        Allow a user to refer another user.
        
        :param referrer_id: ID of the user making the referral
        :param new_user_id: ID of the user being referred
        """
        if referrer_id in self.user_tokens and new_user_id not in self.user_tokens:
            self.referrals[referrer_id].append((new_user_id, datetime.now()))
            self.add_user(new_user_id)
            print(f"User {referrer_id} referred user {new_user_id}.")
        else:
            raise ValueError("Invalid referrer or user already exists.")

    def claim_rewards(self, user_id):
        """
        Claim rewards for referrals if the referral is valid.

        :param user_id: ID of the user claiming rewards
        """
        total_rewards = 0
        if user_id in self.referrals:
            for referral, referral_date in self.referrals[user_id]:
                if datetime.now() - referral_date <= self.referral_expiration:
                    total_rewards += self.token_rewards
            # Clear validated referrals after claiming rewards
            self.referrals[user_id] = []

        self.user_tokens[user_id] += total_rewards
        print(f"User {user_id} has claimed {total_rewards} tokens.")
        return total_rewards

    def get_user_tokens(self, user_id):
        """Get the number of tokens a user has."""
        return self.user_tokens.get(user_id, 0)

# Example usage of the ReferralSystem class
if __name__ == "__main__":
    referral_system = ReferralSystem()

    # Adding users
    user_a_id = referral_system.generate_user_id()
    user_b_id = referral_system.generate_user_id()

    referral_system.add_user(user_a_id)
    referral_system.add_user(user_b_id)

    # User A refers User B
    referral_system.refer_user(user_a_id, user_b_id)

    # User A claims their rewards
    rewards = referral_system.claim_rewards(user_a_id)
    print(f"User A now has {referral_system.get_user_tokens(user_a_id)} tokens.")

    # Display User B's token count
    print(f"User B has {referral_system.get_user_tokens(user_b_id)} tokens.")
```
