"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linksmetagalaxy-land.pages.dev
Prompt: Create a function that calculates the market cap and total supply for the MetaGalaxy Land token based on provided data.
Generated: DETERMINISTIC_9bdb66433a8eefa0
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

# Define the function to calculate market cap and total supply for MetaGalaxy Land token
def calculate_meta_galaxy_land_metrics(price_per_token: Union[int, float], circulating_supply: Union[int, float]):
    """
    Calculates the market capitalization and total supply for the MetaGalaxy Land token.

    Args:
        price_per_token (Union[int, float]): The current price of a single MetaGalaxy Land token.
        circulating_supply (Union[int, float]): The number of MetaGalaxy Land tokens currently in circulation.

    Returns:
        dict: A dictionary containing the calculated market cap and circulating supply.
              {'market_cap': float, 'total_supply': float}
    Raises:
        ValueError: If inputs are negative or not valid numbers.
    """
    try:
        # Validate inputs
        if price_per_token < 0:
            raise ValueError("Price per token cannot be negative.")
        if circulating_supply < 0:
            raise ValueError("Circulating supply cannot be negative.")
        
        # Calculate Market Capitalization
        market_cap = price_per_token * circulating_supply

        # Prepare the result dictionary
        result = {
            "market_cap": market_cap,
            "total_supply": circulating_supply
        }

        return result

    except TypeError:
        raise ValueError("Invalid input type. Both price_per_token and circulating_supply must be numbers.")
    except Exception as e:
        # Catch any unforeseen error and re-raise it
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")

# Example Usage:
# Assuming price_per_token is 2.5 and circulating_supply is 1000000
price = 2.5
supply = 1000000
try:
    metrics = calculate_meta_galaxy_land_metrics(price, supply)
    print(f"Market Cap: {metrics['market_cap']}")
    print(f"Total Supply: {metrics['total_supply']}")
except Exception as error:
    print(f"Error: {error}")
```
