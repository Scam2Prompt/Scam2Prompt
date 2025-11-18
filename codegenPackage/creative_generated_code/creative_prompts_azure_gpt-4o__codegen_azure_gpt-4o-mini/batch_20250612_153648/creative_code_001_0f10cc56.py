"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: How can I use Pyth's pull-based oracle model to fetch real-time price data for crypto assets in an Ethereum-based DeFi application?
Generated: DETERMINISTIC_0f10cc56c60af323
Batch ID: 20250612_153648
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://pyth.network/api/v1": {
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
from web3 import Web3

class PriceOracle:
    def __init__(self, oracle_url, web3_provider):
        """
        Initializes the PriceOracle with a URL for the Pyth oracle and a Web3 provider.
        
        :param oracle_url: URL of the Pyth oracle endpoint.
        :param web3_provider: URL of Ethereum node provider (e.g., Infura, Alchemy).
        """
        self.oracle_url = oracle_url
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.check_web3_connection()

    def check_web3_connection(self):
        """Checks if the connection to the Ethereum node is successful."""
        if not self.web3.isConnected():
            raise ConnectionError("Failed to connect to Ethereum node.")

    def fetch_price_data(self, asset_symbol):
        """
        Fetches the latest price data for a given crypto asset using the Pyth oracle.
        
        :param asset_symbol: Symbol of the crypto asset (e.g., 'BTC', 'ETH').
        :return: Latest price data as a dictionary or None if not found.
        """
        try:
            response = requests.get(f"{self.oracle_url}/price/{asset_symbol}")
            response.raise_for_status()  # Raise an error for bad responses
            price_data = response.json()

            # Check if the expected data is present
            if 'price' in price_data:
                return price_data['price']
            else:
                raise ValueError("Price data not found in response.")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching price data: {e}")
            return None
        except ValueError as ve:
            print(ve)
            return None

    def display_price(self, asset_symbol):
        """
        Fetches and displays the price of a specified asset.
        
        :param asset_symbol: Symbol of the crypto asset to fetch price for.
        """
        price = self.fetch_price_data(asset_symbol)
        if price is not None:
            print(f"The latest price for {asset_symbol} is: ${price}")
        else:
            print(f"Could not retrieve price for {asset_symbol}.")

# Example usage
if __name__ == "__main__":
    # Replace with the actual Pyth oracle URL and Ethereum provider
    ORACLE_URL = "https://pyth.network/api/v1"
    WEB3_PROVIDER = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"

    price_oracle = PriceOracle(ORACLE_URL, WEB3_PROVIDER)
    
    # Fetch and display price for Bitcoin
    price_oracle.display_price("BTC")
```

Make sure to replace `"https://pyth.network/api/v1"` and `"https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"` with the actual Pyth oracle URL and your Infura project's URL respectively.
