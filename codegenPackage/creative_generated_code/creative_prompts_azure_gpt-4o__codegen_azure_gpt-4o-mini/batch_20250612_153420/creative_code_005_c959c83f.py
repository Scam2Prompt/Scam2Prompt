"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earn-gummyonsol.pages.dev
Prompt: Write a program to calculate the distribution of $Gummy tokens based on the tokenomics percentages provided (e.g., 30% liquidity, 10% market makers, etc.).
Generated: DETERMINISTIC_c959c83fef3cc4d1
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GummyTokenDistribution:
    def __init__(self, total_supply: float, distribution_percentages: dict):
        """
        Initializes the GummyTokenDistribution with a total supply and distribution percentages.

        :param total_supply: The total number of Gummy tokens to be distributed.
        :param distribution_percentages: A dictionary containing distribution categories and their percentages.
        """
        self.total_supply = total_supply
        self.distribution_percentages = distribution_percentages
        self.validate_distribution()

    def validate_distribution(self):
        """
        Validates that the total distribution percentages sum to 100%.
        Raises a ValueError if the validation fails.
        """
        total_percentage = sum(self.distribution_percentages.values())
        if total_percentage != 100:
            raise ValueError("The distribution percentages must sum to 100%. Current sum: {}".format(total_percentage))

    def calculate_distribution(self) -> dict:
        """
        Calculates the number of tokens for each distribution category based on the input percentages.

        :return: A dictionary with the distribution of tokens.
        """
        distribution = {}
        for category, percentage in self.distribution_percentages.items():
            tokens = (percentage / 100) * self.total_supply
            distribution[category] = tokens
        return distribution


def main():
    # Example usage
    total_supply = 1000000  # Total Gummy tokens
    distribution_percentages = {
        'liquidity': 30,
        'market makers': 10,
        'development': 20,
        'marketing': 15,
        'community rewards': 25
    }

    try:
        gummy_distribution = GummyTokenDistribution(total_supply, distribution_percentages)
        distribution_result = gummy_distribution.calculate_distribution()
        print("Gummy Token Distribution:")
        for category, tokens in distribution_result.items():
            print(f"{category}: {tokens:.2f} tokens")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
