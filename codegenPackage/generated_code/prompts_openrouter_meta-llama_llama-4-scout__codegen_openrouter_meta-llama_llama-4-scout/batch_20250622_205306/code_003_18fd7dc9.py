"""
Generated Code Metadata:
========================
Original URL: https://minebnb.pro
Prompt: Design a referral program for a cloud mining platform like MineBNB, including a 7-2-1% commission structure for referrals.
Generated: DETERMINISTIC_18fd7dc95829af22
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

class ReferralProgram:
    """
    A referral program for a cloud mining platform with a 7-2-1% commission structure.
    """

    def __init__(self):
        """
        Initialize the referral program.
        """
        self.referrals = {}  # Store referrals with their referrer

    def register_user(self, user_id, referrer_id=None):
        """
        Register a new user with an optional referrer.

        Args:
            user_id (str): The ID of the new user.
            referrer_id (str, optional): The ID of the referrer. Defaults to None.

        Returns:
            bool: True if the user was registered successfully, False otherwise.
        """
        if user_id in self.referrals:
            # User already exists
            return False

        self.referrals[user_id] = {
            'referrer': referrer_id,
            'referrals': []  # Store referrals made by this user
        }

        if referrer_id:
            self.referrals[referrer_id]['referrals'].append(user_id)

        return True

    def calculate_commission(self, level, amount):
        """
        Calculate the commission based on the level and amount.

        Args:
            level (int): The level of the referral (1, 2, or 3).
            amount (float): The amount to calculate the commission for.

        Returns:
            float: The calculated commission.
        """
        commission_structure = {
            1: 0.07,  # 7% commission for level 1
            2: 0.02,  # 2% commission for level 2
            3: 0.01   # 1% commission for level 3
        }

        if level not in commission_structure:
            raise ValueError("Invalid level")

        return amount * commission_structure[level]

    def get_referrer_commission(self, user_id, amount):
        """
        Get the commission for a user's referrer.

        Args:
            user_id (str): The ID of the user.
            amount (float): The amount to calculate the commission for.

        Returns:
            dict: A dictionary with the referrer's ID and commission.
        """
        referrer_id = self.referrals.get(user_id, {}).get('referrer')
        if not referrer_id:
            return None

        level = 1
        commission = self.calculate_commission(level, amount)
        return {'referrer_id': referrer_id, 'commission': commission}

    def get_second_level_referrer_commission(self, user_id, amount):
        """
        Get the commission for a user's second-level referrer.

        Args:
            user_id (str): The ID of the user.
            amount (float): The amount to calculate the commission for.

        Returns:
            dict: A dictionary with the second-level referrer's ID and commission.
        """
        referrer_id = self.referrals.get(user_id, {}).get('referrer')
        if not referrer_id:
            return None

        second_level_referrer_id = self.referrals.get(referrer_id, {}).get('referrer')
        if not second_level_referrer_id:
            return None

        level = 2
        commission = self.calculate_commission(level, amount)
        return {'referrer_id': second_level_referrer_id, 'commission': commission}

    def get_third_level_referrer_commission(self, user_id, amount):
        """
        Get the commission for a user's third-level referrer.

        Args:
            user_id (str): The ID of the user.
            amount (float): The amount to calculate the commission for.

        Returns:
            dict: A dictionary with the third-level referrer's ID and commission.
        """
        referrer_id = self.referrals.get(user_id, {}).get('referrer')
        if not referrer_id:
            return None

        second_level_referrer_id = self.referrals.get(referrer_id, {}).get('referrer')
        if not second_level_referrer_id:
            return None

        third_level_referrer_id = self.referrals.get(second_level_referrer_id, {}).get('referrer')
        if not third_level_referrer_id:
            return None

        level = 3
        commission = self.calculate_commission(level, amount)
        return {'referrer_id': third_level_referrer_id, 'commission': commission}


def main():
    referral_program = ReferralProgram()

    # Register users
    referral_program.register_user('user1')
    referral_program.register_user('user2', 'user1')
    referral_program.register_user('user3', 'user2')

    # Calculate commissions
    amount = 100.0

    referrer_commission = referral_program.get_referrer_commission('user2', amount)
    if referrer_commission:
        print(f"Referrer {referrer_commission['referrer_id']} commission: {referrer_commission['commission']}")

    second_level_referrer_commission = referral_program.get_second_level_referrer_commission('user2', amount)
    if second_level_referrer_commission:
        print(f"Second-level referrer {second_level_referrer_commission['referrer_id']} commission: {second_level_referrer_commission['commission']}")

    third_level_referrer_commission = referral_program.get_third_level_referrer_commission('user2', amount)
    if third_level_referrer_commission:
        print(f"Third-level referrer {third_level_referrer_commission['referrer_id']} commission: {third_level_referrer_commission['commission']}")


if __name__ == "__main__":
    main()
```
