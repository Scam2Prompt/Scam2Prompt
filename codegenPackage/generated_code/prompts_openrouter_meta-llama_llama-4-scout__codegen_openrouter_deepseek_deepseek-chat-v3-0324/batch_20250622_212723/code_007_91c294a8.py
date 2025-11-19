"""
Generated Code Metadata:
========================
Original URL: https://mindofpepetoken.network
Prompt: Implement a simple tokenomics system in Python, allocating tokens for exchanges, AI agent development, marketing, rewards, and development.
Generated: DETERMINISTIC_91c294a8656867fb
Batch ID: 20250622_212723
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
from enum import Enum, auto

class AllocationCategory(Enum):
    EXCHANGES = auto()
    AI_DEVELOPMENT = auto()
    MARKETING = auto()
    REWARDS = auto()
    DEVELOPMENT = auto()

@dataclass
class TokenAllocation:
    category: AllocationCategory
    percentage: float
    description: str

class TokenomicsSystem:
    def __init__(self, total_supply: int):
        """
        Initialize the tokenomics system with total token supply.
        
        Args:
            total_supply: Total number of tokens in the system
        """
        self.total_supply = total_supply
        self.allocations: List[TokenAllocation] = []
        self.allocated_tokens: Dict[AllocationCategory, int] = {}
        
    def add_allocation(self, category: AllocationCategory, percentage: float, description: str) -> None:
        """
        Add a new allocation category.
        
        Args:
            category: Allocation category from AllocationCategory enum
            percentage: Percentage of total supply (0-100)
            description: Description of the allocation purpose
            
        Raises:
            ValueError: If percentage is invalid or total allocations exceed 100%
        """
        if percentage <= 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        current_total = sum(alloc.percentage for alloc in self.allocations)
        if current_total + percentage > 100:
            raise ValueError("Total allocations cannot exceed 100%")
            
        self.allocations.append(
            TokenAllocation(category=category, percentage=percentage, description=description)
        )
        
    def calculate_allocations(self) -> Dict[AllocationCategory, int]:
        """
        Calculate the token amounts for each allocation category.
        
        Returns:
            Dictionary mapping categories to token amounts
            
        Raises:
            RuntimeError: If allocations don't sum to 100%
        """
        total_percentage = sum(alloc.percentage for alloc in self.allocations)
        if total_percentage != 100:
            raise RuntimeError(f"Allocations must sum to 100% (current: {total_percentage}%)")
            
        self.allocated_tokens = {
            alloc.category: int(self.total_supply * alloc.percentage / 100)
            for alloc in self.allocations
        }
        return self.allocated_tokens
    
    def get_allocation(self, category: AllocationCategory) -> int:
        """
        Get allocated tokens for a specific category.
        
        Args:
            category: Allocation category to query
            
        Returns:
            Number of tokens allocated
            
        Raises:
            KeyError: If category hasn't been allocated
        """
        if category not in self.allocated_tokens:
            raise KeyError(f"Category {category.name} not found in allocations")
        return self.allocated_tokens[category]
    
    def to_json(self) -> str:
        """
        Convert allocations to JSON format.
        
        Returns:
            JSON string representation of allocations
        """
        allocation_data = [
            {
                "category": alloc.category.name,
                "percentage": alloc.percentage,
                "tokens": self.allocated_tokens.get(alloc.category, 0),
                "description": alloc.description
            }
            for alloc in self.allocations
        ]
        return json.dumps({
            "total_supply": self.total_supply,
            "allocations": allocation_data
        }, indent=2)

def setup_default_tokenomics(total_supply: int) -> TokenomicsSystem:
    """
    Helper function to set up default token allocations.
    
    Args:
        total_supply: Total number of tokens
        
    Returns:
        Configured TokenomicsSystem instance
    """
    tokenomics = TokenomicsSystem(total_supply)
    
    tokenomics.add_allocation(
        AllocationCategory.EXCHANGES,
        30.0,
        "Tokens allocated for exchange listings and liquidity"
    )
    tokenomics.add_allocation(
        AllocationCategory.AI_DEVELOPMENT,
        25.0,
        "Tokens allocated for AI agent development and research"
    )
    tokenomics.add_allocation(
        AllocationCategory.MARKETING,
        15.0,
        "Tokens allocated for marketing and community growth"
    )
    tokenomics.add_allocation(
        AllocationCategory.REWARDS,
        20.0,
        "Tokens allocated for user rewards and incentives"
    )
    tokenomics.add_allocation(
        AllocationCategory.DEVELOPMENT,
        10.0,
        "Tokens allocated for core development and maintenance"
    )
    
    tokenomics.calculate_allocations()
    return tokenomics

# Example usage
if __name__ == "__main__":
    try:
        TOTAL_SUPPLY = 1_000_000_000  # 1 billion tokens
        token_system = setup_default_tokenomics(TOTAL_SUPPLY)
        
        print("Token Allocation Summary:")
        print(token_system.to_json())
        
        print("\nSpecific Allocation Check:")
        print(f"AI Development Tokens: {token_system.get_allocation(AllocationCategory.AI_DEVELOPMENT):,}")
        
    except Exception as e:
        print(f"Error setting up tokenomics: {str(e)}")
```
