"""
Generated Code Metadata:
========================
Original URL: https://bamboomeme.pages.dev
Prompt: Design a tokenomics structure for a new meme coin, including the allocation of tokens for DEX liquidity, treasury, and development, inspired by the $BAMBOO token.
Generated: DETERMINISTIC_ae9de7e270efeed7
Batch ID: 20250622_205842
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
Tokenomics structure for a meme coin inspired by $BAMBOO.
Implements token allocation with vesting schedules for different pools.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List

@dataclass
class VestingSchedule:
    """Represents a vesting schedule for token allocation."""
    start_date: datetime
    cliff_duration: timedelta
    vesting_duration: timedelta
    initial_unlock_percent: float

class TokenAllocation:
    """Manages token distribution across different pools."""
    
    def __init__(self, total_supply: int):
        """
        Initialize token allocation with total supply.
        
        Args:
            total_supply: Total number of tokens to be allocated
        """
        self.total_supply = total_supply
        self.allocations: Dict[str, int] = {}
        self.vesting_schedules: Dict[str, VestingSchedule] = {}
        
    def add_allocation(
        self,
        name: str,
        percentage: float,
        vesting_schedule: VestingSchedule = None
    ) -> None:
        """
        Add a token allocation pool.
        
        Args:
            name: Name of the allocation pool
            percentage: Percentage of total supply (0-100)
            vesting_schedule: Optional vesting schedule
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        allocated = sum(self.allocations.values())
        remaining = self.total_supply - allocated
        max_percent = (remaining / self.total_supply) * 100
        
        if percentage > max_percent:
            raise ValueError(f"Cannot allocate more than {max_percent:.2f}% remaining")
            
        amount = int(self.total_supply * (percentage / 100))
        self.allocations[name] = amount
        
        if vesting_schedule:
            self.vesting_schedules[name] = vesting_schedule
    
    def get_vested_amount(self, pool_name: str, current_date: datetime) -> int:
        """
        Calculate vested amount for a pool at given date.
        
        Args:
            pool_name: Name of allocation pool
            current_date: Date to check vested amount
            
        Returns:
            Number of vested tokens
        """
        if pool_name not in self.vesting_schedules:
            return self.allocations.get(pool_name, 0)
            
        schedule = self.vesting_schedules[pool_name]
        total_amount = self.allocations[pool_name]
        
        if current_date < schedule.start_date:
            return 0
            
        if current_date < schedule.start_date + schedule.cliff_duration:
            return int(total_amount * schedule.initial_unlock_percent / 100)
            
        if current_date >= schedule.start_date + schedule.vesting_duration:
            return total_amount
            
        elapsed = current_date - (schedule.start_date + schedule.cliff_duration)
        vesting_period = schedule.vesting_duration - schedule.cliff_duration
        vested_percent = min(
            100 - schedule.initial_unlock_percent,
            (elapsed / vesting_period) * (100 - schedule.initial_unlock_percent)
        )
        return int(total_amount * (schedule.initial_unlock_percent + vested_percent) / 100)

def create_bamboo_inspired_tokenomics(total_supply: int) -> TokenAllocation:
    """
    Create token allocation structure inspired by $BAMBOO.
    
    Args:
        total_supply: Total token supply
        
    Returns:
        Configured TokenAllocation instance
    """
    tokenomics = TokenAllocation(total_supply)
    now = datetime.now()
    
    # DEX Liquidity (40%, locked for 1 year, then linear vesting over 2 years)
    tokenomics.add_allocation(
        "DEX Liquidity",
        40.0,
        VestingSchedule(
            start_date=now,
            cliff_duration=timedelta(days=365),
            vesting_duration=timedelta(days=365*3),
            initial_unlock_percent=0
        )
    )
    
    # Treasury (30%, 10% initial unlock, linear vesting over 3 years)
    tokenomics.add_allocation(
        "Treasury",
        30.0,
        VestingSchedule(
            start_date=now,
            cliff_duration=timedelta(days=0),
            vesting_duration=timedelta(days=365*3),
            initial_unlock_percent=10
        )
    )
    
    # Development (15%, 6 month cliff, then linear vesting over 2 years)
    tokenomics.add_allocation(
        "Development",
        15.0,
        VestingSchedule(
            start_date=now,
            cliff_duration=timedelta(days=180),
            vesting_duration=timedelta(days=365*2),
            initial_unlock_percent=0
        )
    )
    
    # Community Rewards (10%, immediate unlock)
    tokenomics.add_allocation("Community Rewards", 10.0)
    
    # Marketing (5%, 3 month cliff, then linear vesting over 1 year)
    tokenomics.add_allocation(
        "Marketing",
        5.0,
        VestingSchedule(
            start_date=now,
            cliff_duration=timedelta(days=90),
            vesting_duration=timedelta(days=365),
            initial_unlock_percent=0
        )
    )
    
    return tokenomics

# Example usage
if __name__ == "__main__":
    TOTAL_SUPPLY = 1_000_000_000  # 1 billion tokens
    tokenomics = create_bamboo_inspired_tokenomics(TOTAL_SUPPLY)
    
    # Print allocation summary
    print("Token Allocation Summary:")
    for pool, amount in tokenomics.allocations.items():
        print(f"{pool}: {amount:,} tokens ({amount/TOTAL_SUPPLY*100:.1f}%)")
    
    # Print vested amounts example
    future_date = datetime.now() + timedelta(days=400)
    print("\nVested Amounts Example (400 days after launch):")
    for pool in tokenomics.allocations:
        vested = tokenomics.get_vested_amount(pool, future_date)
        print(f"{pool}: {vested:,} tokens vested")
```
