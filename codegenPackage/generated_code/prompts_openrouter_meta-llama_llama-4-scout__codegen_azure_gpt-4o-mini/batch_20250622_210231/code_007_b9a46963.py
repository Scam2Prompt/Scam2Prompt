"""
Generated Code Metadata:
========================
Original URL: https://scottytheais.web.app
Prompt: Propose a tokenomics model in Python for a new crypto project with a similar structure to Scotty AI's token distribution and supply.
Generated: DETERMINISTIC_b9a469638360e415
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenomicsModel:
    """
    A class to represent the tokenomics model for a cryptocurrency project.
    
    Attributes:
        total_supply (int): The total supply of tokens.
        distribution (dict): A dictionary to hold the distribution of tokens.
    """

    def __init__(self, total_supply):
        """
        Initializes the TokenomicsModel with a total supply and sets up the distribution.

        Args:
            total_supply (int): The total number of tokens to be distributed.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        
        self.total_supply = total_supply
        self.distribution = {
            "team": 0,
            "advisors": 0,
            "investors": 0,
            "community": 0,
            "development": 0,
            "marketing": 0,
            "liquidity": 0,
            "reserve": 0
        }

    def set_distribution(self, team, advisors, investors, community, development, marketing, liquidity, reserve):
        """
        Sets the distribution of tokens across various categories.

        Args:
            team (float): Percentage of tokens for the team.
            advisors (float): Percentage of tokens for advisors.
            investors (float): Percentage of tokens for investors.
            community (float): Percentage of tokens for the community.
            development (float): Percentage of tokens for development.
            marketing (float): Percentage of tokens for marketing.
            liquidity (float): Percentage of tokens for liquidity.
            reserve (float): Percentage of tokens for reserve.

        Raises:
            ValueError: If the total percentage exceeds 100 or any percentage is negative.
        """
        percentages = [team, advisors, investors, community, development, marketing, liquidity, reserve]
        
        if any(p < 0 for p in percentages):
            raise ValueError("Percentages must be non-negative.")
        
        total_percentage = sum(percentages)
        if total_percentage > 100:
            raise ValueError("Total percentage cannot exceed 100.")
        
        self.distribution["team"] = (team / 100) * self.total_supply
        self.distribution["advisors"] = (advisors / 100) * self.total_supply
        self.distribution["investors"] = (investors / 100) * self.total_supply
        self.distribution["community"] = (community / 100) * self.total_supply
        self.distribution["development"] = (development / 100) * self.total_supply
        self.distribution["marketing"] = (marketing / 100) * self.total_supply
        self.distribution["liquidity"] = (liquidity / 100) * self.total_supply
        self.distribution["reserve"] = (reserve / 100) * self.total_supply

    def get_distribution(self):
        """
        Returns the current token distribution.

        Returns:
            dict: A dictionary containing the distribution of tokens.
        """
        return self.distribution

    def __str__(self):
        """
        Returns a string representation of the tokenomics model.

        Returns:
            str: A string summarizing the total supply and distribution.
        """
        distribution_str = ', '.join(f"{key}: {value}" for key, value in self.distribution.items())
        return f"Total Supply: {self.total_supply}, Distribution: {{{distribution_str}}}"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tokenomics model with a total supply of 1,000,000 tokens
        tokenomics = TokenomicsModel(total_supply=1_000_000)

        # Set the distribution percentages
        tokenomics.set_distribution(
            team=20,
            advisors=10,
            investors=15,
            community=25,
            development=10,
            marketing=10,
            liquidity=5,
            reserve=5
        )

        # Print the distribution
        print(tokenomics)

    except ValueError as e:
        print(f"Error: {e}")
```
