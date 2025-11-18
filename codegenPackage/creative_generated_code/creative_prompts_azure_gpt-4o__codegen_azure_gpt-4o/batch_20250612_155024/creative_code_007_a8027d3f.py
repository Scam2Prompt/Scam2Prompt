"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythpro.com
Prompt: Create a script to validate the accuracy of market data retrieved from Pyth price feed oracles.
Generated: DETERMINISTIC_a8027d3f6fe4987b
Batch ID: 20250612_155024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://pyth.network/api/v2/prices": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from typing import Dict, Any

# Constants
PYTH_ORACLE_API_URL = "https://pyth.network/api/v2/prices"  # Replace with actual API endpoint
EXPECTED_SYMBOLS = {"BTC/USD", "ETH/USD", "SOL/USD"}  # Add symbols you expect to validate
PRICE_TOLERANCE = 0.01  # Acceptable price deviation (1%)

# Custom exception for data validation errors
class MarketDataValidationError(Exception):
    pass

def fetch_price_data() -> Dict[str, Any]:
    """
    Fetch price data from the Pyth price feed API.

    Returns:
        Dictionary containing the price data.
    Raises:
        requests.exceptions.RequestException: if the request fails.
    """
    try:
        response = requests.get(PYTH_ORACLE_API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching price data from Pyth API: {e}")

def validate_price_data(data: Dict[str, Any]) -> None:
    """
    Validate the accuracy of market data retrieved from Pyth price feed.

    Args:
        data: Dictionary containing the price data.

    Raises:
        MarketDataValidationError: If validation fails for any symbol.
    """
    for symbol in EXPECTED_SYMBOLS:
        if symbol not in data:
            raise MarketDataValidationError(f"Symbol {symbol} not found in price feed data.")

        symbol_data = data[symbol]
        price = symbol_data.get("price", None)
        confidence_interval = symbol_data.get("confidence_interval", None)

        if price is None or confidence_interval is None:
            raise MarketDataValidationError(
                f"Missing price or confidence interval for symbol {symbol}."
            )

        # Check if the price is within the acceptable tolerance
        lower_bound = price * (1 - PRICE_TOLERANCE)
        upper_bound = price * (1 + PRICE_TOLERANCE)

        if not (lower_bound <= confidence_interval[0] <= upper_bound):
            raise MarketDataValidationError(
                f"Price deviation too large for symbol {symbol}: "
                f"price={price}, confidence_interval={confidence_interval}"
            )

def main():
    """
    Main function to validate market data.
    """
    print("Starting market data validation...")

    try:
        # Step 1: Fetch data from Pyth oracle API
        price_data = fetch_price_data()

        # Step 2: Validate the fetched data
        validate_price_data(price_data)

        print("Market data validation successful!")
    except MarketDataValidationError as e:
        print(f"Market data validation failed: {e}")
    except RuntimeError as e:
        print(f"Runtime error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
