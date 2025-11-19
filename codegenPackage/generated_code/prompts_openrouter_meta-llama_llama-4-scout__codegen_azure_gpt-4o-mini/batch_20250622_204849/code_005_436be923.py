"""
Generated Code Metadata:
========================
Original URL: https://memekombat-api.pages.dev
Prompt: Create a tokenomics analysis tool for Meme Kombat, focusing on the 50% presale, 30% staking and battle rewards, 10% DEX, and 10% community rewards allocations.
Generated: DETERMINISTIC_436be9232227cdc2
Batch ID: 20250622_204849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class TokenomicsAnalysis:
    """
    A class to analyze the tokenomics of Meme Kombat.
    """

    def __init__(self, total_supply):
        """
        Initializes the TokenomicsAnalysis with the total supply of tokens.

        :param total_supply: Total supply of tokens (in integer).
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.allocations = {
            "presale": 0.50,
            "staking_and_battle_rewards": 0.30,
            "dex": 0.10,
            "community_rewards": 0.10
        }

    def calculate_allocations(self):
        """
        Calculates the token allocations based on the total supply.

        :return: A dictionary with the allocation amounts.
        """
        allocation_amounts = {}
        for key, percentage in self.allocations.items():
            allocation_amounts[key] = self.total_supply * percentage
        return allocation_amounts

    def to_json(self):
        """
        Converts the allocation amounts to a JSON string.

        :return: JSON string of the allocation amounts.
        """
        try:
            allocation_amounts = self.calculate_allocations()
            return json.dumps(allocation_amounts, indent=4)
        except Exception as e:
            raise RuntimeError(f"Error converting to JSON: {e}")

def main():
    """
    Main function to run the tokenomics analysis tool.
    """
    try:
        total_supply = int(input("Enter the total supply of tokens: "))
        tokenomics = TokenomicsAnalysis(total_supply)
        allocations_json = tokenomics.to_json()
        print("Tokenomics Allocations:")
        print(allocations_json)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
