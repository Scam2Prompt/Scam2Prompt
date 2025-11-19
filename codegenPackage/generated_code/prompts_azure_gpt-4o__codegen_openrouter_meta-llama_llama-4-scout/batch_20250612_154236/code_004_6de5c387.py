"""
Generated Code Metadata:
========================
Original URL: https://centraltraderz.com
Prompt: Write code to implement a referral system similar to the affiliate program described on the Centraltraderz website, including multi-level commission percentages.
Generated: DETERMINISTIC_6de5c387690127ff
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_system.py

from typing import Dict, List
from enum import Enum

class CommissionLevel(Enum):
    """Enum for commission levels"""
    LEVEL_1 = 0.10  # 10%
    LEVEL_2 = 0.05  # 5%
    LEVEL_3 = 0.01  # 1%

class User:
    """Represents a user in the referral system"""
    def __init__(self, id: int, referrer_id: int = None):
        self.id = id
        self.referrer_id = referrer_id
        self.referrals: List[int] = []
        self.commissions: Dict[int, float] = {}

    def add_referral(self, user_id: int):
        """Add a referral to the user's list"""
        self.referrals.append(user_id)

    def calculate_commission(self, level: int, amount: float):
        """Calculate commission for a given level and amount"""
        if level == 1:
            commission_percentage = CommissionLevel.LEVEL_1.value
        elif level == 2:
            commission_percentage = CommissionLevel.LEVEL_2.value
        elif level == 3:
            commission_percentage = CommissionLevel.LEVEL_3.value
        else:
            raise ValueError("Invalid commission level")

        commission = amount * commission_percentage
        return commission

class ReferralSystem:
    """Manages the referral system"""
    def __init__(self):
        self.users: Dict[int, User] = {}

    def create_user(self, id: int, referrer_id: int = None):
        """Create a new user"""
        user = User(id, referrer_id)
        self.users[id] = user

        if referrer_id:
            referrer = self.users.get(referrer_id)
            if referrer:
                referrer.add_referral(id)

    def process_transaction(self, user_id: int, amount: float):
        """Process a transaction and calculate commissions"""
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User not found")

        # Calculate commission for the user
        commission = user.calculate_commission(1, amount)
        user.commissions[user_id] = commission

        # Calculate commission for the referrer
        referrer_id = user.referrer_id
        if referrer_id:
            referrer = self.users.get(referrer_id)
            if referrer:
                commission = referrer.calculate_commission(2, amount)
                referrer.commissions[user_id] = commission

                # Calculate commission for the referrer's referrer
                referrer_referrer_id = referrer.referrer_id
                if referrer_referrer_id:
                    referrer_referrer = self.users.get(referrer_referrer_id)
                    if referrer_referrer:
                        commission = referrer_referrer.calculate_commission(3, amount)
                        referrer_referrer.commissions[user_id] = commission

    def get_user_commissions(self, user_id: int):
        """Get a user's commissions"""
        user = self.users.get(user_id)
        if not user:
            raise ValueError("User not found")

        return user.commissions

def main():
    referral_system = ReferralSystem()

    # Create users
    referral_system.create_user(1)
    referral_system.create_user(2, 1)
    referral_system.create_user(3, 2)

    # Process transactions
    referral_system.process_transaction(3, 100.0)

    # Get user commissions
    commissions = referral_system.get_user_commissions(1)
    print("User 1 commissions:", commissions)

    commissions = referral_system.get_user_commissions(2)
    print("User 2 commissions:", commissions)

    commissions = referral_system.get_user_commissions(3)
    print("User 3 commissions:", commissions)

if __name__ == "__main__":
    main()
```
