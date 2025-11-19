"""
Generated Code Metadata:
========================
Original URL: https://popofrogg.pages.dev
Prompt: Create a script to calculate token allocation percentages for presale, staking, marketing, rewards, and liquidity, based on the tokenomics of $FROP.
Generated: DETERMINISTIC_a6ced57334c7713e
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Tokenomics:
    def __init__(self, total_supply):
        """
        Initialize the Tokenomics class with the total supply of tokens.

        :param total_supply: Total number of tokens available for allocation.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.allocations = {
            "presale": 0,
            "staking": 0,
            "marketing": 0,
            "rewards": 0,
            "liquidity": 0
        }

    def set_allocation(self, category, percentage):
        """
        Set the allocation percentage for a specific category.

        :param category: The category for which to set the allocation (e.g., 'presale', 'staking').
        :param percentage: The percentage of the total supply to allocate to the category.
        """
        if category not in self.allocations:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.allocations.keys())}.")
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")

        self.allocations[category] = (percentage / 100) * self.total_supply

    def get_allocations(self):
        """
        Get the current allocations for all categories.

        :return: A dictionary with the allocation amounts for each category.
        """
        return self.allocations

    def get_allocation_percentages(self):
        """
        Get the allocation percentages for all categories based on the total supply.

        :return: A dictionary with the allocation percentages for each category.
        """
        return {category: (amount / self.total_supply) * 100 for category, amount in self.allocations.items()}

    def display_allocations(self):
        """
        Display the allocations in a readable format.
        """
        print("Token Allocation Percentages:")
        for category, amount in self.allocations.items():
            percentage = (amount / self.total_supply) * 100
            print(f"{category.capitalize()}: {percentage:.2f}% ({amount} tokens)")


if __name__ == "__main__":
    try:
        # Example usage
        total_supply = 1_000_000_000  # Total supply of $FROP tokens
        tokenomics = Tokenomics(total_supply)

        # Set allocations
        tokenomics.set_allocation("presale", 20)
        tokenomics.set_allocation("staking", 15)
        tokenomics.set_allocation("marketing", 10)
        tokenomics.set_allocation("rewards", 25)
        tokenomics.set_allocation("liquidity", 30)

        # Display allocations
        tokenomics.display_allocations()

    except ValueError as e:
        print(f"Error: {e}")
```
