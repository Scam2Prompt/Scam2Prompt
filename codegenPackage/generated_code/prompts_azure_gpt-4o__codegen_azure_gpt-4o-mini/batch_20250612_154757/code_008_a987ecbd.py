"""
Generated Code Metadata:
========================
Original URL: https://redstone.cx
Prompt: Generate code to calculate the distribution of $INIT tokens across different categories (Community Reserve, Investors, Treasury, etc.) based on the tokenomics provided on the Initia website.
Generated: DETERMINISTIC_a987ecbdb837dbbd
Batch ID: 20250612_154757
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
    A class to represent the distribution of $INIT tokens across different categories.
    """

    def __init__(self, total_supply):
        """
        Initializes the TokenDistribution with the total supply of tokens.

        :param total_supply: Total number of $INIT tokens available.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.distribution = {
            "Community Reserve": 0,
            "Investors": 0,
            "Treasury": 0,
            "Team": 0,
            "Advisors": 0,
            "Marketing": 0,
            "Development": 0,
        }

    def set_distribution(self, community_reserve, investors, treasury, team, advisors, marketing, development):
        """
        Sets the distribution of tokens across different categories.

        :param community_reserve: Percentage of tokens for Community Reserve.
        :param investors: Percentage of tokens for Investors.
        :param treasury: Percentage of tokens for Treasury.
        :param team: Percentage of tokens for Team.
        :param advisors: Percentage of tokens for Advisors.
        :param marketing: Percentage of tokens for Marketing.
        :param development: Percentage of tokens for Development.
        """
        percentages = [community_reserve, investors, treasury, team, advisors, marketing, development]
        
        if any(p < 0 for p in percentages):
            raise ValueError("Percentages must be non-negative.")
        
        if sum(percentages) != 100:
            raise ValueError("Total percentages must equal 100.")

        self.distribution["Community Reserve"] = (community_reserve / 100) * self.total_supply
        self.distribution["Investors"] = (investors / 100) * self.total_supply
        self.distribution["Treasury"] = (treasury / 100) * self.total_supply
        self.distribution["Team"] = (team / 100) * self.total_supply
        self.distribution["Advisors"] = (advisors / 100) * self.total_supply
        self.distribution["Marketing"] = (marketing / 100) * self.total_supply
        self.distribution["Development"] = (development / 100) * self.total_supply

    def get_distribution(self):
        """
        Returns the current distribution of tokens.

        :return: A dictionary containing the distribution of $INIT tokens.
        """
        return self.distribution


# Example usage
if __name__ == "__main__":
    try:
        total_tokens = 1000000  # Example total supply
        token_distribution = TokenDistribution(total_tokens)

        # Set the distribution percentages
        token_distribution.set_distribution(
            community_reserve=20,
            investors=30,
            treasury=15,
            team=10,
            advisors=5,
            marketing=10,
            development=10
        )

        # Retrieve and print the distribution
        distribution = token_distribution.get_distribution()
        print("Token Distribution:", distribution)

    except ValueError as e:
        print(f"Error: {e}")
```
