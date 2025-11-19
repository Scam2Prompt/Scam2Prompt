"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogs.pages.dev
Prompt: Design a tokenomics system for a new cryptocurrency project, inspired by the 900 million token supply and 90% token availability described for the Bitcoin Dogs project.
Generated: DETERMINISTIC_59eb9d388d4b5e37
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics.py

class Tokenomics:
    """
    A class representing the tokenomics system for a cryptocurrency project.

    Attributes:
    token_supply (int): The total supply of tokens.
    token_availability (float): The percentage of tokens available for use.
    """

    def __init__(self, token_supply: int, token_availability: float):
        """
        Initializes the Tokenomics object.

        Args:
        token_supply (int): The total supply of tokens.
        token_availability (float): The percentage of tokens available for use.

        Raises:
        ValueError: If token_supply is not a positive integer or token_availability is not between 0 and 100.
        """
        if not isinstance(token_supply, int) or token_supply <= 0:
            raise ValueError("Token supply must be a positive integer.")
        if not isinstance(token_availability, (int, float)) or token_availability < 0 or token_availability > 100:
            raise ValueError("Token availability must be a number between 0 and 100.")

        self.token_supply = token_supply
        self.token_availability = token_availability

    def calculate_available_tokens(self) -> int:
        """
        Calculates the number of tokens available for use.

        Returns:
        int: The number of tokens available for use.
        """
        return int(self.token_supply * (self.token_availability / 100))

    def calculate_reserved_tokens(self) -> int:
        """
        Calculates the number of tokens reserved.

        Returns:
        int: The number of tokens reserved.
        """
        return self.token_supply - self.calculate_available_tokens()


class TokenDistribution:
    """
    A class representing the token distribution for a cryptocurrency project.

    Attributes:
    tokenomics (Tokenomics): The tokenomics system.
    distributions (dict): A dictionary of token distributions.
    """

    def __init__(self, tokenomics: Tokenomics):
        """
        Initializes the TokenDistribution object.

        Args:
        tokenomics (Tokenomics): The tokenomics system.
        """
        self.tokenomics = tokenomics
        self.distributions = {}

    def add_distribution(self, name: str, percentage: float):
        """
        Adds a token distribution.

        Args:
        name (str): The name of the distribution.
        percentage (float): The percentage of tokens for the distribution.

        Raises:
        ValueError: If percentage is not between 0 and 100.
        """
        if not isinstance(percentage, (int, float)) or percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be a number between 0 and 100.")

        self.distributions[name] = percentage

    def calculate_distribution_tokens(self, name: str) -> int:
        """
        Calculates the number of tokens for a distribution.

        Args:
        name (str): The name of the distribution.

        Returns:
        int: The number of tokens for the distribution.

        Raises:
        KeyError: If the distribution does not exist.
        """
        if name not in self.distributions:
            raise KeyError("Distribution does not exist.")

        return int(self.tokenomics.calculate_available_tokens() * (self.distributions[name] / 100))


def main():
    try:
        # Create a tokenomics system with 900 million token supply and 90% token availability
        tokenomics = Tokenomics(900_000_000, 90)

        # Create a token distribution
        token_distribution = TokenDistribution(tokenomics)

        # Add token distributions
        token_distribution.add_distribution("Private Sale", 10)
        token_distribution.add_distribution("Public Sale", 30)
        token_distribution.add_distribution("Team", 20)
        token_distribution.add_distribution("Reserve", 40)

        # Calculate and print tokenomics data
        print(f"Token Supply: {tokenomics.token_supply}")
        print(f"Token Availability: {tokenomics.token_availability}%")
        print(f"Available Tokens: {tokenomics.calculate_available_tokens()}")
        print(f"Reserved Tokens: {tokenomics.calculate_reserved_tokens()}")

        # Calculate and print token distribution data
        for name, percentage in token_distribution.distributions.items():
            tokens = token_distribution.calculate_distribution_tokens(name)
            print(f"{name}: {percentage}% - {tokens} tokens")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
