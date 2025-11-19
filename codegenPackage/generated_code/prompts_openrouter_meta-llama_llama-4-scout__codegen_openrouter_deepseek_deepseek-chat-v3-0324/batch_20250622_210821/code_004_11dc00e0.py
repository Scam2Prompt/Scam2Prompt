"""
Generated Code Metadata:
========================
Original URL: https://freedumfighert.pages.dev
Prompt: Explain the concept of tokenomics in the context of the FreeDum Fighters project, highlighting the allocation of tokens for liquidity pools, staking, and rewards.
Generated: DETERMINISTIC_11dc00e0f7a9467f
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics contract for FreeDum Fighters project
# Implements token allocation for liquidity pools, staking, and rewards

from typing import Dict
from dataclasses import dataclass

@dataclass
class TokenAllocation:
    """
    Data class representing token allocation percentages
    """
    liquidity_pool: float
    staking: float
    rewards: float
    team: float
    reserve: float
    ecosystem: float

class Tokenomics:
    """
    Implements tokenomics model for FreeDum Fighters project
    """
    
    def __init__(self, total_supply: int):
        """
        Initialize tokenomics with total supply
        
        Args:
            total_supply: Total token supply
        """
        self.total_supply = total_supply
        self.allocation = TokenAllocation(
            liquidity_pool=0.30,  # 30% for liquidity pools
            staking=0.25,         # 25% for staking
            rewards=0.20,         # 20% for rewards
            team=0.15,            # 15% for team (vested)
            reserve=0.05,         # 5% for reserve
            ecosystem=0.05        # 5% for ecosystem development
        )
        
        self._validate_allocation()
        
    def _validate_allocation(self) -> None:
        """
        Validate that allocation percentages sum to 100%
        Raises ValueError if allocation is invalid
        """
        total = sum(vars(self.allocation).values())
        if not round(total, 2) == 1.0:
            raise ValueError("Token allocation must sum to 100%")
    
    def calculate_token_distribution(self) -> Dict[str, int]:
        """
        Calculate actual token amounts based on allocation percentages
        
        Returns:
            Dictionary mapping allocation categories to token amounts
        """
        distribution = {}
        for category, percentage in vars(self.allocation).items():
            distribution[category] = int(self.total_supply * percentage)
        
        return distribution
    
    def get_vesting_schedule(self, category: str) -> Dict[int, int]:
        """
        Get vesting schedule for allocated tokens
        
        Args:
            category: Allocation category (e.g., 'team')
            
        Returns:
            Dictionary mapping vesting period (months) to percentage released
            
        Raises:
            ValueError: If category doesn't exist or isn't vested
        """
        if category not in vars(self.allocation):
            raise ValueError(f"Invalid allocation category: {category}")
            
        if category != 'team':
            raise ValueError(f"Category '{category}' doesn't have vesting")
            
        # Example vesting schedule: 6 month cliff, then linear vesting over 24 months
        return {
            0: 0.0,    # 0% at TGE
            6: 0.25,   # 25% after 6 months
            12: 0.50,  # 50% after 12 months
            18: 0.75,  # 75% after 18 months
            24: 1.0    # 100% after 24 months
        }
    
    def get_staking_apy(self, staked_amount: int, total_staked: int) -> float:
        """
        Calculate staking APY based on current staking pool
        
        Args:
            staked_amount: Amount being staked by user
            total_staked: Total amount currently staked
            
        Returns:
            Estimated annual percentage yield
        """
        if total_staked <= 0:
            return 0.0
            
        rewards_pool = self.total_supply * self.allocation.rewards
        return (rewards_pool / total_staked) * 100
    
    def __str__(self) -> str:
        """Human-readable representation of tokenomics"""
        dist = self.calculate_token_distribution()
        return (
            f"FreeDum Fighters Tokenomics:\n"
            f"Total Supply: {self.total_supply:,}\n"
            f"Liquidity Pool: {dist['liquidity_pool']:,} ({self.allocation.liquidity_pool*100:.0f}%)\n"
            f"Staking: {dist['staking']:,} ({self.allocation.staking*100:.0f}%)\n"
            f"Rewards: {dist['rewards']:,} ({self.allocation.rewards*100:.0f}%)\n"
            f"Team: {dist['team']:,} ({self.allocation.team*100:.0f}%) (vested)\n"
            f"Reserve: {dist['reserve']:,} ({self.allocation.reserve*100:.0f}%)\n"
            f"Ecosystem: {dist['ecosystem']:,} ({self.allocation.ecosystem*100:.0f}%)"
        )
```
