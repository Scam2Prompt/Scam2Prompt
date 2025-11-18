"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-daomars-com.pages.dev
Prompt: Implement a staking system that allows users to stake MDAO tokens and receive rewards in partner project tokens, as described in the MarsDAO DAPP Partnership.
Generated: DETERMINISTIC_98211a96a6ae6d59
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import Dict

class StakingSystem:
    """
    A staking system that allows users to stake MDAO tokens and earn rewards in partner project tokens.
    """

    def __init__(self, reward_rate: float):
        """
        Initializes the staking system.

        Args:
            reward_rate (float): Reward rate in partner tokens per MDAO token staked per second.
        """
        self.reward_rate = reward_rate  # Reward rate in partner tokens (per MDAO per second)
        self.staked_balance: Dict[str, float] = {}  # User address mapped to their staked MDAO balance
        self.stake_timestamp: Dict[str, float] = {}  # User address mapped to their staking start timestamp
        self.reward_balance: Dict[str, float] = {}  # User address mapped to their accumulated rewards

    def stake_tokens(self, user_address: str, amount: float):
        """
        Stake MDAO tokens into the system.

        Args:
            user_address (str): The address of the user staking tokens.
            amount (float): The amount of MDAO tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        # Calculate any accumulated rewards before updating balances
        self._update_rewards(user_address)

        # Update staked balance and timestamp
        self.staked_balance[user_address] = self.staked_balance.get(user_address, 0) + amount
        self.stake_timestamp[user_address] = time.time()

    def unstake_tokens(self, user_address: str):
        """
        Unstake MDAO tokens from the system and claim rewards.

        Args:
            user_address (str): The address of the user unstaking tokens.
        
        Returns:
            tuple: Unstaked MDAO tokens and earned partner project rewards.
        """
        if user_address not in self.staked_balance or self.staked_balance[user_address] <= 0:
            raise ValueError("No tokens staked for this user.")

        # Calculate final rewards
        self._update_rewards(user_address)

        # Retrieve staked balance and rewards
        staked_amount = self.staked_balance[user_address]
        rewards = self.reward_balance[user_address]

        # Reset balances
        self.staked_balance[user_address] = 0
        self.reward_balance[user_address] = 0

        return staked_amount, rewards

    def _update_rewards(self, user_address: str):
        """
        Internal method to update rewards for a user based on their staking duration.

        Args:
            user_address (str): The address of the user whose rewards are being updated.
        """
        if user_address not in self.staked_balance or self.staked_balance[user_address] <= 0:
            return  # No staking for this user, no rewards to update

        # Calculate elapsed time since last update or staking
        current_time = time.time()
        elapsed_time = current_time - self.stake_timestamp[user_address]

        # Calculate rewards earned during this period
        earned_rewards = elapsed_time * self.staked_balance[user_address] * self.reward_rate

        # Update reward balance and reset timestamp
        self.reward_balance[user_address] = self.reward_balance.get(user_address, 0) + earned_rewards
        self.stake_timestamp[user_address] = current_time

    def get_rewards(self, user_address: str) -> float:
        """
        Get the current reward balance for a user.

        Args:
            user_address (str): The address of the user checking their rewards.
        
        Returns:
            float: The amount of partner project tokens earned.
        """
        self._update_rewards(user_address)  # Refresh rewards before returning
        return self.reward_balance.get(user_address, 0)

    def get_staked_balance(self, user_address: str) -> float:
        """
        Get the current staked balance for a user.

        Args:
            user_address (str): The address of the user checking their staked balance.
        
        Returns:
            float: The amount of MDAO tokens staked.
        """
        return self.staked_balance.get(user_address, 0)


# Example usage (uncomment to run):
# staking_system = StakingSystem(reward_rate=0.01)
# staking_system.stake_tokens(user_address="user1", amount=100)
# time.sleep(2)  # Simulate staking duration
# print(staking_system.get_rewards("user1"))  # Should show rewards earned in partner tokens
# staked, rewards = staking_system.unstake_tokens("user1")
# print(f"Unstaked {staked} MDAO, earned {rewards} partner tokens.")
```
