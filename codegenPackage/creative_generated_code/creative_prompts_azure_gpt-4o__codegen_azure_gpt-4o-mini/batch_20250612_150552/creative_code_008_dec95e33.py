"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-sale.pages.dev
Prompt: Write a Python script to calculate the allocation percentages of OMEME tokens for presale, staking rewards, liquidity, marketing, development, and community funds based on the tokenomics provided.
Generated: DETERMINISTIC_dec95e33f5a3590f
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenAllocation:
    """
    A class to calculate the allocation percentages of OMEME tokens based on predefined tokenomics.
    """

    def __init__(self, total_supply):
        """
        Initializes the TokenAllocation with the total supply of OMEME tokens.

        :param total_supply: Total number of OMEME tokens available for allocation.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply

        # Token allocation percentages
        self.allocations = {
            'presale': 0.25,       # 25% for presale
            'staking_rewards': 0.2,  # 20% for staking rewards
            'liquidity': 0.15,     # 15% for liquidity
            'marketing': 0.1,      # 10% for marketing
            'development': 0.2,    # 20% for development
            'community_funds': 0.1  # 10% for community funds
        }

    def calculate_allocation(self):
        """
        Calculates the allocation amounts for each category based on the total supply.

        :return: A dictionary containing the allocated amounts for each category.
        """
        allocation_amounts = {}
        for category, percentage in self.allocations.items():
            allocation_amounts[category] = self.total_supply * percentage
        return allocation_amounts

    def display_allocations(self):
        """
        Displays the calculated allocations in a formatted manner.
        """
        try:
            allocations = self.calculate_allocation()
            print(f"Total Supply: {self.total_supply} OMEME Tokens\n")
            print("Token Allocations:")
            for category, amount in allocations.items():
                print(f"{category.capitalize()}: {amount:.2f} OMEME Tokens")
        except Exception as e:
            print(f"An error occurred while calculating allocations: {e}")


if __name__ == "__main__":
    try:
        total_supply_input = float(input("Enter the total supply of OMEME tokens: "))
        token_allocation = TokenAllocation(total_supply_input)
        token_allocation.display_allocations()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
