"""
Generated Code Metadata:
========================
Original URL: https://normilio.pages.dev
Prompt: Design a basic tokenomics structure for a cryptocurrency project like Normilio, including a total supply of 1,000,000,000 coins.
Generated: DETERMINISTIC_54587bc53f87e40d
Batch ID: 20250622_211131
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
    A class to represent the tokenomics structure of a cryptocurrency project.
    """

    def __init__(self, total_supply: int):
        """
        Initializes the Tokenomics with a total supply.

        :param total_supply: Total number of tokens available for the project.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        
        self.total_supply = total_supply
        self.distributions = {
            "team": 0,
            "development": 0,
            "marketing": 0,
            "liquidity": 0,
            "community": 0,
            "reserve": 0,
        }

    def set_distribution(self, category: str, amount: int):
        """
        Sets the distribution amount for a specific category.

        :param category: The category to set the distribution for.
        :param amount: The amount to distribute to the category.
        """
        if category not in self.distributions:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.distributions.keys())}.")
        
        if amount < 0:
            raise ValueError("Amount must be a non-negative integer.")
        
        if self.get_total_distributed() + amount > self.total_supply:
            raise ValueError("Total distribution exceeds total supply.")
        
        self.distributions[category] += amount

    def get_total_distributed(self) -> int:
        """
        Returns the total amount of tokens distributed across all categories.

        :return: Total distributed tokens.
        """
        return sum(self.distributions.values())

    def get_remaining_supply(self) -> int:
        """
        Returns the remaining supply of tokens that can be distributed.

        :return: Remaining tokens.
        """
        return self.total_supply - self.get_total_distributed()

    def get_distribution_summary(self) -> dict:
        """
        Returns a summary of the token distribution.

        :return: A dictionary containing the distribution details.
        """
        return {
            "total_supply": self.total_supply,
            "distributed": self.get_total_distributed(),
            "remaining_supply": self.get_remaining_supply(),
            "distributions": self.distributions,
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize tokenomics with a total supply of 1,000,000,000
        tokenomics = Tokenomics(total_supply=1_000_000_000)

        # Set distributions for various categories
        tokenomics.set_distribution("team", 150_000_000)
        tokenomics.set_distribution("development", 200_000_000)
        tokenomics.set_distribution("marketing", 100_000_000)
        tokenomics.set_distribution("liquidity", 50_000_000)
        tokenomics.set_distribution("community", 300_000_000)
        tokenomics.set_distribution("reserve", 200_000_000)

        # Print the distribution summary
        print(tokenomics.get_distribution_summary())

    except ValueError as e:
        print(f"Error: {e}")
```
