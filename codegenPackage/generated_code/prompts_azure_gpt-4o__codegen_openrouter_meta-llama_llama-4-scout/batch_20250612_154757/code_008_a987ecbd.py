"""
Generated Code Metadata:
========================
Original URL: https://redstone.cx
Prompt: Generate code to calculate the distribution of $INIT tokens across different categories (Community Reserve, Investors, Treasury, etc.) based on the tokenomics provided on the Initia website.
Generated: DETERMINISTIC_a987ecbdb837dbbd
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_distribution_calculator.py

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class TokenCategory(Enum):
    """Enum representing different token categories."""
    COMMUNITY_RESERVE = "Community Reserve"
    INVESTORS = "Investors"
    TREASURY = "Treasury"
    FOUNDATION = "Foundation"
    ADVISORS = "Advisors"
    ECOSYSTEM = "Ecosystem"

@dataclass
class TokenAllocation:
    """Dataclass to represent token allocation."""
    category: TokenCategory
    percentage: float

class TokenDistributionCalculator:
    """Class to calculate token distribution."""

    def __init__(self, total_tokens: int, allocations: List[TokenAllocation]):
        """
        Initialize the calculator.

        Args:
        total_tokens (int): Total number of tokens.
        allocations (List[TokenAllocation]): List of token allocations.
        """
        self.total_tokens = total_tokens
        self.allocations = allocations

    def calculate_distribution(self) -> Dict[TokenCategory, int]:
        """
        Calculate token distribution across different categories.

        Returns:
        Dict[TokenCategory, int]: Dictionary with token category as key and token count as value.
        """
        distribution = {}
        for allocation in self.allocations:
            tokens = int(self.total_tokens * allocation.percentage / 100)
            distribution[allocation.category] = tokens
        # Handle potential rounding errors
        remainder = self.total_tokens - sum(distribution.values())
        if remainder > 0:
            distribution[TokenCategory.COMMUNITY_RESERVE] += remainder
        return distribution

def main():
    # Example usage
    total_init_tokens = 1000000000  # 1 billion INIT tokens

    # Tokenomics allocations (example percentages)
    allocations = [
        TokenAllocation(TokenCategory.COMMUNITY_RESERVE, 20),
        TokenAllocation(TokenCategory.INVESTORS, 15),
        TokenAllocation(TokenCategory.TREASURY, 10),
        TokenAllocation(TokenCategory.FOUNDATION, 5),
        TokenAllocation(TokenCategory.ADVISORS, 2),
        TokenAllocation(TokenCategory.ECOSYSTEM, 48),
    ]

    calculator = TokenDistributionCalculator(total_init_tokens, allocations)
    distribution = calculator.calculate_distribution()

    print("INIT Token Distribution:")
    for category, tokens in distribution.items():
        print(f"{category.value}: {tokens} tokens ({tokens / total_init_tokens * 100:.2f}%)")

if __name__ == "__main__":
    main()
```
