"""
Generated Code Metadata:
========================
Original URL: https://claimpage-gummyonsol.pages.dev
Prompt: Generate code to calculate the $Gummy token distribution based on the provided tokenomics: 30% CEX Liquidity, 10% Market Makers, 20% Marketing LP, and 40% burnt.
Generated: DETERMINISTIC_583c95a6d9fff78b
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GummyTokenDistribution:
    def __init__(self, total_supply: float):
        """
        Initialize the GummyTokenDistribution with the total supply of tokens.

        :param total_supply: Total supply of Gummy tokens.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply

    def calculate_distribution(self):
        """
        Calculate the distribution of Gummy tokens based on predefined tokenomics.

        :return: A dictionary containing the distribution of tokens.
        """
        distribution = {
            "CEX_Liquidity": self._calculate_percentage(30),
            "Market_Makers": self._calculate_percentage(10),
            "Marketing_LP": self._calculate_percentage(20),
            "Burnt": self._calculate_percentage(40)
        }
        return distribution

    def _calculate_percentage(self, percentage: float) -> float:
        """
        Calculate the amount of tokens for a given percentage of the total supply.

        :param percentage: The percentage of the total supply to calculate.
        :return: The calculated amount of tokens.
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        return (percentage / 100) * self.total_supply


if __name__ == "__main__":
    try:
        total_supply = float(input("Enter the total supply of Gummy tokens: "))
        gummy_distribution = GummyTokenDistribution(total_supply)
        distribution = gummy_distribution.calculate_distribution()
        print("Gummy Token Distribution:")
        for key, value in distribution.items():
            print(f"{key}: {value:.2f} tokens")
    except ValueError as e:
        print(f"Error: {e}")
```
