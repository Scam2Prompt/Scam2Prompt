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
class Tokenomics:
    def __init__(self, total_supply):
        """
        Initialize the Tokenomics system with a total supply of tokens.

        :param total_supply: Total number of tokens available for allocation.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        
        self.total_supply = total_supply
        self.allocations = {
            "presale": 0,
            "rewards": 0,
            "ico_bonus": 0,
            "marketing": 0,
            "ecosystem_operations": 0,
            "other": 0
        }

    def allocate_tokens(self, category, amount):
        """
        Allocate tokens to a specific category.

        :param category: The category to allocate tokens to.
        :param amount: The amount of tokens to allocate.
        :raises ValueError: If the category is invalid or if the allocation exceeds the remaining supply.
        """
        if category not in self.allocations:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.allocations.keys())}.")
        
        if amount < 0:
            raise ValueError("Allocation amount must be a non-negative integer.")
        
        if self.get_remaining_supply() < amount:
            raise ValueError("Insufficient remaining supply for allocation.")
        
        self.allocations[category] += amount

    def get_remaining_supply(self):
        """
        Calculate the remaining supply of tokens after allocations.

        :return: Remaining supply of tokens.
        """
        total_allocated = sum(self.allocations.values())
        return self.total_supply - total_allocated

    def get_allocation(self, category):
        """
        Get the allocated amount for a specific category.

        :param category: The category to retrieve the allocation for.
        :return: Allocated amount for the specified category.
        :raises ValueError: If the category is invalid.
        """
        if category not in self.allocations:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.allocations.keys())}.")
        
        return self.allocations[category]

    def get_total_allocations(self):
        """
        Get the total allocations across all categories.

        :return: Dictionary of allocations by category.
        """
        return self.allocations

    def __str__(self):
        """
        String representation of the Tokenomics system.

        :return: A string summarizing the total supply and allocations.
        """
        return f"Total Supply: {self.total_supply}, Allocations: {self.allocations}, Remaining Supply: {self.get_remaining_supply()}"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Tokenomics system with a total supply of 1,000,000 tokens
        tokenomics = Tokenomics(total_supply=1000000)

        # Allocate tokens to various categories
        tokenomics.allocate_tokens("presale", 200000)
        tokenomics.allocate_tokens("rewards", 150000)
        tokenomics.allocate_tokens("ico_bonus", 100000)
        tokenomics.allocate_tokens("marketing", 50000)
        tokenomics.allocate_tokens("ecosystem_operations", 100000)

        # Print the current state of token allocations
        print(tokenomics)

    except ValueError as e:
        print(f"Error: {e}")
```
