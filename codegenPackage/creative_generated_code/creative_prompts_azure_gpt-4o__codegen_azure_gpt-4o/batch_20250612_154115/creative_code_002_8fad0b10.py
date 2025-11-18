"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xyzwthelly.com
Prompt: Provide an example of how to use the Valantis API to query trade volume and total value locked (TVL) statistics for nBTC.
Generated: DETERMINISTIC_8fad0b105ffe88a5
Batch ID: 20250612_154115
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.valantis.io/v1": {
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

# Constants for API endpoint and asset identifier
API_BASE_URL = "https://api.valantis.io/v1"
ASSET_SYMBOL = "nBTC"

def fetch_asset_statistics(asset_symbol):
    """
    Function to fetch trade volume and total value locked (TVL) statistics
    for a given asset symbol using the Valantis API.

    Args:
        asset_symbol (str): The symbol of the asset to query (e.g., "nBTC").

    Returns:
        dict: A dictionary containing trade volume and TVL statistics for the asset.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the API request.
        ValueError: If the API response contains an error or invalid data.
    """
    endpoint = f"{API_BASE_URL}/assets/{asset_symbol}/statistics"
    try:
        # Make the GET request to the Valantis API
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the JSON response
        data = response.json()
        if "trade_volume" not in data or "tvl" not in data:
            raise ValueError("Unexpected response structure: Missing required fields.")
        
        return {
            "trade_volume": data["trade_volume"],
            "tvl": data["tvl"]
        }
    except requests.exceptions.RequestException as req_err:
        # Handle network-related errors
        raise SystemError(f"API request failed: {req_err}")
    except ValueError as val_err:
        # Handle unexpected data or validation issues
        raise ValueError(f"Data validation error: {val_err}")
    except Exception as generic_err:
        # Catch-all for any other errors
        raise RuntimeError(f"An unexpected error occurred: {generic_err}")

if __name__ == "__main__":
    try:
        # Fetch statistics for nBTC (or another asset by changing `ASSET_SYMBOL`)
        asset_statistics = fetch_asset_statistics(ASSET_SYMBOL)
        print(f"Trade Volume for {ASSET_SYMBOL}: {asset_statistics['trade_volume']}")
        print(f"Total Value Locked (TVL) for {ASSET_SYMBOL}: {asset_statistics['tvl']}")
    except Exception as error:
        # Print error details to the console
        print(f"Error: {error}")
```
