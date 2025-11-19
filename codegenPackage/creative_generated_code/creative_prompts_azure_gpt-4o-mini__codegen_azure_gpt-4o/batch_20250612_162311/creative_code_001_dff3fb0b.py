"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythcloud.com
Prompt: Write a code snippet to fetch market data from Pyth Cloud's price feed oracles for a blockchain application.
Generated: DETERMINISTIC_dff3fb0b146596bd
Batch ID: 20250612_162311
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://pyth-api.example.com": {
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

def fetch_pyth_market_data(api_url: str, market: str):
    """
    Fetch market data from Pyth Cloud's price feed oracles.

    Args:
        api_url (str): The base URL of the Pyth Cloud API.
        market (str): The market symbol to fetch data for (e.g., "BTC/USD").

    Returns:
        dict: The market data retrieved from the API.

    Raises:
        Exception: If the API request fails or the response is invalid.
    """
    try:
        # Construct the complete API endpoint
        endpoint = f"{api_url}/price_feed/{market}"

        # Send a GET request to the API
        response = requests.get(endpoint)

        # Raise an error if the request was not successful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Validate the structure of the response
        if 'price' not in data or 'timestamp' not in data:
            raise ValueError("Invalid response structure from Pyth API")

        return data

    except requests.exceptions.RequestException as e:
        # Handle any HTTP-related errors
        raise Exception(f"Error fetching data from Pyth API: {str(e)}")

    except ValueError as ve:
        # Handle data validation errors
        raise Exception(f"Data validation error: {str(ve)}")

# Example usage
if __name__ == "__main__":
    # Define the Pyth Cloud API URL (replace with actual API URL in production)
    PYTH_API_URL = "https://pyth-api.example.com"
    MARKET = "BTC/USD"

    try:
        # Fetch market data
        market_data = fetch_pyth_market_data(PYTH_API_URL, MARKET)
        print("Market Data:", market_data)
    except Exception as err:
        print(f"Failed to fetch market data: {err}")
```
