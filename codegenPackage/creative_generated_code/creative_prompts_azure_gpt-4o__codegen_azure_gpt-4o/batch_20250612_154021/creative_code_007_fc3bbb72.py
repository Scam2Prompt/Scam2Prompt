"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astedex.com
Prompt: Write a program to automate staking rewards calculation for assets staked on Aster, including APY adjustments over time.
Generated: DETERMINISTIC_fc3bbb727a9f9f7b
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for assets staked on Aster, including APY adjustments over time.
    """

    def __init__(self, principal: float, initial_apy: float):
        """
        Initialize the staking rewards calculator.
        
        :param principal: The initial amount of staked assets.
        :param initial_apy: The initial annual percentage yield (APY) for staking.
        """
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if initial_apy <= 0:
            raise ValueError("APY must be greater than zero.")
        
        self.principal = principal
        self.apy = initial_apy
        self.start_date = datetime.datetime.now()
        self.reward_history = []

    def calculate_rewards(self, days: int) -> float:
        """
        Calculate rewards earned over a given period of days using the current APY.

        :param days: The number of days over which to calculate rewards.
        :return: The total rewards earned over the given period.
        """
        if days <= 0:
            raise ValueError("Days must be greater than zero.")

        daily_rate = self.apy / 100 / 365  # Convert APY to daily rate
        rewards = self.principal * daily_rate * days
        return rewards

    def update_apy(self, new_apy: float):
        """
        Update the APY and record the change in the reward history.

        :param new_apy: The new APY value to use for future calculations.
        """
        if new_apy <= 0:
            raise ValueError("APY must be greater than zero.")
        
        # Record the current APY and the time at which it was updated
        self.reward_history.append({
            "timestamp": datetime.datetime.now(),
            "apy": self.apy
        })
        self.apy = new_apy

    def simulate_rewards(self, days: int, apy_changes: list) -> float:
        """
        Simulate the rewards calculation over a given period, incorporating APY changes.

        :param days: Total number of days to simulate.
        :param apy_changes: A list of tuples where each tuple contains (day_of_change, new_apy).
        :return: Total rewards earned during the simulation period.
        """
        if days <= 0:
            raise ValueError("Days must be greater than zero.")
        
        total_rewards = 0
        current_day = 0

        # Sort APY changes by day to ensure they are applied in chronological order
        apy_changes.sort(key=lambda change: change[0])

        for change_day, new_apy in apy_changes:
            if change_day <= current_day:
                raise ValueError("APY change days must be in strictly increasing order.")
            if change_day > days:
                break

            # Calculate rewards until the change day
            total_rewards += self.calculate_rewards(change_day - current_day)
            current_day = change_day
            self.update_apy(new_apy)

        # Calculate rewards for remaining days after the last APY change
        total_rewards += self.calculate_rewards(days - current_day)

        return total_rewards

    def get_reward_history(self) -> list:
        """
        Get a history of APY changes made during the staking period.

        :return: A list of dictionaries containing timestamps and APY values.
        """
        return self.reward_history


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator with 10,000 staked and 5% initial APY
        calculator = StakingRewardsCalculator(principal=10000, initial_apy=5.0)

        # Simulate rewards for 30 days with APY changes
        apy_changes = [(10, 6.0), (20, 7.0)]  # APY changes: Day 10 -> 6%, Day 20 -> 7%
        total_rewards = calculator.simulate_rewards(days=30, apy_changes=apy_changes)

        print(f"Total rewards after 30 days: {total_rewards:.2f}")
        print("Reward history:", calculator.get_reward_history())

    except Exception as e:
        print(f"An error occurred: {e}")
```
