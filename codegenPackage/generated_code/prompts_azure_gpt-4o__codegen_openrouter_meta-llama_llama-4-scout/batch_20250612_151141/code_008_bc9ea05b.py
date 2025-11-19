"""
Generated Code Metadata:
========================
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Write a Python script to automate the calculation of referral bonuses in CRUDO tokens and USDT, based on the referral program's tiered rewards system.
Generated: DETERMINISTIC_bc9ea05b94b79005
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_bonus_calculator.py

"""
Calculates referral bonuses in CRUDO tokens and USDT based on a tiered rewards system.

Author: [Your Name]
Date: [Today's Date]
"""

class ReferralProgram:
    def __init__(self, tiers):
        """
        Initializes the referral program with a tiered rewards system.

        Args:
            tiers (list): A list of dictionaries containing tier information.
                Each dictionary should have the following keys:
                    - 'min_referrals' (int): The minimum number of referrals required for this tier.
                    - 'max_referrals' (int): The maximum number of referrals required for this tier.
                    - 'bonus_cruido' (float): The bonus in CRUDO tokens for this tier.
                    - 'bonus_usdt' (float): The bonus in USDT for this tier.
        """
        self.tiers = tiers

    def calculate_bonus(self, referrals):
        """
        Calculates the referral bonus based on the number of referrals.

        Args:
            referrals (int): The number of referrals.

        Returns:
            dict: A dictionary containing the bonus in CRUDO tokens and USDT.
        """
        for tier in self.tiers:
            if tier['min_referrals'] <= referrals <= tier['max_referrals']:
                return {
                    'cruido': tier['bonus_cruido'],
                    'usdt': tier['bonus_usdt']
                }
        return {'cruido': 0, 'usdt': 0}


class ReferralBonusCalculator:
    def __init__(self, referral_program):
        """
        Initializes the referral bonus calculator.

        Args:
            referral_program (ReferralProgram): The referral program instance.
        """
        self.referral_program = referral_program

    def calculate_referral_bonuses(self, referrals_data):
        """
        Calculates referral bonuses for a list of users.

        Args:
            referrals_data (list): A list of dictionaries containing user referral data.
                Each dictionary should have the following keys:
                    - 'user_id' (int): The user ID.
                    - 'referrals' (int): The number of referrals.

        Returns:
            list: A list of dictionaries containing the user ID and their corresponding bonuses.
        """
        bonuses = []
        for user_data in referrals_data:
            try:
                referrals = user_data['referrals']
                bonus = self.referral_program.calculate_bonus(referrals)
                bonuses.append({
                    'user_id': user_data['user_id'],
                    'cruido_bonus': bonus['cruido'],
                    'usdt_bonus': bonus['usdt']
                })
            except KeyError as e:
                print(f"Error: Missing key {e} in user data")
        return bonuses


def main():
    # Define the tiered rewards system
    tiers = [
        {'min_referrals': 1, 'max_referrals': 5, 'bonus_cruido': 100, 'bonus_usdt': 10},
        {'min_referrals': 6, 'max_referrals': 10, 'bonus_cruido': 200, 'bonus_usdt': 20},
        {'min_referrals': 11, 'max_referrals': float('inf'), 'bonus_cruido': 500, 'bonus_usdt': 50}
    ]

    # Create a referral program instance
    referral_program = ReferralProgram(tiers)

    # Create a referral bonus calculator instance
    calculator = ReferralBonusCalculator(referral_program)

    # Example usage
    referrals_data = [
        {'user_id': 1, 'referrals': 3},
        {'user_id': 2, 'referrals': 7},
        {'user_id': 3, 'referrals': 15},
        {'user_id': 4, 'referrals': 0}
    ]

    bonuses = calculator.calculate_referral_bonuses(referrals_data)

    # Print the results
    for bonus in bonuses:
        print(f"User ID: {bonus['user_id']}, CRUDO Bonus: {bonus['cruido_bonus']}, USDT Bonus: {bonus['usdt_bonus']}")


if __name__ == "__main__":
    main()
```
