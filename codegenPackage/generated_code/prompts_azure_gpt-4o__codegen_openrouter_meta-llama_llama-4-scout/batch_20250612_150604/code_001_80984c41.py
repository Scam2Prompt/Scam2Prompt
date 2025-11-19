"""
Generated Code Metadata:
========================
Original URL: https://pinguonbase-claims.pages.dev
Prompt: Create a staking system called "Iceberg Growing" where token holders can stake their tokens and earn rewards over time, inspired by the Pingu token's staking mechanism.
Generated: DETERMINISTIC_80984c414742fdaa
Batch ID: 20250612_150604
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# iceberg_growing.py

import time
from typing import Dict

class IcebergGrowing:
    def __init__(self, total_rewards: int, staking_duration: int):
        """
        Initialize the Iceberg Growing staking system.

        Args:
        - total_rewards (int): The total rewards available for distribution.
        - staking_duration (int): The duration of the staking period in seconds.
        """
        self.total_rewards = total_rewards
        self.staking_duration = staking_duration
        self.stakers: Dict[str, Staker] = {}
        self.start_time = 0

    def start_staking(self):
        """
        Start the staking period.
        """
        self.start_time = int(time.time())

    def stake(self, user_id: str, amount: int):
        """
        Stake tokens.

        Args:
        - user_id (str): The ID of the user staking tokens.
        - amount (int): The amount of tokens to stake.

        Raises:
        - ValueError: If the staking period has not started.
        """
        if not self.start_time:
            raise ValueError("Staking period has not started")

        if user_id in self.stakers:
            self.stakers[user_id].amount += amount
        else:
            self.stakers[user_id] = Staker(amount, self.staking_duration)

    def unstake(self, user_id: str):
        """
        Unstake tokens and claim rewards.

        Args:
        - user_id (str): The ID of the user unstaking tokens.

        Returns:
        - int: The rewards earned by the user.

        Raises:
        - ValueError: If the user has not staked tokens.
        """
        if user_id not in self.stakers:
            raise ValueError("User has not staked tokens")

        staker = self.stakers[user_id]
        elapsed_time = int(time.time()) - self.start_time
        rewards = self.calculate_rewards(staker, elapsed_time)
        del self.stakers[user_id]
        return rewards

    def calculate_rewards(self, staker: 'Staker', elapsed_time: int):
        """
        Calculate the rewards earned by a staker.

        Args:
        - staker (Staker): The staker object.
        - elapsed_time (int): The elapsed time in seconds.

        Returns:
        - int: The rewards earned by the staker.
        """
        if elapsed_time < staker.staking_duration:
            return 0

        reward_rate = self.total_rewards / (self.staking_duration * len(self.stakers))
        return int(staker.amount * reward_rate * (elapsed_time / self.staking_duration))


class Staker:
    def __init__(self, amount: int, staking_duration: int):
        """
        Initialize a staker.

        Args:
        - amount (int): The amount of tokens staked.
        - staking_duration (int): The staking duration in seconds.
        """
        self.amount = amount
        self.staking_duration = staking_duration


def main():
    # Example usage
    iceberg = IcebergGrowing(total_rewards=1000, staking_duration=86400)  # 1 day
    iceberg.start_staking()

    iceberg.stake("user1", 100)
    iceberg.stake("user2", 200)

    time.sleep(2)  # simulate time passing

    rewards1 = iceberg.unstake("user1")
    rewards2 = iceberg.unstake("user2")

    print(f"User 1 rewards: {rewards1}")
    print(f"User 2 rewards: {rewards2}")


if __name__ == "__main__":
    main()
```
