"""
Generated Code Metadata:
========================
Original URL: https://coindoor.trade
Prompt: Create a script that integrates a referral program with multi-level income tracking, as described in Coindoor's 5-level referral system.
Generated: DETERMINISTIC_d1df5afb8e3d9be5
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """
    Class representing a user in the referral program.
    Each user can have multiple referrals and track their earnings.
    """
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.referrals = []  # List to store referrals
        self.earnings = 0.0  # Total earnings from referrals

    def add_referral(self, referral):
        """
        Add a referral to the user's list of referrals.
        
        :param referral: User object representing the referred user
        """
        self.referrals.append(referral)

    def calculate_earnings(self, level_income):
        """
        Calculate earnings based on the referral levels.
        
        :param level_income: List of income per level
        """
        for level in range(min(len(self.referrals), len(level_income))):
            self.earnings += len(self.referrals[level]) * level_income[level]

    def __str__(self):
        return f"User({self.user_id}, {self.name}, Earnings: {self.earnings})"


class ReferralSystem:
    """
    Class to manage the referral program and track user earnings.
    """
    def __init__(self):
        self.users = {}  # Dictionary to store users by user_id

    def add_user(self, user):
        """
        Add a user to the referral system.
        
        :param user: User object to be added
        """
        if user.user_id in self.users:
            raise ValueError(f"User ID {user.user_id} already exists.")
        self.users[user.user_id] = user

    def refer_user(self, referrer_id, new_user):
        """
        Handle the referral of a new user by an existing user.
        
        :param referrer_id: ID of the user who is referring
        :param new_user: User object representing the new user
        """
        if referrer_id not in self.users:
            raise ValueError(f"Referrer ID {referrer_id} does not exist.")
        
        referrer = self.users[referrer_id]
        referrer.add_referral(new_user)
        self.add_user(new_user)

    def calculate_all_earnings(self, level_income):
        """
        Calculate earnings for all users in the system.
        
        :param level_income: List of income per level
        """
        for user in self.users.values():
            user.calculate_earnings(level_income)

    def __str__(self):
        return "\n".join(str(user) for user in self.users.values())


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the referral system
        referral_system = ReferralSystem()

        # Create users
        user1 = User(user_id=1, name="Alice")
        user2 = User(user_id=2, name="Bob")
        user3 = User(user_id=3, name="Charlie")
        user4 = User(user_id=4, name="David")
        user5 = User(user_id=5, name="Eve")

        # Add users to the system
        referral_system.add_user(user1)
        referral_system.add_user(user2)
        referral_system.add_user(user3)

        # Refer new users
        referral_system.refer_user(referrer_id=1, new_user=user4)  # Alice refers David
        referral_system.refer_user(referrer_id=1, new_user=user5)  # Alice refers Eve

        # Define income per level (example values)
        level_income = [10, 5, 3, 2, 1]  # Income for levels 1 to 5

        # Calculate earnings for all users
        referral_system.calculate_all_earnings(level_income)

        # Print all users and their earnings
        print(referral_system)

    except ValueError as e:
        print(f"Error: {e}")
```
