"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheaidapp.pages.dev
Prompt: Create a Python script to simulate staking rewards distribution for $SCOTTY tokens over a 3-year period, factoring in the dynamic rewards rate and pool percentage.
Generated: DETERMINISTIC_eabf999ace3865d7
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta

class StakingPool:
    def __init__(self, initial_stake: float, annual_reward_rate: float, pool_percentage: float):
        """
        Initialize the StakingPool with initial stake, annual reward rate, and pool percentage.

        :param initial_stake: Initial amount of $SCOTTY tokens staked.
        :param annual_reward_rate: Annual reward rate as a percentage (e.g., 5 for 5%).
        :param pool_percentage: Percentage of the total rewards distributed to this pool (0 to 1).
        """
        self.initial_stake = initial_stake
        self.annual_reward_rate = annual_reward_rate / 100  # Convert percentage to decimal
        self.pool_percentage = pool_percentage
        self.total_rewards = 0

    def calculate_rewards(self, years: int) -> float:
        """
        Calculate the total rewards earned over a specified number of years.

        :param years: Number of years to simulate staking rewards.
        :return: Total rewards earned.
        """
        rewards = 0
        for year in range(1, years + 1):
            # Simulate a dynamic reward rate for each year (for demonstration purposes)
            dynamic_rate = self.annual_reward_rate * (0.8 + random.uniform(0, 0.4))  # 80% to 120% of the base rate
            yearly_reward = self.initial_stake * dynamic_rate * self.pool_percentage
            rewards += yearly_reward
            self.total_rewards += yearly_reward
            print(f"Year {year}: Reward Rate: {dynamic_rate*100:.2f}%, Yearly Rewards: {yearly_reward:.2f}")

        return rewards

    def get_total_rewards(self) -> float:
        """
        Retrieve the total rewards accumulated.

        :return: Total rewards.
        """
        return self.total_rewards

def simulate_staking():
    """
    Simulate a staking rewards distribution scenario.
    """
    try:
        # Simulation parameters
        initial_stake = 1000.0  # Initial stake in $SCOTTY tokens
        annual_reward_rate = 5.0  # Annual reward rate in percentage
        pool_percentage = 0.2  # 20% of total rewards distributed to this pool
        years = 3  # Simulation duration in years

        # Initialize the staking pool
        staking_pool = StakingPool(initial_stake, annual_reward_rate, pool_percentage)

        # Calculate rewards over the specified duration
        total_rewards = staking_pool.calculate_rewards(years)

        # Output the total rewards
        print(f"\nTotal Rewards over {years} years: {total_rewards:.2f} $SCOTTY tokens")

    except Exception as e:
        print(f"An error occurred during simulation: {e}")

if __name__ == "__main__":
    simulate_staking()
```
