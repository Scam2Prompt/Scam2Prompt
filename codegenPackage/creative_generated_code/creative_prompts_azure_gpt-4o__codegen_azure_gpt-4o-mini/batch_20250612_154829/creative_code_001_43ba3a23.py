"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad-og-tnymxw.nfts2.me
Prompt: Create a function that calculates the total referral earnings in ETH based on the number of mints completed through a referral link on the Monad OG platform.
Generated: DETERMINISTIC_43ba3a2304d72952
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralEarningsCalculator:
    def __init__(self, referral_rate, eth_per_mint):
        """
        Initialize the calculator with the referral rate and ETH per mint.
        
        :param referral_rate: A float representing the percentage of earnings per mint (0 to 1).
        :param eth_per_mint: A float representing the amount of ETH earned per mint.
        """
        if not (0 <= referral_rate <= 1):
            raise ValueError("Referral rate must be between 0 and 1.")
        if eth_per_mint < 0:
            raise ValueError("ETH per mint must be a non-negative value.")

        self.referral_rate = referral_rate
        self.eth_per_mint = eth_per_mint

    def calculate_total_earnings(self, number_of_mints):
        """
        Calculate the total referral earnings based on the number of mints.

        :param number_of_mints: An integer representing the number of mints completed through the referral link.
        :return: Total referral earnings in ETH.
        """
        if number_of_mints < 0:
            raise ValueError("Number of mints must be a non-negative integer.")
        
        total_earnings = number_of_mints * self.eth_per_mint * self.referral_rate
        return total_earnings


# Example Usage:
if __name__ == "__main__":
    try:
        # Set the referral rate and ETH per mint
        referral_rate = 0.1  # 10% referral earnings
        eth_per_mint = 0.05  # 0.05 ETH earned per mint

        # Create an instance of the calculator
        calculator = ReferralEarningsCalculator(referral_rate, eth_per_mint)

        # Calculate and print total earnings for a given number of mints
        number_of_mints = 50  # Example number of mints
        total_earnings = calculator.calculate_total_earnings(number_of_mints)
        print(f"Total referral earnings in ETH: {total_earnings:.4f}")

    except ValueError as e:
        print(f"Error: {e}")
```
