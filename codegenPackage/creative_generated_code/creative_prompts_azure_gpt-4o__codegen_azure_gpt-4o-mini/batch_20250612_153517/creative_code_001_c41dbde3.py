"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-babywif-io.pages.dev
Prompt: Generate code to calculate the token distribution percentages for Baby WIF ($BIF) based on the given tokenomics: 95% for Presale+Liquidity and 5% for CEX Listing. Use Python for the implementation.
Generated: DETERMINISTIC_c41dbde311b4dfc8
Batch ID: 20250612_153517
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
    A class to represent the token distribution for Baby WIF ($BIF).
    """

    def __init__(self, total_supply: float):
        """
        Initialize the TokenDistribution with total supply.

        :param total_supply: Total number of tokens available for distribution.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        self.total_supply = total_supply
        self.distributions = {
            "Presale+Liquidity": 0.95,
            "CEX Listing": 0.05
        }

    def calculate_distribution(self) -> dict:
        """
        Calculate the token distribution based on the defined percentages.

        :return: A dictionary containing the distribution amounts for each category.
        """
        distribution_amounts = {}

        for category, percentage in self.distributions.items():
            amount = self.total_supply * percentage
            distribution_amounts[category] = amount

        return distribution_amounts

    def display_distribution(self):
        """
        Display the token distribution in a readable format.
        """
        try:
            distribution = self.calculate_distribution()
            print("Token Distribution for Baby WIF ($BIF):")
            for category, amount in distribution.items():
                print(f"{category}: {amount:.2f} tokens")
        except Exception as e:
            print(f"An error occurred while calculating the distribution: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        total_supply = float(input("Enter the total supply of Baby WIF ($BIF): "))
        token_distribution = TokenDistribution(total_supply)
        token_distribution.display_distribution()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
