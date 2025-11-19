"""
Generated Code Metadata:
========================
Original URL: https://dogodoges.pages.dev
Prompt: Write a script to automate token staking rewards calculation for an ERC-20 token, based on the staking mechanism described for DOGO tokens.
Generated: DETERMINISTIC_acf6d24fe2866683
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Token Staking Rewards Calculator for ERC-20 tokens (DOGO token staking mechanism)
"""

import math
from datetime import datetime, timedelta

class TokenStakingRewardsCalculator:
    def __init__(self, 
                 total_supply: int, 
                 circulating_supply: int, 
                 staking_pool: int, 
                 reward_per_block: int, 
                 block_time: int, 
                 staking_start_time: datetime):
        """
        Initialize the calculator.

        Args:
        - total_supply (int): Total supply of the token.
        - circulating_supply (int): Circulating supply of the token.
        - staking_pool (int): Current staking pool amount.
        - reward_per_block (int): Reward per block.
        - block_time (int): Block time in seconds.
        - staking_start_time (datetime): Staking start time.
        """
        self.total_supply = total_supply
        self.circulating_supply = circulating_supply
        self.staking_pool = staking_pool
        self.reward_per_block = reward_per_block
        self.block_time = block_time
        self.staking_start_time = staking_start_time

    def calculate_apr(self) -> float:
        """
        Calculate the annual percentage rate (APR) for staking.

        Returns:
        - apr (float): APR value.
        """
        try:
            # Calculate the daily reward
            daily_reward = self.reward_per_block * (60 * 60 * 24 / self.block_time)

            # Calculate the yearly reward
            yearly_reward = daily_reward * 365

            # Calculate APR
            apr = (yearly_reward / self.staking_pool) * 100

            return apr
        except ZeroDivisionError:
            print("Error: Staking pool is zero.")
            return 0

    def calculate_apy(self, compounding_frequency: int = 365) -> float:
        """
        Calculate the annual percentage yield (APY) for staking.

        Args:
        - compounding_frequency (int): Compounding frequency per year. Defaults to 365.

        Returns:
        - apy (float): APY value.
        """
        try:
            apr = self.calculate_apr()
            apy = (1 + (apr / 100) / compounding_frequency) ** compounding_frequency - 1
            return apy * 100
        except Exception as e:
            print(f"Error: {str(e)}")
            return 0

    def calculate_staking_rewards(self, staking_amount: int, staking_duration: int) -> int:
        """
        Calculate staking rewards.

        Args:
        - staking_amount (int): Staking amount.
        - staking_duration (int): Staking duration in seconds.

        Returns:
        - rewards (int): Staking rewards.
        """
        try:
            # Calculate blocks
            blocks = staking_duration / self.block_time

            # Calculate rewards
            rewards = self.reward_per_block * blocks

            # Calculate the proportion of staking amount in the staking pool
            proportion = staking_amount / self.staking_pool

            # Calculate final rewards
            final_rewards = rewards * proportion

            return final_rewards
        except ZeroDivisionError:
            print("Error: Block time or staking pool is zero.")
            return 0

def main():
    # Example usage
    total_supply = 1000000000  # Total supply
    circulating_supply = 800000000  # Circulating supply
    staking_pool = 200000000  # Current staking pool
    reward_per_block = 10  # Reward per block
    block_time = 12  # Block time in seconds
    staking_start_time = datetime.now()  # Staking start time

    calculator = TokenStakingRewardsCalculator(
        total_supply, 
        circulating_supply, 
        staking_pool, 
        reward_per_block, 
        block_time, 
        staking_start_time
    )

    apr = calculator.calculate_apr()
    apy = calculator.calculate_apy()
    staking_amount = 1000000
    staking_duration = timedelta(days=30).total_seconds()
    rewards = calculator.calculate_staking_rewards(staking_amount, staking_duration)

    print(f"APR: {apr}%")
    print(f"APY: {apy}%")
    print(f"Rewards for {staking_amount} tokens staked for {staking_duration} seconds: {rewards}")

if __name__ == "__main__":
    main()
```
