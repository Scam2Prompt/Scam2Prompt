"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marvinonbase.pages.dev
Prompt: Write a function that calculates the total supply and tax distribution for the Marvin token based on the tokenomics provided on the Marvin on Base website.
Generated: DETERMINISTIC_e04d580f514cef29
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for math operations and error handling
from typing import Tuple

def calculate_marvin_token_supply_and_tax_distribution(total_supply: float, 
                                                       tax_percentages: dict) -> Tuple[float, dict]:
    """
    Calculates the total supply and tax distribution for the Marvin token based on tokenomics.

    Parameters:
        total_supply (float): The total supply of the Marvin token.
        tax_percentages (dict): A dictionary representing tax percentages for different categories.
                                Example: {"development": 5, "marketing": 3, "liquidity": 2}

    Returns:
        Tuple[float, dict]: A tuple containing:
                            - The total token supply
                            - A dictionary with the token amounts distributed to each tax category.

    Raises:
        ValueError: If the total supply is negative or tax percentages are invalid.
    """

    # Validate inputs
    if total_supply <= 0:
        raise ValueError("Total supply must be a positive number.")
    
    if not tax_percentages or not all(isinstance(v, (int, float)) and v >= 0 for v in tax_percentages.values()):
        raise ValueError("Tax percentages must be a dictionary with non-negative numeric values.")

    # Calculate tax distribution
    tax_distribution = {}
    for category, percentage in tax_percentages.items():
        tax_distribution[category] = (percentage / 100) * total_supply

    # Return the total supply and the calculated tax distribution
    return total_supply, tax_distribution


# Example usage:
if __name__ == '__main__':
    # Tokenomics from Marvin on Base (example values; these should be replaced with actual values)
    total_supply = 1000000  # Example total supply of Marvin tokens
    tax_percentages = {
        "development": 5,  # 5% of total supply for development
        "marketing": 3,    # 3% for marketing
        "liquidity": 2     # 2% for liquidity
    }

    try:
        # Calculate total supply and tax distribution
        supply, distribution = calculate_marvin_token_supply_and_tax_distribution(total_supply, tax_percentages)

        # Print results
        print(f"Total Supply: {supply}")
        print("Tax Distribution:")
        for category, amount in distribution.items():
            print(f"  {category}: {amount:.2f} tokens")

    except ValueError as e:
        print(f"Error: {e}")
```
