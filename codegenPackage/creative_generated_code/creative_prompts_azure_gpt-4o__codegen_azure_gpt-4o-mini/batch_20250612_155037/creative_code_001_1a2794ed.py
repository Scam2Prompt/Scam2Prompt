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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReferralEarningsCalculator:
    """
    A class to calculate referral earnings based on the number of NFT mints
    completed through a referral link.

    Attributes:
        referral_rate (float): The percentage of earnings per NFT mint.
    """

    def __init__(self, referral_rate: float):
        """
        Initializes the ReferralEarningsCalculator with a referral rate.

        Args:
            referral_rate (float): The percentage of earnings per NFT mint.
        """
        if not (0 <= referral_rate <= 1):
            logging.error("Invalid referral rate: must be between 0 and 1.")
            raise ValueError("Referral rate must be between 0 and 1.")
        self.referral_rate = referral_rate

    def calculate_earnings(self, number_of_mints: int) -> float:
        """
        Calculates the referral earnings based on the number of mints.

        Args:
            number_of_mints (int): The number of NFT mints completed.

        Returns:
            float: The total earnings from referrals.

        Raises:
            ValueError: If the number_of_mints is negative.
        """
        if number_of_mints < 0:
            logging.error("Invalid number of mints: must be non-negative.")
            raise ValueError("Number of mints must be non-negative.")

        earnings = number_of_mints * self.referral_rate
        logging.info(f"Calculated earnings: {earnings} for {number_of_mints} mints.")
        return earnings

def main():
    """
    Main function to run the Referral Earnings Calculation.
    """
    try:
        # Example usage
        referral_rate = 0.05  # 5% earnings per mint
        number_of_mints = 100  # Example number of mints

        # Create an instance of the calculator
        calculator = ReferralEarningsCalculator(referral_rate)

        # Calculate earnings
        earnings = calculator.calculate_earnings(number_of_mints)
        print(f"Total referral earnings: ${earnings:.2f}")

    except ValueError as e:
        logging.exception("An error occurred during referral earnings calculation.")

if __name__ == "__main__":
    main()
```
