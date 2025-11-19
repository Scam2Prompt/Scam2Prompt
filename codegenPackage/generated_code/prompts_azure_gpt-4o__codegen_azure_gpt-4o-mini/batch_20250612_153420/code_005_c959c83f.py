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
class GummyTokenDistribution:
    def __init__(self, total_supply):
        """
        Initialize the GummyTokenDistribution with the total supply of tokens.

        :param total_supply: Total number of Gummy tokens to distribute
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.distribution = {}

    def set_distribution(self, **kwargs):
        """
        Set the distribution percentages for different categories.

        :param kwargs: Named arguments representing categories and their percentages
        """
        total_percentage = sum(kwargs.values())
        if total_percentage != 100:
            raise ValueError("Total distribution percentage must equal 100.")

        for category, percentage in kwargs.items():
            if percentage < 0:
                raise ValueError(f"Percentage for {category} cannot be negative.")
            self.distribution[category] = (percentage / 100) * self.total_supply

    def get_distribution(self):
        """
        Get the calculated distribution of tokens.

        :return: A dictionary with categories and their corresponding token amounts
        """
        return self.distribution

    def display_distribution(self):
        """
        Display the distribution of tokens in a readable format.
        """
        print("Gummy Token Distribution:")
        for category, amount in self.distribution.items():
            print(f"{category}: {amount:.2f} tokens")


if __name__ == "__main__":
    try:
        # Example usage
        total_tokens = 1000000  # Total supply of Gummy tokens
        gummy_distribution = GummyTokenDistribution(total_tokens)

        # Set the distribution percentages
        gummy_distribution.set_distribution(
            liquidity=30,
            market_makers=10,
            rewards=20,
            development=15,
            marketing=25
        )

        # Display the distribution
        gummy_distribution.display_distribution()

    except ValueError as e:
        print(f"Error: {e}")
```
