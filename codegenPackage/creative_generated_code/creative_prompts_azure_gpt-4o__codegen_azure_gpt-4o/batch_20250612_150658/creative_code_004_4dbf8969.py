"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supercore-7hg.pages.dev
Prompt: Write a script to enable staking functionality for PLS and 9MM tokens, including tracking rewards and pool stats.
Generated: DETERMINISTIC_4dbf89691fc35158
Batch ID: 20250612_150658
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

class StakingPool:
    """
    A class to manage staking functionality for PLS and 9MM tokens, including tracking rewards and pool stats.
    """
    def __init__(self, reward_rate_pls: float, reward_rate_9mm: float):
        """
        Initialize the staking pool with reward rates for each token.

        :param reward_rate_pls: Reward rate for PLS tokens (tokens per second).
        :param reward_rate_9mm: Reward rate for 9MM tokens (tokens per second).
        """
        self.staked_tokens = {'PLS': {}, '9MM': {}}  # Stores staked balances per user for PLS and 9MM
        self.rewards = {'PLS': {}, '9MM': {}}       # Stores accumulated rewards per user for PLS and 9MM
        self.reward_rates = {'PLS': reward_rate_pls, '9MM': reward_rate_9mm}
        self.last_update_time = time.time()         # Tracks the last time rewards were calculated

    def _update_rewards(self, token: str, user: str):
        """
        Internal method to update rewards for a specific user and token.

        :param token: The token type ('PLS' or '9MM').
        :param user: The user ID (e.g., wallet address or unique identifier).
        """
        current_time = time.time()
        if user in self.staked_tokens[token]:
            staked_amount = self.staked_tokens[token][user]
            elapsed_time = current_time - self.last_update_time

            # Calculate rewards based on elapsed time and reward rate
            new_rewards = elapsed_time * self.reward_rates[token] * staked_amount
            self.rewards[token][user] = self.rewards[token].get(user, 0) + new_rewards

        # Update the last update time
        self.last_update_time = current_time

    def stake_tokens(self, token: str, user: str, amount: float):
        """
        Allows a user to stake tokens.

        :param token: The token type ('PLS' or '9MM').
        :param user: The user ID (e.g., wallet address or unique identifier).
        :param amount: The amount of tokens to stake.
        """
        if token not in self.staked_tokens:
            raise ValueError("Invalid token type. Use 'PLS' or '9MM'.")

        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")

        # Update rewards before modifying the stake balance
        self._update_rewards(token, user)

        # Update the user's staked balance
        self.staked_tokens[token][user] = self.staked_tokens[token].get(user, 0) + amount

    def unstake_tokens(self, token: str, user: str, amount: float):
        """
        Allows a user to unstake tokens.

        :param token: The token type ('PLS' or '9MM').
        :param user: The user ID (e.g., wallet address or unique identifier).
        :param amount: The amount of tokens to unstake.
        """
        if token not in self.staked_tokens:
            raise ValueError("Invalid token type. Use 'PLS' or '9MM'.")

        if user not in self.staked_tokens[token] or self.staked_tokens[token][user] < amount:
            raise ValueError("Insufficient staked balance to unstake.")

        if amount <= 0:
            raise ValueError("Unstaking amount must be greater than zero.")

        # Update rewards before modifying the stake balance
        self._update_rewards(token, user)

        # Reduce the user's staked balance
        self.staked_tokens[token][user] -= amount

        # If the balance becomes zero, remove the user from the pool
        if self.staked_tokens[token][user] == 0:
            del self.staked_tokens[token][user]

    def claim_rewards(self, token: str, user: str) -> float:
        """
        Allows a user to claim accumulated rewards.

        :param token: The token type ('PLS' or '9MM').
        :param user: The user ID (e.g., wallet address or unique identifier).
        :return: The amount of rewards claimed.
        """
        if token not in self.rewards or user not in self.rewards[token]:
            raise ValueError("No rewards available to claim.")

        # Update rewards before claiming
        self._update_rewards(token, user)

        # Retrieve and reset the user's rewards
        claimed_rewards = self.rewards[token].get(user, 0)
        self.rewards[token][user] = 0

        return claimed_rewards

    def get_pool_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Returns current staking pool stats, including total staked amounts and rewards.

        :return: A dictionary containing pool stats for both tokens.
        """
        stats = {
            'PLS': {
                'total_staked': sum(self.staked_tokens['PLS'].values()),
                'total_rewards': sum(self.rewards['PLS'].values()),
            },
            '9MM': {
                'total_staked': sum(self.staked_tokens['9MM'].values()),
                'total_rewards': sum(self.rewards['9MM'].values()),
            }
        }
        return stats


# Example usage:
if __name__ == "__main__":
    # Initialize staking pool with reward rates
    pool = StakingPool(reward_rate_pls=0.01, reward_rate_9mm=0.02)

    # Stake tokens
    pool.stake_tokens('PLS', 'user1', 100)
    pool.stake_tokens('9MM', 'user2', 200)

    # Simulate time passing
    time.sleep(5)

    # Claim rewards
    print("Rewards claimed by user1 (PLS):", pool.claim_rewards('PLS', 'user1'))
    print("Rewards claimed by user2 (9MM):", pool.claim_rewards('9MM', 'user2'))

    # Get pool stats
    print("Current pool stats:", pool.get_pool_stats())
```
