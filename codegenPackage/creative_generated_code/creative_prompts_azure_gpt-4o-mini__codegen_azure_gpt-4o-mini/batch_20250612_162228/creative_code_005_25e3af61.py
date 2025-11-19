"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-presales.pages.dev
Prompt: Create a function that calculates potential rewards from staking $QUBE tokens based on the current sell tax structure.
Generated: DETERMINISTIC_25e3af61668d5d27
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsCalculator:
    def __init__(self, staking_amount: float, sell_tax_rate: float, reward_rate: float):
        """
        Initialize the StakingRewardsCalculator.

        :param staking_amount: The amount of $QUBE tokens staked.
        :param sell_tax_rate: The current sell tax rate as a decimal (e.g., 0.05 for 5%).
        :param reward_rate: The potential reward rate as a decimal (e.g., 0.10 for 10%).
        """
        self.staking_amount = staking_amount
        self.sell_tax_rate = sell_tax_rate
        self.reward_rate = reward_rate

    def calculate_rewards(self, time_period: int) -> float:
        """
        Calculate the potential rewards from staking $QUBE tokens.

        :param time_period: The time period for which rewards are calculated (in months).
        :return: The total potential rewards in $QUBE tokens.
        :raises ValueError: If any input values are negative or invalid.
        """
        # Validate input parameters
        if self.staking_amount < 0:
            raise ValueError("Staking amount must be non-negative.")
        if not (0 <= self.sell_tax_rate < 1):
            raise ValueError("Sell tax rate must be between 0 and 1.")
        if not (0 <= self.reward_rate < 1):
            raise ValueError("Reward rate must be between 0 and 1.")
        if time_period < 0:
            raise ValueError("Time period must be non-negative.")

        # Calculate potential rewards before tax deduction
        potential_rewards = self.staking_amount * self.reward_rate * time_period
        
        # Calculate effective rewards after applying sell tax
        effective_rewards = potential_rewards * (1 - self.sell_tax_rate)

        return effective_rewards

# Example usage
if __name__ == "__main__":
    try:
        calculator = StakingRewardsCalculator(staking_amount=1000, sell_tax_rate=0.05, reward_rate=0.10)
        rewards = calculator.calculate_rewards(time_period=12)
        print(f"Potential rewards from staking: {rewards:.2f} $QUBE")
    except ValueError as e:
        print(f"Error: {e}")
```
