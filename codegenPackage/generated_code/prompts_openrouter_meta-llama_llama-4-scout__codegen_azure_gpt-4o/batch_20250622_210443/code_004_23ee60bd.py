"""
Generated Code Metadata:
========================
Original URL: https://memekombat-in.pages.dev
Prompt: Design a tokenomics system for a new gaming platform, inspired by Meme Kombat's 50% presale, 30% staking and battle rewards, 10% DEX, and 10% community rewards.
Generated: DETERMINISTIC_23ee60bda485f10c
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import decimal
from decimal import Decimal

# Set up decimal precision for financial calculations
decimal.getcontext().prec = 28

class TokenomicsSystem:
    """
    A class to represent the tokenomics system for a gaming platform.
    Inspired by Meme Kombat's allocation percentages.
    """

    def __init__(self, total_supply):
        """
        Initialize the tokenomics system with the total token supply.

        :param total_supply: Total number of tokens available in the system.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        
        self.total_supply = Decimal(total_supply)
        self.allocations = {
            "presale": Decimal("0.50"),  # 50% for presale
            "staking_rewards": Decimal("0.30"),  # 30% for staking and battle rewards
            "dex_liquidity": Decimal("0.10"),  # 10% for DEX liquidity
            "community_rewards": Decimal("0.10")  # 10% for community rewards
        }
        self.distribution = self.calculate_distribution()

    def calculate_distribution(self):
        """
        Calculate the token distribution based on allocation percentages.

        :return: A dictionary with the token distribution for each category.
        """
        distribution = {}
        for category, percentage in self.allocations.items():
            distribution[category] = self.total_supply * percentage
        return distribution

    def get_distribution(self):
        """
        Get the token distribution.

        :return: A dictionary with the token distribution for each category.
        """
        return self.distribution

    def validate_distribution(self):
        """
        Validate that the total allocation percentages sum up to 100%.

        :return: True if valid, raises ValueError otherwise.
        """
        total_percentage = sum(self.allocations.values())
        if total_percentage != Decimal("1.00"):
            raise ValueError("Allocation percentages must sum up to 100%.")
        return True

    def update_allocation(self, category, new_percentage):
        """
        Update the allocation percentage for a specific category.

        :param category: The category to update (e.g., 'presale', 'staking_rewards').
        :param new_percentage: The new percentage to allocate (as a decimal).
        """
        if category not in self.allocations:
            raise KeyError(f"Category '{category}' does not exist.")
        if new_percentage < 0 or new_percentage > 1:
            raise ValueError("Percentage must be between 0 and 1.")
        
        self.allocations[category] = Decimal(new_percentage)
        self.validate_distribution()  # Ensure total percentages are valid
        self.distribution = self.calculate_distribution()  # Recalculate distribution

    def display_distribution(self):
        """
        Display the token distribution in a user-friendly format.
        """
        print("Token Distribution:")
        for category, amount in self.distribution.items():
            print(f"{category.capitalize()}: {amount} tokens")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tokenomics system with a total supply of 1,000,000 tokens
        total_supply = 1_000_000
        tokenomics = TokenomicsSystem(total_supply)

        # Display the initial distribution
        tokenomics.display_distribution()

        # Update the allocation for 'community_rewards' to 15% and display the updated distribution
        tokenomics.update_allocation("community_rewards", 0.15)
        tokenomics.display_distribution()

    except Exception as e:
        print(f"Error: {e}")
```
