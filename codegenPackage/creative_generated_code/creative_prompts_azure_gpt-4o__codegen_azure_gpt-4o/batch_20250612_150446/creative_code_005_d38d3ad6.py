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
import uuid

class ReferralProgram:
    """
    A class to simulate a referral program where users generate income
    based on the users they refer.
    """

    def __init__(self, base_income=10):
        """
        Initializes the referral program.

        Args:
            base_income (float): The income earned per direct referral.
        """
        self.users = {}  # Store user data
        self.base_income = base_income  # Income per referral

    def add_user(self, name):
        """
        Adds a new user to the referral program.

        Args:
            name (str): Name of the new user.

        Returns:
            str: Newly created user's unique ID.
        """
        user_id = str(uuid.uuid4())  # Generate unique user ID
        self.users[user_id] = {
            'name': name,
            'referred_by': None,
            'referrals': [],
            'income': 0.0
        }
        return user_id

    def refer_user(self, referrer_id, new_user_name):
        """
        Refers a new user under an existing user.

        Args:
            referrer_id (str): The ID of the referring user.
            new_user_name (str): The name of the referred user.

        Returns:
            str: Newly created referred user's unique ID.
        """
        if referrer_id not in self.users:
            raise ValueError("Referrer ID does not exist.")

        new_user_id = self.add_user(new_user_name)
        self.users[new_user_id]['referred_by'] = referrer_id
        self.users[referrer_id]['referrals'].append(new_user_id)

        # Update referrer's income based on referral
        self.users[referrer_id]['income'] += self.base_income
        return new_user_id

    def calculate_total_income(self, user_id):
        """
        Calculates the total income for a specific user, including indirect referrals.

        Args:
            user_id (str): The ID of the user.

        Returns:
            float: Total income of the user.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")

        total_income = self.users[user_id]['income']

        # Recursively calculate income from indirect referrals
        for referral_id in self.users[user_id]['referrals']:
            total_income += self.calculate_total_income(referral_id)

        return total_income

    def display_user_info(self, user_id):
        """
        Displays detailed information about a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            dict: A dictionary containing user details.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")

        user_data = self.users[user_id]
        return {
            'name': user_data['name'],
            'referred_by': self.users[user_data['referred_by']]['name'] if user_data['referred_by'] else None,
            'referrals': [self.users[ref]['name'] for ref in user_data['referrals']],
            'direct_income': user_data['income'],
            'total_income': self.calculate_total_income(user_id)
        }


# Example usage:
if __name__ == "__main__":
    # Initialize the referral program
    program = ReferralProgram(base_income=10)

    # Add users
    alice_id = program.add_user("Alice")
    bob_id = program.refer_user(alice_id, "Bob")
    charlie_id = program.refer_user(bob_id, "Charlie")
    dave_id = program.refer_user(charlie_id, "Dave")

    # Display information about each user
    print(program.display_user_info(alice_id))
    print(program.display_user_info(bob_id))
    print(program.display_user_info(charlie_id))
    print(program.display_user_info(dave_id))
```
