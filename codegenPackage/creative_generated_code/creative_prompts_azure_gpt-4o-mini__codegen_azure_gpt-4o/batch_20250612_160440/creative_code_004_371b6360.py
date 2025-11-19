"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coindoor.trade
Prompt: Illustrate how to implement a referral program in a trading application, inspired by Coindoor's five-level referral income structure.
Generated: DETERMINISTIC_371b63606d7b6b28
Batch ID: 20250612_160440
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
    Implements a five-level referral income structure for a trading application.
    """

    def __init__(self):
        # Initialize data structures to store users and their referrals
        self.users = {}  # Format: {user_id: {'name': str, 'referrals': list, 'level_income': float}}
        self.referral_tree = {}  # Format: {referrer_id: [referred_ids]}
        self.referral_percentages = [0.10, 0.05, 0.03, 0.02, 0.01]  # Level-based income percentages

    def register_user(self, name, referrer_id=None):
        """
        Registers a new user in the program. Optionally links them to a referrer.
        
        :param name: Name of the new user.
        :param referrer_id: ID of the referrer (if any).
        :return: New user's ID.
        """
        # Generate a unique ID for the new user
        user_id = str(uuid.uuid4())
        self.users[user_id] = {'name': name, 'referrals': [], 'level_income': 0.0}

        # Link the user to a referrer if provided
        if referrer_id and referrer_id in self.users:
            self.referral_tree.setdefault(referrer_id, []).append(user_id)

        return user_id

    def distribute_income(self, user_id, trade_amount):
        """
        Distributes referral income up to five levels for a trade made by a user.

        :param user_id: ID of the user who initiated the trade.
        :param trade_amount: Amount of the trade (used to calculate referral income).
        """
        current_referrer = user_id
        for level, percentage in enumerate(self.referral_percentages):
            current_referrer = self.get_referrer(current_referrer)
            if not current_referrer:
                break  # No referrer at this level

            # Calculate referral income for the current level
            income = trade_amount * percentage
            self.users[current_referrer]['level_income'] += income

    def get_referrer(self, user_id):
        """
        Gets the referrer of a given user.

        :param user_id: ID of the user.
        :return: ID of the referrer if exists, otherwise None.
        """
        for referrer, referrals in self.referral_tree.items():
            if user_id in referrals:
                return referrer
        return None

    def get_user_info(self, user_id):
        """
        Retrieves information about a user.

        :param user_id: ID of the user.
        :return: Dictionary containing user info.
        """
        return self.users.get(user_id, None)


# Example Usage:
if __name__ == "__main__":
    # Create an instance of the referral program
    referral_program = ReferralProgram()

    # Register users and create referral hierarchy
    alice_id = referral_program.register_user("Alice")
    bob_id = referral_program.register_user("Bob", referrer_id=alice_id)
    charlie_id = referral_program.register_user("Charlie", referrer_id=bob_id)
    dave_id = referral_program.register_user("Dave", referrer_id=charlie_id)
    eve_id = referral_program.register_user("Eve", referrer_id=dave_id)

    # Simulate a trade and distribute referral income
    referral_program.distribute_income(eve_id, trade_amount=1000)

    # Display user information
    for user_id in [alice_id, bob_id, charlie_id, dave_id, eve_id]:
        print(f"User Info for {referral_program.get_user_info(user_id)['name']}: {referral_program.get_user_info(user_id)}")
```
