"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elon-crypto.online
Prompt: Generate a script that simulates the referral bonus system for OctaFx VIP plans, ensuring it adheres to the zero-level referral bonus structure mentioned on the webpage.
Generated: DETERMINISTIC_e2899b5ef169c58b
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Bonus Simulation Script for OctaFx VIP Plans

This script simulates a referral bonus system based on a zero-level referral structure.
It adheres to the following conditions:
1. Users can refer other users and earn a fixed bonus for each successful referral.
2. Only direct referrals (zero-level) are considered for bonuses.
"""

import sys

class ReferralBonusSystem:
    """
    Class to manage the referral bonus system.
    """
    def __init__(self, bonus_per_referral):
        """
        Initialize the referral bonus system.

        :param bonus_per_referral: The fixed bonus amount for each referral.
        """
        self.bonus_per_referral = bonus_per_referral
        self.users = {}  # Dictionary to store user data (user_id: referred_users)

    def add_user(self, user_id):
        """
        Add a user to the system.

        :param user_id: Unique ID of the user.
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists!")
        self.users[user_id] = []

    def refer_user(self, referrer_id, referred_id):
        """
        Simulate a user referral.

        :param referrer_id: ID of the referrer.
        :param referred_id: ID of the referred user.
        """
        if referrer_id not in self.users:
            raise ValueError(f"Referrer {referrer_id} does not exist!")
        if referred_id in self.users:
            raise ValueError(f"User {referred_id} already exists! Cannot refer an existing user.")
        
        # Add referred user and update referrer's list
        self.users[referrer_id].append(referred_id)
        self.add_user(referred_id)

    def calculate_bonus(self, user_id):
        """
        Calculate the total referral bonus for a user.

        :param user_id: ID of the user.
        :return: Total bonus amount for the user.
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} does not exist!")
        return len(self.users[user_id]) * self.bonus_per_referral

    def display_referral_data(self):
        """
        Display the referral data for all users.
        """
        print("Referral Data:")
        for user_id, referred_users in self.users.items():
            bonus = self.calculate_bonus(user_id)
            print(f"User: {user_id}, Referred Users: {referred_users}, Bonus: ${bonus}")

# Main script logic
if __name__ == "__main__":
    try:
        # Initialize the referral bonus system with a fixed bonus amount
        bonus_system = ReferralBonusSystem(bonus_per_referral=50)

        # Simulate adding users and referrals
        bonus_system.add_user("VIP001")
        bonus_system.refer_user("VIP001", "VIP002")
        bonus_system.refer_user("VIP001", "VIP003")
        bonus_system.refer_user("VIP002", "VIP004")  # VIP002 refers VIP004

        # Display referral data and bonuses for all users
        bonus_system.display_referral_data()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
```
