"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythcall.com
Prompt: Write a script to validate and process price data from Pyth Network's oracles for use in a decentralized finance application.
Generated: DETERMINISTIC_72c205216b1cf3b3
Batch ID: 20250612_155024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://pyth.network/api/latest_price_feed": {
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
import json

# Constants
PYTH_API_URL = "https://pyth.network/api/latest_price_feed"  # Replace with the actual API endpoint
MAX_RETRIES = 3  # Maximum number of retry attempts for API calls
SUPPORTED_SYMBOLS = {"BTC/USD", "ETH/USD", "SOL/USD"}  # List of symbols we want to process
PRICE_TOLERANCE_THRESHOLD = 0.01  # Maximum percentage difference allowed for price changes

class PriceValidationError(Exception):
    """Custom exception for invalid price data."""
    pass

def fetch_price_data():
    """
    Fetches price data from the Pyth Network API.
    Returns:
        dict: Parsed JSON response containing price feed data.
    Raises:
        Exception: If the request fails or the API returns an invalid response.
    """
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(PYTH_API_URL, timeout=10)
            response.raise_for_status()
            return response.json()  # Assumes response is in JSON format
        except requests.exceptions.RequestException as e:
            print(f"API request failed on attempt {attempt + 1}: {e}")
            if attempt == MAX_RETRIES - 1:
                raise Exception("Failed to fetch price data after multiple attempts.")
    raise Exception("Unexpected error during API call.")

def validate_price_data(price_data):
    """
    Validates the price data fetched from the Pyth Network API.
    Args:
        price_data (dict): Raw price data from Pyth Network.
    Returns:
        dict: Validated and filtered price data.
    Raises:
        PriceValidationError: If any price feed is invalid.
    """
    validated_data = {}

    for feed in price_data.get("feeds", []):
        symbol = feed.get("symbol")
        price = feed.get("price")
        confidence = feed.get("confidence_interval")

        # Ensure the symbol is supported
        if symbol not in SUPPORTED_SYMBOLS:
            continue

        # Validate that price and confidence interval exist and are numeric
        if price is None or confidence is None:
            raise PriceValidationError(f"Missing price or confidence interval for symbol: {symbol}")
        if not isinstance(price, (int, float)) or not isinstance(confidence, (int, float)):
            raise PriceValidationError(f"Invalid price or confidence interval for symbol: {symbol}")

        # Ensure confidence interval is within a reasonable range
        if confidence > price * PRICE_TOLERANCE_THRESHOLD:
            raise PriceValidationError(f"Confidence interval too high for symbol: {symbol}")

        # Add validated data to the dictionary
        validated_data[symbol] = {
            "price": price,
            "confidence_interval": confidence,
        }

    return validated_data

def process_price_data(validated_data):
    """
    Processes the validated price data for use in a DeFi application.
    Args:
        validated_data (dict): Price data that has passed validation checks.
    Returns:
        dict: Processed data ready for use in the application.
    """
    processed_data = {}

    for symbol, data in validated_data.items():
        price = data["price"]
        confidence = data["confidence_interval"]

        # Example processing: Calculate price range based on confidence interval
        lower_bound = price - confidence
        upper_bound = price + confidence

        processed_data[symbol] = {
            "price": price,
            "confidence_interval": confidence,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
        }

    return processed_data

def main():
    """
    Main entry point for the script.
    Fetches, validates, and processes price data from the Pyth Network API.
    """
    try:
        # Step 1: Fetch price data from the Pyth API
        raw_price_data = fetch_price_data()

        # Step 2: Validate the fetched price data
        validated_price_data = validate_price_data(raw_price_data)

        # Step 3: Process the validated price data
        processed_price_data = process_price_data(validated_price_data)

        # Output the processed data (for demonstration purposes)
        print(json.dumps(processed_price_data, indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
