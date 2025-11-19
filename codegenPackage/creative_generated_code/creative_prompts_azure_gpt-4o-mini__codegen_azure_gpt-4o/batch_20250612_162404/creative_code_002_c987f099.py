"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxgainfinance.com
Prompt: Create a code snippet that implements a referral tracking system for Max Gain Finance, allowing users to earn commissions from Level 1 and Level 2 referrals.
Generated: DETERMINISTIC_c987f0997c6272c8
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_tracking_system.py

import uuid

class ReferralTrackingSystem:
    """
    Referral Tracking System for Max Gain Finance.
    Allows users to earn commissions from Level 1 and Level 2 referrals.
    """

    def __init__(self):
        # Dictionary to store user data and referral relationships.
        # Format: {user_id: {"parent": parent_id, "referrals": [child_id1, child_id2, ...], "commission": 0.0}}
        self.users = {}

    def generate_user_id(self):
        """
        Generates a unique user ID for a new user.
        """
        return str(uuid.uuid4())

    def register_user(self, parent_id=None):
        """
        Registers a new user in the system.
        :param parent_id: Optional, parent user's ID (used for referral tracking).
        :return: Newly registered user's ID.
        """
        user_id = self.generate_user_id()
        self.users[user_id] = {
            "parent": parent_id,
            "referrals": [],
            "commission": 0.0
        }
        
        # If the user has a parent, update the parent's referral list
        if parent_id and parent_id in self.users:
            self.users[parent_id]["referrals"].append(user_id)

        return user_id

    def calculate_commission(self, user_id):
        """
        Calculates the current commission earned by a user from their referrals.
        :param user_id: User ID for which to calculate commission.
        :return: Total commission earned.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found in the system.")

        # Commission rates
        level_1_rate = 0.05  # 5% commission from Level 1 referrals
        level_2_rate = 0.02  # 2% commission from Level 2 referrals

        # Initialize total commission
        total_commission = 0.0

        # Level 1 referrals
        level_1_referrals = self.users[user_id]["referrals"]
        for referral_id in level_1_referrals:
            total_commission += level_1_rate

            # Level 2 referrals
            level_2_referrals = self.users[referral_id]["referrals"]
            total_commission += len(level_2_referrals) * level_2_rate

        return total_commission

    def update_commission(self, user_id):
        """
        Updates the user's commission in the system.
        :param user_id: User ID for which to update commission.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found in the system.")
        
        self.users[user_id]["commission"] = self.calculate_commission(user_id)

    def get_user_details(self, user_id):
        """
        Retrieves user details such as referrals and commission earned.
        :param user_id: User ID for which to retrieve details.
        :return: Dictionary containing user details.
        """
        if user_id not in self.users:
            raise ValueError("User ID not found in the system.")
        
        return self.users[user_id]


# Example usage of the referral tracking system
if __name__ == "__main__":
    system = ReferralTrackingSystem()

    # Register users
    user1 = system.register_user()  # Root user
    user2 = system.register_user(parent_id=user1)  # Level 1 referral
    user3 = system.register_user(parent_id=user1)  # Another Level 1 referral
    user4 = system.register_user(parent_id=user2)  # Level 2 referral
    user5 = system.register_user(parent_id=user2)  # Another Level 2 referral

    # Update commissions
    system.update_commission(user1)
    system.update_commission(user2)

    # Retrieve and display user details
    print("User 1 Details:", system.get_user_details(user1))
    print("User 2 Details:", system.get_user_details(user2))
```
