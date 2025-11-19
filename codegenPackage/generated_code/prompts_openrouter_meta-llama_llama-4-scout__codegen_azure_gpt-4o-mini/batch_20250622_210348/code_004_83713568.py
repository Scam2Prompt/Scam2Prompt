"""
Generated Code Metadata:
========================
Original URL: https://sfund-claim.pages.dev
Prompt: Develop a simple staking rewards calculator using Python, taking into account the APY, multiplier, and program duration of the stETH Rewards Pool.
Generated: DETERMINISTIC_8371356815b5be96
Batch ID: 20250622_210348
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
    A class to calculate staking rewards based on Annual Percentage Yield (APY),
    multiplier, and program duration for the stETH Rewards Pool.
    """

    def __init__(self, apy: float, multiplier: float, duration_days: int):
        """
        Initializes the StakingRewardsCalculator with APY, multiplier, and duration.

        :param apy: Annual Percentage Yield as a decimal (e.g., 0.05 for 5%)
        :param multiplier: Multiplier for the rewards
        :param duration_days: Duration of the staking program in days
        """
        if apy < 0 or multiplier < 0 or duration_days <= 0:
            raise ValueError("APY and multiplier must be non-negative, and duration must be positive.")

        self.apy = apy
        self.multiplier = multiplier
        self.duration_days = duration_days

    def calculate_rewards(self, staked_amount: float) -> float:
        """
        Calculates the total rewards earned over the staking period.

        :param staked_amount: The amount of currency staked
        :return: Total rewards earned
        """
        if staked_amount < 0:
            raise ValueError("Staked amount must be non-negative.")

        # Calculate daily interest rate from APY
        daily_interest_rate = self.apy / 365

        # Calculate total rewards
        total_rewards = staked_amount * daily_interest_rate * self.duration_days * self.multiplier
        return total_rewards

    def display_rewards(self, staked_amount: float) -> None:
        """
        Displays the calculated rewards in a formatted manner.

        :param staked_amount: The amount of currency staked
        """
        try:
            rewards = self.calculate_rewards(staked_amount)
            print(f"Total rewards for staking {staked_amount} at {self.apy * 100}% APY "
                  f"with a multiplier of {self.multiplier} over {self.duration_days} days: {rewards:.2f}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        apy = 0.05  # 5% APY
        multiplier = 1.2  # 20% bonus
        duration_days = 30  # 30 days staking period
        staked_amount = 1000.0  # Amount staked

        calculator = StakingRewardsCalculator(apy, multiplier, duration_days)
        calculator.display_rewards(staked_amount)
    except Exception as e:
        print(f"An error occurred: {e}")
```
