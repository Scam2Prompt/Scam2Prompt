"""
Generated Code Metadata:
========================
Original URL: https://bitcoindog.pages.dev
Prompt: Design a tokenomics system for a new cryptocurrency project, using the 900 million token supply and 90% token availability described in the Bitcoin Dogs tokenomics section.
Generated: DETERMINISTIC_375866fb3ab459a2
Batch ID: 20250622_210122
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
Tokenomics implementation for a cryptocurrency project with:
- Total supply: 900 million tokens
- Circulating supply: 90% of total supply
"""

from dataclasses import dataclass
from typing import Dict
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 6

@dataclass
class TokenAllocation:
    """Data class representing token allocation details"""
    name: str
    percentage: Decimal
    vesting_period: int = 0  # in months
    cliff_period: int = 0    # in months

class Tokenomics:
    """Implements tokenomics for the cryptocurrency project"""
    
    def __init__(self):
        self.total_supply = Decimal('900000000')  # 900 million tokens
        self.circulating_supply_percentage = Decimal('0.9')  # 90%
        
        # Initialize token allocations
        self.allocations = [
            TokenAllocation(name="Public Sale", percentage=Decimal('0.4')),  # 40%
            TokenAllocation(name="Team", percentage=Decimal('0.2'), vesting_period=24, cliff_period=12),  # 20%
            TokenAllocation(name="Advisors", percentage=Decimal('0.1'), vesting_period=18, cliff_period=6),  # 10%
            TokenAllocation(name="Ecosystem", percentage=Decimal('0.15')),  # 15%
            TokenAllocation(name="Liquidity", percentage=Decimal('0.1')),  # 10%
            TokenAllocation(name="Reserve", percentage=Decimal('0.05')),  # 5%
        ]
        
        self._validate_allocations()
    
    def _validate_allocations(self) -> None:
        """Validate that allocations sum to 100%"""
        total = sum(alloc.percentage for alloc in self.allocations)
        if total != Decimal('1'):
            raise ValueError(f"Allocations must sum to 100%, current sum: {total*100}%")
    
    def calculate_circulating_supply(self) -> Decimal:
        """Calculate circulating supply (90% of total supply)"""
        return self.total_supply * self.circulating_supply_percentage
    
    def calculate_allocation_amounts(self) -> Dict[str, Decimal]:
        """Calculate token amounts for each allocation category"""
        return {
            alloc.name: self.total_supply * alloc.percentage
            for alloc in self.allocations
        }
    
    def get_vesting_schedule(self, allocation_name: str) -> Dict[str, int]:
        """Get vesting schedule for a specific allocation"""
        for alloc in self.allocations:
            if alloc.name == allocation_name:
                return {
                    'vesting_period': alloc.vesting_period,
                    'cliff_period': alloc.cliff_period
                }
        raise ValueError(f"Allocation '{allocation_name}' not found")
    
    def get_token_distribution_report(self) -> Dict[str, Dict]:
        """Generate comprehensive token distribution report"""
        circulating = self.calculate_circulating_supply()
        allocations = self.calculate_allocation_amounts()
        
        return {
            'total_supply': float(self.total_supply),
            'circulating_supply': float(circulating),
            'allocations': {
                name: {
                    'percentage': float(alloc.percentage * 100),
                    'tokens': float(amount),
                    'vesting_period': alloc.vesting_period,
                    'cliff_period': alloc.cliff_period
                }
                for alloc, (name, amount) in zip(self.allocations, allocations.items())
            }
        }

# Example usage
if __name__ == "__main__":
    try:
        tokenomics = Tokenomics()
        report = tokenomics.get_token_distribution_report()
        
        print("Token Distribution Report:")
        print(f"Total Supply: {report['total_supply']:,} tokens")
        print(f"Circulating Supply: {report['circulating_supply']:,} tokens (90%)")
        
        print("\nAllocations:")
        for name, details in report['allocations'].items():
            print(f"{name}: {details['tokens']:,} tokens ({details['percentage']}%)")
            if details['vesting_period'] > 0:
                print(f"  - Vesting: {details['vesting_period']} months with {details['cliff_period']} month cliff")
    
    except ValueError as e:
        print(f"Error in tokenomics configuration: {e}")
```
