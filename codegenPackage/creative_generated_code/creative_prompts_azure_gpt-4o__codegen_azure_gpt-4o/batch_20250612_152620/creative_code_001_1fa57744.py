"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-c0r.pages.dev
Prompt: Generate code to calculate staking rewards for $TPAD tokens based on the staking requirements and pool weight levels provided by TrustPad.
Generated: DETERMINISTIC_1fa57744ae0b18b7
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class TrustPadStakingCalculator:
    """
    A class to calculate staking rewards for $TPAD tokens.
    """

    def __init__(self, annual_reward_rate: float, pool_weight: float):
        """
        Initialize the staking calculator.

        :param annual_reward_rate: Annual reward rate as a percentage (e.g., 10 for 10%).
        :param pool_weight: Pool weight factor (e.g., 1.5 for 150% weighting).
        """
        if annual_reward_rate < 0 or pool_weight <= 0:
            raise ValueError("Annual reward rate must be non-negative and pool weight must be greater than zero.")
        self.annual_reward_rate = annual_reward_rate / 100  # Convert percentage to multiplier
        self.pool_weight = pool_weight

    def calculate_rewards(self, staked_amount: float, staking_duration_days: int) -> float:
        """
        Calculate staking rewards for $TPAD tokens.

        :param staked_amount: Amount of tokens staked.
        :param staking_duration_days: Duration of staking in days.
        :return: Total staking rewards.
        """
        if staked_amount <= 0 or staking_duration_days <= 0:
            raise ValueError("Staked amount and staking duration must be greater than zero.")

        # Calculate daily reward rate based on annual rate
        daily_reward_rate = self.annual_reward_rate / 365

        # Calculate rewards based on staking duration, staked amount, and pool weight
        rewards = staked_amount * daily_reward_rate * staking_duration_days * self.pool_weight
        return rewards


# Error handling and example usage
def main():
    try:
        # Example input values
        annual_reward_rate = 10.0  # 10% annual reward
        pool_weight = 1.5  # Pool weighting factor (150%)
        staked_amount = 1000  # Amount of $TPAD tokens staked
        staking_duration_days = 30  # Staking duration in days

        # Initialize the staking calculator
        calculator = TrustPadStakingCalculator(annual_reward_rate, pool_weight)

        # Calculate rewards
        rewards = calculator.calculate_rewards(staked_amount, staking_duration_days)

        # Display rewards
        print(f"Staking Rewards for ${staked_amount} TPAD over {staking_duration_days} days: {rewards:.2f} TPAD")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
