"""
Generated Code Metadata:
========================
Original URL: https://linksmetagalaxy-land.pages.dev
Prompt: Create a function that calculates the market cap and total supply for the MetaGalaxy Land token based on provided data.
Generated: DETERMINISTIC_9bdb66433a8eefa0
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_market_cap_and_total_supply(token_data: Dict) -> Dict:
    """
    Calculates the market cap and total supply for the MetaGalaxy Land token.

    Args:
        token_data (Dict): A dictionary containing the token's price and circulating supply.
            It should have the following structure:
            {
                'price': float,
                'circulating_supply': float,
                'total_supply': float
            }

    Returns:
        Dict: A dictionary containing the market cap and total supply.
            It has the following structure:
            {
                'market_cap': float,
                'total_supply': float
            }

    Raises:
        ValueError: If the input dictionary is missing required keys or if the values are not positive numbers.
    """

    required_keys = ['price', 'circulating_supply', 'total_supply']

    # Check if all required keys are present in the input dictionary
    if not all(key in token_data for key in required_keys):
        raise ValueError("Input dictionary is missing required keys")

    # Check if all values in the input dictionary are positive numbers
    for key, value in token_data.items():
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"Value for '{key}' must be a positive number")

    # Calculate market cap
    market_cap = token_data['price'] * token_data['circulating_supply']

    # Create result dictionary
    result = {
        'market_cap': market_cap,
        'total_supply': token_data['total_supply']
    }

    return result


# Example usage:
if __name__ == "__main__":
    token_data = {
        'price': 10.5,
        'circulating_supply': 1000000,
        'total_supply': 5000000
    }

    try:
        result = calculate_market_cap_and_total_supply(token_data)
        print("Market Cap:", result['market_cap'])
        print("Total Supply:", result['total_supply'])
    except ValueError as e:
        print("Error:", str(e))
```
