"""
Generated Code Metadata:
========================
Original URL: https://claim-jindo-coin.pages.dev
Prompt: Design a tokenomics structure for a new cryptocurrency inspired by the Jindo breed, allocating token supply for presale, community, and other purposes.
Generated: DETERMINISTIC_0cfb5b42072dfaeb
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class Tokenomics:
    total_supply: int
    presale_allocation: float
    community_allocation: float
    development_allocation: float
    marketing_allocation: float
    liquidity_allocation: float
    allocations: Dict[str, float] = field(init=False)

    def __post_init__(self):
        # Calculate the allocations based on the total supply
        self.allocations = {
            "presale": self.presale_allocation * self.total_supply,
            "community": self.community_allocation * self.total_supply,
            "development": self.development_allocation * self.total_supply,
            "marketing": self.marketing_allocation * self.total_supply,
            "liquidity": self.liquidity_allocation * self.total_supply,
        }
        self.validate_allocations()

    def validate_allocations(self):
        """
        Validate that the total allocation does not exceed 100% of the total supply.
        Raises ValueError if the total allocation exceeds 100%.
        """
        total_allocated = sum(self.allocations.values())
        if total_allocated > self.total_supply:
            raise ValueError(f"Total allocations exceed total supply: {total_allocated} > {self.total_supply}")

    def get_allocation(self, category: str) -> float:
        """
        Get the allocation for a specific category.
        
        :param category: The category for which to retrieve the allocation.
        :return: The allocation amount for the specified category.
        :raises KeyError: If the category does not exist.
        """
        try:
            return self.allocations[category]
        except KeyError as e:
            raise KeyError(f"Allocation category '{category}' does not exist.") from e

    def __str__(self) -> str:
        """
        String representation of the Tokenomics structure.
        
        :return: A string summarizing the token allocations.
        """
        return f"Tokenomics(total_supply={self.total_supply}, allocations={self.allocations})"

# Example usage
if __name__ == "__main__":
    try:
        # Define the total supply and allocation percentages
        total_supply = 1_000_000_000  # 1 billion tokens
        presale_allocation = 0.20  # 20%
        community_allocation = 0.25  # 25%
        development_allocation = 0.15  # 15%
        marketing_allocation = 0.10  # 10%
        liquidity_allocation = 0.30  # 30%

        # Create a Tokenomics instance
        tokenomics = Tokenomics(
            total_supply=total_supply,
            presale_allocation=presale_allocation,
            community_allocation=community_allocation,
            development_allocation=development_allocation,
            marketing_allocation=marketing_allocation,
            liquidity_allocation=liquidity_allocation
        )

        # Print the tokenomics structure
        print(tokenomics)

        # Example of getting a specific allocation
        print(f"Community Allocation: {tokenomics.get_allocation('community')} tokens")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
