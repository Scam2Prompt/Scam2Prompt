"""
Generated Code Metadata:
========================
Original URL: https://gmntga1.pages.dev
Prompt: Generate code to calculate and display token distribution percentages for $Gummy, including the breakdown of liquidity, market makers, and team allocations mentioned on the website.
Generated: DETERMINISTIC_1d5d90b1294586b3
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenDistribution:
    """
    A class to represent the token distribution for $Gummy.
    """

    def __init__(self, total_supply):
        """
        Initializes the TokenDistribution with the total supply of tokens.

        :param total_supply: Total number of tokens available.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.distributions = {
            "liquidity": 0,
            "market_makers": 0,
            "team": 0
        }

    def set_distribution(self, liquidity, market_makers, team):
        """
        Sets the distribution amounts for liquidity, market makers, and team.

        :param liquidity: Amount allocated for liquidity.
        :param market_makers: Amount allocated for market makers.
        :param team: Amount allocated for the team.
        """
        if liquidity < 0 or market_makers < 0 or team < 0:
            raise ValueError("Distribution amounts must be non-negative.")
        
        total_allocated = liquidity + market_makers + team
        if total_allocated > self.total_supply:
            raise ValueError("Total allocated exceeds total supply.")

        self.distributions["liquidity"] = liquidity
        self.distributions["market_makers"] = market_makers
        self.distributions["team"] = team

    def calculate_distribution_percentages(self):
        """
        Calculates the distribution percentages for each category.

        :return: A dictionary containing the percentage distribution.
        """
        percentages = {}
        for key, value in self.distributions.items():
            percentages[key] = (value / self.total_supply) * 100 if self.total_supply > 0 else 0
        return percentages

    def display_distribution(self):
        """
        Displays the token distribution percentages in a readable format.
        """
        percentages = self.calculate_distribution_percentages()
        print("Token Distribution Percentages for $Gummy:")
        for category, percentage in percentages.items():
            print(f"{category.capitalize()}: {percentage:.2f}%")

# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000  # Example total supply
        token_distribution = TokenDistribution(total_supply)
        
        # Set the distribution amounts
        token_distribution.set_distribution(liquidity=300000, market_makers=200000, team=500000)
        
        # Display the distribution percentages
        token_distribution.display_distribution()
    except ValueError as e:
        print(f"Error: {e}")
```
