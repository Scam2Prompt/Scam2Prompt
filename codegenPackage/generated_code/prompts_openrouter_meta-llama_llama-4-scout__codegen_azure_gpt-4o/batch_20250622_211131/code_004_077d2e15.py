"""
Generated Code Metadata:
========================
Original URL: https://memekombatioclaim.pages.dev
Prompt: "Create a tokenomics model for a new gaming platform, similar to Meme Kombat's 50% presale, 30% staking and battle rewards, and 10% community rewards."
Generated: DETERMINISTIC_077d2e15ba8d2553
Batch ID: 20250622_211131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class TokenomicsModel:
    """
    A class to represent the tokenomics model for a gaming platform.
    """

    def __init__(self, total_supply):
        """
        Initialize the TokenomicsModel with the total token supply.

        :param total_supply: Total number of tokens available in the system.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.allocations = {
            "presale": 0,
            "staking_rewards": 0,
            "community_rewards": 0,
            "reserve": 0
        }
        self._allocate_tokens()

    def _allocate_tokens(self):
        """
        Allocate tokens based on the predefined percentages:
        - 50% for presale
        - 30% for staking and battle rewards
        - 10% for community rewards
        - 10% for reserve (remaining tokens)
        """
        self.allocations["presale"] = self.total_supply * 0.50
        self.allocations["staking_rewards"] = self.total_supply * 0.30
        self.allocations["community_rewards"] = self.total_supply * 0.10
        self.allocations["reserve"] = self.total_supply * 0.10

    def get_allocation(self, category):
        """
        Get the token allocation for a specific category.

        :param category: The category to retrieve allocation for (e.g., 'presale').
        :return: The number of tokens allocated to the category.
        """
        if category not in self.allocations:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.allocations.keys())}")
        return self.allocations[category]

    def to_json(self):
        """
        Export the tokenomics model to a JSON representation.

        :return: A JSON string representing the tokenomics model.
        """
        return json.dumps({
            "total_supply": self.total_supply,
            "allocations": self.allocations
        }, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tokenomics model with a total supply of 1,000,000 tokens
        total_supply = 1_000_000
        tokenomics = TokenomicsModel(total_supply)

        # Print allocations
        print("Token Allocations:")
        for category, amount in tokenomics.allocations.items():
            print(f"{category.capitalize()}: {amount} tokens")

        # Export to JSON
        print("\nTokenomics Model (JSON):")
        print(tokenomics.to_json())

    except ValueError as e:
        print(f"Error: {e}")
```
