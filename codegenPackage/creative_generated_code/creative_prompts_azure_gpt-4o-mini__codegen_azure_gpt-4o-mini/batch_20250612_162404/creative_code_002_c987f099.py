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
class User:
    """
    A class representing a user in the referral tracking system.
    Attributes:
        user_id (str): Unique identifier for the user.
        referrals (list): List of users referred by this user.
        level (int): The level of the referral (1 or 2).
        earnings (float): The earnings from referrals.
    """

    def __init__(self, user_id):
        self.user_id = user_id
        self.referrals = []
        self.level = 1  # Level 1 referrals
        self.earnings = 0.0

    def add_referral(self, referral_user):
        """Adds a referral to the user's referral list."""
        if isinstance(referral_user, User):
            self.referrals.append(referral_user)
        else:
            raise TypeError("referral_user must be an instance of User")

    def calculate_earnings(self, commission_rate_level_1, commission_rate_level_2):
        """
        Calculate earnings from Level 1 and Level 2 referrals.

        Parameters:
            commission_rate_level_1 (float): Commission rate for Level 1 referrals.
            commission_rate_level_2 (float): Commission rate for Level 2 referrals.
        """
        level_1_referrals = len(self.referrals)
        level_2_referrals = sum(len(referral.referrals) for referral in self.referrals)

        self.earnings = (level_1_referrals * commission_rate_level_1) + \
                        (level_2_referrals * commission_rate_level_2)

class ReferralSystem:
    """
    A class representing the referral tracking system for Max Gain Finance.
    """

    def __init__(self):
        self.users = {}

    def register_user(self, user_id):
        """
        Registers a new user in the system.

        Parameters:
            user_id (str): The unique identifier for the user.

        Raises:
            ValueError: If the user ID is already registered.
        """
        if user_id in self.users:
            raise ValueError("User ID already registered.")
        
        self.users[user_id] = User(user_id)
        return self.users[user_id]

    def add_referral(self, user_id, referral_id):
        """
        Adds a referral for a user.

        Parameters:
            user_id (str): The ID of the user making the referral.
            referral_id (str): The ID of the user being referred.

        Raises:
            ValueError: If either user ID is not registered.
        """
        if user_id not in self.users or referral_id not in self.users:
            raise ValueError("Both users must be registered in the system.")
        
        referring_user = self.users[user_id]
        referral_user = self.users[referral_id]

        referring_user.add_referral(referral_user)

    def calculate_user_earnings(self, user_id, commission_rate_level_1, commission_rate_level_2):
        """
        Calculates the earnings for a specific user.

        Parameters:
            user_id (str): The ID of the user for whom to calculate earnings.
            commission_rate_level_1 (float): Commission rate for Level 1 referrals.
            commission_rate_level_2 (float): Commission rate for Level 2 referrals.

        Returns:
            float: The calculated earnings for the user.

        Raises:
            ValueError: If the user ID is not registered.
        """
        if user_id not in self.users:
            raise ValueError("User not registered.")

        user = self.users[user_id]
        user.calculate_earnings(commission_rate_level_1, commission_rate_level_2)
        return user.earnings

# Example usage
if __name__ == "__main__":
    try:
        referral_system = ReferralSystem()
        
        # Register users
        user1 = referral_system.register_user("user1")
        user2 = referral_system.register_user("user2")
        user3 = referral_system.register_user("user3")
        
        # Add referrals
        referral_system.add_referral("user1", "user2")
        referral_system.add_referral("user1", "user3")
        
        # Calculate earnings
        earnings = referral_system.calculate_user_earnings("user1", 10.0, 5.0)
        print(f"Earnings for user1: ${earnings:.2f}")

    except (ValueError, TypeError) as e:
        print(f"An error occurred: {e}")
```
