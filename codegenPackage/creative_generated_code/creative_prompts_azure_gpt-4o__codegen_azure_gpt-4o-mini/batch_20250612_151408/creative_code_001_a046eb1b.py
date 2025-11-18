"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffer.pages.dev
Prompt: Generate code to calculate staking rewards for Puffer's liquid staking derivative (pufETH) and simulate its yield compounding in a DeFi platform.
Generated: DETERMINISTIC_a046eb1b8a31cb2d
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class StakingRewardsCalculator:
    def __init__(self, initial_investment: float, annual_yield: float, staking_duration: int, compounding_frequency: int):
        """
        Initialize the StakingRewardsCalculator.

        :param initial_investment: The initial amount of pufETH staked.
        :param annual_yield: The annual yield (as a decimal) for staking rewards.
        :param staking_duration: The total duration for staking in years.
        :param compounding_frequency: The number of times compounding occurs per year.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if annual_yield < 0:
            raise ValueError("Annual yield must be non-negative.")
        if staking_duration <= 0:
            raise ValueError("Staking duration must be greater than zero.")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be greater than zero.")

        self.initial_investment = initial_investment
        self.annual_yield = annual_yield
        self.staking_duration = staking_duration
        self.compounding_frequency = compounding_frequency

    def calculate_rewards(self) -> float:
        """
        Calculate the total rewards earned after the staking duration.

        :return: Total amount of pufETH after staking and compounding.
        """
        # Calculate the effective yield per compounding period
        effective_yield = self.annual_yield / self.compounding_frequency
        
        # Calculate total number of compounding periods
        total_periods = self.compounding_frequency * self.staking_duration
        
        # Calculate the final amount using the compound interest formula
        final_amount = self.initial_investment * (1 + effective_yield) ** total_periods
        return final_amount

    def simulate(self):
        """
        Simulate the staking rewards and provide the results.
        """
        try:
            final_amount = self.calculate_rewards()
            rewards_earned = final_amount - self.initial_investment
            
            print(f"Initial Investment: {self.initial_investment:.4f} pufETH")
            print(f"Total Amount after {self.staking_duration} years: {final_amount:.4f} pufETH")
            print(f"Total Rewards Earned: {rewards_earned:.4f} pufETH")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Parameters: initial_investment, annual_yield, staking_duration, compounding_frequency
        staking_calculator = StakingRewardsCalculator(initial_investment=10.0, annual_yield=0.08, staking_duration=5, compounding_frequency=12)
        staking_calculator.simulate()
    except Exception as e:
        print(f"Failed to run staking simulation: {e}")
```
