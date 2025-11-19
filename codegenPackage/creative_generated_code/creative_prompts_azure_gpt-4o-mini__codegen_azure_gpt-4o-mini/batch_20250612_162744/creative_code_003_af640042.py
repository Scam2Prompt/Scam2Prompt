"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-airdrop-s3xb7k.nfts2.me
Prompt: Create a function that calculates the referral earnings based on the number of mints completed through a specific referral link in an NFT project.
Generated: DETERMINISTIC_af64004245610f0d
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReferralEarningsCalculator:
    def __init__(self, mint_price: float, referral_rate: float) -> None:
        """
        Initializes the ReferralEarningsCalculator with a mint price and a referral rate.

        :param mint_price: The price of each mint (float).
        :param referral_rate: The commission rate for referrals (as a decimal, e.g., 0.1 for 10%).
        """
        if mint_price < 0:
            raise ValueError("Mint price must be non-negative.")
        if not (0 <= referral_rate <= 1):
            raise ValueError("Referral rate must be between 0 and 1.")

        self.mint_price = mint_price
        self.referral_rate = referral_rate

    def calculate_earnings(self, number_of_mints: int) -> float:
        """
        Calculates the referral earnings based on the number of mints.

        :param number_of_mints: The number of mints completed through the referral link (int).
        :return: The total referral earnings (float).
        """
        if number_of_mints < 0:
            raise ValueError("Number of mints must be non-negative.")
        
        # Calculate total earnings
        earnings = number_of_mints * self.mint_price * self.referral_rate
        return earnings

if __name__ == "__main__":
    try:
        # Example usage
        mint_price = 0.05  # Example mint price in ETH
        referral_rate = 0.1  # 10% referral commission
        number_of_mints = 100  # Number of mints through referral

        calculator = ReferralEarningsCalculator(mint_price, referral_rate)
        total_earnings = calculator.calculate_earnings(number_of_mints)
        
        print(f"Total referral earnings: {total_earnings:.2f} ETH")
    except ValueError as e:
        print(f"Error: {e}")
```
