"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswapsale-io.pages.dev
Prompt: Write a Python script to calculate token distribution percentages (e.g., 25% to Community, 13% Reserved Funding, etc.) based on UniswapSale's allocation data for a total supply of 10,000,000 IQN tokens.
Generated: DETERMINISTIC_2445f758d7ab5d55
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# token_distribution.py

class TokenDistribution:
    def __init__(self, total_supply):
        """
        Initializes the TokenDistribution with a total supply of tokens.

        :param total_supply: Total supply of tokens (in this case, 10,000,000 IQN).
        """
        self.total_supply = total_supply
        self.allocations = {}

    def add_allocation(self, category, percentage):
        """
        Adds an allocation category with its corresponding percentage.

        :param category: The name of the allocation category.
        :param percentage: The percentage of the total supply allocated to this category.
        :raises ValueError: If the percentage is not in the range [0, 100].
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        self.allocations[category] = percentage

    def calculate_distribution(self):
        """
        Calculates the distribution of tokens based on the allocations.

        :return: A dictionary containing the allocation category and the number of tokens.
        """
        distribution = {}
        for category, percentage in self.allocations.items():
            tokens_allocated = (percentage / 100) * self.total_supply
            distribution[category] = tokens_allocated
        return distribution

    def display_distribution(self):
        """
        Prints the token distribution in a readable format.
        """
        distribution = self.calculate_distribution()
        print(f"Total Supply: {self.total_supply} IQN Tokens\n")
        print("Token Distribution:")
        for category, tokens in distribution.items():
            print(f"{category}: {tokens:.2f} IQN Tokens ({self.allocations[category]}%)")

if __name__ == "__main__":
    # Total supply of IQN tokens
    TOTAL_SUPPLY = 10_000_000

    # Create an instance of TokenDistribution
    token_distribution = TokenDistribution(total_supply=TOTAL_SUPPLY)

    # Define allocation categories and their percentages
    allocations = {
        "Community": 25,
        "Reserved Funding": 13,
        "Liquidity": 20,
        "Development": 15,
        "Marketing": 10,
        "Exchange Listing": 5,
        "Advisors": 5,
        "Team": 7
    }

    # Adding allocations to the TokenDistribution object
    for category, percentage in allocations.items():
        try:
            token_distribution.add_allocation(category, percentage)
        except ValueError as e:
            print(f"Error adding allocation for {category}: {e}")

    # Display the final token distribution
    token_distribution.display_distribution()
```
