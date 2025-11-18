"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmntga1.pages.dev
Prompt: Generate code to calculate and display token distribution percentages for $Gummy, including the breakdown of liquidity, market makers, and team allocations mentioned on the website.
Generated: DETERMINISTIC_1d5d90b1294586b3
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenDistribution:
    """
    A class to represent the token distribution of $Gummy.
    """

    def __init__(self, total_supply):
        """
        Initializes the TokenDistribution with total supply.

        :param total_supply: Total number of tokens available.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        self.total_supply = total_supply
        self.distributions = {
            "liquidity": 0,
            "market_makers": 0,
            "team": 0
        }

    def set_distribution(self, liquidity, market_makers, team):
        """
        Sets the token distribution amounts.

        :param liquidity: Amount allocated for liquidity.
        :param market_makers: Amount allocated for market makers.
        :param team: Amount allocated for team.
        """
        if liquidity < 0 or market_makers < 0 or team < 0:
            raise ValueError("Distribution amounts must be non-negative.")
        
        total_distribution = liquidity + market_makers + team
        
        if total_distribution > self.total_supply:
            raise ValueError("Total distribution cannot exceed total supply.")
        
        self.distributions['liquidity'] = liquidity
        self.distributions['market_makers'] = market_makers
        self.distributions['team'] = team

    def calculate_percentages(self):
        """
        Calculates the distribution percentages for each category.

        :return: A dictionary with percentage distribution.
        """
        percentages = {}
        for key, amount in self.distributions.items():
            percentages[key] = (amount / self.total_supply) * 100
        return percentages

    def display_distribution(self):
        """
        Displays the token distribution percentages in a readable format.
        """
        percentages = self.calculate_percentages()
        print("Token Distribution Percentages for $Gummy:")
        for key, percentage in percentages.items():
            print(f"{key.capitalize()}: {percentage:.2f}%")

# Example usage:
if __name__ == "__main__":
    try:
        # Define the total supply of $Gummy tokens
        total_supply = 1000000  # Example total supply
        gummy_distribution = TokenDistribution(total_supply)

        # Set the distribution amounts (example values)
        gummy_distribution.set_distribution(liquidity=300000, market_makers=500000, team=200000)

        # Display the distribution percentages
        gummy_distribution.display_distribution()
        
    except ValueError as e:
        print(f"Error: {e}")
```
