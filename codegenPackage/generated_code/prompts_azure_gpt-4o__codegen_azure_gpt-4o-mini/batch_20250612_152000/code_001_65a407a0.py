"""
Generated Code Metadata:
========================
Original URL: https://y45y45y54.pages.dev
Prompt: How can I use the Pyth Network's on-demand oracle to fetch real-time price updates for multiple assets in an EVM-compatible blockchain? Provide code examples.
Generated: DETERMINISTIC_65a407a069dfe888
Batch ID: 20250612_152000
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

# Generated Code:
# ===============

```python
import requests
import json
import time

class PythOracle:
    """
    A class to interact with the Pyth Network's on-demand oracle for fetching real-time price updates.
    """

    def __init__(self, base_url):
        """
        Initializes the PythOracle with the base URL for the Pyth Network API.

        :param base_url: The base URL for the Pyth Network API.
        """
        self.base_url = base_url

    def fetch_price(self, asset_id):
        """
        Fetches the real-time price for a given asset.

        :param asset_id: The unique identifier for the asset.
        :return: The price of the asset or None if an error occurs.
        """
        try:
            response = requests.get(f"{self.base_url}/price/{asset_id}")
            response.raise_for_status()  # Raise an error for bad responses
            price_data = response.json()
            return price_data.get('price', None)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price for asset {asset_id}: {e}")
            return None

    def fetch_prices(self, asset_ids):
        """
        Fetches prices for multiple assets.

        :param asset_ids: A list of asset IDs to fetch prices for.
        :return: A dictionary mapping asset IDs to their prices.
        """
        prices = {}
        for asset_id in asset_ids:
            price = self.fetch_price(asset_id)
            if price is not None:
                prices[asset_id] = price
        return prices

def main():
    """
    Main function to demonstrate fetching real-time prices for multiple assets.
    """
    # Base URL for the Pyth Network API
    pyth_base_url = "https://api.pyth.network"  # Replace with the actual Pyth API endpoint
    oracle = PythOracle(pyth_base_url)

    # List of asset IDs to fetch prices for
    asset_ids = [
        "asset_id_1",  # Replace with actual asset IDs
        "asset_id_2",
        "asset_id_3"
    ]

    while True:
        # Fetch prices for the specified assets
        prices = oracle.fetch_prices(asset_ids)
        print("Current Prices:", prices)

        # Wait for a specified interval before fetching prices again
        time.sleep(60)  # Fetch prices every 60 seconds

if __name__ == "__main__":
    main()
```

**Note:** Replace `"https://api.pyth.network"` and the asset IDs in the `asset_ids` list with the actual Pyth Network API endpoint and valid asset IDs.
