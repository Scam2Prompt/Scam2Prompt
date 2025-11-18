"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-com.pages.dev
Prompt: Develop a Python script to calculate token allocation percentages for presale, staking rewards, liquidity, marketing, development, and community funds based on the Oracle Meme tokenomics data.
Generated: DETERMINISTIC_21dcc2617e2da17a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# token_allocation.py

class TokenAllocation:
    """A class to calculate the token allocation percentages for various categories."""

    def __init__(self, total_supply: float):
        """
        Initializes the TokenAllocation with the total supply of tokens.
        
        Args:
            total_supply (float): The total number of tokens available.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply

        # Allocation data initialized to zero
        self.allocations = {
            'presale': 0,
            'staking_rewards': 0,
            'liquidity': 0,
            'marketing': 0,
            'development': 0,
            'community_funds': 0,
        }

    def set_allocation(self, category: str, amount: float):
        """
        Sets the allocation amount for a specific category.
        
        Args:
            category (str): The category for which to set the allocation.
            amount (float): The number of tokens allocated to the category.

        Raises:
            ValueError: If the category is invalid or amount is negative.
        """
        if category not in self.allocations:
            raise ValueError(f"Invalid category: {category}. Valid categories are {list(self.allocations.keys())}.")
        
        if amount < 0:
            raise ValueError("Allocation amount cannot be negative.")

        self.allocations[category] = amount

    def calculate_percentages(self):
        """
        Calculates the allocation percentages for each category based on the total supply.

        Returns:
            dict: A dictionary containing the percentage of each allocation category.
        """
        percentages = {}
        for category, amount in self.allocations.items():
            percentages[category] = (amount / self.total_supply) * 100 if self.total_supply > 0 else 0
        return percentages

    def display_allocations(self):
        """
        Displays the allocations and their corresponding percentages.
        """
        allocations_percentages = self.calculate_percentages()
        
        print(f"Total Supply: {self.total_supply}")
        print("Token Allocations and Percentages:")
        for category, amount in self.allocations.items():
            percentage = allocations_percentages[category]
            print(f"{category.capitalize()}: {amount} tokens ({percentage:.2f}%)")

if __name__ == "__main__":
    try:
        # Example: Initialize with a total supply of 1,000,000 tokens
        total_supply = 1_000_000
        token_allocation = TokenAllocation(total_supply)

        # Set allocations for each category
        token_allocation.set_allocation('presale', 300_000)
        token_allocation.set_allocation('staking_rewards', 200_000)
        token_allocation.set_allocation('liquidity', 150_000)
        token_allocation.set_allocation('marketing', 150_000)
        token_allocation.set_allocation('development', 100_000)
        token_allocation.set_allocation('community_funds', 100_000)

        # Display token allocations and percentages
        token_allocation.display_allocations()

    except ValueError as e:
        print(f"Error: {e}")
```
