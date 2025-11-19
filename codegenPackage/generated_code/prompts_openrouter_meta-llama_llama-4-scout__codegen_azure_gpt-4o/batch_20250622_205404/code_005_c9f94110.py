"""
Generated Code Metadata:
========================
Original URL: https://metamask-portfolio.vercel.app
Prompt: Implement a staking feature for a cryptocurrency portfolio management system, allowing users to stake their assets and earn rewards.
Generated: DETERMINISTIC_c9f941102ae2657b
Batch ID: 20250622_205404
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
    A class to manage staking of cryptocurrency assets and reward distribution.
    """

    def __init__(self, reward_rate: float):
        """
        Initialize the staking system.

        :param reward_rate: Annual reward rate (percentage) for staking.
        """
        self.reward_rate = reward_rate / 100  # Convert percentage to decimal
        self.stakes = {}  # Dictionary to store user stakes
        self.reward_history = {}  # Dictionary to store user reward history

    def stake_assets(self, user_id: str, amount: float):
        """
        Stake assets for a user.

        :param user_id: Unique identifier for the user.
        :param amount: Amount of assets to stake.
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        current_time = datetime.now()

        # If the user already has stakes, update the stake amount and timestamp
        if user_id in self.stakes:
            self._update_rewards(user_id)  # Calculate rewards before updating
            self.stakes[user_id]['amount'] += amount
            self.stakes[user_id]['timestamp'] = current_time
        else:
            # Create a new stake entry for the user
            self.stakes[user_id] = {
                'amount': amount,
                'timestamp': current_time
            }

        print(f"User {user_id} staked {amount} assets.")

    def _update_rewards(self, user_id: str):
        """
        Update rewards for a user based on their staking duration.

        :param user_id: Unique identifier for the user.
        """
        if user_id not in self.stakes:
            return

        stake_info = self.stakes[user_id]
        current_time = datetime.now()
        staked_duration = current_time - stake_info['timestamp']

        # Calculate rewards based on annual reward rate
        rewards = stake_info['amount'] * self.reward_rate * (staked_duration.days / 365)

        # Update reward history
        if user_id not in self.reward_history:
            self.reward_history[user_id] = 0
        self.reward_history[user_id] += rewards

        # Update the timestamp to the current time
        self.stakes[user_id]['timestamp'] = current_time

    def claim_rewards(self, user_id: str):
        """
        Claim rewards for a user.

        :param user_id: Unique identifier for the user.
        :return: The amount of rewards claimed.
        :raises KeyError: If the user has no rewards to claim.
        """
        self._update_rewards(user_id)  # Ensure rewards are up-to-date

        if user_id not in self.reward_history or self.reward_history[user_id] == 0:
            raise KeyError(f"User {user_id} has no rewards to claim.")

        rewards = self.reward_history[user_id]
        self.reward_history[user_id] = 0  # Reset rewards after claiming

        print(f"User {user_id} claimed {rewards:.2f} rewards.")
        return rewards

    def unstake_assets(self, user_id: str):
        """
        Unstake assets for a user and claim any pending rewards.

        :param user_id: Unique identifier for the user.
        :return: A tuple containing the unstaked amount and claimed rewards.
        :raises KeyError: If the user has no assets staked.
        """
        if user_id not in self.stakes:
            raise KeyError(f"User {user_id} has no assets staked.")

        self._update_rewards(user_id)  # Ensure rewards are up-to-date

        stake_info = self.stakes.pop(user_id)  # Remove stake entry
        claimed_rewards = self.claim_rewards(user_id)  # Claim rewards

        print(f"User {user_id} unstaked {stake_info['amount']} assets.")
        return stake_info['amount'], claimed_rewards

    def get_stake_info(self, user_id: str):
        """
        Get staking information for a user.

        :param user_id: Unique identifier for the user.
        :return: A dictionary containing stake amount and timestamp.
        :raises KeyError: If the user has no assets staked.
        """
        if user_id not in self.stakes:
            raise KeyError(f"User {user_id} has no assets staked.")

        return self.stakes[user_id]

    def get_reward_info(self, user_id: str):
        """
        Get reward information for a user.

        :param user_id: Unique identifier for the user.
        :return: The amount of rewards available for the user.
        """
        self._update_rewards(user_id)  # Ensure rewards are up-to-date

        return self.reward_history.get(user_id, 0)


# Example usage
if __name__ == "__main__":
    staking_system = StakingSystem(reward_rate=10)  # 10% annual reward rate

    try:
        staking_system.stake_assets("user1", 1000)
        time.sleep(2)  # Simulate time passing
        print("Reward info:", staking_system.get_reward_info("user1"))
        print("Stake info:", staking_system.get_stake_info("user1"))
        rewards = staking_system.claim_rewards("user1")
        print(f"Claimed rewards: {rewards:.2f}")
        unstaked_amount, claimed_rewards = staking_system.unstake_assets("user1")
        print(f"Unstaked amount: {unstaked_amount}, Claimed rewards: {claimed_rewards:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
