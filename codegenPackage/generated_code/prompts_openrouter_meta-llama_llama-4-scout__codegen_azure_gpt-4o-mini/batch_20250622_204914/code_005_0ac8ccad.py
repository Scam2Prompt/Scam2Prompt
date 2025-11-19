"""
Generated Code Metadata:
========================
Original URL: https://app-pepeunchained.pages.dev
Prompt: Explain the tokenomics of $PEPU, including the allocation of tokens for presale, staking, marketing, liquidity, project finance, and chain inventory.
Generated: DETERMINISTIC_0ac8ccad24774e9e
Batch ID: 20250622_204914
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
    A class to represent the tokenomics of the $PEPU token.
    """

    def __init__(self):
        """
        Initializes the tokenomics with predefined allocations.
        """
        self.allocations = {
            "presale": 0.20,  # 20% for presale
            "staking": 0.25,  # 25% for staking
            "marketing": 0.15,  # 15% for marketing
            "liquidity": 0.20,  # 20% for liquidity
            "project_finance": 0.10,  # 10% for project finance
            "chain_inventory": 0.10  # 10% for chain inventory
        }
        self.total_supply = 1_000_000_000  # Total supply of $PEPU tokens

    def calculate_allocation(self):
        """
        Calculates the number of tokens allocated to each category based on the total supply.

        Returns:
            dict: A dictionary containing the number of tokens allocated to each category.
        """
        allocation_amounts = {}
        for category, percentage in self.allocations.items():
            allocation_amounts[category] = self.total_supply * percentage
        return allocation_amounts

    def display_tokenomics(self):
        """
        Displays the tokenomics allocation in a readable format.
        """
        try:
            allocation_amounts = self.calculate_allocation()
            print("Tokenomics of $PEPU:")
            for category, amount in allocation_amounts.items():
                print(f"{category.capitalize()}: {amount:.0f} tokens")
        except Exception as e:
            print(f"An error occurred while displaying tokenomics: {e}")

if __name__ == "__main__":
    # Create an instance of the Tokenomics class
    tokenomics = Tokenomics()
    
    # Display the tokenomics allocation
    tokenomics.display_tokenomics()
```
