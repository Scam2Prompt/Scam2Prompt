"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaclaim.pages.dev
Prompt: Write a program to calculate the estimated earnings from staking MZERO tokens over a specified period using the provided APR.
Generated: DETERMINISTIC_567f197c03422f08
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    """
    A class to calculate estimated earnings from staking MZERO tokens.
    """

    def __init__(self, initial_investment: float, apr: float, staking_duration_months: int):
        """
        Initializes the StakingCalculator instance.

        :param initial_investment: The initial amount of MZERO tokens staked (in tokens).
        :param apr: The annual percentage rate (APR) as a decimal (e.g., 0.05 for 5%).
        :param staking_duration_months: The duration for which the tokens are staked (in months).
        """
        self.initial_investment = initial_investment
        self.apr = apr
        self.staking_duration_months = staking_duration_months

    def calculate_estimated_earnings(self) -> float:
        """
        Calculates the estimated earnings from staking MZERO tokens.

        :return: The estimated earnings (in tokens) after the staking duration.
        """
        # Ensure valid input
        if self.initial_investment < 0:
            raise ValueError("Initial investment cannot be negative.")
        if not (0 <= self.apr <= 1):
            raise ValueError("APR must be between 0 and 1.")
        if self.staking_duration_months < 0:
            raise ValueError("Staking duration cannot be negative.")

        # Calculate the monthly interest rate from the APR
        monthly_rate = self.apr / 12

        # Calculate the estimated earnings after the specified duration
        estimated_earnings = self.initial_investment * ((1 + monthly_rate) ** self.staking_duration_months - 1)

        return estimated_earnings

def main():
    """
    Main function to execute the staking calculator.
    """
    try:
        # User inputs
        initial_investment = float(input("Enter the amount of MZERO tokens to stake: "))
        apr = float(input("Enter the Annual Percentage Rate (APR) as a decimal (e.g., 0.05 for 5%): "))
        staking_duration_months = int(input("Enter the staking duration in months: "))

        # Create an instance of the StakingCalculator
        staking_calculator = StakingCalculator(initial_investment, apr, staking_duration_months)

        # Calculate and display estimated earnings
        estimated_earnings = staking_calculator.calculate_estimated_earnings()
        print(f"Estimated earnings after {staking_duration_months} months: {estimated_earnings:.2f} MZERO tokens")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
