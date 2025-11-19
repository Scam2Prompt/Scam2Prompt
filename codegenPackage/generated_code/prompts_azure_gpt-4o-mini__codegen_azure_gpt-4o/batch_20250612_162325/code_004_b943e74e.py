"""
Generated Code Metadata:
========================
Original URL: https://peng-six.vercel.app
Prompt: What are the key features of the $PENG tokenomics? Provide a code example that calculates the total supply and remaining liquidity based on the given tokenomics data.
Generated: DETERMINISTIC_b943e74e0a46d12b
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics Calculator for $PENG Token
# This script calculates the total supply and remaining liquidity based on the given tokenomics data.

class PengTokenomics:
    """
    A class to represent the tokenomics of the $PENG token.
    """

    def __init__(self, total_supply, allocations):
        """
        Initialize the tokenomics with total supply and allocation details.

        :param total_supply: Total supply of the $PENG token (int).
        :param allocations: Dictionary containing allocation details (dict).
        """
        self.total_supply = total_supply
        self.allocations = allocations

    def calculate_remaining_liquidity(self):
        """
        Calculate the remaining liquidity after allocations.

        :return: Remaining liquidity (int).
        """
        allocated_tokens = sum(self.allocations.values())
        if allocated_tokens > self.total_supply:
            raise ValueError("Allocated tokens exceed total supply!")
        return self.total_supply - allocated_tokens


# Example tokenomics data
# Total supply of $PENG token
TOTAL_SUPPLY = 1_000_000_000  # 1 billion tokens

# Allocations (in tokens)
ALLOCATIONS = {
    "team": 200_000_000,       # 20% for the team
    "marketing": 150_000_000,  # 15% for marketing
    "development": 250_000_000,  # 25% for development
    "community_rewards": 100_000_000,  # 10% for community rewards
    "reserve": 50_000_000,     # 5% for reserve
}

# Instantiate the PengTokenomics class
peng_tokenomics = PengTokenomics(TOTAL_SUPPLY, ALLOCATIONS)

# Calculate remaining liquidity
try:
    remaining_liquidity = peng_tokenomics.calculate_remaining_liquidity()
    print(f"Total Supply: {TOTAL_SUPPLY}")
    print(f"Remaining Liquidity: {remaining_liquidity}")
except ValueError as e:
    print(f"Error: {e}")
```
