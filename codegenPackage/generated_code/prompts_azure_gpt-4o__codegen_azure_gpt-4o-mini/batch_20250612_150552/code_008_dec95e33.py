"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-sale.pages.dev
Prompt: Write a Python script to calculate the allocation percentages of OMEME tokens for presale, staking rewards, liquidity, marketing, development, and community funds based on the tokenomics provided.
Generated: DETERMINISTIC_dec95e33f5a3590f
Batch ID: 20250612_150552
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

        :param total_supply: Total number of OMEME tokens available.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply

        # Define allocation percentages
        self.allocations = {
            "presale": 0.20,        # 20% for presale
            "staking_rewards": 0.25, # 25% for staking rewards
            "liquidity": 0.15,      # 15% for liquidity
            "marketing": 0.10,      # 10% for marketing
            "development": 0.20,    # 20% for development
            "community_funds": 0.10  # 10% for community funds
        }

    def calculate_allocations(self):
        """
        Calculate the number of tokens allocated to each category based on the total supply.

        :return: A dictionary with the allocation amounts for each category.
        """
        allocation_amounts = {}
        for category, percentage in self.allocations.items():
            allocation_amounts[category] = self.total_supply * percentage
        return allocation_amounts

    def display_allocations(self):
        """
        Display the allocation amounts for each category in a readable format.
        """
        try:
            allocations = self.calculate_allocations()
            print("OMEME Token Allocations:")
            for category, amount in allocations.items():
                print(f"{category.replace('_', ' ').title()}: {amount:.2f} tokens")
        except Exception as e:
            print(f"An error occurred while calculating allocations: {e}")


if __name__ == "__main__":
    try:
        # Example total supply of OMEME tokens
        total_supply = 1_000_000  # 1 million tokens
        tokenomics = Tokenomics(total_supply)
        tokenomics.display_allocations()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
