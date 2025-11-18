"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedogeverse-com.pages.dev
Prompt: Write code to implement a token allocation tracker for $DOGEVERSE, showing percentages allocated to presale, staking, liquidity, marketing, ecosystem funds, and exchanges.
Generated: DETERMINISTIC_1c9c5b31d645bd57
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict

class TokenAllocationTracker:
    """
    Class to track and display token allocation for $DOGEVERSE.
    """

    def __init__(self, total_supply: int):
        """
        Initialize the tracker with the total supply of tokens.
        :param total_supply: The total supply of $DOGEVERSE tokens.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.allocations = {
            "Presale": 0.0,
            "Staking": 0.0,
            "Liquidity": 0.0,
            "Marketing": 0.0,
            "Ecosystem Funds": 0.0,
            "Exchanges": 0.0,
        }

    def set_allocation(self, category: str, percentage: float):
        """
        Set the allocation percentage for a specific category.
        :param category: The category to set the allocation for.
        :param percentage: The percentage to allocate (must be between 0 and 100).
        """
        if category not in self.allocations:
            raise ValueError(f"Invalid category: {category}.")
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        self.allocations[category] = percentage

    def get_allocation(self, category: str) -> float:
        """
        Get the allocation percentage for a specific category.
        :param category: The category to retrieve the allocation for.
        :return: The allocation percentage.
        """
        if category not in self.allocations:
            raise ValueError(f"Invalid category: {category}.")
        return self.allocations[category]

    def calculate_token_distribution(self) -> Dict[str, int]:
        """
        Calculate the token distribution based on current allocation percentages.
        :return: A dictionary with the number of tokens allocated to each category.
        """
        distribution = {}
        for category, percentage in self.allocations.items():
            distribution[category] = int((percentage / 100) * self.total_supply)
        return distribution

    def validate_allocations(self):
        """
        Validate that the sum of all allocations does not exceed 100%.
        :return: True if allocations are valid, False otherwise.
        """
        total_percentage = sum(self.allocations.values())
        if total_percentage > 100:
            raise ValueError(
                f"Total allocation exceeds 100%: {total_percentage:.2f}%."
            )
        return True

    def display_allocations(self):
        """
        Display the current allocations in a readable format.
        """
        print("Token Allocations (%):")
        for category, percentage in self.allocations.items():
            print(f"  {category}: {percentage:.2f}%")
        print("\nToken Distribution:")
        distribution = self.calculate_token_distribution()
        for category, tokens in distribution.items():
            print(f"  {category}: {tokens} tokens")


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the tracker with a total token supply of 1,000,000
        tracker = TokenAllocationTracker(total_supply=1_000_000)

        # Set allocation percentages
        tracker.set_allocation("Presale", 20.0)
        tracker.set_allocation("Staking", 15.0)
        tracker.set_allocation("Liquidity", 25.0)
        tracker.set_allocation("Marketing", 10.0)
        tracker.set_allocation("Ecosystem Funds", 20.0)
        tracker.set_allocation("Exchanges", 10.0)

        # Validate allocations
        tracker.validate_allocations()

        # Display allocations and token distribution
        tracker.display_allocations()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
