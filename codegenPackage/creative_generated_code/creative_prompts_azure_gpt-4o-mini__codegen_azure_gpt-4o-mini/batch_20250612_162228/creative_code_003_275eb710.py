"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-gummyonsol.pages.dev
Prompt: Develop a Python script that calculates the distribution percentages of the $Gummy tokenomics as described on the Gummy on Sol website.
Generated: DETERMINISTIC_275eb710129ab5a7
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TokenomicsDistribution:
    def __init__(self, total_supply):
        """
        Initializes the TokenomicsDistribution with the total supply of $Gummy tokens.
        
        :param total_supply: Total supply of $Gummy tokens (float or int)
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        
        self.total_supply = total_supply
        self.distributions = {
            "Team": 0.10,               # 10% for Team
            "Advisors": 0.05,           # 5% for Advisors
            "Liquidity": 0.20,          # 20% for Liquidity
            "Marketing": 0.15,          # 15% for Marketing
            "Development": 0.10,        # 10% for Development
            "Ecosystem": 0.40           # 40% for Ecosystem
        }

    def calculate_distribution(self):
        """
        Calculates the distribution amounts based on the total supply and the tokenomics distribution percentages.

        :return: A dictionary containing the distribution amounts for each category
        """
        distribution_amounts = {}
        
        for category, percentage in self.distributions.items():
            distribution_amounts[category] = self.total_supply * percentage
        
        return distribution_amounts

    def display_distribution(self):
        """
        Displays the distribution amounts in a formatted manner.
        """
        distribution_amounts = self.calculate_distribution()
        print("Tokenomics Distribution of $Gummy Tokens:")
        
        for category, amount in distribution_amounts.items():
            print(f"{category}: {amount:.2f} tokens")

def main():
    """
    Main function to execute the TokenomicsDistribution calculations.
    """
    try:
        # Example total supply for $Gummy tokens
        total_supply = 1_000_000_000  # 1 billion tokens

        # Create an instance of TokenomicsDistribution
        tokenomics = TokenomicsDistribution(total_supply)
        
        # Display the distribution
        tokenomics.display_distribution()
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
