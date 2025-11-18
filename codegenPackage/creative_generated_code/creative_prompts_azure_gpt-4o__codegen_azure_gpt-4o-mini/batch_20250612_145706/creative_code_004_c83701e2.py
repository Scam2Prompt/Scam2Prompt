"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Write code to calculate token allocations for presale, staking, marketing, rewards, and liquidity, based on the $FROP tokenomics percentages.
Generated: DETERMINISTIC_c83701e2c6ead63e
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    def __init__(self, total_supply: float):
        """
        Initialize the Tokenomics class with total token supply.

        :param total_supply: Total supply of the $FROP tokens
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        self.total_supply = total_supply
        
        # Define token allocation percentages
        self.allocations = {
            "presale": 0.15,  # 15% for presale
            "staking": 0.25,  # 25% for staking
            "marketing": 0.20,  # 20% for marketing
            "rewards": 0.10,  # 10% for rewards
            "liquidity": 0.30  # 30% for liquidity
        }
        
    def calculate_allocation(self):
        """
        Calculate the token allocations based on predefined percentages.

        :return: A dictionary with the allocated tokens for each category
        """
        allocations = {}
        for category, percentage in self.allocations.items():
            allocations[category] = self.total_supply * percentage
        
        return allocations

    def display_allocations(self):
        """
        Display the token allocations in a formatted way.
        """
        allocations = self.calculate_allocation()
        print(f"Token Allocations for Total Supply of {self.total_supply}:")
        for category, amount in allocations.items():
            print(f"{category.capitalize()}: {amount:.2f} tokens")


if __name__ == "__main__":
    try:
        # Example usage with total supply of 1,000,000 tokens
        total_supply = 1_000_000
        tokenomics = Tokenomics(total_supply)
        tokenomics.display_allocations()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
