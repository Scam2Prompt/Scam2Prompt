"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythop.com
Prompt: Write code to enable a blockchain-based application to fetch and validate market data using Pythop's price feed oracle service.
Generated: DETERMINISTIC_ed208f404c0753f9
Batch ID: 20250612_155015
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pyth.network/v1": {
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

class PythNetworkError(Exception):
    """Custom exception for Pyth network errors."""
    pass

class MarketDataFetcher:
    BASE_URL = "https://api.pyth.network/v1"

    def __init__(self):
        """Initialize the MarketDataFetcher with default values."""
        self.prices = {}

    def fetch_market_data(self, asset_symbol: str):
        """
        Fetch market data for the given asset symbol using Pyth's price feed.

        Args:
            asset_symbol (str): The symbol of the asset to fetch data for.

        Raises:
            PythNetworkError: If there is an issue connecting to the Pyth API or fetching data.

        Returns:
            dict: The market data for the requested asset.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/prices/{asset_symbol}")

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()

            # Validate the response data
            if 'price' not in data:
                raise PythNetworkError(f"Invalid data format for asset {asset_symbol}.")

            self.prices[asset_symbol] = data['price']
            return data

        except requests.RequestException as e:
            raise PythNetworkError(f"Error fetching market data: {e}")

    def validate_market_data(self, asset_symbol: str) -> bool:
        """
        Validate the fetched market data for a given asset symbol.

        Args:
            asset_symbol (str): The symbol of the asset to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        if asset_symbol in self.prices:
            price = self.prices[asset_symbol]
            # Basic validation check for price
            if isinstance(price, (int, float)) and price > 0:
                return True
        return False

if __name__ == "__main__":
    # Example usage of the MarketDataFetcher class
    fetcher = MarketDataFetcher()
    asset = "BTC/USD"  # Example asset symbol

    try:
        data = fetcher.fetch_market_data(asset)
        print(f"Fetched market data for {asset}: {data}")

        if fetcher.validate_market_data(asset):
            print(f"Market data for {asset} is valid.")
        else:
            print(f"Market data for {asset} is invalid.")
            
    except PythNetworkError as e:
        print(f"Failed to fetch or validate market data: {e}")
```
