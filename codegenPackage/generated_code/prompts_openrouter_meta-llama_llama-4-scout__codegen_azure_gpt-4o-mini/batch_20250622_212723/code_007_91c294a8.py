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
class Tokenomics:
    """
    A simple tokenomics system to allocate tokens for various purposes.
    """

    def __init__(self, total_supply):
        """
        Initializes the Tokenomics system with a total supply of tokens.

        :param total_supply: Total number of tokens available for allocation.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.allocations = {
            "exchanges": 0,
            "ai_agent_development": 0,
            "marketing": 0,
            "rewards": 0,
            "development": 0
        }

    def allocate_tokens(self, category, amount):
        """
        Allocates tokens to a specific category.

        :param category: The category to allocate tokens to.
        :param amount: The amount of tokens to allocate.
        :raises ValueError: If the category is invalid or if the allocation exceeds the remaining supply.
        """
        if category not in self.allocations:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.allocations.keys())}")

        if amount < 0:
            raise ValueError("Allocation amount must be a non-negative integer.")

        if self.get_remaining_supply() < amount:
            raise ValueError("Insufficient tokens remaining for allocation.")

        self.allocations[category] += amount

    def get_remaining_supply(self):
        """
        Calculates the remaining supply of tokens after allocations.

        :return: Remaining tokens available for allocation.
        """
        allocated_total = sum(self.allocations.values())
        return self.total_supply - allocated_total

    def get_allocations(self):
        """
        Returns the current allocations of tokens.

        :return: A dictionary of token allocations by category.
        """
        return self.allocations

    def __str__(self):
        """
        Returns a string representation of the tokenomics system.

        :return: A summary of total supply and current allocations.
        """
        return (f"Total Supply: {self.total_supply}\n"
                f"Allocations: {self.allocations}\n"
                f"Remaining Supply: {self.get_remaining_supply()}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tokenomics system with a total supply of 1,000,000 tokens
        tokenomics = Tokenomics(total_supply=1000000)

        # Allocate tokens to various categories
        tokenomics.allocate_tokens("exchanges", 200000)
        tokenomics.allocate_tokens("ai_agent_development", 150000)
        tokenomics.allocate_tokens("marketing", 100000)
        tokenomics.allocate_tokens("rewards", 250000)
        tokenomics.allocate_tokens("development", 300000)

        # Print the current allocations and remaining supply
        print(tokenomics)

    except ValueError as e:
        print(f"Error: {e}")
```
