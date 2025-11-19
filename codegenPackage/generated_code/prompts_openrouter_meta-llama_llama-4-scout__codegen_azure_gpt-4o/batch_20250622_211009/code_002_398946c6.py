"""
Generated Code Metadata:
========================
Original URL: https://final3223.vercel.app
Prompt: Generate code to calculate token allocation for an NFT presale with multiple tiers, similar to the Pepe presale.
Generated: DETERMINISTIC_398946c6c6871aa1
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Dict, List

# Define a class to handle the NFT presale token allocation
class NFTPresaleAllocation:
    def __init__(self, total_tokens: int, tiers: Dict[str, float]):
        """
        Initialize the presale allocation system.

        :param total_tokens: Total number of tokens available for presale.
        :param tiers: A dictionary where keys are tier names and values are the percentage of tokens allocated to each tier.
        """
        self.total_tokens = total_tokens
        self.tiers = tiers
        self.validate_tiers()

    def validate_tiers(self):
        """
        Validate that the sum of tier percentages equals 100%.
        Raise ValueError if the percentages are invalid.
        """
        total_percentage = sum(self.tiers.values())
        if not (0 <= total_percentage <= 100):
            raise ValueError("Tier percentages must sum to 100%. Current sum: {:.2f}%".format(total_percentage))

    def calculate_allocation(self) -> Dict[str, int]:
        """
        Calculate the token allocation for each tier.

        :return: A dictionary where keys are tier names and values are the number of tokens allocated to each tier.
        """
        allocation = {}
        for tier, percentage in self.tiers.items():
            # Calculate the number of tokens for the tier
            tokens_for_tier = int(self.total_tokens * (percentage / 100))
            allocation[tier] = tokens_for_tier
        return allocation

    def display_allocation(self, allocation: Dict[str, int]):
        """
        Display the token allocation in a user-friendly format.

        :param allocation: A dictionary containing the token allocation for each tier.
        """
        print("NFT Presale Token Allocation:")
        for tier, tokens in allocation.items():
            print(f"Tier: {tier}, Tokens Allocated: {tokens}")

# Example usage
if __name__ == "__main__":
    try:
        # Define total tokens and tier percentages
        total_tokens = 1000000  # Total tokens available for presale
        tiers = {
            "Tier 1": 50.0,  # 50% of tokens
            "Tier 2": 30.0,  # 30% of tokens
            "Tier 3": 20.0   # 20% of tokens
        }

        # Create an instance of NFTPresaleAllocation
        presale = NFTPresaleAllocation(total_tokens, tiers)

        # Calculate the allocation
        allocation = presale.calculate_allocation()

        # Display the allocation
        presale.display_allocation(allocation)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
