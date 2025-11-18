"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proofoftalk.pages.dev
Prompt: Develop a tokenomics optimization tool for Web3 startups, incorporating features like those mentioned in the mentorship and workshop sessions of the Proof of Pitch competition.
Generated: DETERMINISTIC_234bc553569851b3
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

# Constants
MAX_SUPPLY = 1_000_000  # Maximum token supply
DEFAULT_ALLOCATION = {
    "team": 20,       # Percentage allocated to the team
    "investors": 25,  # Percentage allocated to investors
    "community": 40,  # Percentage allocated to the community
    "reserve": 15     # Percentage allocated to reserve
}

# Error classes
class AllocationError(Exception):
    """Custom exception for allocation errors."""
    pass

class TokenomicsOptimizer:
    """
    A tool to optimize token allocations for Web3 startups.
    """

    def __init__(self, max_supply: int = MAX_SUPPLY):
        """
        Initialize the TokenomicsOptimizer.

        :param max_supply: Maximum token supply.
        """
        self.max_supply = max_supply
        self.allocations = DEFAULT_ALLOCATION.copy()

    def set_allocations(self, allocations: Dict[str, int]) -> None:
        """
        Set custom allocations.

        :param allocations: A dictionary where keys are allocation categories and values are percentages.
        :raises AllocationError: If total allocation does not equal 100%.
        """
        if sum(allocations.values()) != 100:
            raise AllocationError("Total allocation percentages must equal 100.")
        self.allocations = allocations

    def calculate_token_distribution(self) -> Dict[str, int]:
        """
        Calculate token distribution based on current allocations.

        :return: A dictionary with allocations and token counts.
        """
        token_distribution = {
            category: int(self.max_supply * percentage / 100)
            for category, percentage in self.allocations.items()
        }
        return token_distribution

    def export_tokenomics(self, filename: str = "tokenomics.json") -> None:
        """
        Export the tokenomics data to a JSON file.

        :param filename: Name of the file to write.
        """
        try:
            data = {
                "max_supply": self.max_supply,
                "allocations": self.allocations,
                "token_distribution": self.calculate_token_distribution()
            }
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Tokenomics data successfully exported to {filename}.")
        except Exception as e:
            print(f"Error exporting tokenomics data: {e}")

    def optimize_for_investors(self, desired_investor_share: int) -> None:
        """
        Optimize token allocations by increasing investor share.

        :param desired_investor_share: Desired percentage allocation for investors.
        :raises AllocationError: If desired share is infeasible.
        """
        remaining_percentage = 100 - desired_investor_share
        if remaining_percentage < 0:
            raise AllocationError("Desired investor share exceeds 100%.")
        
        # Redistribute the remaining percentage among other categories proportionally
        non_investor_categories = {k: v for k, v in self.allocations.items() if k != "investors"}
        redistribution_factor = remaining_percentage / sum(non_investor_categories.values())
        self.allocations["investors"] = desired_investor_share

        for category in non_investor_categories:
            self.allocations[category] = int(non_investor_categories[category] * redistribution_factor)

        if sum(self.allocations.values()) != 100:
            # Adjust last category to correct rounding errors
            last_category = list(self.allocations.keys())[-1]
            self.allocations[last_category] += 100 - sum(self.allocations.values())

# Main function
def main():
    """
    Main function to interact with the tokenomics optimizer.
    """
    optimizer = TokenomicsOptimizer()

    print("Current Token Allocations:")
    print(optimizer.allocations)

    try:
        # Example: Adjust allocations for a higher investor share
        optimizer.optimize_for_investors(desired_investor_share=30)
        print("Optimized Token Allocations:")
        print(optimizer.allocations)

        # Calculate token distribution
        distribution = optimizer.calculate_token_distribution()
        print("Calculated Token Distribution:")
        print(distribution)

        # Export tokenomics data
        optimizer.export_tokenomics()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
