"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoin-presale.pages.dev
Prompt: Generate a function to calculate the staking rewards for the 99Bitcoins token based on the dynamic rate provided.
Generated: DETERMINISTIC_d0e3e619b86fcdb5
Batch ID: 20250612_164319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardCalculator:
    """
    A class to calculate staking rewards for the 99Bitcoins token based on a dynamic rate.
    """

    def __init__(self, staked_amount: float, annual_rate: float):
        """
        Initialize the staking reward calculator.

        :param staked_amount: The amount of tokens staked.
        :param annual_rate: The annual reward rate as a percentage (e.g., 5 for 5%).
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than zero.")
        if annual_rate < 0:
            raise ValueError("Annual rate cannot be negative.")

        self.staked_amount = staked_amount
        self.annual_rate = annual_rate / 100  # Convert percentage to decimal

    def calculate_rewards(self, staking_period_in_years: float) -> float:
        """
        Calculate the staking rewards over a given period.

        :param staking_period_in_years: The period over which rewards are calculated in years.
        :return: The total rewards earned over the staking period.
        :raises ValueError: If the staking period is less than or equal to zero.
        """
        if staking_period_in_years <= 0:
            raise ValueError("Staking period must be greater than zero.")

        # Calculate rewards based on compound interest formula
        total_rewards = self.staked_amount * (1 + self.annual_rate) ** staking_period_in_years - self.staked_amount
        return round(total_rewards, 2)  # Round to two decimal places for currency representation


# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of StakingRewardCalculator
        calculator = StakingRewardCalculator(staked_amount=1000, annual_rate=5)

        # Calculate rewards for a staking period of 2 years
        rewards = calculator.calculate_rewards(staking_period_in_years=2)
        
        print(f"Total rewards earned over 2 years: {rewards} tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
