"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fluff-top.pages.dev
Prompt: Write a Python program to calculate the rewards for staking Seamless (SEAM) and Stablecomp (SCOMP) based on BitMart's APY rates.
Generated: DETERMINISTIC_96cc45da4e6ba822
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for debugging and error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StakingCalculator:
    """
    A class to calculate rewards for staking Seamless (SEAM) and Stablecomp (SCOMP).
    """

    def __init__(self, principal_seam: float, principal_scomp: float, apy_seam: float, apy_scomp: float):
        """
        Initialize the staking calculator with the principal amounts and APY rates.

        :param principal_seam: The amount of SEAM staked.
        :param principal_scomp: The amount of SCOMP staked.
        :param apy_seam: The annual percentage yield for SEAM.
        :param apy_scomp: The annual percentage yield for SCOMP.
        """
        self.principal_seam = principal_seam
        self.principal_scomp = principal_scomp
        self.apy_seam = apy_seam
        self.apy_scomp = apy_scomp

    def calculate_rewards(self, years: float) -> dict:
        """
        Calculate the staking rewards for SEAM and SCOMP over a specified number of years.

        :param years: The number of years for which the rewards are calculated.
        :return: A dictionary containing the rewards for SEAM and SCOMP.
        """
        if years < 0:
            logging.error("Years cannot be negative.")
            raise ValueError("Years must be a non-negative number.")

        seam_rewards = self.principal_seam * (1 + self.apy_seam) ** years - self.principal_seam
        scomp_rewards = self.principal_scomp * (1 + self.apy_scomp) ** years - self.principal_scomp

        return {
            "SEAM Rewards": seam_rewards,
            "SCOMP Rewards": scomp_rewards,
        }

def main():
    """
    Main function to run the staking rewards calculation.
    """
    try:
        # Example inputs
        principal_seam = 1000.0  # Amount of SEAM staked
        principal_scomp = 1500.0  # Amount of SCOMP staked
        apy_seam = 0.12  # 12% APY for SEAM
        apy_scomp = 0.08  # 8% APY for SCOMP
        years = 5  # Calculate rewards for 5 years

        # Initialize the staking calculator
        calculator = StakingCalculator(principal_seam, principal_scomp, apy_seam, apy_scomp)

        # Calculate the rewards
        rewards = calculator.calculate_rewards(years)

        # Display the rewards
        logging.info(f"Rewards after {years} years: {rewards}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
