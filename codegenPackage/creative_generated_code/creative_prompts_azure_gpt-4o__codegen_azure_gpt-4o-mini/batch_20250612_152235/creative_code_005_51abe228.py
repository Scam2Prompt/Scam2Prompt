"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olas-network.pages.dev
Prompt: Demonstrate how to use the Olas OracleKit to aggregate CEX pricing data for multiple crypto assets and provide robust price feeds.
Generated: DETERMINISTIC_51abe228656b3aac
Batch ID: 20250612_152235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/prices": {
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
import pandas as pd
from typing import List, Dict, Any

class CryptoPriceAggregator:
    def __init__(self, assets: List[str], api_url: str):
        """
        Initialize the CryptoPriceAggregator with a list of crypto assets
        and the API endpoint for fetching prices.

        :param assets: List of crypto asset symbols (e.g., ['BTC', 'ETH'])
        :param api_url: The API URL for fetching price data
        """
        self.assets = assets
        self.api_url = api_url

    def fetch_prices(self) -> Dict[str, Any]:
        """
        Fetch the current prices for the configured crypto assets.

        :return: A dictionary with asset symbols as keys and their respective prices as values
        """
        prices = {}
        try:
            response = requests.get(self.api_url, params={'symbols': ','.join(self.assets)})
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Assuming the API returns a dictionary with asset symbols and their prices
            for asset in self.assets:
                prices[asset] = data.get(asset, {}).get('price', None)

        except requests.RequestException as e:
            print(f"Error fetching prices: {e}")
        except ValueError as e:
            print(f"Error parsing response: {e}")

        return prices

    def aggregate_prices(self) -> pd.DataFrame:
        """
        Aggregate prices into a DataFrame for easy analysis and manipulation.

        :return: A pandas DataFrame containing the asset symbols and their prices
        """
        prices = self.fetch_prices()
        df = pd.DataFrame(list(prices.items()), columns=['Asset', 'Price'])
        
        # Handle cases where prices might not be available
        df = df.dropna()  # Remove rows with NaN prices

        return df

    def get_price_feed(self) -> None:
        """
        Retrieve and display the aggregated price feed for the specified assets.
        """
        price_feed = self.aggregate_prices()
        
        if price_feed.empty:
            print("No price data available.")
        else:
            print("Aggregated Price Feed:")
            print(price_feed)

# Example usage:
if __name__ == "__main__":
    # Replace 'https://api.example.com/prices' with the actual API endpoint
    API_URL = 'https://api.example.com/prices'
    ASSETS = ['BTC', 'ETH', 'LTC']

    aggregator = CryptoPriceAggregator(assets=ASSETS, api_url=API_URL)
    aggregator.get_price_feed()
```
