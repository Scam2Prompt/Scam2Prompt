"""
Generated Code Metadata:
========================
Original URL: https://grooveup.pages.dev
Prompt: Develop a tokenomics system for a decentralized music platform with a total supply of 1 billion tokens, allocating tokens for seed investors, liquidity, stream rewards, marketing, development, and team.
Generated: DETERMINISTIC_993e023ad87d2219
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Tokenomics:
    def __init__(self, total_supply=1_000_000_000):
        """
        Initialize the Tokenomics system with a total supply of tokens.

        :param total_supply: Total number of tokens available (default is 1 billion).
        """
        self.total_supply = total_supply
        self.allocations = {
            'seed_investors': 0,
            'liquidity': 0,
            'stream_rewards': 0,
            'marketing': 0,
            'development': 0,
            'team': 0
        }

    def allocate_tokens(self, category, amount):
        """
        Allocate tokens to a specific category.

        :param category: The category to allocate tokens to.
        :param amount: The amount of tokens to allocate.
        :raises ValueError: If the allocation exceeds the remaining supply or is negative.
        """
        if amount < 0:
            raise ValueError("Allocation amount cannot be negative.")
        
        if self.get_remaining_supply() < amount:
            raise ValueError("Not enough tokens remaining for allocation.")

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
        :return: Allocated amount for the category.
        :raises KeyError: If the category does not exist.
        """
        if category not in self.allocations:
            raise KeyError(f"Category '{category}' does not exist.")
        return self.allocations[category]

    def display_allocations(self):
        """
        Display the current allocations of tokens across all categories.
        """
        print("Current Token Allocations:")
        for category, amount in self.allocations.items():
            print(f"{category}: {amount} tokens")
        print(f"Remaining Supply: {self.get_remaining_supply()} tokens")


# Example usage
if __name__ == "__main__":
    try:
        tokenomics = Tokenomics()

        # Allocate tokens to different categories
        tokenomics.allocate_tokens('seed_investors', 100_000_000)
        tokenomics.allocate_tokens('liquidity', 50_000_000)
        tokenomics.allocate_tokens('stream_rewards', 300_000_000)
        tokenomics.allocate_tokens('marketing', 100_000_000)
        tokenomics.allocate_tokens('development', 150_000_000)
        tokenomics.allocate_tokens('team', 200_000_000)

        # Display the allocations
        tokenomics.display_allocations()

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
