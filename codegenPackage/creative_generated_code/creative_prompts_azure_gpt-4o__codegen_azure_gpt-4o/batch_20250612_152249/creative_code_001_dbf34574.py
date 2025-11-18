"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: Generate code to implement staking functionality for the $ZUSHI token, ensuring users can stake their tokens and receive rewards based on the distribution model outlined in the Zushi ecosystem.
Generated: DETERMINISTIC_dbf34574892d1921
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_zushi.py

import time
from typing import Dict

class ZushiStaking:
    """
    A class to manage staking functionality for $ZUSHI token.
    Users can stake tokens and receive rewards based on a distribution model.
    """

    def __init__(self, reward_rate_per_second: float):
        """
        Initialize the staking contract.

        :param reward_rate_per_second: Reward rate in tokens distributed per second for staking.
        """
        self.staked_balances: Dict[str, float] = {}  # Track staked tokens by address
        self.reward_balances: Dict[str, float] = {}  # Track earned rewards by address
        self.last_updated_time: Dict[str, float] = {}  # Timestamp of last staking event for each address
        self.reward_rate = reward_rate_per_second  # Reward rate in tokens per second

    def stake_tokens(self, user_address: str, amount: float):
        """
        Stake tokens in the contract.

        :param user_address: Address of the user staking tokens.
        :param amount: Amount of tokens to be staked.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        # Update rewards before modifying staked balance
        self._update_rewards(user_address)

        # Add staked balance for the user
        if user_address not in self.staked_balances:
            self.staked_balances[user_address] = 0
        self.staked_balances[user_address] += amount

        # Update the last updated time
        self.last_updated_time[user_address] = time.time()

        print(f"User {user_address} staked {amount} $ZUSHI tokens.")

    def unstake_tokens(self, user_address: str):
        """
        Unstake all tokens for a user and collect rewards.

        :param user_address: Address of the user unstaking tokens.
        :return: Tuple of (unstaked amount, earned rewards).
        """
        if user_address not in self.staked_balances or self.staked_balances[user_address] <= 0:
            raise ValueError("No tokens to unstake.")

        # Update rewards before unstaking
        self._update_rewards(user_address)

        # Retrieve staked balance and rewards
        staked_amount = self.staked_balances[user_address]
        earned_rewards = self.reward_balances.get(user_address, 0)

        # Reset staked and reward balances
        self.staked_balances[user_address] = 0
        self.reward_balances[user_address] = 0
        self.last_updated_time[user_address] = time.time()

        print(f"User {user_address} unstaked {staked_amount} $ZUSHI tokens and earned {earned_rewards} reward tokens.")
        return staked_amount, earned_rewards

    def _update_rewards(self, user_address: str):
        """
        Private method to update rewards for a user based on elapsed time.

        :param user_address: Address of the user whose rewards are being updated.
        """
        if user_address not in self.last_updated_time:
            self.last_updated_time[user_address] = time.time()

        # Calculate time elapsed since last update
        current_time = time.time()
        time_elapsed = current_time - self.last_updated_time[user_address]

        # Calculate rewards based on time elapsed
        if user_address not in self.reward_balances:
            self.reward_balances[user_address] = 0

        rewards_earned = self.staked_balances.get(user_address, 0) * self.reward_rate * time_elapsed
        self.reward_balances[user_address] += rewards_earned
        self.last_updated_time[user_address] = current_time

    def check_rewards(self, user_address: str):
        """
        Check the rewards earned by a user.

        :param user_address: Address of the user checking rewards.
        :return: The amount of rewards earned.
        """
        # Update rewards before returning the balance
        self._update_rewards(user_address)
        return self.reward_balances.get(user_address, 0)


# Example Usage:
if __name__ == "__main__":
    # Initialize staking contract with a reward rate of 0.01 tokens per second
    staking_contract = ZushiStaking(reward_rate_per_second=0.01)

    # Example user actions
    staking_contract.stake_tokens("user1", 100)
    time.sleep(5)  # Simulate time passing

    rewards = staking_contract.check_rewards("user1")
    print(f"User1 has earned {rewards} $ZUSHI reward tokens.")

    unstaked_amount, earned_rewards = staking_contract.unstake_tokens("user1")
    print(f"User1 unstaked {unstaked_amount} tokens and earned {earned_rewards} reward tokens.")
```
