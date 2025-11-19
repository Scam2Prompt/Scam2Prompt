"""
Generated Code Metadata:
========================
Original URL: https://jellynfts.web.app
Prompt: Develop a staking rewards calculator for Jelly token holders based on the project's staking utilities.
Generated: DETERMINISTIC_08c2af5c7ac87e53
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for Jelly token holders.
    """

    def __init__(self, annual_reward_rate: float, staking_start_date: datetime.date):
        """
        Initialize the staking rewards calculator.

        :param annual_reward_rate: Annual reward rate as a percentage (e.g., 5 for 5%).
        :param staking_start_date: The date when staking started.
        """
        self.annual_reward_rate = annual_reward_rate / 100  # Convert percentage to decimal
        self.staking_start_date = staking_start_date

    def calculate_rewards(self, staked_amount: float, current_date: datetime.date) -> float:
        """
        Calculate the staking rewards for a given staked amount and current date.

        :param staked_amount: The amount of Jelly tokens staked.
        :param current_date: The current date for reward calculation.
        :return: The calculated staking rewards.
        """
        # Validate inputs
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than zero.")
        if current_date < self.staking_start_date:
            raise ValueError("Current date cannot be earlier than the staking start date.")

        # Calculate the number of days staked
        days_staked = (current_date - self.staking_start_date).days

        # Calculate rewards based on annual reward rate
        daily_reward_rate = self.annual_reward_rate / 365  # Daily reward rate
        rewards = staked_amount * daily_reward_rate * days_staked

        return rewards


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the staking rewards calculator
        staking_start_date = datetime.date(2023, 1, 1)
        annual_reward_rate = 5.0  # 5% annual reward rate
        calculator = StakingRewardsCalculator(annual_reward_rate, staking_start_date)

        # Define the staked amount and current date
        staked_amount = 1000.0  # 1000 Jelly tokens
        current_date = datetime.date(2023, 10, 1)

        # Calculate rewards
        rewards = calculator.calculate_rewards(staked_amount, current_date)
        print(f"Staking rewards: {rewards:.2f} Jelly tokens")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
