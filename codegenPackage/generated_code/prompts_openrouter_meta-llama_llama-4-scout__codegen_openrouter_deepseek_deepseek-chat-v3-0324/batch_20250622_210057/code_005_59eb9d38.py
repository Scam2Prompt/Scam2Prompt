"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogs.pages.dev
Prompt: Design a tokenomics system for a new cryptocurrency project, inspired by the 900 million token supply and 90% token availability described for the Bitcoin Dogs project.
Generated: DETERMINISTIC_59eb9d388d4b5e37
Batch ID: 20250622_210057
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
Tokenomics System Implementation

This module implements a tokenomics system for a cryptocurrency project
with a fixed supply and controlled distribution mechanism.
"""

from dataclasses import dataclass
from typing import Dict, List
import math

@dataclass
class TokenAllocation:
    """Represents a category of token allocation"""
    name: str
    percentage: float
    vesting_period: int  # in months
    cliff_period: int    # in months
    recipients: List[str] = None

class Tokenomics:
    """Implements the tokenomics system for the cryptocurrency project"""
    
    def __init__(self, total_supply: int = 900_000_000):
        """
        Initialize the tokenomics system with total supply.
        
        Args:
            total_supply: Total number of tokens to be created (default: 900 million)
        """
        self.total_supply = total_supply
        self.available_supply = int(total_supply * 0.9)  # 90% available
        self.reserved_supply = total_supply - self.available_supply
        self.allocations: Dict[str, TokenAllocation] = {}
        
    def add_allocation(self, allocation: TokenAllocation) -> None:
        """
        Add a new token allocation category.
        
        Args:
            allocation: TokenAllocation object describing the allocation
            
        Raises:
            ValueError: If allocation percentages exceed 100% when combined
        """
        total_percent = sum(a.percentage for a in self.allocations.values()) + allocation.percentage
        if total_percent > 100:
            raise ValueError("Total allocation percentage cannot exceed 100%")
            
        self.allocations[allocation.name] = allocation
        
    def calculate_allocation_amount(self, allocation_name: str) -> int:
        """
        Calculate the token amount for a specific allocation.
        
        Args:
            allocation_name: Name of the allocation category
            
        Returns:
            Number of tokens allocated to this category
            
        Raises:
            KeyError: If allocation category doesn't exist
        """
        if allocation_name not in self.allocations:
            raise KeyError(f"Allocation '{allocation_name}' not found")
            
        allocation = self.allocations[allocation_name]
        return math.floor(self.available_supply * (allocation.percentage / 100))
        
    def get_vesting_schedule(self, allocation_name: str) -> Dict[int, int]:
        """
        Generate a vesting schedule for an allocation.
        
        Args:
            allocation_name: Name of the allocation category
            
        Returns:
            Dictionary mapping month number to tokens released
            
        Raises:
            KeyError: If allocation category doesn't exist
        """
        if allocation_name not in self.allocations:
            raise KeyError(f"Allocation '{allocation_name}' not found")
            
        allocation = self.allocations[allocation_name]
        total_amount = self.calculate_allocation_amount(allocation_name)
        schedule = {}
        
        # Handle cliff period
        for month in range(1, allocation.cliff_period + 1):
            schedule[month] = 0
            
        # Calculate linear vesting after cliff
        vesting_months = allocation.vesting_period - allocation.cliff_period
        monthly_amount = total_amount // vesting_months
        
        for month in range(allocation.cliff_period + 1, allocation.vesting_period + 1):
            schedule[month] = monthly_amount
            
        # Add remainder to last month
        schedule[allocation.vesting_period] += total_amount - (monthly_amount * vesting_months)
        
        return schedule
        
    def validate_allocations(self) -> bool:
        """Validate that all allocations sum to 100% of available supply"""
        total_percent = sum(a.percentage for a in self.allocations.values())
        return math.isclose(total_percent, 100.0, abs_tol=0.001)
        
    def get_total_allocated(self) -> int:
        """Get total number of tokens allocated across all categories"""
        return sum(self.calculate_allocation_amount(name) for name in self.allocations)

# Example usage
if __name__ == "__main__":
    tokenomics = Tokenomics()
    
    # Define allocations
    allocations = [
        TokenAllocation(
            name="Team",
            percentage=20,
            vesting_period=36,
            cliff_period=12,
            recipients=["team_wallet_1", "team_wallet_2"]
        ),
        TokenAllocation(
            name="Advisors",
            percentage=10,
            vesting_period=24,
            cliff_period=6,
            recipients=["advisor_wallet_1", "advisor_wallet_2"]
        ),
        TokenAllocation(
            name="Ecosystem",
            percentage=30,
            vesting_period=48,
            cliff_period=0,
            recipients=["ecosystem_fund"]
        ),
        TokenAllocation(
            name="Community",
            percentage=40,
            vesting_period=12,
            cliff_period=0,
            recipients=["community_pool"]
        )
    ]
    
    # Add allocations
    for allocation in allocations:
        tokenomics.add_allocation(allocation)
    
    # Validate allocations
    if not tokenomics.validate_allocations():
        raise ValueError("Allocations do not sum to 100%")
    
    # Print allocation details
    print(f"Total Supply: {tokenomics.total_supply:,}")
    print(f"Available Supply: {tokenomics.available_supply:,} (90%)")
    print(f"Reserved Supply: {tokenomics.reserved_supply:,} (10%)")
    
    for name in tokenomics.allocations:
        amount = tokenomics.calculate_allocation_amount(name)
        print(f"\n{name} Allocation:")
        print(f"  Percentage: {tokenomics.allocations[name].percentage}%")
        print(f"  Amount: {amount:,} tokens")
        print(f"  Vesting: {tokenomics.allocations[name].vesting_period} months")
        print(f"  Cliff: {tokenomics.allocations[name].cliff_period} months")
        
        vesting_schedule = tokenomics.get_vesting_schedule(name)
        print("\n  Vesting Schedule:")
        for month, tokens in vesting_schedule.items():
            print(f"    Month {month}: {tokens:,} tokens")
```
