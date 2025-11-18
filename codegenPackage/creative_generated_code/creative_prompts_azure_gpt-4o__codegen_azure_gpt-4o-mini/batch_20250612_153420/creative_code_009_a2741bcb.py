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
from decimal import Decimal, getcontext
from typing import Dict, List

# Set the precision for Decimal operations
getcontext().prec = 18

class StakingRewardsSystem:
    def __init__(self):
        self.stakers: Dict[str, Decimal] = {}  # Mapping of user addresses to staked amounts
        self.rewards: Dict[str, Decimal] = {}  # Mapping of user addresses to accumulated rewards
        self.platform_token_rewards_per_stake = Decimal('0.1')  # Example reward rate per stake
        self.stablecoin_rewards_per_stake = Decimal('0.05')  # Example reward rate per stake
        self.last_distribution_time: float = time.time()  # Timestamp of the last reward distribution
        self.reward_distribution_interval: int = 3600  # Reward distribution every hour (3600 seconds)

    def stake(self, user_address: str, amount: Decimal) -> None:
        """Allow a user to stake a specified amount of tokens."""
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        # Update staked amount and rewards
        self.stakers[user_address] = self.stakers.get(user_address, Decimal('0')) + amount
        self.rewards[user_address] = self.rewards.get(user_address, Decimal('0'))

        print(f"User {user_address} has staked {amount} tokens. Total staked: {self.stakers[user_address]}")

    def distribute_rewards(self) -> None:
        """Distribute rewards to all stakers based on their stakes."""
        current_time = time.time()
        if current_time - self.last_distribution_time < self.reward_distribution_interval:
            print("Rewards distribution is not ready yet. Please wait.")
            return
        
        for user_address, staked_amount in self.stakers.items():
            # Calculate rewards based on staked amount
            platform_token_reward = staked_amount * self.platform_token_rewards_per_stake
            stablecoin_reward = staked_amount * self.stablecoin_rewards_per_stake
            
            # Update the user's rewards
            self.rewards[user_address] += platform_token_reward + stablecoin_reward
            
            print(f"Distributed rewards to {user_address}: {platform_token_reward} platform tokens, "
                  f"{stablecoin_reward} stablecoins. Total rewards: {self.rewards[user_address]}")
        
        self.last_distribution_time = current_time  # Update last distribution time

    def claim_rewards(self, user_address: str) -> Decimal:
        """Allow a user to claim their accumulated rewards."""
        if user_address not in self.rewards or self.rewards[user_address] <= 0:
            raise ValueError("No rewards available to claim.")
        
        claimed_amount = self.rewards[user_address]
        self.rewards[user_address] = Decimal('0')  # Reset rewards after claiming
        
        print(f"User {user_address} has claimed rewards: {claimed_amount}")
        return claimed_amount

# Example usage:
if __name__ == "__main__":
    staking_system = StakingRewardsSystem()
    
    try:
        staking_system.stake("user1", Decimal('100'))
        staking_system.stake("user2", Decimal('200'))
        
        # Simulate time delay for reward distribution
        time.sleep(staking_system.reward_distribution_interval + 1)
        
        staking_system.distribute_rewards()
        
        # Users claim their rewards
        staking_system.claim_rewards("user1")
        staking_system.claim_rewards("user2")
        
    except ValueError as e:
        print(f"Error: {e}")
```
