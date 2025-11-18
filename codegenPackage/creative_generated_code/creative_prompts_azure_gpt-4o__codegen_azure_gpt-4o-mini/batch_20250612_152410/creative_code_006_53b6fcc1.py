"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://injective-networks.web.app
Prompt: Create a script to calculate and visualize staking rewards over different time periods (e.g., 1 month, 3 months, 1 year) using Injective's APR data.
Generated: DETERMINISTIC_53b6fcc138fd2392
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class StakingRewardsCalculator:
    """
    A class to calculate and visualize staking rewards based on given APR data.
    """

    def __init__(self, apr):
        """
        Initializes the calculator with the given APR.

        :param apr: Annual Percentage Rate as a percentage (e.g., 10 for 10%)
        """
        if not (0 <= apr <= 100):
            raise ValueError("APR must be between 0 and 100.")
        self.apr = apr / 100  # Convert percentage to decimal

    def calculate_rewards(self, principal, time_periods):
        """
        Calculate the staking rewards for specified time periods.

        :param principal: The initial amount staked.
        :param time_periods: A list of time periods in years (e.g., [1/12, 3/12, 1])
        :return: A list of rewards for each time period.
        """
        rewards = []
        for time in time_periods:
            # Calculate the total amount after interest
            total_amount = principal * (1 + self.apr * time)
            rewards.append(total_amount - principal)  # Reward is the difference
        return rewards

    def visualize_rewards(self, time_periods, rewards):
        """
        Generate a bar chart to visualize the staking rewards.

        :param time_periods: A list of time periods in years.
        :param rewards: A list of calculated rewards for each time period.
        """
        plt.figure(figsize=(10, 5))
        plt.bar([f"{int(t * 12)} months" for t in time_periods], rewards, color='skyblue')
        plt.title('Staking Rewards Over Different Time Periods')
        plt.xlabel('Time Period')
        plt.ylabel('Rewards')
        plt.grid(axis='y')
        plt.show()

def main():
    # Example usage of the StakingRewardsCalculator
    try:
        apr = 10  # Example APR of 10%
        principal = 1000  # Example principal amount of $1000
        time_periods = [1/12, 3/12, 1]  # 1 month, 3 months, 1 year

        # Instantiate the calculator
        calculator = StakingRewardsCalculator(apr)

        # Calculate rewards
        rewards = calculator.calculate_rewards(principal, time_periods)

        # Visualize the results
        calculator.visualize_rewards(time_periods, rewards)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
