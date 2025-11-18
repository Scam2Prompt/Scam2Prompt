"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xyo-sushi.lat
Prompt: Write a tutorial-style Python code snippet to calculate the expected rewards from staking USDT in SushiSwap's staking pool based on the provided APY.
Generated: DETERMINISTIC_41597bce6052e70b
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

class StakingCalculator:
    """
    A class to calculate expected rewards from staking USDT in a SushiSwap staking pool.
    """

    def __init__(self, initial_investment: float, apy: float, duration_years: float):
        """
        Initializes the StakingCalculator with investment details.

        :param initial_investment: The amount of USDT to stake.
        :param apy: Annual Percentage Yield (APY) as a percentage (e.g., 12 for 12%).
        :param duration_years: The duration for which to calculate rewards, in years.
        """
        self.initial_investment = decimal.Decimal(initial_investment)
        self.apy = decimal.Decimal(apy) / decimal.Decimal(100)  # Convert APY to decimal
        self.duration_years = decimal.Decimal(duration_years)

    def calculate_expected_rewards(self) -> decimal.Decimal:
        """
        Calculates the expected rewards from staking.

        :return: Expected rewards as a decimal value.
        """
        try:
            # Compound interest formula: A = P * (1 + r/n)^(nt)
            # For simplicity, we assume compounding happens once a year (n=1)
            rewards = self.initial_investment * (1 + self.apy) ** self.duration_years - self.initial_investment
            return rewards
        except Exception as e:
            print(f"An error occurred while calculating expected rewards: {e}")
            return decimal.Decimal(0)

def main():
    """
    Main function to run the staking rewards calculation.
    """
    try:
        # Input values (these can be modified as needed)
        initial_investment = float(input("Enter the initial investment in USDT: "))
        apy = float(input("Enter the APY (in percentage): "))
        duration_years = float(input("Enter the duration in years: "))

        # Create an instance of the StakingCalculator
        calculator = StakingCalculator(initial_investment, apy, duration_years)

        # Calculate expected rewards
        expected_rewards = calculator.calculate_expected_rewards()

        # Display the result
        print(f"Expected rewards from staking {initial_investment} USDT over {duration_years} years at an APY of {apy}%: {expected_rewards:.2f} USDT")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
