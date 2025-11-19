"""
Generated Code Metadata:
========================
Original URL: https://autobux.top
Prompt: Provide code to implement a three-level referral system with earnings tracking, similar to the one described on the AUTOBUX platform.
Generated: DETERMINISTIC_354c8ddd7d63a0e9
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_system.py

class User:
    """Represents a user in the referral system."""

    def __init__(self, user_id, referrer=None):
        """
        Initializes a new user.

        Args:
            user_id (int): Unique identifier for the user.
            referrer (User, optional): The user who referred this user. Defaults to None.
        """
        self.user_id = user_id
        self.referrer = referrer
        self.direct_referrals = []
        self.earnings = 0.0

    def add_referral(self, user):
        """
        Adds a direct referral to this user.

        Args:
            user (User): The user being referred.
        """
        self.direct_referrals.append(user)

    def update_earnings(self, amount):
        """
        Updates the earnings for this user.

        Args:
            amount (float): The amount to add to the user's earnings.
        """
        self.earnings += amount


class ReferralSystem:
    """Manages the three-level referral system."""

    def __init__(self):
        """
        Initializes a new referral system.
        """
        self.users = {}
        self.referral_rates = {
            1: 0.1,  # 10% for level 1 referrals
            2: 0.05,  # 5% for level 2 referrals
            3: 0.01,  # 1% for level 3 referrals
        }

    def create_user(self, user_id, referrer_id=None):
        """
        Creates a new user.

        Args:
            user_id (int): Unique identifier for the user.
            referrer_id (int, optional): The ID of the user who referred this user. Defaults to None.

        Returns:
            User: The newly created user.

        Raises:
            ValueError: If the referrer ID is invalid.
        """
        if referrer_id and referrer_id not in self.users:
            raise ValueError("Invalid referrer ID")

        referrer = self.users.get(referrer_id)
        user = User(user_id, referrer)
        self.users[user_id] = user

        if referrer:
            referrer.add_referral(user)

        return user

    def track_earnings(self, user_id, amount):
        """
        Tracks earnings for a user and updates referrals accordingly.

        Args:
            user_id (int): The ID of the user earning the amount.
            amount (float): The amount earned.

        Raises:
            ValueError: If the user ID is invalid.
        """
        if user_id not in self.users:
            raise ValueError("Invalid user ID")

        user = self.users[user_id]
        user.update_earnings(amount)

        # Update referrals
        self._update_referrals(user, amount)

    def _update_referrals(self, user, amount):
        """
        Updates referrals for the given user.

        Args:
            user (User): The user to update referrals for.
            amount (float): The amount earned.
        """
        level = 1
        current_user = user
        while current_user.referrer and level <= 3:
            referrer = current_user.referrer
            referral_rate = self.referral_rates[level]
            referral_amount = amount * referral_rate
            referrer.update_earnings(referral_amount)
            current_user = referrer
            level += 1


def main():
    # Example usage:
    referral_system = ReferralSystem()

    # Create users
    user1 = referral_system.create_user(1)
    user2 = referral_system.create_user(2, 1)
    user3 = referral_system.create_user(3, 2)
    user4 = referral_system.create_user(4, 1)

    # Track earnings
    referral_system.track_earnings(4, 100.0)

    # Print earnings
    print("User 1 earnings:", user1.earnings)
    print("User 2 earnings:", user2.earnings)
    print("User 3 earnings:", user3.earnings)
    print("User 4 earnings:", user4.earnings)


if __name__ == "__main__":
    main()
```
