"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: Propose a tokenomics model for PrivateAI (PGPT) incorporating revenue streams from DAO operations, staking, AI queries, and data marketplace transactions.
Generated: DETERMINISTIC_ec04e5f7f28b973b
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
# PrivateAI (PGPT) Tokenomics Model
# Includes DAO operations, staking, AI queries, and data marketplace transactions

from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum, auto
import math

class TokenType(Enum):
    """Types of tokens in the ecosystem"""
    UTILITY = auto()  # PGPT utility token
    GOVERNANCE = auto()  # DAO governance token
    STAKING = auto()  # Staking rewards token

class RevenueStream(Enum):
    """Different revenue streams for the protocol"""
    DAO_OPERATIONS = auto()
    STAKING = auto()
    AI_QUERIES = auto()
    DATA_MARKETPLACE = auto()

@dataclass
class TokenAllocation:
    """Represents allocation of tokens to different pools"""
    allocation_name: str
    percentage: float
    vesting_period: int  # in months
    initial_unlock: float  # percentage initially unlocked

@dataclass
class RevenueDistribution:
    """How revenue is distributed among stakeholders"""
    stream: RevenueStream
    dao_treasury_percent: float
    staking_rewards_percent: float
    burn_percent: float
    team_percent: float
    liquidity_providers_percent: float

class PrivateAITokenomics:
    """Implements the tokenomics model for PrivateAI (PGPT)"""
    
    def __init__(self):
        self.total_supply = 1_000_000_000  # 1 billion tokens
        self.token_allocations = self._initialize_token_allocations()
        self.revenue_distributions = self._initialize_revenue_distributions()
        self.staking_apr = 0.15  # 15% APR for staking
        
    def _initialize_token_allocations(self) -> List[TokenAllocation]:
        """Initialize the token allocation pools"""
        return [
            TokenAllocation("DAO Treasury", 0.30, 24, 0.10),
            TokenAllocation("Team", 0.20, 36, 0.05),
            TokenAllocation("Ecosystem Growth", 0.25, 18, 0.15),
            TokenAllocation("Staking Rewards", 0.15, 0, 1.00),  # No vesting
            TokenAllocation("Liquidity", 0.10, 6, 0.50)
        ]
    
    def _initialize_revenue_distributions(self) -> List[RevenueDistribution]:
        """Initialize revenue distribution models"""
        return [
            RevenueDistribution(
                RevenueStream.DAO_OPERATIONS,
                dao_treasury_percent=0.40,
                staking_rewards_percent=0.30,
                burn_percent=0.10,
                team_percent=0.15,
                liquidity_providers_percent=0.05
            ),
            RevenueDistribution(
                RevenueStream.STAKING,
                dao_treasury_percent=0.20,
                staking_rewards_percent=0.60,
                burn_percent=0.05,
                team_percent=0.10,
                liquidity_providers_percent=0.05
            ),
            RevenueDistribution(
                RevenueStream.AI_QUERIES,
                dao_treasury_percent=0.30,
                staking_rewards_percent=0.40,
                burn_percent=0.10,
                team_percent=0.15,
                liquidity_providers_percent=0.05
            ),
            RevenueDistribution(
                RevenueStream.DATA_MARKETPLACE,
                dao_treasury_percent=0.25,
                staking_rewards_percent=0.35,
                burn_percent=0.15,
                team_percent=0.20,
                liquidity_providers_percent=0.05
            )
        ]
    
    def calculate_allocation(self, allocation_name: str) -> float:
        """Calculate token amount for a specific allocation"""
        for alloc in self.token_allocations:
            if alloc.allocation_name == allocation_name:
                return self.total_supply * alloc.percentage
        raise ValueError(f"Allocation {allocation_name} not found")
    
    def calculate_revenue_distribution(
        self, 
        stream: RevenueStream, 
        revenue_amount: float
    ) -> Dict[str, float]:
        """Calculate distribution of revenue for a given stream"""
        for dist in self.revenue_distributions:
            if dist.stream == stream:
                return {
                    "dao_treasury": revenue_amount * dist.dao_treasury_percent,
                    "staking_rewards": revenue_amount * dist.staking_rewards_percent,
                    "burn": revenue_amount * dist.burn_percent,
                    "team": revenue_amount * dist.team_percent,
                    "liquidity_providers": revenue_amount * dist.liquidity_providers_percent
                }
        raise ValueError(f"Revenue stream {stream} not found")
    
    def calculate_staking_rewards(
        self, 
        staked_amount: float, 
        duration_days: float
    ) -> float:
        """Calculate staking rewards for a given amount and duration"""
        if staked_amount <= 0:
            raise ValueError("Staked amount must be positive")
        if duration_days <= 0:
            raise ValueError("Duration must be positive")
        
        annual_rate = self.staking_apr
        daily_rate = annual_rate / 365
        return staked_amount * daily_rate * duration_days
    
    def calculate_vested_tokens(
        self, 
        allocation_name: str, 
        months_passed: int
    ) -> float:
        """Calculate vested tokens for an allocation after months passed"""
        for alloc in self.token_allocations:
            if alloc.allocation_name == allocation_name:
                if alloc.vesting_period == 0:
                    return self.calculate_allocation(allocation_name)
                
                if months_passed <= 0:
                    return 0
                
                initial_unlock = self.calculate_allocation(allocation_name) * alloc.initial_unlock
                if months_passed >= alloc.vesting_period:
                    return self.calculate_allocation(allocation_name)
                
                remaining_tokens = self.calculate_allocation(allocation_name) - initial_unlock
                vested = initial_unlock + (remaining_tokens * (months_passed / alloc.vesting_period))
                return vested
        raise ValueError(f"Allocation {allocation_name} not found")

# Example usage
if __name__ == "__main__":
    tokenomics = PrivateAITokenomics()
    
    # Example calculations
    dao_allocation = tokenomics.calculate_allocation("DAO Treasury")
    print(f"DAO Treasury Allocation: {dao_allocation:,.2f} PGPT")
    
    revenue_dist = tokenomics.calculate_revenue_distribution(
        RevenueStream.AI_QUERIES,
        1_000_000  # $1M revenue
    )
    print("\nAI Query Revenue Distribution:")
    for key, value in revenue_dist.items():
        print(f"{key}: ${value:,.2f}")
    
    staking_rewards = tokenomics.calculate_staking_rewards(
        10_000,  # 10,000 PGPT staked
        30  # 30 days
    )
    print(f"\nStaking Rewards for 30 days: {staking_rewards:,.2f} PGPT")
    
    vested_tokens = tokenomics.calculate_vested_tokens(
        "Team",
        12  # After 12 months
    )
    print(f"\nTeam Vested Tokens after 12 months: {vested_tokens:,.2f} PGPT")
```
