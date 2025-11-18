"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafkreibeiglm45azw6myhsirtwvfq6qpbsfqnnjq2sf32tpnfhjutzndmu.ipfs.dweb.link
Prompt: Provide code to calculate the estimated rewards for staking AEVO tokens at 17.81% APR over a specified time period.
Generated: DETERMINISTIC_74edb64d0807d707
Batch ID: 20250612_152249
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
    A class to calculate estimated rewards for staking AEVO tokens.
    """

    def __init__(self, apr: float):
        """
        Initializes the StakingCalculator with the given annual percentage rate (APR).

        :param apr: Annual Percentage Rate (in percentage) for staking rewards.
        """
        if apr < 0:
            raise ValueError("APR must be a non-negative value.")
        self.apr = apr / 100  # Convert percentage to decimal

    def calculate_rewards(self, principal: float, time_years: float) -> float:
        """
        Calculates the estimated rewards for the given principal amount over the specified time period.

        :param principal: The amount of AEVO tokens staked.
        :param time_years: The time period (in years) for which the tokens are staked.
        :return: Estimated rewards from staking.
        """
        if principal < 0:
            raise ValueError("Principal amount must be a non-negative value.")
        if time_years < 0:
            raise ValueError("Time period must be a non-negative value.")

        # Calculate rewards using the formula: Rewards = Principal * APR * Time
        rewards = principal * self.apr * time_years
        return rewards

def main():
    """
    Main function to execute the staking rewards calculation.
    """
    try:
        apr = 17.81  # Annual Percentage Rate for AEVO tokens
        principal = float(input("Enter the amount of AEVO tokens to stake: "))
        time_years = float(input("Enter the time period in years: "))

        # Create a StakingCalculator instance
        staking_calculator = StakingCalculator(apr)
        
        # Calculate estimated rewards
        estimated_rewards = staking_calculator.calculate_rewards(principal, time_years)

        print(f"Estimated rewards for staking {principal} AEVO tokens over {time_years} years: {estimated_rewards:.2f} AEVO tokens")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
