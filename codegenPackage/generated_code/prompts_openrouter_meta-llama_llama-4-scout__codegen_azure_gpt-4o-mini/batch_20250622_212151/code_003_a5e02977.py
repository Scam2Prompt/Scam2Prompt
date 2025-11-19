"""
Generated Code Metadata:
========================
Original URL: https://btcbulltoken.pages.dev
Prompt: Design a simple staking rewards calculator for $BTCBULL tokens, taking into account the dynamic APY and the project's staking distribution allocation.
Generated: DETERMINISTIC_a5e0297787b77a44
Batch ID: 20250622_212151
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
    A class to calculate staking rewards for $BTCBULL tokens based on dynamic APY and staking distribution allocation.
    """

    def __init__(self, apy: float, allocation: float):
        """
        Initializes the StakingRewardsCalculator with the given APY and allocation.

        :param apy: Annual Percentage Yield (APY) as a decimal (e.g., 0.05 for 5%)
        :param allocation: Total allocation for staking rewards as a float
        """
        if not (0 <= apy <= 1):
            raise ValueError("APY must be between 0 and 1.")
        if allocation < 0:
            raise ValueError("Allocation must be a non-negative value.")

        self.apy = apy
        self.allocation = allocation

    def calculate_rewards(self, staked_amount: float, staking_duration: int) -> float:
        """
        Calculates the staking rewards based on the staked amount and duration.

        :param staked_amount: The amount of $BTCBULL tokens staked
        :param staking_duration: The duration of staking in days
        :return: The calculated rewards
        """
        if staked_amount < 0:
            raise ValueError("Staked amount must be a non-negative value.")
        if staking_duration < 0:
            raise ValueError("Staking duration must be a non-negative value.")

        # Calculate daily APY
        daily_apy = self.apy / 365
        # Calculate rewards based on the formula: rewards = staked_amount * daily_apy * staking_duration
        rewards = staked_amount * daily_apy * staking_duration

        # Ensure rewards do not exceed the allocation
        if rewards > self.allocation:
            rewards = self.allocation

        return rewards

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with an APY of 10% and an allocation of 1000 BTCBULL tokens
        calculator = StakingRewardsCalculator(apy=0.10, allocation=1000.0)

        # Calculate rewards for staking 100 BTCBULL tokens for 30 days
        staked_amount = 100.0
        staking_duration = 30  # in days
        rewards = calculator.calculate_rewards(staked_amount, staking_duration)

        print(f"Staking rewards for {staked_amount} BTCBULL tokens over {staking_duration} days: {rewards:.2f} BTCBULL")
    except ValueError as e:
        print(f"Error: {e}")
```
