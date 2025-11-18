"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Develop a script to extrapolate APR over different time ranges for reward calculation, incorporating both EVM and Solana reward mechanisms.
Generated: DETERMINISTIC_3e2e12f3324fc6e2
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class APRCalculator:
    """
    A class to calculate Annual Percentage Rate (APR) and extrapolate it over different time ranges
    for reward calculation based on Ethereum Virtual Machine (EVM) and Solana reward mechanisms.
    """

    def __init__(self, initial_investment, reward_rate, time_periods):
        """
        Initialize the APRCalculator with required parameters.

        :param initial_investment: float, initial amount of investment
        :param reward_rate: float, reward rate (in decimal form, e.g., 0.05 for 5%)
        :param time_periods: list of int, time periods (in years) to extrapolate APR
        """
        self.initial_investment = initial_investment
        self.reward_rate = reward_rate
        self.time_periods = time_periods

    def calculate_apr(self):
        """
        Calculate the APR based on the reward rate.

        :return: float, calculated APR as a percentage
        """
        return self.reward_rate * 100  # Convert to percentage

    def extrapolate_rewards(self):
        """
        Extrapolate rewards over the specified time periods.

        :return: dict, mapping time period to reward amount
        """
        apr = self.calculate_apr()
        rewards = {}
        for years in self.time_periods:
            try:
                # Calculate the final amount using compound interest formula
                final_amount = self.initial_investment * (1 + self.reward_rate) ** years
                rewards[years] = final_amount - self.initial_investment  # Reward earned
            except Exception as e:
                rewards[years] = f"Error calculating rewards for {years} years: {str(e)}"

        return rewards

def main():
    """
    Main function to execute the APR calculation and reward extrapolation.
    """
    try:
        # Example input parameters
        initial_investment = 1000.0  # Initial investment amount in USD
        reward_rate = 0.05            # 5% reward rate
        time_periods = [1, 2, 3, 5]   # Years to extrapolate rewards

        # Instantiate the APRCalculator
        calculator = APRCalculator(initial_investment, reward_rate, time_periods)

        # Calculate and display the APR
        apr = calculator.calculate_apr()
        print(f"Calculated APR: {apr:.2f}%")

        # Extrapolate rewards and display results
        rewards = calculator.extrapolate_rewards()
        for years, reward in rewards.items():
            print(f"Reward over {years} years: {reward:.2f} USD" if isinstance(reward, float) else reward)

    except Exception as main_exception:
        print(f"An error occurred in the main execution: {str(main_exception)}")

if __name__ == "__main__":
    main()
```
