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
# Tokenomics System for CRUDO Token
# Language: Python
# This script defines the allocation of CRUDO tokens for various purposes.

class Tokenomics:
    """
    A class to represent the tokenomics system for the CRUDO token.
    """

    def __init__(self, total_supply):
        """
        Initialize the tokenomics system with the total supply of tokens.

        :param total_supply: Total supply of CRUDO tokens (integer).
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

        :param category: The category to allocate tokens to (string).
        :param amount: The number of tokens to allocate (integer).
        """
        if category not in self.allocations:
            raise ValueError(f"Invalid category '{category}'. Valid categories are: {', '.join(self.allocations.keys())}.")
        if amount <= 0:
            raise ValueError("Allocation amount must be a positive integer.")
        if self.get_unallocated_tokens() < amount:
            raise ValueError("Insufficient unallocated tokens for this allocation.")
        
        self.allocations[category] += amount

    def get_unallocated_tokens(self):
        """
        Calculate the number of unallocated tokens.

        :return: Number of unallocated tokens (integer).
        """
        allocated_tokens = sum(self.allocations.values())
        return self.total_supply - allocated_tokens

    def get_allocation_summary(self):
        """
        Get a summary of token allocations.

        :return: Dictionary containing allocation details.
        """
        return {
            "total_supply": self.total_supply,
            "allocated_tokens": sum(self.allocations.values()),
            "unallocated_tokens": self.get_unallocated_tokens(),
            "allocations": self.allocations
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tokenomics system with a total supply of 1,000,000 CRUDO tokens
        crudo_tokenomics = Tokenomics(total_supply=1_000_000)

        # Allocate tokens to various categories
        crudo_tokenomics.allocate_tokens("presale", 200_000)
        crudo_tokenomics.allocate_tokens("rewards", 150_000)
        crudo_tokenomics.allocate_tokens("ico_bonus", 100_000)
        crudo_tokenomics.allocate_tokens("marketing", 250_000)
        crudo_tokenomics.allocate_tokens("ecosystem_operations", 200_000)
        crudo_tokenomics.allocate_tokens("other", 50_000)

        # Print the allocation summary
        summary = crudo_tokenomics.get_allocation_summary()
        print("Token Allocation Summary:")
        print(f"Total Supply: {summary['total_supply']}")
        print(f"Allocated Tokens: {summary['allocated_tokens']}")
        print(f"Unallocated Tokens: {summary['unallocated_tokens']}")
        print("Allocations:")
        for category, amount in summary['allocations'].items():
            print(f"  {category}: {amount}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
