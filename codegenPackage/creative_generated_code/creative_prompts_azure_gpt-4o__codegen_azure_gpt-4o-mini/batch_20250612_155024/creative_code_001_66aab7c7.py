"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythgame.com
Prompt: Recommend libraries or APIs for accessing Pyth Network's market data and demonstrate how to use them in a blockchain application.
Generated: DETERMINISTIC_66aab7c72e9d3960
Batch ID: 20250612_155024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pyth.network": {
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

class PythNetworkAPI:
    """
    A class to interact with the Pyth Network API for accessing market data.
    """

    BASE_URL = "https://api.pyth.network"  # Base URL for the Pyth Network API

    def fetch_market_data(self, asset_symbol):
        """
        Fetch market data for a given asset symbol.

        Parameters:
        asset_symbol (str): The symbol of the asset to fetch market data for.

        Returns:
        dict: Parsed JSON data containing market information.

        Raises:
        ValueError: If the asset_symbol is empty.
        requests.exceptions.RequestException: For handling any request errors.
        """
        if not asset_symbol:
            raise ValueError("Asset symbol must not be empty")

        endpoint = f"{self.BASE_URL}/prices/{asset_symbol}"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Return parsed JSON data
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching market data: {e}")
            return None

def main():
    """
    Main function to demonstrate fetching market data from Pyth Network.
    """
    pyth_api = PythNetworkAPI()
    
    # Example asset symbol to fetch data for
    asset_symbol = "BTC/USD"
    
    # Fetch market data
    market_data = pyth_api.fetch_market_data(asset_symbol)

    # Output the fetched market data
    if market_data:
        print(json.dumps(market_data, indent=4))  # Pretty-print JSON response

if __name__ == "__main__":
    main()
```
