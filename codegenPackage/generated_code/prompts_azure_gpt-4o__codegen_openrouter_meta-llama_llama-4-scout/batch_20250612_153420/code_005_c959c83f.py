"""
Generated Code Metadata:
========================
Original URL: https://earn-gummyonsol.pages.dev
Prompt: Write a program to calculate the distribution of $Gummy tokens based on the tokenomics percentages provided (e.g., 30% liquidity, 10% market makers, etc.).
Generated: DETERMINISTIC_c959c83fef3cc4d1
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# token_distribution.py

class TokenDistributionCalculator:
    def __init__(self, total_tokens):
        """
        Initializes the TokenDistributionCalculator with the total number of tokens.

        Args:
            total_tokens (int): The total number of Gummy tokens.
        """
        self.total_tokens = total_tokens
        self.distribution = {}

    def add_distribution(self, category, percentage):
        """
        Adds a distribution category with its corresponding percentage.

        Args:
            category (str): The category name (e.g., "liquidity", "market makers").
            percentage (float): The percentage of tokens for the category.

        Raises:
            ValueError: If the percentage is not between 0 and 100.
        """
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100")

        self.distribution[category] = percentage

    def calculate_distribution(self):
        """
        Calculates the number of tokens for each distribution category.

        Returns:
            dict: A dictionary with categories as keys and token counts as values.

        Raises:
            ValueError: If the total percentage does not add up to 100.
        """
        total_percentage = sum(self.distribution.values())
        if not (abs(total_percentage - 100) < 1e-6):  # Allow for floating-point errors
            raise ValueError("Total percentage must add up to 100")

        token_distribution = {}
        for category, percentage in self.distribution.items():
            token_distribution[category] = int(self.total_tokens * (percentage / 100))

        # Adjust for any rounding errors
        remaining_tokens = self.total_tokens - sum(token_distribution.values())
        if remaining_tokens > 0:
            # Add the remaining tokens to the first category
            categories = list(token_distribution.keys())
            token_distribution[categories[0]] += remaining_tokens

        return token_distribution


def main():
    try:
        total_tokens = 1000000  # Example total tokens
        calculator = TokenDistributionCalculator(total_tokens)

        # Example distribution percentages
        distribution_percentages = {
            "liquidity": 30,
            "market makers": 10,
            "team": 20,
            "community": 40
        }

        for category, percentage in distribution_percentages.items():
            calculator.add_distribution(category, percentage)

        token_distribution = calculator.calculate_distribution()

        print("Token Distribution:")
        for category, tokens in token_distribution.items():
            print(f"{category.capitalize()}: {tokens} tokens")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
