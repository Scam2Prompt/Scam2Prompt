"""
Generated Code Metadata:
========================
Original URL: https://wienerdogai-en.pages.dev
Prompt: Generate a tokenomics breakdown for a new cryptocurrency project, allocating tokens for presale, staking, community rewards, and liquidity, similar to WienerAI's tokenomics.
Generated: DETERMINISTIC_098cfe592c8e24b4
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics Breakdown Calculator for Cryptocurrency Projects

import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Allocation:
    name: str
    percentage: float
    description: str
    vesting_period: str = None
    lockup_period: str = None

class Tokenomics:
    def __init__(self, total_supply: int):
        """
        Initialize tokenomics with total supply and empty allocations.
        
        Args:
            total_supply (int): Total token supply (in smallest units)
        """
        self.total_supply = total_supply
        self.allocations: List[Allocation] = []
    
    def add_allocation(
        self,
        name: str,
        percentage: float,
        description: str,
        vesting_period: str = None,
        lockup_period: str = None
    ) -> None:
        """
        Add a new token allocation category.
        
        Args:
            name (str): Name of allocation category
            percentage (float): Percentage of total supply (0-100)
            description (str): Purpose of this allocation
            vesting_period (str, optional): Vesting schedule if applicable
            lockup_period (str, optional): Lockup period if applicable
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
        
        if sum(a.percentage for a in self.allocations) + percentage > 100:
            raise ValueError("Total allocations cannot exceed 100%")
            
        self.allocations.append(
            Allocation(name, percentage, description, vesting_period, lockup_period)
        )
    
    def calculate_amounts(self) -> Dict[str, Dict]:
        """
        Calculate token amounts for each allocation based on percentages.
        
        Returns:
            Dict[str, Dict]: Dictionary with allocation details and calculated amounts
        """
        if not self.allocations:
            raise ValueError("No allocations have been added")
            
        if sum(a.percentage for a in self.allocations) != 100:
            raise ValueError("Allocations must sum to 100%")
        
        results = {}
        for allocation in self.allocations:
            amount = int(self.total_supply * (allocation.percentage / 100))
            results[allocation.name] = {
                "percentage": allocation.percentage,
                "amount": amount,
                "description": allocation.description,
                "vesting_period": allocation.vesting_period,
                "lockup_period": allocation.lockup_period
            }
        
        return results
    
    def to_json(self) -> str:
        """
        Convert tokenomics breakdown to JSON format.
        
        Returns:
            str: JSON string representation of tokenomics
        """
        amounts = self.calculate_amounts()
        return json.dumps({
            "total_supply": self.total_supply,
            "allocations": amounts
        }, indent=2)

# Example usage with WienerAI-like tokenomics
if __name__ == "__main__":
    try:
        # Initialize with 1 billion tokens (with 18 decimals)
        tokenomics = Tokenomics(total_supply=1_000_000_000 * 10**18)
        
        # Add allocations (similar to WienerAI's structure)
        tokenomics.add_allocation(
            name="Presale",
            percentage=30.0,
            description="Tokens allocated for presale investors",
            lockup_period="30 days after launch"
        )
        
        tokenomics.add_allocation(
            name="Staking Rewards",
            percentage=20.0,
            description="Tokens reserved for staking rewards",
            vesting_period="Linear release over 3 years"
        )
        
        tokenomics.add_allocation(
            name="Community Rewards",
            percentage=15.0,
            description="Tokens for community incentives and airdrops",
            vesting_period="Quarterly releases over 2 years"
        )
        
        tokenomics.add_allocation(
            name="Liquidity Pool",
            percentage=10.0,
            description="Tokens allocated for DEX liquidity provision",
            lockup_period="Locked for 6 months"
        )
        
        tokenomics.add_allocation(
            name="Team",
            percentage=10.0,
            description="Tokens allocated for development team",
            vesting_period="12 month cliff, then monthly over 2 years"
        )
        
        tokenomics.add_allocation(
            name="Marketing",
            percentage=10.0,
            description="Tokens allocated for marketing efforts",
            vesting_period="Monthly releases over 18 months"
        )
        
        tokenomics.add_allocation(
            name="Development Fund",
            percentage=5.0,
            description="Tokens reserved for future development",
            vesting_period="Quarterly releases over 3 years"
        )
        
        # Print results
        print("Tokenomics Breakdown:")
        print(tokenomics.to_json())
        
    except ValueError as e:
        print(f"Error in tokenomics configuration: {e}")
```
