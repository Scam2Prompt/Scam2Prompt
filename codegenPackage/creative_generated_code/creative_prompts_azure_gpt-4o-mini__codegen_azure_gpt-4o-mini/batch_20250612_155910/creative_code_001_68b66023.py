"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-launch.web.app
Prompt: Write a function that calculates potential staking rewards for $STARS holders based on the number of tokens they hold and the dynamic APY during the presale.
Generated: DETERMINISTIC_68b66023121b2488
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardCalculator:
    def __init__(self, apy: float):
        """
        Initialize the StakingRewardCalculator with a given APY (Annual Percentage Yield).
        
        :param apy: The annual percentage yield as a decimal (e.g., 0.05 for 5%).
        """
        if not (0 <= apy <= 1):
            raise ValueError("APY must be between 0 and 1.")
        self.apy = apy

    def calculate_rewards(self, token_amount: float, duration_days: int) -> float:
        """
        Calculate the potential staking rewards for a given amount of tokens over a specified duration.
        
        :param token_amount: The amount of $STARS tokens held (must be non-negative).
        :param duration_days: The duration for which the tokens are staked in days (must be non-negative).
        :return: The calculated rewards based on the provided token amount and duration.
        
        :raises ValueError: If token_amount or duration_days is negative.
        """
        if token_amount < 0:
            raise ValueError("Token amount must be non-negative.")
        if duration_days < 0:
            raise ValueError("Duration in days must be non-negative.")

        # Calculate the rewards using the formula for compound interest
        # Rewards = Token Amount * (1 + APY)^(Duration in Years) - Token Amount
        duration_years = duration_days / 365
        rewards = token_amount * ((1 + self.apy) ** duration_years - 1)
        return rewards

# Example usage
if __name__ == "__main__":
    try:
        apy_value = 0.1  # Example APY of 10%
        token_holding = 1000  # Example holding of 1000 $STARS tokens
        staking_duration = 30  # Staked for 30 days
        
        calculator = StakingRewardCalculator(apy=apy_value)
        reward = calculator.calculate_rewards(token_amount=token_holding, duration_days=staking_duration)
        
        print(f"Potential staking rewards for {token_holding} $STARS over {staking_duration} days: ${reward:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
