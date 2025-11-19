"""
Generated Code Metadata:
========================
Original URL: https://doge2014sale.pages.dev
Prompt: Generate a code snippet for calculating the total supply and allocation percentages for Doge2014 tokens based on the provided tokenomics.
Generated: DETERMINISTIC_fde70b67acde8c79
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Doge2014 Tokenomics Calculation Script
# This script calculates the total supply and allocation percentages for Doge2014 tokens.

# Import necessary modules
import sys

def calculate_tokenomics(tokenomics):
    """
    Calculate the total supply and allocation percentages based on tokenomics.

    Args:
        tokenomics (dict): A dictionary containing allocation categories and their respective token amounts.

    Returns:
        dict: A dictionary containing allocation percentages for each category.
    """
    try:
        # Calculate total supply
        total_supply = sum(tokenomics.values())
        
        # Validate total supply
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        
        # Calculate allocation percentages
        allocation_percentages = {
            category: (amount / total_supply) * 100
            for category, amount in tokenomics.items()
        }
        
        return total_supply, allocation_percentages
    except Exception as e:
        print(f"Error calculating tokenomics: {e}", file=sys.stderr)
        return None, None

def main():
    """
    Main function to execute the tokenomics calculation.
    """
    # Define tokenomics (example data)
    tokenomics = {
        "Development": 500000,
        "Marketing": 300000,
        "Community Rewards": 200000,
        "Liquidity Pool": 100000,
    }

    # Calculate total supply and allocation percentages
    total_supply, allocation_percentages = calculate_tokenomics(tokenomics)

    # Check if calculation was successful
    if total_supply is not None and allocation_percentages is not None:
        print(f"Total Supply: {total_supply} Doge2014 tokens")
        print("Allocation Percentages:")
        for category, percentage in allocation_percentages.items():
            print(f"  {category}: {percentage:.2f}%")
    else:
        print("Failed to calculate tokenomics.")

if __name__ == "__main__":
    main()
```
