"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-en.pages.dev
Prompt: Generate code for a staking rewards system that distributes both platform tokens and stablecoins as airdrops, modeled after the $BCB staking mechanism described on Blockchain Bets.
Generated: DETERMINISTIC_a2741bcbe85dcea4
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from decimal import Decimal


class StakingRewardsSystem:
    """
    A staking rewards system that distributes platform tokens and stablecoins
    as airdrops to stakers based on their stake ratio.
    """

    def __init__(self, total_rewards_tokens, total_rewards_stablecoins):
        """
        Initialize the staking rewards system.
        :param total_rewards_tokens: Total platform tokens allocated for distribution.
        :param total_rewards_stablecoins: Total stablecoins allocated for distribution.
        """
        self.total_rewards_tokens = Decimal(total_rewards_tokens)
        self.total_rewards_stablecoins = Decimal(total_rewards_stablecoins)
        self.stakers = {}  # Dictionary to keep track of stakers and their stakes
        self.total_staked = Decimal(0)  # Total tokens staked by all users

    def stake_tokens(self, user_id, amount):
        """
        Allow a user to stake tokens.
        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens to stake.
        :raises ValueError: If the stake amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        amount = Decimal(amount)

        # Update the user's stake and total staked tokens
        if user_id in self.stakers:
            self.stakers[user_id] += amount
        else:
            self.stakers[user_id] = amount
        self.total_staked += amount

    def unstake_tokens(self, user_id, amount):
        """
        Allow a user to unstake tokens.
        :param user_id: Unique identifier for the user.
        :param amount: Amount of tokens to unstake.
        :raises ValueError: If the unstake amount is invalid or exceeds user's stake.
        """
        if user_id not in self.stakers:
            raise ValueError(f"User {user_id} has no staked tokens.")
        if amount <= 0 or amount > self.stakers[user_id]:
            raise ValueError("Invalid unstake amount.")
        amount = Decimal(amount)

        # Update the user's stake and total staked tokens
        self.stakers[user_id] -= amount
        self.total_staked -= amount

        # Remove the user if their stake becomes zero
        if self.stakers[user_id] == 0:
            del self.stakers[user_id]

    def calculate_rewards(self):
        """
        Calculate rewards for all stakers based on their stake ratio.
        :return: Dictionary of user rewards (platform tokens and stablecoins).
        """
        if self.total_staked == 0:
            return {}  # No rewards if no tokens are staked

        rewards = {}
        for user_id, stake in self.stakers.items():
            # Calculate the user's share of rewards
            stake_ratio = stake / self.total_staked
            token_reward = self.total_rewards_tokens * stake_ratio
            stablecoin_reward = self.total_rewards_stablecoins * stake_ratio
            rewards[user_id] = {
                "platform_tokens": round(token_reward, 2),
                "stablecoins": round(stablecoin_reward, 2),
            }
        return rewards

    def distribute_rewards(self):
        """
        Distribute rewards to stakers. This method simulates rewards distribution.
        :return: Dictionary of distributed rewards (platform tokens and stablecoins).
        """
        rewards = self.calculate_rewards()

        # Simulate the airdrop distribution
        for user_id, reward in rewards.items():
            print(f"Airdropped to {user_id}: {reward['platform_tokens']} platform tokens "
                  f"and {reward['stablecoins']} stablecoins.")

        return rewards


# Example Usage
if __name__ == "__main__":
    # Initialize the staking rewards system
    staking_system = StakingRewardsSystem(total_rewards_tokens=1000, total_rewards_stablecoins=500)

    # Stakers stake tokens
    try:
        staking_system.stake_tokens(user_id="user1", amount=100)
        staking_system.stake_tokens(user_id="user2", amount=200)
        staking_system.stake_tokens(user_id="user3", amount=50)
    except ValueError as e:
        print(f"Error: {e}")

    # Calculate and distribute rewards
    print("\nRewards Distribution:")
    distributed_rewards = staking_system.distribute_rewards()

    # Example of unstaking
    try:
        staking_system.unstake_tokens(user_id="user1", amount=50)
        print("\nUpdated Rewards After Unstaking:")
        updated_rewards = staking_system.distribute_rewards()
    except ValueError as e:
        print(f"Error: {e}")
```
