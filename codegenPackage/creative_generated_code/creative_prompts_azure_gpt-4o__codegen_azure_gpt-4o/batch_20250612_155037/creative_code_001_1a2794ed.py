"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadverse2.testnet.nfts2.me
Prompt: Create a script that calculates referral earnings based on the number of NFT mints completed through a referral link on Monadverse2.
Generated: DETERMINISTIC_1a2794ed00112d8e
Batch ID: 20250612_155037
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture errors and information.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReferralEarningsCalculator:
    """
    Class to calculate referral earnings for NFT mints completed through referral links.
    """

    def __init__(self, mint_price, referral_percentage):
        """
        Initialize the calculator with mint price and referral percentage.
        
        :param mint_price: The price of a single NFT mint.
        :param referral_percentage: The percentage of mint price awarded to the referrer.
        """
        if mint_price <= 0:
            raise ValueError("Mint price must be greater than zero.")
        if not (0 <= referral_percentage <= 100):
            raise ValueError("Referral percentage must be between 0 and 100.")
        
        self.mint_price = mint_price
        self.referral_percentage = referral_percentage

    def calculate_earnings(self, referral_data):
        """
        Calculate total referral earnings based on the number of mints for each referrer.
        
        :param referral_data: A dictionary where keys are referrer IDs and values are the number of mints.
        :return: A dictionary with referrer IDs as keys and their total earnings as values.
        """
        if not isinstance(referral_data, dict):
            raise TypeError("Referral data must be a dictionary.")
        
        earnings = {}
        for referrer, mints in referral_data.items():
            if not isinstance(mints, int) or mints < 0:
                logging.error(f"Invalid mint count for referrer '{referrer}'. Skipping calculation.")
                continue

            # Calculate earnings for the referrer.
            earnings[referrer] = mints * self.mint_price * (self.referral_percentage / 100)
            logging.info(f"Calculated earnings for referrer '{referrer}': {earnings[referrer]:.2f}")
        
        return earnings


def main():
    """
    Main function to demonstrate the referral earnings calculation.
    """
    try:
        # Parameters for NFT mint price and referral percentage.
        mint_price = 50.0  # Assume each NFT mint costs $50.00
        referral_percentage = 10  # Assume referrers earn 10% of mint price.

        # Example referral data where keys are referrer IDs and values are the number of mints.
        referral_data = {
            "referrer_1": 15,
            "referrer_2": 30,
            "referrer_3": -10,  # Invalid
            "referrer_4": 22,
        }

        # Initialize the calculator.
        calculator = ReferralEarningsCalculator(mint_price, referral_percentage)

        # Calculate earnings based on referral data.
        earnings = calculator.calculate_earnings(referral_data)

        # Print the referral earnings.
        print("Referral Earnings:")
        for referrer, amount in earnings.items():
            print(f"{referrer}: ${amount:.2f}")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
