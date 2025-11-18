"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombat-api.pages.dev
Prompt: Create a function to calculate potential rewards from staking $MK tokens on the Meme Kombat platform, factoring in the current APY rate.
Generated: DETERMINISTIC_ea7db89030c3f0c2
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    def __init__(self, apy: float):
        """
        Initialize the StakingCalculator with the given annual percentage yield (APY).

        :param apy: The annual percentage yield as a decimal (e.g., 0.05 for 5%).
        """
        if apy < 0:
            raise ValueError("APY must be a non-negative value.")
        self.apy = apy

    def calculate_rewards(self, amount: float, duration_days: int) -> float:
        """
        Calculate the potential rewards from staking $MK tokens.

        :param amount: The amount of $MK tokens staked.
        :param duration_days: The duration in days for which the tokens are staked.
        :return: The calculated rewards in $MK tokens.
        :raises ValueError: If amount is negative or duration_days is negative.
        """
        if amount < 0:
            raise ValueError("Staked amount must be a non-negative value.")
        if duration_days < 0:
            raise ValueError("Staking duration must be a non-negative value.")

        # Calculate the daily APY
        daily_apy = self.apy / 365

        # Calculate rewards based on the formula: rewards = amount * daily_apy * duration_days
        rewards = amount * daily_apy * duration_days
        return rewards

# Example usage
if __name__ == "__main__":
    try:
        apy_rate = 0.05  # Example APY of 5%
        staking_amount = 1000  # Example amount of $MK tokens
        staking_duration = 30  # Duration of staking in days

        calculator = StakingCalculator(apy_rate)
        potential_rewards = calculator.calculate_rewards(staking_amount, staking_duration)

        print(f"Potential rewards from staking ${staking_amount} MK tokens for {staking_duration} days: ${potential_rewards:.2f} MK")
    except ValueError as e:
        print(f"Error: {e}")
```
