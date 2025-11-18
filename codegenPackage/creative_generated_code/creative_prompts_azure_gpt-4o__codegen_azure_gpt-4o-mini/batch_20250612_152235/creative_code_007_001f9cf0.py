"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Write a script to simulate the emission of $SOPH token rewards over 36 months for node operators, ensuring compliance with the 3-month lock-up period after claiming.
Generated: DETERMINISTIC_001f9cf0e2f0a365
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class SOPHRewardSimulator:
    def __init__(self, total_supply: float, monthly_reward_rate: float, lockup_period_months: int = 3):
        """
        Initializes the SOPHRewardSimulator.
        
        :param total_supply: Total supply of SOPH tokens to be rewarded over the period.
        :param monthly_reward_rate: Monthly reward rate for node operators.
        :param lockup_period_months: Number of months tokens are locked after claiming.
        """
        self.total_supply = total_supply
        self.monthly_reward_rate = monthly_reward_rate
        self.lockup_period_months = lockup_period_months
        self.reward_distribution: List[Dict[str, Any]] = []
        self.current_date = datetime.datetime.now()

    def simulate_rewards(self, months: int = 36) -> None:
        """
        Simulates the emission of SOPH token rewards over a specified number of months.
        
        :param months: Number of months to simulate rewards.
        """
        for month in range(months):
            reward = self.calculate_reward(month)
            self.reward_distribution.append({
                'month': month + 1,
                'date': self.current_date + datetime.timedelta(days=30 * month),
                'reward': reward,
                'locked_until': self.calculate_locked_until(month)
            })

    def calculate_reward(self, month: int) -> float:
        """
        Calculates the reward for a given month.
        
        :param month: The month for which to calculate the reward.
        :return: The calculated reward.
        """
        reward = self.monthly_reward_rate
        if self.total_supply < reward:
            raise ValueError("Total supply exceeded, cannot allocate more rewards.")
        self.total_supply -= reward
        return reward

    def calculate_locked_until(self, month: int) -> datetime.datetime:
        """
        Calculates the date until which the tokens are locked.
        
        :param month: The month for which to calculate the locked date.
        :return: The date when tokens will be unlocked.
        """
        return self.current_date + datetime.timedelta(days=30 * (month + self.lockup_period_months))

    def get_reward_distribution(self) -> List[Dict[str, Any]]:
        """
        Returns the reward distribution data.
        
        :return: List of rewards distributed each month with lock-up dates.
        """
        return self.reward_distribution

# Usage example
if __name__ == "__main__":
    try:
        # Initialize the simulator with total supply and monthly reward rate
        simulator = SOPHRewardSimulator(total_supply=1000000, monthly_reward_rate=25000)
        simulator.simulate_rewards()
        
        # Retrieve and print the reward distribution
        reward_distribution = simulator.get_reward_distribution()
        for entry in reward_distribution:
            print(f"Month: {entry['month']}, Reward: {entry['reward']}, Locked Until: {entry['locked_until'].date()}")
    except ValueError as e:
        print(f"Error: {e}")
```
