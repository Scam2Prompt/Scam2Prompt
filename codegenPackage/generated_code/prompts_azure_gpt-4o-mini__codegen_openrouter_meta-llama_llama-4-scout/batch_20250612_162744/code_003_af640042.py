"""
Generated Code Metadata:
========================
Original URL: https://scroll-airdrop-s3xb7k.nfts2.me
Prompt: Create a function that calculates the referral earnings based on the number of mints completed through a specific referral link in an NFT project.
Generated: DETERMINISTIC_af64004245610f0d
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

class ReferralEarningsCalculator:
    """
    Calculates referral earnings based on the number of mints completed through a specific referral link in an NFT project.
    """

    def __init__(self, referral_rates: Dict[int, float], base_earnings: float):
        """
        Initializes the ReferralEarningsCalculator.

        Args:
        - referral_rates (Dict[int, float]): A dictionary of mint counts to earnings rates.
        - base_earnings (float): The base earnings for a single mint.
        """
        self.referral_rates = referral_rates
        self.base_earnings = base_earnings

    def calculate_earnings(self, mints: int) -> float:
        """
        Calculates the referral earnings based on the number of mints.

        Args:
        - mints (int): The number of mints completed through the referral link.

        Returns:
        - float: The referral earnings.

        Raises:
        - ValueError: If the number of mints is negative.
        """
        if mints < 0:
            raise ValueError("Number of mints cannot be negative")

        # Find the highest mint count rate that doesn't exceed the number of mints
        rate_tier = max((tier for tier in self.referral_rates if tier <= mints), default=None)

        if rate_tier is None:
            # If no rate tier is found, use the base earnings
            earnings = mints * self.base_earnings
        else:
            # Calculate earnings based on the referral rate
            earnings = mints * self.referral_rates[rate_tier]

        return earnings


def main():
    # Example usage:
    referral_rates = {
        10: 0.1,  # 10% earnings rate for 10 mints
        50: 0.2,  # 20% earnings rate for 50 mints
        100: 0.3  # 30% earnings rate for 100 mints
    }
    base_earnings = 0.05  # 5% base earnings

    calculator = ReferralEarningsCalculator(referral_rates, base_earnings)

    try:
        mints = 75
        earnings = calculator.calculate_earnings(mints)
        print(f"Earnings for {mints} mints: {earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
