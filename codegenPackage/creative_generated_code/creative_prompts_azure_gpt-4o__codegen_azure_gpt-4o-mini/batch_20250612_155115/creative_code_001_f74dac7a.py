"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walris.testnet.nfts2.me
Prompt: Create a function that calculates the total referral earnings in ETH based on the number of mints completed through a referral link on the Walris Chain Rise Testnet.
Generated: DETERMINISTIC_f74dac7a01b0a233
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralEarningsCalculator:
    """
    A class to calculate total referral earnings in ETH based on the number of mints completed through a referral link.
    """

    ETH_PER_MINT = 0.01  # Example earnings per mint in ETH

    def __init__(self):
        """Initialize the calculator, if needed."""
        pass

    def calculate_total_earnings(self, number_of_mints):
        """
        Calculate total earnings based on the number of mints.

        :param number_of_mints: int - The number of mints completed through the referral link.
        :return: float - Total earnings in ETH.
        :raises ValueError: If the number_of_mints is negative.
        """

        # Validate input
        if not isinstance(number_of_mints, int):
            raise ValueError("Number of mints must be an integer.")
        if number_of_mints < 0:
            raise ValueError("Number of mints cannot be negative.")

        # Calculate total earnings
        total_earnings = number_of_mints * self.ETH_PER_MINT
        return total_earnings


if __name__ == "__main__":
    # Example usage
    try:
        calculator = ReferralEarningsCalculator()
        mints = 50  # Example number of mints
        total_earnings = calculator.calculate_total_earnings(mints)
        print(f"Total referral earnings for {mints} mints: {total_earnings} ETH")
    except ValueError as e:
        print(f"Error calculating earnings: {e}")
```
