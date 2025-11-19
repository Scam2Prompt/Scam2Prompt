"""
Generated Code Metadata:
========================
Original URL: https://crypto4rex360.com
Prompt: Generate a Python script to simulate the referral program earnings described on Crypto 4Rex 360, based on user referrals and their respective investment amounts.
Generated: DETERMINISTIC_43f60e16bfd1907d
Batch ID: 20250612_154542
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
    Simulates the referral program earnings based on user referrals and their respective investment amounts.
    """

    def __init__(self, referral_rate, levels):
        """
        Initializes the referral program with a referral rate and levels.

        Args:
            referral_rate (float): The rate at which referrals earn.
            levels (dict): A dictionary of levels with their corresponding investment multipliers.
        """
        self.referral_rate = referral_rate
        self.levels = levels

    def calculate_earnings(self, referrals):
        """
        Calculates the earnings for a given list of referrals.

        Args:
            referrals (list): A list of dictionaries containing the referral's investment amount and level.

        Returns:
            float: The total earnings for the given referrals.
        """
        total_earnings = 0
        for referral in referrals:
            investment_amount = referral['investment_amount']
            level = referral['level']
            if level in self.levels:
                multiplier = self.levels[level]
                earnings = investment_amount * self.referral_rate * multiplier
                total_earnings += earnings
            else:
                print(f"Warning: Unknown level '{level}' for referral with investment amount {investment_amount}.")
        return total_earnings

    def calculate_direct_referral_earnings(self, direct_referrals):
        """
        Calculates the earnings for direct referrals.

        Args:
            direct_referrals (list): A list of dictionaries containing the direct referral's investment amount.

        Returns:
            float: The total earnings for the direct referrals.
        """
        direct_referral_earnings = 0
        for direct_referral in direct_referrals:
            investment_amount = direct_referral['investment_amount']
            earnings = investment_amount * self.referral_rate
            direct_referral_earnings += earnings
        return direct_referral_earnings


def main():
    # Define the referral program parameters
    referral_rate = 0.1  # 10%
    levels = {
        'starter': 1,
        'premium': 2,
        'pro': 3
    }

    # Create a referral program instance
    program = ReferralProgram(referral_rate, levels)

    # Example referrals
    referrals = [
        {'investment_amount': 1000, 'level': 'starter'},
        {'investment_amount': 5000, 'level': 'premium'},
        {'investment_amount': 10000, 'level': 'pro'},
        {'investment_amount': 2000, 'level': 'unknown'}
    ]

    # Example direct referrals
    direct_referrals = [
        {'investment_amount': 1000},
        {'investment_amount': 500}
    ]

    try:
        # Calculate earnings for referrals
        earnings = program.calculate_earnings(referrals)
        print(f"Total earnings for referrals: ${earnings:.2f}")

        # Calculate earnings for direct referrals
        direct_referral_earnings = program.calculate_direct_referral_earnings(direct_referrals)
        print(f"Total earnings for direct referrals: ${direct_referral_earnings:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
