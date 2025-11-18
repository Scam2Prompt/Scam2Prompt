"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptominnerfx.com
Prompt: Create a script to simulate referral program earnings based on Cryptominnerfx's referral income structure.
Generated: DETERMINISTIC_0cc7e34e8e785865
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralProgram:
    """
    A class to simulate earnings from a referral program based on Cryptominnerfx's structure.
    """

    def __init__(self, base_earning: float, referral_tiers: dict):
        """
        Initializes the referral program with base earnings and referral tiers.

        :param base_earning: The base earning amount for each referral.
        :param referral_tiers: A dictionary mapping the tier level to percentage of base earning.
        """
        if base_earning < 0:
            raise ValueError("Base earning must be a non-negative value.")
        if not isinstance(referral_tiers, dict) or not all(isinstance(k, int) and k > 0 for k in referral_tiers.keys()):
            raise ValueError("Referral tiers must be a dictionary with positive integer keys.")

        self.base_earning = base_earning
        self.referral_tiers = referral_tiers

    def calculate_earnings(self, referrals: list) -> float:
        """
        Calculates total earnings based on the number of referrals at each tier.

        :param referrals: A list where the index represents the tier level and the value at that index is the count of referrals.
        :return: The total earnings from all referrals.
        """
        if not isinstance(referrals, list) or not all(isinstance(x, int) and x >= 0 for x in referrals):
            raise ValueError("Referrals must be a list of non-negative integers.")

        total_earnings = 0.0

        # Loop through referrals and calculate earnings based on tiers
        for tier_level, count in enumerate(referrals, start=1):
            if tier_level in self.referral_tiers:
                tier_percentage = self.referral_tiers[tier_level]
                earnings_for_tier = count * self.base_earning * (tier_percentage / 100)
                total_earnings += earnings_for_tier

        return total_earnings


def main():
    """
    Main function to simulate the referral program earnings.
    """
    # Example referral structure from Cryptominnerfx
    referral_tiers = {
        1: 10,  # 10% for level 1 referrals
        2: 5,   # 5% for level 2 referrals
        3: 2    # 2% for level 3 referrals
    }

    # Initialize the referral program with a base earning of $100
    try:
        program = ReferralProgram(base_earning=100, referral_tiers=referral_tiers)

        # Simulate referrals (3 level 1, 2 level 2, 1 level 3)
        referrals = [3, 2, 1]

        # Calculate total earnings
        total_earnings = program.calculate_earnings(referrals)

        print(f"Total earnings from referrals: ${total_earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
