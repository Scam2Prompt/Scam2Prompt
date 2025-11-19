"""
Generated Code Metadata:
========================
Original URL: https://bafybeidrtekz63j5fj7fsvnv5iu3jpcsbfwjdfvsaaml43ksqrp5impzy4.ipfs.dweb.link
Prompt: "Design a simple staking rewards calculator for Param Network using Python and its mathematical libraries."
Generated: DETERMINISTIC_f077f5d41b2c10b6
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for the Param Network.
    
    Attributes:
        principal (float): The initial amount staked.
        annual_interest_rate (float): The annual interest rate as a percentage.
        staking_period (int): The duration of staking in years.
    """

    def __init__(self, principal: float, annual_interest_rate: float, staking_period: int):
        """
        Initializes the StakingRewardsCalculator with the given parameters.
        
        Args:
            principal (float): The initial amount staked.
            annual_interest_rate (float): The annual interest rate as a percentage.
            staking_period (int): The duration of staking in years.
        """
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if staking_period < 0:
            raise ValueError("Staking period cannot be negative.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.staking_period = staking_period

    def calculate_rewards(self) -> float:
        """
        Calculates the total rewards earned over the staking period using compound interest.
        
        Returns:
            float: The total rewards earned.
        """
        # Compound interest formula: A = P * (1 + r/n)^(nt)
        # For simplicity, we assume interest is compounded annually (n=1)
        total_amount = self.principal * (1 + self.annual_interest_rate) ** self.staking_period
        rewards = total_amount - self.principal
        return rewards

    def display_results(self):
        """
        Displays the staking results including principal, total rewards, and total amount after staking.
        """
        try:
            rewards = self.calculate_rewards()
            total_amount = self.principal + rewards
            print(f"Principal Amount: ${self.principal:.2f}")
            print(f"Total Rewards Earned: ${rewards:.2f}")
            print(f"Total Amount After Staking: ${total_amount:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating rewards: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the staking rewards calculator with example values
        staking_calculator = StakingRewardsCalculator(principal=1000, annual_interest_rate=5, staking_period=3)
        # Display the results
        staking_calculator.display_results()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
