"""
Generated Code Metadata:
========================
Original URL: https://accesslinklimited.com
Prompt: Generate code to implement a referral system that mirrors the 10% commission structure outlined in Access Link Limited's affiliate program.
Generated: DETERMINISTIC_d119c2a8adb5604c
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReferralSystem:
    """
    A class to represent a referral system with a commission structure.
    The system allows users to refer others and earn a 10% commission on their referrals' earnings.
    """

    def __init__(self):
        """
        Initializes the ReferralSystem with an empty dictionary to store users and their referrals.
        """
        self.users = {}  # Dictionary to store user data
        self.referrals = {}  # Dictionary to store referral data

    def add_user(self, user_id):
        """
        Adds a new user to the system.

        :param user_id: Unique identifier for the user
        :raises ValueError: If the user already exists
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists.")
        self.users[user_id] = {'earnings': 0, 'referrals': []}
        self.referrals[user_id] = 0  # Initialize referral count

    def refer_user(self, referrer_id, new_user_id):
        """
        Allows a user to refer a new user.

        :param referrer_id: The user ID of the referrer
        :param new_user_id: The user ID of the new user being referred
        :raises ValueError: If the referrer does not exist or if the new user already exists
        """
        if referrer_id not in self.users:
            raise ValueError(f"Referrer {referrer_id} does not exist.")
        if new_user_id in self.users:
            raise ValueError(f"User {new_user_id} already exists.")

        self.add_user(new_user_id)  # Add the new user
        self.users[referrer_id]['referrals'].append(new_user_id)  # Add new user to referrer's list
        self.referrals[referrer_id] += 1  # Increment referral count

    def record_earnings(self, user_id, amount):
        """
        Records earnings for a user and calculates commission for the referrer.

        :param user_id: The user ID of the user earning money
        :param amount: The amount earned by the user
        :raises ValueError: If the user does not exist or if the amount is negative
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} does not exist.")
        if amount < 0:
            raise ValueError("Earnings amount cannot be negative.")

        self.users[user_id]['earnings'] += amount  # Update user's earnings

        # Calculate commission for the referrer
        referrer_id = self.get_referrer(user_id)
        if referrer_id:
            commission = amount * 0.10  # 10% commission
            self.users[referrer_id]['earnings'] += commission  # Update referrer's earnings

    def get_referrer(self, user_id):
        """
        Retrieves the referrer of a given user.

        :param user_id: The user ID of the user
        :return: The user ID of the referrer or None if no referrer exists
        """
        for referrer, referrals in self.users.items():
            if user_id in referrals['referrals']:
                return referrer
        return None

    def get_user_info(self, user_id):
        """
        Retrieves information about a user.

        :param user_id: The user ID of the user
        :return: A dictionary containing user information
        :raises ValueError: If the user does not exist
        """
        if user_id not in self.users:
            raise ValueError(f"User {user_id} does not exist.")
        return self.users[user_id]

# Example usage:
if __name__ == "__main__":
    referral_system = ReferralSystem()
    referral_system.add_user("user1")
    referral_system.add_user("user2")
    referral_system.refer_user("user1", "user3")
    referral_system.record_earnings("user3", 100)  # user3 earns $100
    print(referral_system.get_user_info("user1"))  # Check user1's info
    print(referral_system.get_user_info("user3"))  # Check user3's info
```
