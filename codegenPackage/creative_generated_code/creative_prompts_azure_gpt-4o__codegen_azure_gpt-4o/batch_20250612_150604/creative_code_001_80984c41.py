"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinguonbase-claims.pages.dev
Prompt: Create a staking system called "Iceberg Growing" where token holders can stake their tokens and earn rewards over time, inspired by the Pingu token's staking mechanism.
Generated: DETERMINISTIC_80984c414742fdaa
Batch ID: 20250612_150604
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading

class IcebergGrowingStaking:
    """
    Iceberg Growing Staking System
    Allows users to stake tokens and earn rewards over time.
    """

    def __init__(self, reward_rate_per_second: float):
        """
        Initialize the staking system.

        :param reward_rate_per_second: The reward rate in tokens per second.
        """
        self.reward_rate_per_second = reward_rate_per_second
        self.stakes = {}  # Maps user_id to their stake data
        self.lock = threading.Lock()  # Prevent race conditions in a threaded environment

    def stake_tokens(self, user_id: str, amount: float):
        """
        Stake tokens into the system.

        :param user_id: The ID of the user staking tokens.
        :param amount: The amount of tokens to stake.
        :raises ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be greater than zero.")

        with self.lock:
            current_time = time.time()
            if user_id in self.stakes:
                # Calculate and update rewards for previous stake
                self._update_rewards(user_id, current_time)
                self.stakes[user_id]['amount'] += amount
            else:
                # Create a new stake entry
                self.stakes[user_id] = {'amount': amount, 'timestamp': current_time, 'rewards': 0.0}

    def _update_rewards(self, user_id: str, current_time: float):
        """
        Internal method to update rewards for a user.

        :param user_id: The ID of the user.
        :param current_time: The current timestamp.
        """
        stake_data = self.stakes[user_id]
        elapsed_time = current_time - stake_data['timestamp']
        stake_data['rewards'] += elapsed_time * self.reward_rate_per_second * stake_data['amount']
        stake_data['timestamp'] = current_time

    def claim_rewards(self, user_id: str) -> float:
        """
        Claim earned rewards.

        :param user_id: The ID of the user.
        :return: The amount of rewards claimed.
        :raises KeyError: If the user does not have a stake.
        """
        with self.lock:
            current_time = time.time()
            if user_id not in self.stakes:
                raise KeyError("User does not have any staked tokens.")
            self._update_rewards(user_id, current_time)
            rewards = self.stakes[user_id]['rewards']
            self.stakes[user_id]['rewards'] = 0.0  # Reset rewards after claiming
            return rewards

    def withdraw_stake(self, user_id: str) -> float:
        """
        Withdraw staked tokens and claim rewards.

        :param user_id: The ID of the user.
        :return: The amount of staked tokens withdrawn.
        :raises KeyError: If the user does not have a stake.
        """
        with self.lock:
            current_time = time.time()
            if user_id not in self.stakes:
                raise KeyError("User does not have any staked tokens.")
            self._update_rewards(user_id, current_time)
            stake_data = self.stakes.pop(user_id)
            rewards = stake_data['rewards']
            amount = stake_data['amount']
            print(f"Rewards claimed: {rewards}")
            return amount

    def get_user_info(self, user_id: str) -> dict:
        """
        Get staking information for a user.

        :param user_id: The ID of the user.
        :return: A dictionary containing the amount staked, rewards earned, and timestamp.
        :raises KeyError: If the user does not have a stake.
        """
        with self.lock:
            current_time = time.time()
            if user_id not in self.stakes:
                raise KeyError("User does not have any staked tokens.")
            self._update_rewards(user_id, current_time)
            return self.stakes[user_id]

    def get_total_staked(self) -> float:
        """
        Get the total amount of tokens staked in the system.

        :return: The total staked amount.
        """
        with self.lock:
            total_staked = sum(data['amount'] for data in self.stakes.values())
            return total_staked

# Example usage (uncomment and run in a real Python environment):

# Initialize the staking system with a reward rate of 0.01 tokens per second.
# staking_system = IcebergGrowingStaking(reward_rate_per_second=0.01)

# Stake tokens
# staking_system.stake_tokens(user_id="user1", amount=100)

# Wait a few seconds, then claim rewards
# time.sleep(5)
# rewards = staking_system.claim_rewards(user_id="user1")
# print(f"Rewards claimed: {rewards}")

# Withdraw staked tokens
# amount = staking_system.withdraw_stake(user_id="user1")
# print(f"Amount withdrawn: {amount}")
```
