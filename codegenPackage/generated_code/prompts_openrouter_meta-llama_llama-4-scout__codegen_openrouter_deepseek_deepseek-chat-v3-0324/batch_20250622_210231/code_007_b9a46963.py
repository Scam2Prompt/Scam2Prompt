"""
Generated Code Metadata:
========================
Original URL: https://scottytheais.web.app
Prompt: Propose a tokenomics model in Python for a new crypto project with a similar structure to Scotty AI's token distribution and supply.
Generated: DETERMINISTIC_b9a469638360e415
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class TokenAllocation:
    name: str
    percentage: float
    vesting_period: str  # e.g., "6 months", "1 year", "immediate"
    lockup_period: str   # e.g., "3 months", "none"

class TokenomicsModel:
    def __init__(self, total_supply: int):
        """
        Initialize the tokenomics model with total token supply.
        
        Args:
            total_supply (int): Total number of tokens to be created
        """
        self.total_supply = total_supply
        self.allocations: List[TokenAllocation] = []
        
    def add_allocation(self, name: str, percentage: float, vesting_period: str, lockup_period: str) -> None:
        """
        Add a new token allocation category.
        
        Args:
            name (str): Name of the allocation category
            percentage (float): Percentage of total supply allocated
            vesting_period (str): Vesting schedule for this allocation
            lockup_period (str): Lockup period before vesting starts
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        if sum(a.percentage for a in self.allocations) + percentage > 100:
            raise ValueError("Total allocations cannot exceed 100%")
            
        self.allocations.append(
            TokenAllocation(
                name=name,
                percentage=percentage,
                vesting_period=vesting_period,
                lockup_period=lockup_period
            )
        )
    
    def calculate_allocation_amounts(self) -> Dict[str, int]:
        """
        Calculate the exact token amounts for each allocation category.
        
        Returns:
            Dict[str, int]: Dictionary mapping allocation names to token amounts
        """
        return {
            alloc.name: int(self.total_supply * (alloc.percentage / 100))
            for alloc in self.allocations
        }
    
    def validate_allocations(self) -> bool:
        """
        Validate that allocations sum to 100%.
        
        Returns:
            bool: True if allocations are valid, False otherwise
        """
        total = sum(alloc.percentage for alloc in self.allocations)
        return abs(total - 100) < 0.0001  # Account for floating point precision
    
    def generate_report(self) -> str:
        """
        Generate a comprehensive tokenomics report.
        
        Returns:
            str: JSON formatted report of token allocations
        """
        if not self.validate_allocations():
            raise ValueError("Allocations do not sum to 100%")
            
        report = {
            "total_supply": self.total_supply,
            "allocations": [
                {
                    "name": alloc.name,
                    "percentage": alloc.percentage,
                    "tokens": int(self.total_supply * (alloc.percentage / 100)),
                    "vesting_period": alloc.vesting_period,
                    "lockup_period": alloc.lockup_period
                }
                for alloc in self.allocations
            ]
        }
        return json.dumps(report, indent=2)

# Example usage similar to Scotty AI's tokenomics
def create_scotty_ai_like_tokenomics():
    tokenomics = TokenomicsModel(total_supply=1_000_000_000)  # 1 billion tokens
    
    # Add allocations similar to Scotty AI's structure
    tokenomics.add_allocation("Ecosystem", 30.0, "3 years", "6 months")
    tokenomics.add_allocation("Team", 20.0, "4 years", "1 year")
    tokenomics.add_allocation("Advisors", 10.0, "2 years", "6 months")
    tokenomics.add_allocation("Marketing", 15.0, "2 years", "3 months")
    tokenomics.add_allocation("Liquidity", 10.0, "immediate", "none")
    tokenomics.add_allocation("Community Rewards", 10.0, "3 years", "none")
    tokenomics.add_allocation("Reserve", 5.0, "5 years", "1 year")
    
    return tokenomics

if __name__ == "__main__":
    try:
        token_model = create_scotty_ai_like_tokenomics()
        print("Tokenomics Model Created Successfully")
        print(token_model.generate_report())
    except ValueError as e:
        print(f"Error creating tokenomics model: {e}")
```
