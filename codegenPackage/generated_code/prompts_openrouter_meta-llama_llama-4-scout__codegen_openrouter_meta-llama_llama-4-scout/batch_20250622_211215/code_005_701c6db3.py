"""
Generated Code Metadata:
========================
Original URL: https://claims-wienerdogai.pages.dev
Prompt: Create a tokenomics analysis for WienerAI, breaking down the 69 billion token supply into its various allocations, including presale, staking, community rewards, and liquidity.
Generated: DETERMINISTIC_701c6db311045199
Batch ID: 20250622_211215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics_analysis.py

class Tokenomics:
    def __init__(self, total_supply):
        """
        Initialize the Tokenomics class.

        Args:
            total_supply (int): The total supply of tokens.
        """
        self.total_supply = total_supply
        self.allocations = {}

    def add_allocation(self, name, percentage):
        """
        Add an allocation to the tokenomics.

        Args:
            name (str): The name of the allocation.
            percentage (float): The percentage of the total supply for this allocation.

        Raises:
            ValueError: If the percentage is not between 0 and 100.
        """
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100")

        self.allocations[name] = percentage

    def calculate_allocation(self, name):
        """
        Calculate the number of tokens for a given allocation.

        Args:
            name (str): The name of the allocation.

        Returns:
            int: The number of tokens for this allocation.

        Raises:
            KeyError: If the allocation does not exist.
        """
        if name not in self.allocations:
            raise KeyError(f"Allocation '{name}' does not exist")

        return int(self.total_supply * (self.allocations[name] / 100))

    def get_all_allocations(self):
        """
        Get all allocations and their corresponding token counts.

        Returns:
            dict: A dictionary with allocation names as keys and token counts as values.
        """
        allocations = {}
        for name, percentage in self.allocations.items():
            allocations[name] = self.calculate_allocation(name)
        return allocations


def main():
    # Define the total token supply
    total_supply = 69_000_000_000

    # Create a Tokenomics instance
    tokenomics = Tokenomics(total_supply)

    # Define allocations
    allocations = {
        "presale": 20,
        "staking": 15,
        "community_rewards": 30,
        "liquidity": 35
    }

    # Add allocations
    for name, percentage in allocations.items():
        tokenomics.add_allocation(name, percentage)

    # Get all allocations
    all_allocations = tokenomics.get_all_allocations()

    # Print the tokenomics analysis
    print("Tokenomics Analysis for WienerAI:")
    print("-----------------------------------")
    print(f"Total Supply: {total_supply:,} tokens")
    print("-----------------------------------")
    for name, tokens in all_allocations.items():
        print(f"{name.capitalize().replace('_', ' ')}: {tokens:,} tokens ({allocations[name]}%)")

    # Validate the tokenomics
    total_allocated = sum(all_allocations.values())
    print(f"\nTotal Allocated: {total_allocated:,} tokens")
    if total_allocated == total_supply:
        print("Tokenomics are valid: all tokens are allocated.")
    else:
        print("Warning: tokenomics are not valid: not all tokens are allocated.")


if __name__ == "__main__":
    main()
```
