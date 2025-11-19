"""
Generated Code Metadata:
========================
Original URL: https://monadverse2.testnet.nfts2.me
Prompt: Create a function that calculates referral earnings for a user based on the number of mints completed through their referral link, inspired by Monadverse2's model.
Generated: DETERMINISTIC_e3f6de2315dfd89a
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReferralEarningsCalculator:
    """
    A class to calculate referral earnings based on the number of mints completed
    through a user's referral link.
    """

    def __init__(self, base_earning_per_mint: float, referral_bonus: float):
        """
        Initializes the calculator with the base earning per mint and the referral bonus.

        :param base_earning_per_mint: The amount earned for each mint completed.
        :param referral_bonus: The additional bonus earned for each mint completed through a referral.
        """
        if base_earning_per_mint < 0 or referral_bonus < 0:
            raise ValueError("Earnings and bonuses must be non-negative.")

        self.base_earning_per_mint = base_earning_per_mint
        self.referral_bonus = referral_bonus

    def calculate_earnings(self, mints_completed: int) -> float:
        """
        Calculates the total earnings based on the number of mints completed.

        :param mints_completed: The number of mints completed through the referral link.
        :return: The total earnings from the completed mints.
        """
        if mints_completed < 0:
            raise ValueError("Number of mints completed cannot be negative.")

        # Calculate total earnings
        total_earnings = (self.base_earning_per_mint + self.referral_bonus) * mints_completed
        return total_earnings


def main():
    """
    Main function to demonstrate the usage of the ReferralEarningsCalculator.
    """
    try:
        # Initialize the calculator with example values
        calculator = ReferralEarningsCalculator(base_earning_per_mint=10.0, referral_bonus=2.0)

        # Example: Calculate earnings for 5 mints completed
        mints_completed = 5
        earnings = calculator.calculate_earnings(mints_completed)

        print(f"Earnings for {mints_completed} mints completed: ${earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
