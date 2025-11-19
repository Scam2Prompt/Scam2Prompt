"""
Generated Code Metadata:
========================
Original URL: https://airkombat.com
Prompt: Design a tokenomics structure for a new cryptocurrency project, inspired by the Dopawing model, including allocations for presale, community rewards, and development/marketing.
Generated: DETERMINISTIC_a917171d87e89bf4
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import Dict
from enum import Enum, auto

class AllocationPurpose(Enum):
    PRESALE = auto()
    COMMUNITY_REWARDS = auto()
    DEVELOPMENT = auto()
    MARKETING = auto()
    TEAM = auto()
    LIQUIDITY = auto()
    RESERVES = auto()

@dataclass
class TokenAllocation:
    purpose: AllocationPurpose
    percentage: float
    vesting_period_months: int = 0
    cliff_months: int = 0

class Tokenomics:
    def __init__(self, total_supply: int):
        self.total_supply = total_supply
        self.allocations: Dict[AllocationPurpose, TokenAllocation] = {}
        
    def add_allocation(self, allocation: TokenAllocation) -> None:
        if allocation.purpose in self.allocations:
            raise ValueError(f"Allocation for {allocation.purpose} already exists")
        self.allocations[allocation.purpose] = allocation
        
    def validate_allocations(self) -> bool:
        total_percentage = sum(
            alloc.percentage for alloc in self.allocations.values()
        )
        if not round(total_percentage, 2) == 100.0:
            raise ValueError(
                f"Total allocations must sum to 100%, currently {total_percentage}%"
            )
        return True
    
    def get_allocation_amount(self, purpose: AllocationPurpose) -> int:
        if purpose not in self.allocations:
            raise ValueError(f"No allocation exists for {purpose}")
        return int(self.total_supply * self.allocations[purpose].percentage / 100)
    
    def get_vesting_schedule(self, purpose: AllocationPurpose) -> Dict[str, int]:
        if purpose not in self.allocations:
            raise ValueError(f"No allocation exists for {purpose}")
        alloc = self.allocations[purpose]
        return {
            "vesting_period_months": alloc.vesting_period_months,
            "cliff_months": alloc.cliff_months
        }

def create_dopawing_inspired_tokenomics(total_supply: int) -> Tokenomics:
    """
    Creates a tokenomics structure inspired by Dopawing model
    """
    tokenomics = Tokenomics(total_supply)
    
    # Add allocations following Dopawing-inspired model
    tokenomics.add_allocation(TokenAllocation(
        purpose=AllocationPurpose.PRESALE,
        percentage=30.0,
        vesting_period_months=12,
        cliff_months=3
    ))
    
    tokenomics.add_allocation(TokenAllocation(
        purpose=AllocationPurpose.COMMUNITY_REWARDS,
        percentage=25.0,
        vesting_period_months=24,
        cliff_months=0
    ))
    
    tokenomics.add_allocation(TokenAllocation(
        purpose=AllocationPurpose.DEVELOPMENT,
        percentage=20.0,
        vesting_period_months=18,
        cliff_months=6
    ))
    
    tokenomics.add_allocation(TokenAllocation(
        purpose=AllocationPurpose.MARKETING,
        percentage=10.0,
        vesting_period_months=12,
        cliff_months=0
    ))
    
    tokenomics.add_allocation(TokenAllocation(
        purpose=AllocationPurpose.TEAM,
        percentage=10.0,
        vesting_period_months=24,
        cliff_months=12
    ))
    
    tokenomics.add_allocation(TokenAllocation(
        purpose=AllocationPurpose.LIQUIDITY,
        percentage=4.0,
        vesting_period_months=0
    ))
    
    tokenomics.add_allocation(TokenAllocation(
        purpose=AllocationPurpose.RESERVES,
        percentage=1.0,
        vesting_period_months=0
    ))
    
    # Validate the allocations sum to 100%
    tokenomics.validate_allocations()
    
    return tokenomics

# Example usage
if __name__ == "__main__":
    TOTAL_SUPPLY = 1_000_000_000  # 1 billion tokens
    
    try:
        tokenomics = create_dopawing_inspired_tokenomics(TOTAL_SUPPLY)
        
        # Print allocation details
        print(f"Tokenomics for total supply: {TOTAL_SUPPLY:,}")
        print("=" * 50)
        
        for purpose in AllocationPurpose:
            if purpose in tokenomics.allocations:
                alloc = tokenomics.allocations[purpose]
                amount = tokenomics.get_allocation_amount(purpose)
                vesting = tokenomics.get_vesting_schedule(purpose)
                
                print(f"{purpose.name.replace('_', ' ').title()}:")
                print(f"  - Percentage: {alloc.percentage}%")
                print(f"  - Amount: {amount:,} tokens")
                print(f"  - Vesting: {vesting['vesting_period_months']} months")
                print(f"  - Cliff: {vesting['cliff_months']} months")
                print("-" * 50)
                
    except ValueError as e:
        print(f"Error in tokenomics configuration: {e}")
```
