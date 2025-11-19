"""
Generated Code Metadata:
========================
Original URL: https://unichain-pass.nfts2.me
Prompt: Create a function that calculates referral earnings based on the number of mints completed through a unique referral link for an NFT project.
Generated: DETERMINISTIC_6283f14cddd54fb0
Batch ID: 20250612_162734
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
    through a unique referral link for an NFT project.
    """

    def __init__(self, mint_price: float, referral_bonus: float):
        """
        Initializes the calculator with the mint price and referral bonus.

        :param mint_price: The price of each NFT mint.
        :param referral_bonus: The bonus earned for each mint through a referral.
        """
        if mint_price <= 0:
            raise ValueError("Mint price must be greater than zero.")
        if referral_bonus < 0:
            raise ValueError("Referral bonus cannot be negative.")

        self.mint_price = mint_price
        self.referral_bonus = referral_bonus

    def calculate_earnings(self, number_of_mints: int) -> float:
        """
        Calculates the total referral earnings based on the number of mints.

        :param number_of_mints: The number of mints completed through the referral link.
        :return: The total referral earnings.
        """
        if number_of_mints < 0:
            raise ValueError("Number of mints cannot be negative.")

        total_earnings = number_of_mints * self.referral_bonus
        return total_earnings

    def calculate_total_value(self, number_of_mints: int) -> float:
        """
        Calculates the total value generated from mints including referral earnings.

        :param number_of_mints: The number of mints completed through the referral link.
        :return: The total value generated from mints.
        """
        if number_of_mints < 0:
            raise ValueError("Number of mints cannot be negative.")

        total_value = number_of_mints * self.mint_price + self.calculate_earnings(number_of_mints)
        return total_value


# Example usage:
if __name__ == "__main__":
    try:
        mint_price = 0.05  # Example mint price in ETH
        referral_bonus = 0.01  # Example referral bonus in ETH
        number_of_mints = 10  # Example number of mints

        calculator = ReferralEarningsCalculator(mint_price, referral_bonus)
        earnings = calculator.calculate_earnings(number_of_mints)
        total_value = calculator.calculate_total_value(number_of_mints)

        print(f"Referral Earnings: {earnings} ETH")
        print(f"Total Value Generated: {total_value} ETH")
    except ValueError as e:
        print(f"Error: {e}")
```
