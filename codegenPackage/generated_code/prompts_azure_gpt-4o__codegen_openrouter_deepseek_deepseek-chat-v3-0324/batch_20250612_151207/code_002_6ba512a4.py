"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Generate code to calculate and display token staking rewards for a platform with fixed token supply and a profit-sharing model, as described in Blockchain Bets.
Generated: DETERMINISTIC_6ba512a42f846ab6
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Staker:
    """Represents a staker with their stake amount and duration."""
    address: str
    amount: float
    duration: int  # in days

@dataclass
class RewardParameters:
    """Parameters for reward calculation."""
    total_supply: float
    annual_reward_rate: float  # as percentage (e.g., 10 for 10%)
    min_stake_duration: int  # in days
    max_stake_duration: int  # in days

class StakingRewardCalculator:
    """
    Calculates staking rewards based on a fixed token supply and profit-sharing model.
    Implements duration-based reward multipliers.
    """
    
    def __init__(self, params: RewardParameters):
        self.params = params
        self._validate_parameters()
    
    def _validate_parameters(self):
        """Validate reward parameters."""
        if self.params.total_supply <= 0:
            raise ValueError("Total supply must be positive")
        if not (0 < self.params.annual_reward_rate <= 100):
            raise ValueError("Annual reward rate must be between 0 and 100")
        if self.params.min_stake_duration <= 0:
            raise ValueError("Minimum stake duration must be positive")
        if self.params.max_stake_duration < self.params.min_stake_duration:
            raise ValueError("Max stake duration must be >= min stake duration")
    
    def calculate_daily_reward_pool(self) -> float:
        """Calculate the daily reward pool based on annual reward rate."""
        annual_reward = (self.params.annual_reward_rate / 100) * self.params.total_supply
        return annual_reward / 365
    
    def calculate_duration_multiplier(self, duration: int) -> float:
        """
        Calculate the duration multiplier for rewards.
        Linear scaling between min and max duration.
        """
        if duration < self.params.min_stake_duration:
            return 0.0
        
        normalized_duration = min(duration, self.params.max_stake_duration)
        min_multiplier = 1.0
        max_multiplier = 2.0  # 2x for max duration
        
        if self.params.min_stake_duration == self.params.max_stake_duration:
            return max_multiplier
        
        return min_multiplier + (
            (normalized_duration - self.params.min_stake_duration) / 
            (self.params.max_stake_duration - self.params.min_stake_duration)
        ) * (max_multiplier - min_multiplier)
    
    def calculate_staker_rewards(
        self, 
        stakers: List[Staker], 
        days_elapsed: int
    ) -> Dict[str, float]:
        """
        Calculate rewards for all stakers.
        
        Args:
            stakers: List of stakers
            days_elapsed: Number of days since staking began
            
        Returns:
            Dictionary mapping staker addresses to their rewards
        """
        if days_elapsed <= 0:
            raise ValueError("Days elapsed must be positive")
        
        daily_reward_pool = self.calculate_daily_reward_pool()
        total_weighted_stake = 0.0
        stake_details = []
        
        # Calculate weighted stakes
        for staker in stakers:
            if staker.amount <= 0:
                continue
                
            effective_duration = min(staker.duration, days_elapsed)
            multiplier = self.calculate_duration_multiplier(effective_duration)
            weighted_stake = staker.amount * multiplier
            total_weighted_stake += weighted_stake
            stake_details.append((staker.address, weighted_stake))
        
        if total_weighted_stake == 0:
            return {}
        
        # Distribute rewards proportionally
        rewards = {}
        for address, weighted_stake in stake_details:
            share = weighted_stake / total_weighted_stake
            rewards[address] = share * daily_reward_pool * days_elapsed
        
        return rewards

def display_rewards(rewards: Dict[str, float], token_symbol: str = "BBT"):
    """Display rewards in a user-friendly format."""
    print(f"\n{'Address':<42} {'Reward':>15}")
    print("-" * 60)
    for address, reward in rewards.items():
        print(f"{address:<42} {reward:>15.4f} {token_symbol}")
    print("-" * 60)
    total = sum(rewards.values())
    print(f"{'Total Rewards Distributed':<42} {total:>15.4f} {token_symbol}\n")

# Example usage
if __name__ == "__main__":
    # Configuration
    params = RewardParameters(
        total_supply=1_000_000,  # 1 million tokens
        annual_reward_rate=10.0,  # 10% annual reward
        min_stake_duration=30,    # 30 days minimum
        max_stake_duration=365    # 1 year maximum
    )
    
    # Sample stakers
    stakers = [
        Staker("0x123...abc", 5000, 90),
        Staker("0x456...def", 10000, 180),
        Staker("0x789...ghi", 25000, 365),
        Staker("0xabc...123", 500, 15)  # Will get 0 reward (below min duration)
    ]
    
    calculator = StakingRewardCalculator(params)
    rewards = calculator.calculate_staker_rewards(stakers, days_elapsed=90)
    
    display_rewards(rewards)
```
