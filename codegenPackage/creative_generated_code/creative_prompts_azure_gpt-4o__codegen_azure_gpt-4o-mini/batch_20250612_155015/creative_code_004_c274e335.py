"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythnet.com
Prompt: Create a Python script that connects to PythNet's price feed oracle and retrieves the latest price of a specified asset.
Generated: DETERMINISTIC_c274e335ff0b40ef
Batch ID: 20250612_155015
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pyth.network/v1/prices": {
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

class PythNetPriceFeed:
    """A class to interact with PythNet's price feed oracle."""

    BASE_URL = "https://api.pyth.network/v1/prices"

    def __init__(self, asset_symbol):
        """
        Initializes the PythNetPriceFeed with a specified asset symbol.

        :param asset_symbol: The symbol of the asset to retrieve the price for.
        """
        self.asset_symbol = asset_symbol

    def fetch_latest_price(self):
        """
        Fetches the latest price for the specified asset.

        :return: The latest price as a float.
        :raises ValueError: If the asset is not found or price data is unavailable.
        :raises ConnectionError: If there is an issue connecting to the PythNet API.
        """
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Raise an error for bad responses

            data = response.json()
            asset_prices = data.get("data", [])
            
            # Iterate through asset prices to find the specified asset
            for asset in asset_prices:
                if asset.get("symbol") == self.asset_symbol:
                    return float(asset.get("price"))

            raise ValueError(f"Price data for asset '{self.asset_symbol}' not found.")

        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to connect to PythNet API: {e}")

if __name__ == "__main__":
    # Example usage
    asset = "ETH/USD"  # Specify the asset symbol
    pyth_net = PythNetPriceFeed(asset)

    try:
        latest_price = pyth_net.fetch_latest_price()
        print(f"The latest price of {asset} is: ${latest_price:.2f}")
    except (ValueError, ConnectionError) as e:
        print(f"Error: {e}")
```
