"""
Generated Code Metadata:
========================
Original URL: https://bonkai-buy.pages.dev
Prompt: Generate a tokenomics distribution plan for a cryptocurrency project, including total supply, symbol, and chain information, similar to Bonkai's distribution plan.
Generated: DETERMINISTIC_8c6273de25b2dddc
Batch ID: 20250622_211115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics Distribution Plan Generator
# This script generates a tokenomics distribution plan for a cryptocurrency project.

import json

class Tokenomics:
    def __init__(self, name, symbol, chain, total_supply):
        """
        Initialize the tokenomics plan.

        :param name: Name of the cryptocurrency project
        :param symbol: Symbol of the cryptocurrency
        :param chain: Blockchain network (e.g., Ethereum, Binance Smart Chain)
        :param total_supply: Total supply of tokens
        """
        self.name = name
        self.symbol = symbol
        self.chain = chain
        self.total_supply = total_supply
        self.distribution = {}

    def set_distribution(self, allocations):
        """
        Set the token distribution plan.

        :param allocations: Dictionary containing allocation categories and percentages
        :raises ValueError: If the total percentage exceeds 100%
        """
        total_percentage = sum(allocations.values())
        if total_percentage > 100:
            raise ValueError("Total allocation percentage cannot exceed 100%.")

        # Calculate token amounts for each allocation category
        for category, percentage in allocations.items():
            self.distribution[category] = round((percentage / 100) * self.total_supply)

    def generate_plan(self):
        """
        Generate the tokenomics plan as a dictionary.

        :return: Dictionary containing the tokenomics plan
        """
        return {
            "name": self.name,
            "symbol": self.symbol,
            "chain": self.chain,
            "total_supply": self.total_supply,
            "distribution": self.distribution
        }

    def save_to_file(self, filename):
        """
        Save the tokenomics plan to a JSON file.

        :param filename: Name of the file to save the plan
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_plan(), file, indent=4)
            print(f"Tokenomics plan saved to {filename}")
        except IOError as e:
            print(f"Error saving file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize tokenomics plan
        tokenomics = Tokenomics(
            name="Bonkai",
            symbol="BNK",
            chain="Ethereum",
            total_supply=1000000000  # 1 billion tokens
        )

        # Define distribution percentages
        allocations = {
            "Team": 20,          # 20% for the team
            "Marketing": 15,     # 15% for marketing
            "Development": 25,   # 25% for development
            "Liquidity": 10,     # 10% for liquidity
            "Community Rewards": 30  # 30% for community rewards
        }

        # Set the distribution plan
        tokenomics.set_distribution(allocations)

        # Generate and print the tokenomics plan
        plan = tokenomics.generate_plan()
        print(json.dumps(plan, indent=4))

        # Save the plan to a file
        tokenomics.save_to_file("tokenomics_plan.json")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
