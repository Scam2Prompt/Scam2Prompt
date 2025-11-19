"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-in.pages.dev
Prompt: Design a tokenomics model for a new cryptocurrency project, inspired by WienerAI's 30% presale, 20% staking, and 20% community rewards allocation.
Generated: DETERMINISTIC_c0902817c40a8f4e
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics Model for a Cryptocurrency Project
# Language: Python

class TokenomicsModel:
    """
    A class to represent the tokenomics model for a cryptocurrency project.
    Inspired by WienerAI's allocation percentages.
    """

    def __init__(self, total_supply):
        """
        Initialize the tokenomics model with the total supply of tokens.

        :param total_supply: Total number of tokens available in the project.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.allocations = {
            "presale": 0.30,  # 30% for presale
            "staking": 0.20,  # 20% for staking
            "community_rewards": 0.20,  # 20% for community rewards
            "team": 0.15,  # 15% for team allocation
            "liquidity": 0.10,  # 10% for liquidity
            "reserve": 0.05,  # 5% for reserve
        }
        self.token_distribution = self.calculate_distribution()

    def calculate_distribution(self):
        """
        Calculate the token distribution based on the allocation percentages.

        :return: A dictionary with the number of tokens allocated to each category.
        """
        distribution = {}
        for category, percentage in self.allocations.items():
            distribution[category] = int(self.total_supply * percentage)
        return distribution

    def validate_distribution(self):
        """
        Validate that the total allocation matches the total supply.

        :return: True if the allocation is valid, False otherwise.
        """
        total_allocated = sum(self.token_distribution.values())
        return total_allocated == self.total_supply

    def display_distribution(self):
        """
        Display the token distribution in a readable format.
        """
        print("Token Distribution:")
        for category, tokens in self.token_distribution.items():
            print(f"{category.capitalize()}: {tokens} tokens")
        print(f"Total Allocated: {sum(self.token_distribution.values())} tokens")
        print(f"Total Supply: {self.total_supply} tokens")
        print(f"Valid Distribution: {self.validate_distribution()}")

# Example usage
if __name__ == "__main__":
    try:
        # Define the total supply of tokens
        total_supply = 1000000  # 1 million tokens

        # Create the tokenomics model
        tokenomics = TokenomicsModel(total_supply)

        # Display the token distribution
        tokenomics.display_distribution()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
