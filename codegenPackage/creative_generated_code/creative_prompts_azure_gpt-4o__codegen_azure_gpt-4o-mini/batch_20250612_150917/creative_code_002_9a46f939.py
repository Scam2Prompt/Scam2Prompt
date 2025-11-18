"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcdaily.info
Prompt: Create a program that fetches real-time Ethereum price data and compares it against key resistance levels ($3,800, $4,500, and $5,000) mentioned in the 2025 bull market analysis.
Generated: DETERMINISTIC_9a46f939a07bf279
Batch ID: 20250612_150917
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
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

class EthereumPriceFetcher:
    def __init__(self, api_url="https://api.coingecko.com/api/v3/simple/price"):
        """
        Initialize the EthereumPriceFetcher with the API URL.
        
        :param api_url: The API URL to fetch Ethereum prices from.
        """
        self.api_url = api_url
        self.resistance_levels = [3800, 4500, 5000]

    def fetch_current_price(self):
        """
        Fetch the current Ethereum price in USD.

        :return: Current price of Ethereum in USD or None if an error occurs.
        """
        try:
            response = requests.get(self.api_url, params={"ids": "ethereum", "vs_currencies": "usd"})
            response.raise_for_status()  # Raise an error for bad HTTP status codes
            data = response.json()
            return data['ethereum']['usd']
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Ethereum price: {e}")
            return None
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Error processing response: {e}")
            return None

    def compare_price_with_resistances(self, current_price):
        """
        Compare the current Ethereum price with defined resistance levels.

        :param current_price: The current price of Ethereum in USD.
        :return: A list of resistance levels that are below the current price.
        """
        if current_price is None:
            return []

        # Determine which resistance levels are below the current price
        below_resistances = [level for level in self.resistance_levels if current_price > level]
        return below_resistances

    def run(self):
        """
        Execute the fetching and comparison of the Ethereum price.
        """
        current_price = self.fetch_current_price()
        if current_price is not None:
            print(f"Current Ethereum Price: ${current_price:.2f}")
            below_resistances = self.compare_price_with_resistances(current_price)
            if below_resistances:
                print("Resistance levels below the current price:", below_resistances)
            else:
                print("No resistance levels below the current price.")
        else:
            print("Failed to retrieve the current Ethereum price.")

if __name__ == "__main__":
    eth_price_fetcher = EthereumPriceFetcher()
    eth_price_fetcher.run()
```
