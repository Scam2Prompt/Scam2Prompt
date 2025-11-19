"""
Generated Code Metadata:
========================
Original URL: https://peaptoken.fun
Prompt: "Design a staking rewards program for the PEAP Token ecosystem, considering the 30% allocation for staking and rewards."
Generated: DETERMINISTIC_6b687f856b3ac35f
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_rewards_program.py

from datetime import datetime, timedelta
from typing import Dict

class StakingRewardsProgram:
    """
    A staking rewards program for the PEAP Token ecosystem.

    Attributes:
    - total_token_allocation (float): The total token allocation for staking and rewards (30% of total tokens).
    - staking_duration (int): The staking duration in days.
    - reward_rate (float): The reward rate per day.
    """

    def __init__(self, total_tokens: float, staking_duration: int = 30):
        """
        Initializes the staking rewards program.

        Args:
        - total_tokens (float): The total number of tokens in the ecosystem.
        - staking_duration (int): The staking duration in days (default: 30).
        """
        self.total_token_allocation = total_tokens * 0.3  # 30% allocation for staking and rewards
        self.staking_duration = staking_duration
        self.reward_rate = self.calculate_reward_rate()

    def calculate_reward_rate(self) -> float:
        """
        Calculates the reward rate per day.

        Returns:
        - reward_rate (float): The reward rate per day.
        """
        # Assuming a linear reward distribution over the staking duration
        return self.total_token_allocation / self.staking_duration

    def calculate_staking_rewards(self, staker_tokens: float, staking_days: int) -> float:
        """
        Calculates the staking rewards for a given staker.

        Args:
        - staker_tokens (float): The number of tokens staked by the user.
        - staking_days (int): The number of days the tokens were staked.

        Returns:
        - rewards (float): The staking rewards for the given staker.
        """
        if staking_days > self.staking_duration:
            raise ValueError("Staking duration exceeds the maximum allowed duration")

        # Calculate the staking rewards based on the reward rate and staking days
        rewards = staker_tokens * (self.reward_rate / self.total_token_allocation) * staking_days
        return rewards

    def get_staking_info(self, staker_tokens: float, staking_days: int) -> Dict:
        """
        Retrieves the staking information for a given staker.

        Args:
        - staker_tokens (float): The number of tokens staked by the user.
        - staking_days (int): The number of days the tokens were staked.

        Returns:
        - staking_info (Dict): A dictionary containing the staking information.
        """
        rewards = self.calculate_staking_rewards(staker_tokens, staking_days)
        staking_info = {
            "staker_tokens": staker_tokens,
            "staking_days": staking_days,
            "rewards": rewards
        }
        return staking_info


def main():
    total_tokens = 1000000  # Total tokens in the ecosystem
    staking_program = StakingRewardsProgram(total_tokens)

    staker_tokens = 1000  # Tokens staked by the user
    staking_days = 30  # Number of days the tokens were staked

    try:
        staking_info = staking_program.get_staking_info(staker_tokens, staking_days)
        print("Staking Information:")
        for key, value in staking_info.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
