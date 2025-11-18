"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-dogeverse.pages.dev
Prompt: Create a Python script to calculate the token allocation percentages for $DOGEVERSE based on the provided tokenomics.
Generated: DETERMINISTIC_0f3025ad01b8b658
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3
"""
Token Allocation Percentage Calculator for $DOGEVERSE
This script calculates the allocation percentages of different token categories based on provided tokenomics.
"""

class Tokenomics:
    def __init__(self, total_supply: float):
        """
        Initialize the Tokenomics class with the total supply of tokens.

        :param total_supply: The total supply of $DOGEVERSE tokens
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.allocations = {}

    def add_allocation(self, category: str, amount: float):
        """
        Add a token allocation category with its corresponding amount.

        :param category: The name of the allocation category
        :param amount: The amount allocated to that category
        """
        if amount < 0:
            raise ValueError(f"Allocation amount for '{category}' must be non-negative.")
        self.allocations[category] = amount

    def calculate_percentages(self):
        """
        Calculate the allocation percentages for each category.

        :return: A dictionary with categories as keys and their allocation percentages as values
        """
        percentages = {}
        for category, amount in self.allocations.items():
            percentages[category] = (amount / self.total_supply) * 100
        return percentages

def main():
    """
    Main function to execute the token allocation percentage calculation.
    """
    try:
        # Define total supply of $DOGEVERSE tokens
        total_supply = 1_000_000_000  # Example total supply

        # Create an instance of Tokenomics
        tokenomics = Tokenomics(total_supply)

        # Add various allocations
        tokenomics.add_allocation('Liquidity', 200_000_000)
        tokenomics.add_allocation('Marketing', 150_000_000)
        tokenomics.add_allocation('Development', 250_000_000)
        tokenomics.add_allocation('Community', 100_000_000)
        tokenomics.add_allocation('Reserve', 300_000_000)

        # Calculate and display percentages
        percentages = tokenomics.calculate_percentages()
        for category, percentage in percentages.items():
            print(f"{category}: {percentage:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
