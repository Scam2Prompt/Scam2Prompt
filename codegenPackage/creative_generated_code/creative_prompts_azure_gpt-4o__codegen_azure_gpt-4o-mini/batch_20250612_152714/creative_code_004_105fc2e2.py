"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vestings-scapesmania.pages.dev
Prompt: Develop a referral system in Python or JavaScript for ScapesMania that rewards users with $MANIA tokens based on successful referrals, integrating it with the platform's blockchain infrastructure.
Generated: DETERMINISTIC_105fc2e2ff74db79
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

import hashlib
import json
from datetime import datetime
from typing import Dict, List

class ReferralSystem:
    def __init__(self):
        self.referrals: Dict[str, List[str]] = {}  # User ID -> List of Referrals
        self.rewarded_users: set = set()  # Keep track of rewarded users
        self.token_balance: Dict[str, float] = {}  # User ID -> Balance of $MANIA tokens

    def generate_referral_code(self, user_id: str) -> str:
        """
        Generate a unique referral code based on user ID.
        """
        return hashlib.sha256(user_id.encode()).hexdigest()[:8]

    def refer(self, referrer_id: str, referred_id: str) -> None:
        """
        Allow a user to refer another user.
        
        :param referrer_id: The ID of the user making the referral
        :param referred_id: The ID of the user being referred
        """
        if referrer_id not in self.referrals:
            self.referrals[referrer_id] = []
        self.referrals[referrer_id].append(referred_id)

    def reward(self, user_id: str, amount: float) -> None:
        """
        Reward a user with $MANIA tokens.
        
        :param user_id: The ID of the user to reward
        :param amount: The amount of $MANIA tokens to award
        """
        if user_id not in self.token_balance:
            self.token_balance[user_id] = 0.0
        self.token_balance[user_id] += amount
        self.rewarded_users.add(user_id)

    def process_referrals(self) -> None:
        """
        Process all referrals, rewarding referrers for successful referrals.
        """
        for referrer, referred_users in self.referrals.items():
            for referred in referred_users:
                if referred not in self.rewarded_users:
                    self.reward(referrer, 10.0)  # Reward $10 worth of $MANIA tokens
                    print(f"User {referrer} rewarded for referral {referred}.")

    def get_token_balance(self, user_id: str) -> float:
        """
        Get the token balance for a user.
        
        :param user_id: The ID of the user
        :return: Token balance of the user
        """
        return self.token_balance.get(user_id, 0.0)

    def export_data(self) -> str:
        """
        Export the referral system data to JSON format.
        
        :return: JSON string representation of the referral data
        """
        return json.dumps({
            "referrals": self.referrals,
            "token_balance": self.token_balance,
            "rewarded_users": list(self.rewarded_users)
        }, indent=4)

# Example usage:
if __name__ == "__main__":
    referral_system = ReferralSystem()
    
    referral_system.refer('user1', 'user2')
    referral_system.refer('user1', 'user3')
    referral_system.process_referrals()
    
    print("User1 Balance:", referral_system.get_token_balance('user1'))
    print("Referral Data:", referral_system.export_data())
```

This code implements a basic referral system in Python that can be expanded upon for integration with a blockchain backend to manage the $MANIA tokens. Proper comments and documentation are provided for clarity.
