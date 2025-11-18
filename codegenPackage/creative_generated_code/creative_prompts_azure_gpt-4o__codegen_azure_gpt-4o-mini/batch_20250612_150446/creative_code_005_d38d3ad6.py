"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brexphil.com
Prompt: Write a script to simulate the referral program described by Brexphil Inc., including income generation based on referred users.
Generated: DETERMINISTIC_d38d3ad632479c44
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """Class to represent a user in the referral program."""
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.referrals = []  # List to hold referred users

    def refer(self, new_user):
        """Refer a new user to this user."""
        self.referrals.append(new_user)

    def get_referral_count(self):
        """Return the number of users referred by this user."""
        return len(self.referrals)


class ReferralProgram:
    """Class to manage the referral program."""

    def __init__(self, referral_bonus=10.0):
        self.users = {}  # Store users by user_id
        self.referral_bonus = referral_bonus  # Bonus amount for each referral

    def add_user(self, user):
        """Add a new user to the program."""
        if user.user_id in self.users:
            raise ValueError(f"User with ID {user.user_id} already exists.")
        self.users[user.user_id] = user

    def refer_user(self, referrer_id, new_user_id):
        """Allow a user to refer a new user."""
        if referrer_id not in self.users:
            raise ValueError(f"Referrer with ID {referrer_id} does not exist.")
        if new_user_id in self.users:
            raise ValueError(f"User with ID {new_user_id} already exists.")

        new_user = User(new_user_id)
        self.users[referrer_id].refer(new_user)
        self.add_user(new_user)

    def calculate_income(self, user_id):
        """Calculate total income generated from referrals for a specific user."""
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")

        referred_count = self.users[user_id].get_referral_count()
        total_income = referred_count * self.referral_bonus
        return total_income


def main():
    """Main function to demonstrate the referral program."""
    try:
        program = ReferralProgram(referral_bonus=10.0)

        # Add users
        user1 = User("user1")
        user2 = User("user2")
        user3 = User("user3")

        program.add_user(user1)
        program.add_user(user2)

        # User1 refers User3
        program.refer_user("user1", "user3")

        # Calculate and display income for User1
        income_user1 = program.calculate_income("user1")
        print(f"User1's total income from referrals: ${income_user1}")

        # Trying to refer an existing user to demonstrate error handling
        program.refer_user("user2", "user3")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
