"""
Generated Code Metadata:
========================
Original URL: https://crudo-protocol.xyz
Prompt: Implement a tokenomics system for the CRUDO token, allocating tokens for presale, rewards, ICO bonus, marketing, ecosystem operations, and other purposes.
Generated: DETERMINISTIC_df691a0a1a534484
Batch ID: 20250622_212302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics.py

from dataclasses import dataclass
from enum import Enum
from typing import Dict

class TokenAllocation(Enum):
    """Enum for token allocation purposes"""
    PRESALE = "presale"
    REWARDS = "rewards"
    ICO_BONUS = "ico_bonus"
    MARKETING = "marketing"
    ECOSYSTEM_OPERATIONS = "ecosystem_operations"
    OTHER = "other"

@dataclass
class TokenAllocationDetails:
    """Dataclass for token allocation details"""
    amount: float
    percentage: float
    description: str

class Tokenomics:
    """Class for tokenomics system"""
    def __init__(self, total_supply: float):
        """
        Initialize tokenomics system

        Args:
        total_supply (float): Total supply of CRUDO tokens
        """
        self.total_supply = total_supply
        self.allocations: Dict[TokenAllocation, TokenAllocationDetails] = {}

    def allocate_tokens(self, purpose: TokenAllocation, amount: float, description: str):
        """
        Allocate tokens for a specific purpose

        Args:
        purpose (TokenAllocation): Purpose of token allocation
        amount (float): Amount of tokens to allocate
        description (str): Description of token allocation

        Raises:
        ValueError: If allocation amount exceeds total supply
        """
        if sum(alloc.amount for alloc in self.allocations.values()) + amount > self.total_supply:
            raise ValueError("Allocation amount exceeds total supply")

        percentage = (amount / self.total_supply) * 100
        self.allocations[purpose] = TokenAllocationDetails(amount, percentage, description)

    def get_allocation(self, purpose: TokenAllocation) -> TokenAllocationDetails:
        """
        Get token allocation details for a specific purpose

        Args:
        purpose (TokenAllocation): Purpose of token allocation

        Returns:
        TokenAllocationDetails: Token allocation details

        Raises:
        KeyError: If purpose is not found
        """
        return self.allocations[purpose]

    def get_all_allocations(self) -> Dict[TokenAllocation, TokenAllocationDetails]:
        """
        Get all token allocations

        Returns:
        Dict[TokenAllocation, TokenAllocationDetails]: Dictionary of token allocations
        """
        return self.allocations

def main():
    try:
        # Initialize tokenomics system with total supply of 100 million CRUDO tokens
        tokenomics = Tokenomics(100_000_000)

        # Allocate tokens
        tokenomics.allocate_tokens(TokenAllocation.PRESALE, 20_000_000, "Presale allocation")
        tokenomics.allocate_tokens(TokenAllocation.REWARDS, 15_000_000, "Rewards allocation")
        tokenomics.allocate_tokens(TokenAllocation.ICO_BONUS, 5_000_000, "ICO bonus allocation")
        tokenomics.allocate_tokens(TokenAllocation.MARKETING, 10_000_000, "Marketing allocation")
        tokenomics.allocate_tokens(TokenAllocation.ECOSYSTEM_OPERATIONS, 8_000_000, "Ecosystem operations allocation")
        tokenomics.allocate_tokens(TokenAllocation.OTHER, 2_000_000, "Other allocation")

        # Get and print all allocations
        allocations = tokenomics.get_all_allocations()
        for purpose, details in allocations.items():
            print(f"Purpose: {purpose.value}")
            print(f"Amount: {details.amount}")
            print(f"Percentage: {details.percentage}%")
            print(f"Description: {details.description}")
            print("------------------------")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
