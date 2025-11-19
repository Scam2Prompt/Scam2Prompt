"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify-cs6.pages.dev
Prompt: Create a function to calculate potential earnings from staking $SFUND on Seedify.
Generated: DETERMINISTIC_45b6d1940487c79f
Batch ID: 20250612_160656
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
    A class to encapsulate the staking earnings calculation for $SFUND on Seedify.
    """

    def __init__(self, staked_amount: float, annual_yield: float, staking_period: int):
        """
        Initializes the StakingCalculator with the parameters needed for calculation.
        
        :param staked_amount: The amount of $SFUND staked (in USD).
        :param annual_yield: The annual yield percentage for the staking (as a decimal, e.g., 0.12 for 12%).
        :param staking_period: The period for which the amount is staked (in days).
        """
        if staked_amount < 0:
            raise ValueError("Staked amount must be non-negative.")
        if not (0 <= annual_yield <= 1):
            raise ValueError("Annual yield must be between 0 and 1.")
        if staking_period <= 0:
            raise ValueError("Staking period must be a positive integer.")

        self.staked_amount = staked_amount
        self.annual_yield = annual_yield
        self.staking_period = staking_period

    def calculate_earnings(self) -> float:
        """
        Calculates the potential earnings from staking based on the given parameters.

        :return: The potential earnings (in USD) after the staking period.
        """
        # Calculate the daily yield
        daily_yield = self.annual_yield / 365
        # Calculate earnings
        earnings = self.staked_amount * daily_yield * self.staking_period
        return earnings

    def display_earnings(self):
        """
        Displays the potential earnings in a formatted manner.
        """
        try:
            earnings = self.calculate_earnings()
            print(f"Potential earnings from staking ${self.staked_amount:.2f} "
                  f"at an annual yield of {self.annual_yield * 100:.2f}% "
                  f"for {self.staking_period} days is: ${earnings:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating earnings: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of StakingCalculator with example parameters
        staking_calculator = StakingCalculator(staked_amount=1000, annual_yield=0.12, staking_period=30)
        # Display the potential earnings
        staking_calculator.display_earnings()
    except Exception as e:
        print(f"An error occurred during initialization: {e}")
```
