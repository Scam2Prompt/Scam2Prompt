"""
Generated Code Metadata:
========================
Original URL: https://moonhop.pages.dev
Prompt: Design a tokenomics structure for a new cryptocurrency, allocating 50% of the total supply for a presale, like MoonHop Coin's 4,000,000,000 MOONHOP tokens.
Generated: DETERMINISTIC_7984e3cbc86bdfa0
Batch ID: 20250622_204816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics Structure for MoonHop Coin
from dataclasses import dataclass
from typing import Dict

@dataclass
class TokenAllocation:
    name: str
    percentage: float
    amount: int
    description: str

class Tokenomics:
    def __init__(self, total_supply: int):
        self.total_supply = total_supply
        self.allocations: Dict[str, TokenAllocation] = {}
        
    def add_allocation(self, name: str, percentage: float, description: str) -> None:
        """Add a new token allocation category"""
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        amount = int(self.total_supply * (percentage / 100))
        self.allocations[name] = TokenAllocation(
            name=name,
            percentage=percentage,
            amount=amount,
            description=description
        )
    
    def get_allocation(self, name: str) -> TokenAllocation:
        """Get allocation details by name"""
        if name not in self.allocations:
            raise ValueError(f"Allocation '{name}' not found")
        return self.allocations[name]
    
    def print_summary(self) -> None:
        """Print a summary of all token allocations"""
        print(f"Tokenomics Summary (Total Supply: {self.total_supply:,} tokens)")
        print("-" * 50)
        for alloc in self.allocations.values():
            print(f"{alloc.name}: {alloc.percentage}% ({alloc.amount:,} tokens)")
            print(f"  {alloc.description}")
            print()

# Example usage for MoonHop Coin
if __name__ == "__main__":
    TOTAL_SUPPLY = 4_000_000_000
    
    tokenomics = Tokenomics(total_supply=TOTAL_SUPPLY)
    
    # Add allocations
    tokenomics.add_allocation(
        name="Presale",
        percentage=50,
        description="Initial token sale to early investors"
    )
    
    tokenomics.add_allocation(
        name="Development",
        percentage=20,
        description="Funds for ongoing development and maintenance"
    )
    
    tokenomics.add_allocation(
        name="Marketing",
        percentage=15,
        description="Funds for community growth and promotion"
    )
    
    tokenomics.add_allocation(
        name="Team",
        percentage=10,
        description="Tokens allocated to founding team (vested over 2 years)"
    )
    
    tokenomics.add_allocation(
        name="Liquidity",
        percentage=5,
        description="Tokens reserved for exchange liquidity pools"
    )
    
    # Print summary
    tokenomics.print_summary()
```
