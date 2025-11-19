"""
Generated Code Metadata:
========================
Original URL: https://blastup-io.pages.dev
Prompt: Create a function to simulate staking BlastUP tokens and calculate rewards based on the tier system described (e.g., Bronze, Silver, Gold, etc.).
Generated: DETERMINISTIC_137b531f1e8e0c44
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Dict, Tuple

class Tier(Enum):
    """Enum representing different staking tiers."""
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4
    DIAMOND = 5

class StakingSimulator:
    """
    A class to simulate staking BlastUP tokens and calculate rewards based on tiers.
    
    Attributes:
        tier_thresholds (Dict[Tier, int]): Minimum staked amount required for each tier.
        reward_rates (Dict[Tier, float]): Annual reward rate for each tier.
        staked_amount (float): Amount of tokens currently staked.
        current_tier (Tier): Current tier based on staked amount.
    """
    
    def __init__(self):
        """Initialize the staking simulator with tier thresholds and reward rates."""
        self.tier_thresholds = {
            Tier.BRONZE: 1000,
            Tier.SILVER: 5000,
            Tier.GOLD: 10000,
            Tier.PLATINUM: 50000,
            Tier.DIAMOND: 100000
        }
        
        self.reward_rates = {
            Tier.BRONZE: 0.05,   # 5%
            Tier.SILVER: 0.075,  # 7.5%
            Tier.GOLD: 0.10,     # 10%
            Tier.PLATINUM: 0.125, # 12.5%
            Tier.DIAMOND: 0.15    # 15%
        }
        
        self.staked_amount = 0.0
        self.current_tier = Tier.BRONZE
    
    def stake_tokens(self, amount: float) -> None:
        """
        Stake a specified amount of tokens and update the current tier.
        
        Args:
            amount (float): Amount of tokens to stake.
            
        Raises:
            ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Staked amount must be positive.")
        
        self.staked_amount += amount
        self._update_tier()
    
    def unstake_tokens(self, amount: float) -> None:
        """
        Unstake a specified amount of tokens and update the current tier.
        
        Args:
            amount (float): Amount of tokens to unstake.
            
        Raises:
            ValueError: If the amount is not positive or exceeds staked amount.
        """
        if amount <= 0:
            raise ValueError("Unstaked amount must be positive.")
        if amount > self.staked_amount:
            raise ValueError("Cannot unstake more than the staked amount.")
        
        self.staked_amount -= amount
        self._update_tier()
    
    def _update_tier(self) -> None:
        """Update the current tier based on the staked amount."""
        self.current_tier = Tier.BRONZE
        for tier, threshold in sorted(self.tier_thresholds.items(), key=lambda x: x[1], reverse=True):
            if self.staked_amount >= threshold:
                self.current_tier = tier
                break
    
    def calculate_rewards(self, days: int) -> float:
        """
        Calculate the rewards for a given number of days based on the current tier.
        
        Args:
            days (int): Number of days to calculate rewards for.
            
        Returns:
            float: Calculated rewards.
            
        Raises:
            ValueError: If days is not positive.
        """
        if days <= 0:
            raise ValueError("Days must be positive.")
        
        annual_rate = self.reward_rates[self.current_tier]
        daily_rate = annual_rate / 365
        rewards = self.staked_amount * daily_rate * days
        return rewards
    
    def get_current_tier_info(self) -> Tuple[Tier, float]:
        """
        Get the current tier and its reward rate.
        
        Returns:
            Tuple[Tier, float]: Current tier and its reward rate.
        """
        return (self.current_tier, self.reward_rates[self.current_tier])

# Example usage
if __name__ == "__main__":
    simulator = StakingSimulator()
    
    try:
        simulator.stake_tokens(3000)
        print(f"Staked: {simulator.staked_amount}")
        
        tier, rate = simulator.get_current_tier_info()
        print(f"Current Tier: {tier.name}, Reward Rate: {rate * 100}%")
        
        rewards = simulator.calculate_rewards(30)
        print(f"Estimated rewards for 30 days: {rewards:.2f} tokens")
        
    except ValueError as e:
        print(f"Error: {e}")
```
