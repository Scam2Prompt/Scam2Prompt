"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-site.pages.dev
Prompt: Develop a staking rewards calculator for $PEPU tokens, taking into account the doubled staking rewards offered by Pepe Unchained.
Generated: DETERMINISTIC_bb0d5ee1cbc1a309
Batch ID: 20250622_210822
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
    A class to calculate staking rewards for $PEPU tokens.
    Pepe Unchained offers doubled staking rewards.
    """

    def __init__(self, annual_reward_rate: float, doubled_rewards: bool = True):
        """
        Initialize the staking rewards calculator.

        :param annual_reward_rate: Annual reward rate as a percentage (e.g., 10 for 10%).
        :param doubled_rewards: Boolean indicating if rewards are doubled (default is True).
        """
        if annual_reward_rate <= 0:
            raise ValueError("Annual reward rate must be greater than 0.")
        self.annual_reward_rate = annual_reward_rate
        self.doubled_rewards = doubled_rewards

    def calculate_rewards(self, staked_amount: float, staking_start_date: datetime.date, staking_end_date: datetime.date) -> float:
        """
        Calculate the staking rewards for a given amount and time period.

        :param staked_amount: The amount of $PEPU tokens staked.
        :param staking_start_date: The start date of staking (datetime.date object).
        :param staking_end_date: The end date of staking (datetime.date object).
        :return: The calculated staking rewards.
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than 0.")
        if staking_start_date >= staking_end_date:
            raise ValueError("Staking start date must be earlier than the end date.")

        # Calculate the number of days staked
        days_staked = (staking_end_date - staking_start_date).days

        # Calculate the daily reward rate
        daily_reward_rate = self.annual_reward_rate / 100 / 365

        # Calculate the base rewards
        base_rewards = staked_amount * daily_reward_rate * days_staked

        # Apply doubled rewards if applicable
        if self.doubled_rewards:
            return base_rewards * 2
        return base_rewards


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with an annual reward rate of 10%
        calculator = StakingRewardsCalculator(annual_reward_rate=10)

        # Define staking parameters
        staked_amount = 1000  # Amount of $PEPU tokens staked
        staking_start_date = datetime.date(2023, 1, 1)
        staking_end_date = datetime.date(2023, 6, 1)

        # Calculate rewards
        rewards = calculator.calculate_rewards(staked_amount, staking_start_date, staking_end_date)
        print(f"Staking rewards for {staked_amount} $PEPU tokens: {rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
