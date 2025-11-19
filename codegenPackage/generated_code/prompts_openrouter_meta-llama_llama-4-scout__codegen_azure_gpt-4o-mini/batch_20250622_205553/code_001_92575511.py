"""
Generated Code Metadata:
========================
Original URL: https://wenwen.pages.dev
Prompt: Generate a code snippet for a simple cryptocurrency tokenomics calculator inspired by the Wen token.
Generated: DETERMINISTIC_92575511af2ab5ff
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenomicsCalculator:
    """
    A simple calculator for cryptocurrency tokenomics inspired by the Wen token.
    This class calculates the distribution of tokens based on predefined parameters.
    """

    def __init__(self, total_supply: float):
        """
        Initializes the TokenomicsCalculator with the total supply of tokens.

        :param total_supply: Total number of tokens available for distribution.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply

    def calculate_distribution(self, allocations: dict) -> dict:
        """
        Calculates the distribution of tokens based on the provided allocations.

        :param allocations: A dictionary where keys are allocation names and values are percentages.
        :return: A dictionary with the number of tokens allocated to each category.
        """
        if not isinstance(allocations, dict):
            raise TypeError("Allocations must be a dictionary.")

        distribution = {}
        total_percentage = 0

        for category, percentage in allocations.items():
            if not isinstance(percentage, (int, float)):
                raise TypeError(f"Percentage for {category} must be a number.")
            if percentage < 0:
                raise ValueError(f"Percentage for {category} cannot be negative.")
            total_percentage += percentage

            # Calculate the number of tokens for this category
            tokens = (percentage / 100) * self.total_supply
            distribution[category] = tokens

        if total_percentage != 100:
            raise ValueError("Total percentage of allocations must equal 100.")

        return distribution


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with a total supply of 1,000,000 tokens
        calculator = TokenomicsCalculator(total_supply=1_000_000)

        # Define the allocations for different categories
        allocations = {
            "Development": 20,
            "Marketing": 30,
            "Liquidity": 25,
            "Community": 15,
            "Reserve": 10
        }

        # Calculate the distribution
        distribution = calculator.calculate_distribution(allocations)

        # Print the results
        print("Token Distribution:")
        for category, tokens in distribution.items():
            print(f"{category}: {tokens:.2f} tokens")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
