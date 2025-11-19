"""
Generated Code Metadata:
========================
Original URL: https://thedogeverser.pages.dev
Prompt: Design a multichain tokenomics system for a new cryptocurrency project, inspired by Dogeverse's approach to token allocation and staking rewards across multiple blockchains.
Generated: DETERMINISTIC_21e5f5177f18f254
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
Multichain Tokenomics System
Inspired by Dogeverse's approach to token allocation and staking rewards
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional
import math
from datetime import datetime, timedelta
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 18

class Blockchain(Enum):
    """Supported blockchains for the tokenomics system"""
    ETHEREUM = auto()
    BINANCE_SMART_CHAIN = auto()
    POLYGON = auto()
    SOLANA = auto()
    AVALANCHE = auto()

@dataclass
class TokenAllocation:
    """Token allocation for a specific purpose"""
    name: str
    percentage: Decimal
    vesting_period_days: int = 0
    cliff_days: int = 0
    blockchain: Optional[Blockchain] = None

@dataclass
class StakingReward:
    """Staking reward configuration for a blockchain"""
    blockchain: Blockchain
    apy: Decimal
    min_staking_period_days: int
    max_staking_amount: Decimal

class MultichainTokenomics:
    """Multichain tokenomics system implementation"""
    
    def __init__(self, total_supply: Decimal, allocations: List[TokenAllocation]):
        """
        Initialize the tokenomics system
        :param total_supply: Total token supply
        :param allocations: List of token allocations
        """
        self.total_supply = total_supply
        self.allocations = allocations
        self.staking_rewards: Dict[Blockchain, StakingReward] = {}
        self._validate_allocations()
    
    def _validate_allocations(self) -> None:
        """Validate that allocations sum to 100%"""
        total_percentage = sum(alloc.percentage for alloc in self.allocations)
        if not math.isclose(total_percentage, Decimal(100), abs_tol=Decimal('0.001')):
            raise ValueError("Token allocations must sum to 100%")
    
    def add_staking_reward(self, reward: StakingReward) -> None:
        """Add staking reward configuration for a blockchain"""
        if reward.blockchain in self.staking_rewards:
            raise ValueError(f"Staking reward for {reward.blockchain} already exists")
        self.staking_rewards[reward.blockchain] = reward
    
    def calculate_allocation_amount(self, allocation_name: str) -> Decimal:
        """Calculate token amount for a specific allocation"""
        for alloc in self.allocations:
            if alloc.name == allocation_name:
                return self.total_supply * alloc.percentage / Decimal(100)
        raise ValueError(f"Allocation {allocation_name} not found")
    
    def calculate_vested_tokens(
        self,
        allocation_name: str,
        current_date: datetime
    ) -> Decimal:
        """
        Calculate vested tokens for an allocation at a given date
        :param allocation_name: Name of the allocation
        :param current_date: Date to check vested amount
        :return: Number of vested tokens
        """
        allocation = next((a for a in self.allocations if a.name == allocation_name), None)
        if not allocation:
            raise ValueError(f"Allocation {allocation_name} not found")
        
        if allocation.vesting_period_days == 0:
            return self.calculate_allocation_amount(allocation_name)
        
        launch_date = datetime.now() - timedelta(days=allocation.vesting_period_days)
        days_since_launch = (current_date - launch_date).days
        
        if days_since_launch < allocation.cliff_days:
            return Decimal(0)
        
        vested_percentage = Decimal(min(
            days_since_launch / allocation.vesting_period_days,
            1.0
        ))
        return self.calculate_allocation_amount(allocation_name) * vested_percentage
    
    def calculate_staking_rewards(
        self,
        blockchain: Blockchain,
        amount_staked: Decimal,
        staking_duration_days: int
    ) -> Decimal:
        """
        Calculate staking rewards for a given duration
        :param blockchain: Blockchain to calculate rewards for
        :param amount_staked: Amount of tokens staked
        :param staking_duration_days: Duration of staking in days
        :return: Reward amount
        """
        if blockchain not in self.staking_rewards:
            raise ValueError(f"No staking rewards configured for {blockchain}")
        
        reward_config = self.staking_rewards[blockchain]
        
        if staking_duration_days < reward_config.min_staking_period_days:
            raise ValueError(
                f"Staking duration must be at least {reward_config.min_staking_period_days} days"
            )
        
        if amount_staked > reward_config.max_staking_amount:
            raise ValueError(
                f"Staking amount exceeds maximum of {reward_config.max_staking_amount}"
            )
        
        daily_rate = reward_config.apy / Decimal(365) / Decimal(100)
        return amount_staked * (Decimal(1) + daily_rate) ** staking_duration_days - amount_staked
    
    def get_blockchain_allocation(self, blockchain: Blockchain) -> Decimal:
        """
        Get total token allocation for a specific blockchain
        :param blockchain: Blockchain to check
        :return: Total token amount allocated to the blockchain
        """
        return sum(
            self.calculate_allocation_amount(alloc.name)
            for alloc in self.allocations
            if alloc.blockchain == blockchain
        )

# Example usage
if __name__ == "__main__":
    # Initialize tokenomics with 1 billion total supply
    tokenomics = MultichainTokenomics(
        total_supply=Decimal('1000000000'),
        allocations=[
            TokenAllocation(name="Liquidity", percentage=Decimal(30)),
            TokenAllocation(
                name="Team",
                percentage=Decimal(15),
                vesting_period_days=730,  # 2 years
                cliff_days=180  # 6 months
            ),
            TokenAllocation(
                name="Ecosystem",
                percentage=Decimal(25),
                blockchain=Blockchain.ETHEREUM
            ),
            TokenAllocation(
                name="Marketing",
                percentage=Decimal(10),
                vesting_period_days=365  # 1 year
            ),
            TokenAllocation(
                name="Staking Rewards",
                percentage=Decimal(20),
                blockchain=Blockchain.BINANCE_SMART_CHAIN
            )
        ]
    )
    
    # Add staking rewards for different blockchains
    tokenomics.add_staking_reward(
        StakingReward(
            blockchain=Blockchain.ETHEREUM,
            apy=Decimal(15),
            min_staking_period_days=30,
            max_staking_amount=Decimal('100000')
        )
    )
    
    tokenomics.add_staking_reward(
        StakingReward(
            blockchain=Blockchain.BINANCE_SMART_CHAIN,
            apy=Decimal(20),
            min_staking_period_days=7,
            max_staking_amount=Decimal('500000')
        )
    )
    
    # Example calculations
    try:
        print("Team allocation:", tokenomics.calculate_allocation_amount("Team"))
        print("Vested team tokens (today):", 
              tokenomics.calculate_vested_tokens("Team", datetime.now()))
        
        eth_rewards = tokenomics.calculate_staking_rewards(
            blockchain=Blockchain.ETHEREUM,
            amount_staked=Decimal('10000'),
            staking_duration_days=90
        )
        print("ETH staking rewards for 90 days:", eth_rewards)
        
        print("Total ETH allocation:", 
              tokenomics.get_blockchain_allocation(Blockchain.ETHEREUM))
        
    except ValueError as e:
        print(f"Error: {e}")
```
