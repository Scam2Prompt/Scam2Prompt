"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://super-monad-testnet-live.testnet.nfts2.me
Prompt: Create a function that calculates referral earnings based on the number of mints completed through a generated referral link on the Monad Testnet.
Generated: DETERMINISTIC_b3d8096c92adf1ba
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
    A class to calculate referral earnings based on the number of mints completed.
    """

    # Constants for earning rates
    BASE_EARNING_RATE = 0.05  # Base earning rate per mint
    BONUS_THRESHOLD = 100      # Mints threshold for a bonus
    BONUS_RATE = 0.02          # Bonus earning rate per mint above the threshold

    def __init__(self):
        pass

    def calculate_earnings(self, number_of_mints: int) -> float:
        """
        Calculate referral earnings based on the number of mints.

        Parameters:
        number_of_mints (int): The number of mints completed through the referral link.

        Returns:
        float: Total earnings from referrals.

        Raises:
        ValueError: If the number of mints is negative.
        """
        if number_of_mints < 0:
            raise ValueError("The number of mints cannot be negative.")

        # Calculate basic earnings
        earnings = number_of_mints * self.BASE_EARNING_RATE

        # Check if the number of mints exceeds the threshold for bonuses
        if number_of_mints > self.BONUS_THRESHOLD:
            bonus_mints = number_of_mints - self.BONUS_THRESHOLD
            earnings += bonus_mints * self.BONUS_RATE

        return round(earnings, 2)  # Round to two decimal places for currency representation


# Example usage
if __name__ == "__main__":
    calculator = ReferralEarningsCalculator()
    try:
        mints_completed = 150  # Example input for mints completed
        earnings = calculator.calculate_earnings(mints_completed)
        print(f"Referral earnings for {mints_completed} mints: ${earnings}")
    except ValueError as e:
        print(f"Error: {e}")
```
