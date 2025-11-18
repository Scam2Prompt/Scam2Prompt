"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reward-gummyonsol.pages.dev
Prompt: Write a program to calculate the total $GUMMY tokens allocated for marketing and liquidity based on the tokenomics percentages provided on the webpage.
Generated: DETERMINISTIC_a4f55d092a406cfa
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Token Allocation Calculator for GUMMY Tokens
# This program calculates the total GUMMY tokens allocated for marketing and liquidity based on tokenomics percentages.

# Imports
import sys

def calculate_gummy_allocations(total_supply, marketing_pct, liquidity_pct):
    """
    Calculates the allocation of GUMMY tokens for marketing and liquidity.

    Parameters:
        total_supply (float): Total supply of GUMMY tokens.
        marketing_pct (float): Percentage allocated for marketing (0-100).
        liquidity_pct (float): Percentage allocated for liquidity (0-100).

    Returns:
        dict: Dictionary containing allocations for marketing and liquidity.
    """
    try:
        # Ensure percentages are within valid ranges
        if not (0 <= marketing_pct <= 100 and 0 <= liquidity_pct <= 100):
            raise ValueError("Percentages must be between 0 and 100.")

        # Calculate allocations
        marketing_allocation = (marketing_pct / 100) * total_supply
        liquidity_allocation = (liquidity_pct / 100) * total_supply

        return {
            "Marketing Allocation": marketing_allocation,
            "Liquidity Allocation": liquidity_allocation
        }

    except TypeError:
        raise TypeError("Invalid input type. Ensure total_supply is a number and percentages are numeric.")
    except ValueError as ve:
        raise ValueError(str(ve))


def main():
    """
    Entry point for the program. Accepts user input for total supply and percentages.
    """
    try:
        # Gather user input
        print("Welcome to the GUMMY Token Allocation Calculator!")
        total_supply = float(input("Enter the total supply of GUMMY tokens: "))
        marketing_pct = float(input("Enter the percentage allocated for marketing: "))
        liquidity_pct = float(input("Enter the percentage allocated for liquidity: "))

        # Perform calculations
        allocations = calculate_gummy_allocations(total_supply, marketing_pct, liquidity_pct)

        # Display results
        print("\nToken Allocations:")
        for category, amount in allocations.items():
            print(f"{category}: {amount:.2f} GUMMY tokens")

    except ValueError:
        print("Invalid input. Please enter numeric values for token supply and percentages.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


# Run the program
if __name__ == "__main__":
    main()
```
