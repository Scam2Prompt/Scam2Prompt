"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzyw7qgtjbkq6dimtys2ndltbec2rzobfuk2gxi2gbt5rg3w4c6a.ipfs.dweb.link
Prompt: Write a Python script to calculate the token distribution of $gummy, given the percentages allocated to CEX liquidity, market makers, marketing, LP, burnt, team, and founders.
Generated: DETERMINISTIC_f5908884ec0d9cd9
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_distribution.py

class TokenDistribution:
    def __init__(self, total_supply):
        """
        Initialize the TokenDistribution with the total supply of tokens.

        :param total_supply: Total number of tokens available for distribution
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.distribution = {
            "CEX_liquidity": 0,
            "market_makers": 0,
            "marketing": 0,
            "LP": 0,
            "burnt": 0,
            "team": 0,
            "founders": 0
        }

    def calculate_distribution(self, percentages):
        """
        Calculate the token distribution based on the provided percentages.

        :param percentages: Dictionary containing the percentage allocation for each category
        :raises ValueError: If the total percentage does not equal 100
        """
        total_percentage = sum(percentages.values())
        if total_percentage != 100:
            raise ValueError("Total percentage must equal 100.")

        for category, percentage in percentages.items():
            if category not in self.distribution:
                raise ValueError(f"Unknown category: {category}")
            self.distribution[category] = (percentage / 100) * self.total_supply

    def get_distribution(self):
        """
        Get the current token distribution.

        :return: Dictionary containing the token distribution
        """
        return self.distribution


if __name__ == "__main__":
    # Example usage
    try:
        total_supply = 1000000  # Total supply of $gummy tokens
        percentages = {
            "CEX_liquidity": 20,
            "market_makers": 15,
            "marketing": 10,
            "LP": 25,
            "burnt": 5,
            "team": 15,
            "founders": 10
        }

        # Create a TokenDistribution instance
        token_distribution = TokenDistribution(total_supply)

        # Calculate the distribution
        token_distribution.calculate_distribution(percentages)

        # Print the distribution
        print("Token Distribution:", token_distribution.get_distribution())

    except ValueError as e:
        print(f"Error: {e}")
```
