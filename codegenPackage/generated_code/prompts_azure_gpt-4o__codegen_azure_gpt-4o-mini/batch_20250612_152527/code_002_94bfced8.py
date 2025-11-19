"""
Generated Code Metadata:
========================
Original URL: https://app-virtuswap.pages.dev
Prompt: Write code to simulate a staking mechanism for a DeFi application, inspired by the Virtuswap staking functionality.
Generated: DETERMINISTIC_94bfced884177923
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from decimal import Decimal
from typing import Dict, List

class StakingPool:
    def __init__(self, pool_name: str, reward_rate: Decimal):
        """
        Initialize the staking pool with a name and a reward rate.

        :param pool_name: Name of the staking pool
        :param reward_rate: Reward rate per staked token (as a decimal)
        """
        self.pool_name = pool_name
        self.reward_rate = reward_rate
        self.stakers: Dict[str, Decimal] = {}  # Maps staker address to staked amount
        self.rewards: Dict[str, Decimal] = {}  # Maps staker address to earned rewards

    def stake(self, staker_address: str, amount: Decimal) -> None:
        """
        Allow a user to stake a certain amount of tokens.

        :param staker_address: Address of the staker
        :param amount: Amount of tokens to stake
        :raises ValueError: If the amount is non-positive
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")

        # Update staker's staked amount
        if staker_address in self.stakers:
            self.stakers[staker_address] += amount
        else:
            self.stakers[staker_address] = amount

        # Initialize rewards for the staker if not already present
        if staker_address not in self.rewards:
            self.rewards[staker_address] = Decimal(0)

    def unstake(self, staker_address: str, amount: Decimal) -> None:
        """
        Allow a user to unstake a certain amount of tokens.

        :param staker_address: Address of the staker
        :param amount: Amount of tokens to unstake
        :raises ValueError: If the amount is non-positive or exceeds staked amount
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be positive.")
        if staker_address not in self.stakers or self.stakers[staker_address] < amount:
            raise ValueError("Insufficient staked amount to unstake.")

        # Deduct the unstaked amount
        self.stakers[staker_address] -= amount

        # If the staker has no more staked tokens, remove them from the pool
        if self.stakers[staker_address] == 0:
            del self.stakers[staker_address]

    def calculate_rewards(self, staker_address: str) -> Decimal:
        """
        Calculate the rewards for a staker based on their staked amount.

        :param staker_address: Address of the staker
        :return: Total rewards earned by the staker
        """
        if staker_address not in self.stakers:
            return Decimal(0)

        # Calculate rewards based on the staked amount and reward rate
        staked_amount = self.stakers[staker_address]
        rewards = staked_amount * self.reward_rate
        self.rewards[staker_address] += rewards  # Update total rewards
        return self.rewards[staker_address]

    def get_staked_amount(self, staker_address: str) -> Decimal:
        """
        Get the total staked amount for a staker.

        :param staker_address: Address of the staker
        :return: Total staked amount
        """
        return self.stakers.get(staker_address, Decimal(0))

    def get_rewards(self, staker_address: str) -> Decimal:
        """
        Get the total rewards for a staker.

        :param staker_address: Address of the staker
        :return: Total rewards earned by the staker
        """
        return self.rewards.get(staker_address, Decimal(0))


# Example usage
if __name__ == "__main__":
    # Create a staking pool with a reward rate of 0.05 (5%)
    staking_pool = StakingPool("Virtuswap Staking Pool", Decimal("0.05"))

    # Staking tokens
    staking_pool.stake("user1", Decimal("100"))
    staking_pool.stake("user2", Decimal("200"))

    # Calculate rewards for user1
    rewards_user1 = staking_pool.calculate_rewards("user1")
    print(f"User1 Rewards: {rewards_user1}")

    # Unstake some tokens
    staking_pool.unstake("user1", Decimal("50"))

    # Get staked amount and rewards for user1
    staked_amount_user1 = staking_pool.get_staked_amount("user1")
    total_rewards_user1 = staking_pool.get_rewards("user1")
    print(f"User1 Staked Amount: {staked_amount_user1}, Total Rewards: {total_rewards_user1}")
```
