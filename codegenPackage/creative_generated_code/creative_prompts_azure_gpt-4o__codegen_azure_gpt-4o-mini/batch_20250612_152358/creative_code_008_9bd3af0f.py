"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jwzt-dashboards-inqubeta.pages.dev
Prompt: Generate a script to simulate staking $QUBE tokens for a specified number of days and calculate the total rewards earned.
Generated: DETERMINISTIC_9bd3af0fb2c05e09
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class QubeStaking:
    def __init__(self, initial_amount: float, daily_reward_rate: float):
        """
        Initializes the QubeStaking instance.

        :param initial_amount: Initial amount of $QUBE tokens to stake.
        :param daily_reward_rate: Daily reward rate as a percentage (e.g., 0.05 for 5%).
        """
        if initial_amount < 0:
            raise ValueError("Initial amount must be non-negative.")
        if not (0 <= daily_reward_rate <= 1):
            raise ValueError("Daily reward rate must be between 0 and 1.")

        self.initial_amount = initial_amount
        self.daily_reward_rate = daily_reward_rate
        self.staked_amount = initial_amount
        self.total_rewards = 0.0

    def simulate_staking(self, days: int) -> None:
        """
        Simulates staking for the specified number of days and calculates total rewards.

        :param days: Number of days to stake tokens.
        :raises ValueError: If days is negative.
        """
        if days < 0:
            raise ValueError("Number of days must be non-negative.")

        for day in range(days):
            # Calculate daily rewards
            daily_reward = self.staked_amount * self.daily_reward_rate
            self.total_rewards += daily_reward

    def get_total_rewards(self) -> float:
        """
        Returns the total rewards earned.

        :return: Total rewards earned from staking.
        """
        return self.total_rewards

    def get_end_date(self, start_date: datetime.date, days: int) -> datetime.date:
        """
        Calculates the end date of the staking period.

        :param start_date: The date when staking starts.
        :param days: Number of days to stake.
        :return: The end date after staking for the specified number of days.
        """
        if days < 0:
            raise ValueError("Number of days must be non-negative.")

        return start_date + datetime.timedelta(days=days)

def main():
    try:
        # Set initial parameters
        initial_stake = 1000.0  # Amount of $QUBE tokens
        daily_reward_rate = 0.05  # 5% daily reward rate
        staking_days = 30  # Staking for 30 days
        start_date = datetime.date.today()  # Current date

        # Create a QubeStaking instance
        staking = QubeStaking(initial_amount=initial_stake, daily_reward_rate=daily_reward_rate)

        # Simulate staking
        staking.simulate_staking(days=staking_days)

        # Get total rewards and end date
        total_rewards = staking.get_total_rewards()
        end_date = staking.get_end_date(start_date=start_date, days=staking_days)

        # Output results
        print(f"Total rewards earned after {staking_days} days: ${total_rewards:.2f}")
        print(f"End date of staking: {end_date}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
