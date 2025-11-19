"""
Generated Code Metadata:
========================
Original URL: https://kings-tradefx.com
Prompt: Provide a Python implementation for a referral bonus system in a forex trading platform, similar to the one offered by KINGSTRADE FX during account registration.
Generated: DETERMINISTIC_bd51924d1f78409c
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_bonus_system.py

class ReferralBonusSystem:
    """
    A referral bonus system for a forex trading platform.

    Attributes:
        referral_program (dict): A dictionary containing referral program details.
        users (dict): A dictionary of registered users with their account balances.
    """

    def __init__(self):
        # Initialize referral program details
        self.referral_program = {
            'referrer_bonus': 100,  # bonus for referrer in USD
            'referee_bonus': 50,   # bonus for referee in USD
            'min_deposit': 1000,   # minimum deposit required for referee to be eligible for bonus
            'max_referrals': 10    # maximum number of referrals allowed per referrer
        }

        # Initialize users dictionary
        self.users = {}

    def register_user(self, user_id, referrer_id=None):
        """
        Register a new user.

        Args:
            user_id (str): Unique ID of the user.
            referrer_id (str, optional): ID of the referrer. Defaults to None.

        Returns:
            bool: True if registration is successful, False otherwise.
        """
        if user_id in self.users:
            print(f"User {user_id} already exists.")
            return False

        # Initialize user account balance
        self.users[user_id] = {'balance': 0, 'referrer_id': referrer_id, 'referrals': 0}

        # If referrer ID is provided, update referrer's referrals count
        if referrer_id:
            if referrer_id not in self.users:
                print(f"Referrer {referrer_id} not found.")
                return False
            self.users[referrer_id]['referrals'] += 1

            # Check if referrer has exceeded maximum referrals
            if self.users[referrer_id]['referrals'] > self.referral_program['max_referrals']:
                print(f"Referrer {referrer_id} has exceeded maximum referrals.")
                return False

        print(f"User {user_id} registered successfully.")
        return True

    def deposit(self, user_id, amount):
        """
        Deposit funds into a user's account.

        Args:
            user_id (str): Unique ID of the user.
            amount (float): Deposit amount.

        Returns:
            bool: True if deposit is successful, False otherwise.
        """
        if user_id not in self.users:
            print(f"User {user_id} not found.")
            return False

        # Update user's account balance
        self.users[user_id]['balance'] += amount

        # Check if user is eligible for referral bonus
        if self.users[user_id]['referrer_id'] and amount >= self.referral_program['min_deposit']:
            self.award_referral_bonus(user_id)

        print(f"Deposit successful. New balance: {self.users[user_id]['balance']}")
        return True

    def award_referral_bonus(self, user_id):
        """
        Award referral bonus to referrer and referee.

        Args:
            user_id (str): Unique ID of the user.
        """
        referrer_id = self.users[user_id]['referrer_id']

        # Award bonus to referrer
        self.users[referrer_id]['balance'] += self.referral_program['referrer_bonus']
        print(f"Referrer {referrer_id} awarded ${self.referral_program['referrer_bonus']} bonus.")

        # Award bonus to referee
        self.users[user_id]['balance'] += self.referral_program['referee_bonus']
        print(f"Referee {user_id} awarded ${self.referral_program['referee_bonus']} bonus.")


def main():
    referral_system = ReferralBonusSystem()

    # Register users
    referral_system.register_user('user1')
    referral_system.register_user('user2', 'user1')

    # Deposit funds
    referral_system.deposit('user2', 1000)


if __name__ == '__main__':
    main()
```
