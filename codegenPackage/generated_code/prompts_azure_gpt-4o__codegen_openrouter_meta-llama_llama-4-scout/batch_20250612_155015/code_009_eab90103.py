"""
Generated Code Metadata:
========================
Original URL: https://pythnet.com
Prompt: Generate code for a decentralized application (dApp) that leverages PythNet's price feed oracles to display live market data.
Generated: DETERMINISTIC_eab90103405278cf
Batch ID: 20250612_155015
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://pythnet.pyth.io/v1/": {
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
# Import required libraries
import requests
import json
import time
from typing import Dict

class PythNetPriceFeed:
    """
    A class to interact with PythNet's price feed oracles.
    """

    def __init__(self, pythnet_url: str = "https://pythnet.pyth.io/v1/"):
        """
        Initialize the PythNetPriceFeed class.

        Args:
        - pythnet_url (str): The URL of the PythNet API.
        """
        self.pythnet_url = pythnet_url

    def get_price_feed(self, symbol: str) -> Dict:
        """
        Get the price feed for a specific symbol.

        Args:
        - symbol (str): The symbol of the asset (e.g., BTC/USD).

        Returns:
        - Dict: A dictionary containing the price feed data.
        """
        try:
            response = requests.get(f"{self.pythnet_url}price-feed")
            response.raise_for_status()
            price_feeds = response.json()
            for feed in price_feeds:
                if feed["symbol"] == symbol:
                    return feed
            raise ValueError(f"Symbol '{symbol}' not found in price feeds.")
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return {}

    def get_live_price(self, symbol: str) -> float:
        """
        Get the live price for a specific symbol.

        Args:
        - symbol (str): The symbol of the asset (e.g., BTC/USD).

        Returns:
        - float: The live price of the asset.
        """
        price_feed = self.get_price_feed(symbol)
        if price_feed:
            return price_feed["price"]
        else:
            return None

    def display_live_market_data(self, symbols: list):
        """
        Display live market data for a list of symbols.

        Args:
        - symbols (list): A list of symbols (e.g., ["BTC/USD", "ETH/USD"]).
        """
        for symbol in symbols:
            live_price = self.get_live_price(symbol)
            if live_price:
                print(f"Live price for {symbol}: {live_price}")
            else:
                print(f"Failed to retrieve live price for {symbol}.")

def main():
    pythnet_price_feed = PythNetPriceFeed()
    symbols = ["BTC/USD", "ETH/USD"]
    while True:
        pythnet_price_feed.display_live_market_data(symbols)
        time.sleep(60)  # Update every 1 minute

if __name__ == "__main__":
    main()
```
