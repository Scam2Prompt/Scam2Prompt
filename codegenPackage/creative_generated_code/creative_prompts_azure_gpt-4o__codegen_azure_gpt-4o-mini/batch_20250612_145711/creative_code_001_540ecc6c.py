"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fudthepug.pages.dev
Prompt: Generate code to calculate the token distribution percentages for Simon’s Cat Token based on the provided tokenomics, ensuring the values sum to 100%.
Generated: DETERMINISTIC_540ecc6cab32ccab
Batch ID: 20250612_145711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    def __init__(self, token_data):
        """
        Initialize the Tokenomics class with the provided token distribution data.

        :param token_data: A dictionary containing the token distribution categories and their respective amounts.
        """
        self.token_data = token_data
        self.total_supply = sum(token_data.values())
        
        if self.total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")

    def calculate_distribution_percentages(self):
        """
        Calculate the distribution percentages for each category in the token data.

        :return: A dictionary containing categories and their corresponding percentage of total supply.
        """
        distribution_percentages = {}
        
        for category, amount in self.token_data.items():
            if amount < 0:
                raise ValueError(f"Amount for category '{category}' cannot be negative.")
            percentage = (amount / self.total_supply) * 100
            distribution_percentages[category] = round(percentage, 2)

        # Validate that the percentages sum to 100%
        total_percentage = sum(distribution_percentages.values())
        if total_percentage != 100:
            raise ValueError(f"Distribution percentages do not sum up to 100%. Current total: {total_percentage}")

        return distribution_percentages


def main():
    """
    Main function to execute the token distribution calculation.
    """
    # Example token distribution data for Simon’s Cat Token
    token_data = {
        "Development": 30000000,
        "Marketing": 20000000,
        "Liquidity": 15000000,
        "Ecosystem": 25000000,
        "Team": 10000000,
        "Reserve": 20000000
    }

    try:
        tokenomics = Tokenomics(token_data)
        distribution_percentages = tokenomics.calculate_distribution_percentages()
        print("Token Distribution Percentages:")
        for category, percentage in distribution_percentages.items():
            print(f"{category}: {percentage}%")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
