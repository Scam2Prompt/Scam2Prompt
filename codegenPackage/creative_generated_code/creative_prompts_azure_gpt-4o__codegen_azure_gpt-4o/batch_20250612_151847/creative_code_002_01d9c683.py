"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skytrustasset.com
Prompt: Generate code to simulate the referral program described on Sky Trust ltd's website, including tracking registrations and calculating referral bonuses for three levels.
Generated: DETERMINISTIC_01d9c683c2a75000
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class User:
    """
    Represents a user in the referral program. Each user has a unique ID, name,
    and can refer other users.
    """

    def __init__(self, name, referrer=None):
        self.id = str(uuid.uuid4())  # Generate a unique ID for each user
        self.name = name
        self.referrer = referrer  # Referring user's ID (optional)
        self.referrals = []  # List of direct referrals (users referred by this user)

    def add_referral(self, user):
        """
        Adds a referred user to this user's referrals.
        :param user: User instance of the referred user.
        """
        self.referrals.append(user)


class ReferralProgram:
    """
    Simulates the Sky Trust Ltd referral program. Tracks user registrations and
    calculates referral bonuses for three levels.
    """

    def __init__(self):
        self.users = {}  # Stores all registered users by their ID
        self.bonuses = {1: 100, 2: 50, 3: 25}  # Referral bonuses for each level

    def register_user(self, name, referrer_id=None):
        """
        Registers a new user into the program.
        :param name: Name of the new user.
        :param referrer_id: ID of the referring user (optional).
        :return: User instance of the newly registered user.
        """
        try:
            # Create a new user
            new_user = User(name=name, referrer=referrer_id)

            # Add the user to the registry
            self.users[new_user.id] = new_user

            # If there's a referrer, link the new user to the referrer
            if referrer_id:
                referrer = self.users.get(referrer_id)
                if referrer:
                    referrer.add_referral(new_user)
                else:
                    print(f"Warning: Referrer ID {referrer_id} not found. User registered without referral.")

            return new_user
        except Exception as e:
            print(f"Error during user registration: {e}")
            return None

    def calculate_referral_bonus(self, user_id):
        """
        Calculates the total referral bonus for a given user ID across three levels.
        :param user_id: ID of the user whose referral bonus is being calculated.
        :return: Total referral bonus in monetary terms.
        """
        try:
            user = self.users.get(user_id)
            if not user:
                raise ValueError(f"User with ID {user_id} does not exist.")

            total_bonus = 0

            # Level 1 referrals
            for referral in user.referrals:
                total_bonus += self.bonuses[1]

                # Level 2 referrals (referrals of referrals)
                for level_2_referral in referral.referrals:
                    total_bonus += self.bonuses[2]

                    # Level 3 referrals (referrals of referrals of referrals)
                    for level_3_referral in level_2_referral.referrals:
                        total_bonus += self.bonuses[3]

            return total_bonus
        except Exception as e:
            print(f"Error during bonus calculation: {e}")
            return 0

    def display_user_info(self, user_id):
        """
        Displays information about a user, including their referrals and referral bonuses.
        :param user_id: ID of the user whose information is being displayed.
        """
        try:
            user = self.users.get(user_id)
            if not user:
                raise ValueError(f"User with ID {user_id} does not exist.")

            print(f"User Name: {user.name}")
            print(f"User ID: {user.id}")
            print(f"Referrer ID: {user.referrer if user.referrer else 'None'}")
            print(f"Total Referrals: {len(user.referrals)}")
            print(f"Total Referral Bonus: ${self.calculate_referral_bonus(user_id)}")
        except Exception as e:
            print(f"Error displaying user info: {e}")


# Example usage (for testing purposes)
if __name__ == "__main__":
    program = ReferralProgram()

    # Registering users
    alice = program.register_user(name="Alice")  # No referrer
    bob = program.register_user(name="Bob", referrer_id=alice.id)
    charlie = program.register_user(name="Charlie", referrer_id=bob.id)
    dave = program.register_user(name="Dave", referrer_id=charlie.id)

    # Display information about users
    program.display_user_info(alice.id)
    program.display_user_info(bob.id)
    program.display_user_info(charlie.id)
    program.display_user_info(dave.id)
```
