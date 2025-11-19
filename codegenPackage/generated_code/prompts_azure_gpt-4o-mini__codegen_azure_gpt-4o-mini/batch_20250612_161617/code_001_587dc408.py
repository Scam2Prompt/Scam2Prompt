"""
Generated Code Metadata:
========================
Original URL: https://doge-coin20.pages.dev
Prompt: Write a code snippet to calculate potential rewards for staking DOGE20 tokens based on the fixed supply and staking pool distribution.
Generated: DETERMINISTIC_587dc40890491941
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingRewardsCalculator:
    """
    A class to calculate potential rewards for staking DOGE20 tokens.
    """

    def __init__(self, total_supply: float, staking_pool: float, reward_rate: float):
        """
        Initializes the StakingRewardsCalculator with the total supply, staking pool, and reward rate.

        :param total_supply: Total supply of DOGE20 tokens.
        :param staking_pool: Total amount of DOGE20 tokens in the staking pool.
        :param reward_rate: Annual reward rate as a decimal (e.g., 0.05 for 5%).
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if staking_pool < 0:
            raise ValueError("Staking pool cannot be negative.")
        if not (0 <= reward_rate <= 1):
            raise ValueError("Reward rate must be between 0 and 1.")

        self.total_supply = total_supply
        self.staking_pool = staking_pool
        self.reward_rate = reward_rate

    def calculate_rewards(self, staked_amount: float, duration_years: float) -> float:
        """
        Calculates the potential rewards for a given staked amount over a specified duration.

        :param staked_amount: Amount of DOGE20 tokens staked.
        :param duration_years: Duration in years for which the tokens are staked.
        :return: Potential rewards earned.
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than zero.")
        if duration_years < 0:
            raise ValueError("Duration must be non-negative.")

        # Calculate the proportion of staked tokens to the staking pool
        proportion_staked = staked_amount / self.staking_pool

        # Calculate potential rewards based on the reward rate and duration
        potential_rewards = proportion_staked * self.total_supply * self.reward_rate * duration_years

        return potential_rewards

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with example values
        calculator = StakingRewardsCalculator(total_supply=1_000_000, staking_pool=100_000, reward_rate=0.05)

        # Calculate rewards for a specific staked amount and duration
        staked_amount = 10_000  # Amount of DOGE20 tokens staked
        duration_years = 1      # Duration in years

        rewards = calculator.calculate_rewards(staked_amount, duration_years)
        print(f"Potential rewards for staking {staked_amount} DOGE20 tokens for {duration_years} year(s): {rewards:.2f} DOGE20")
    
    except ValueError as e:
        print(f"Error: {e}")
```
