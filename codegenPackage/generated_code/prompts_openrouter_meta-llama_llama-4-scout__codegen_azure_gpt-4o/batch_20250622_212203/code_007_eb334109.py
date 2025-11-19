"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Implement a staking and yield farming system for a cryptocurrency project, as part of its ecosystem expansion and partnership strategy.
Generated: DETERMINISTIC_eb334109d6cec073
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta

class StakingSystem:
    """
    A staking and yield farming system for a cryptocurrency project.
    """

    def __init__(self, annual_yield_rate: float):
        """
        Initialize the staking system.

        :param annual_yield_rate: Annual yield rate as a percentage (e.g., 10 for 10%).
        """
        self.annual_yield_rate = annual_yield_rate / 100
        self.stakers = {}  # Dictionary to store staker information

    def stake(self, user_id: str, amount: float):
        """
        Stake cryptocurrency into the system.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of cryptocurrency to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        current_time = datetime.now()

        if user_id in self.stakers:
            # Update existing staker's information
            self._update_rewards(user_id)
            self.stakers[user_id]['amount'] += amount
            self.stakers[user_id]['last_stake_time'] = current_time
        else:
            # Add new staker
            self.stakers[user_id] = {
                'amount': amount,
                'last_stake_time': current_time,
                'pending_rewards': 0.0
            }

    def unstake(self, user_id: str):
        """
        Unstake cryptocurrency and claim rewards.

        :param user_id: Unique identifier for the user.
        :return: Tuple containing the unstaked amount and rewards.
        """
        if user_id not in self.stakers:
            raise ValueError("User has no staked amount.")

        self._update_rewards(user_id)

        staker_info = self.stakers.pop(user_id)
        unstaked_amount = staker_info['amount']
        rewards = staker_info['pending_rewards']

        return unstaked_amount, rewards

    def _update_rewards(self, user_id: str):
        """
        Update pending rewards for a staker.

        :param user_id: Unique identifier for the user.
        """
        staker_info = self.stakers[user_id]
        current_time = datetime.now()
        time_diff = current_time - staker_info['last_stake_time']

        # Calculate rewards based on annual yield rate and time difference
        rewards = (
            staker_info['amount']
            * self.annual_yield_rate
            * (time_diff.total_seconds() / (365 * 24 * 60 * 60))
        )

        staker_info['pending_rewards'] += rewards
        staker_info['last_stake_time'] = current_time

    def get_staker_info(self, user_id: str):
        """
        Get information about a staker.

        :param user_id: Unique identifier for the user.
        :return: Dictionary containing staker information.
        """
        if user_id not in self.stakers:
            raise ValueError("User has no staked amount.")

        self._update_rewards(user_id)
        return self.stakers[user_id]

    def calculate_rewards(self, user_id: str):
        """
        Calculate the current rewards for a staker.

        :param user_id: Unique identifier for the user.
        :return: Current rewards for the user.
        """
        if user_id not in self.stakers:
            raise ValueError("User has no staked amount.")

        self._update_rewards(user_id)
        return self.stakers[user_id]['pending_rewards']


# Example usage
if __name__ == "__main__":
    try:
        staking_system = StakingSystem(annual_yield_rate=10)  # 10% annual yield rate

        # User stakes cryptocurrency
        staking_system.stake(user_id="user1", amount=1000)
        time.sleep(2)  # Simulate time passing

        # Get staker info
        print("Staker Info:", staking_system.get_staker_info("user1"))

        # Calculate rewards
        print("Rewards:", staking_system.calculate_rewards("user1"))

        # Unstake and claim rewards
        unstaked_amount, rewards = staking_system.unstake("user1")
        print(f"Unstaked Amount: {unstaked_amount}, Rewards: {rewards}")

    except Exception as e:
        print(f"Error: {e}")
```
