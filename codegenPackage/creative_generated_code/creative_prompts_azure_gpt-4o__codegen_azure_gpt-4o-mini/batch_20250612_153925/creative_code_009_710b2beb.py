"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oksd7.cn
Prompt: Write code to query and display real-time cryptocurrency prices for BTC, ETH, and USDT using the OKX API, as described in the 欧易数字货币计算器 section.
Generated: DETERMINISTIC_710b2beb32a18ed4
Batch ID: 20250612_153925
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.okx.com/api/v5/market/ticker": {
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

class CryptoPriceFetcher:
    """A class to fetch real-time cryptocurrency prices from the OKX API."""

    BASE_URL = "https://www.okx.com/api/v5/market/ticker"

    def __init__(self, symbols):
        """
        Initializes the CryptoPriceFetcher with a list of cryptocurrency symbols.

        Args:
            symbols (list): A list of cryptocurrency symbols to fetch prices for.
        """
        self.symbols = symbols

    def fetch_prices(self):
        """
        Fetches real-time prices for the specified cryptocurrencies.

        Returns:
            dict: A dictionary containing the symbol and its corresponding price.
        """
        try:
            # Construct the request URL with the symbols
            response = requests.get(self.BASE_URL, params={"instId": ','.join(self.symbols)})
            response.raise_for_status()  # Raise an error for HTTP requests that return an error status
            data = response.json()

            # Check if the response is successful
            if data.get("code") != "0":
                raise ValueError(f"Error fetching data: {data.get('msg')}")

            # Extract prices from the response
            prices = {item['instId']: item['last'] for item in data.get('data', [])}
            return prices

        except requests.exceptions.RequestException as e:
            print(f"HTTP Request failed: {e}")
            return {}
        except ValueError as ve:
            print(ve)
            return {}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {}

    def display_prices(self):
        """Fetch and display the cryptocurrency prices."""
        prices = self.fetch_prices()
        if prices:
            for symbol, price in prices.items():
                print(f"The current price of {symbol} is: {price}")
        else:
            print("No prices available to display.")

if __name__ == "__main__":
    # Specify the cryptocurrency symbols to fetch prices for
    symbols_to_fetch = ["BTC-USDT", "ETH-USDT", "USDT-USDC"]
    
    # Create an instance of CryptoPriceFetcher
    price_fetcher = CryptoPriceFetcher(symbols_to_fetch)
    
    # Display the prices
    price_fetcher.display_prices()
```
