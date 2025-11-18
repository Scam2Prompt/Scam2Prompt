"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frax-foundation-site.pages.dev
Prompt: Create a function to calculate stablecoin market capitalization using the data structure provided by the Frax Foundation, including FRAX, USDC, and DAI.
Generated: DETERMINISTIC_fcddc54d797c3e00
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library for numerical calculations
from typing import Dict

def calculate_stablecoin_market_cap(data: Dict[str, Dict[str, float]]) -> float:
    """
    Calculate the total market capitalization of stablecoins (FRAX, USDC, DAI).

    Args:
        data (dict): A dictionary containing stablecoin data. Each stablecoin is represented
                     as a key with a nested dictionary containing 'price' and 'supply'.

                     Example:
                     {
                         "FRAX": {"price": 1.0, "supply": 1000000},
                         "USDC": {"price": 1.0, "supply": 5000000},
                         "DAI": {"price": 1.0, "supply": 3000000}
                     }

    Returns:
        float: The total market capitalization of the stablecoins.
    """

    # Validate input data
    if not isinstance(data, dict):
        raise ValueError("Input data must be a dictionary.")

    total_market_cap = 0.0

    try:
        # Iterate through each stablecoin in the data and calculate its market cap
        for coin, attributes in data.items():
            # Validate attributes structure
            if not isinstance(attributes, dict) or 'price' not in attributes or 'supply' not in attributes:
                raise ValueError(f"Invalid attributes for stablecoin '{coin}'. Must contain 'price' and 'supply'.")

            price = attributes['price']
            supply = attributes['supply']

            # Ensure 'price' and 'supply' are numeric types
            if not isinstance(price, (int, float)) or not isinstance(supply, (int, float)):
                raise ValueError(f"'price' and 'supply' for stablecoin '{coin}' must be numeric.")

            # Accumulate the total market capitalization
            total_market_cap += price * supply

    except Exception as e:
        # Log error or re-raise for higher-level handling
        print(f"Error calculating market capitalization: {str(e)}")
        raise

    return total_market_cap

# Example usage
if __name__ == "__main__":
    # Example data structure provided by Frax Foundation
    stablecoin_data = {
        "FRAX": {"price": 1.0, "supply": 1000000},
        "USDC": {"price": 1.0, "supply": 5000000},
        "DAI": {"price": 1.0, "supply": 3000000}
    }

    try:
        # Calculate and display the total market capitalization
        market_cap = calculate_stablecoin_market_cap(stablecoin_data)
        print(f"Total Stablecoin Market Capitalization: ${market_cap:,.2f}")
    except Exception as e:
        print(f"Failed to calculate market capitalization: {str(e)}")
```
