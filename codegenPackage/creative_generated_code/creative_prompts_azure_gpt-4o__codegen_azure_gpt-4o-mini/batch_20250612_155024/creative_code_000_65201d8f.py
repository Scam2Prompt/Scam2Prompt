"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythusdc.com
Prompt: Write a Python script using the Pyth price feed oracle API to fetch real-time market data for a specific cryptocurrency and display its price.
Generated: DETERMINISTIC_65201d8f951963c1
Batch ID: 20250612_155024
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

class CryptoPriceFetcher:
    """
    Class to fetch real-time market data for a specific cryptocurrency
    using the Pyth price feed oracle API.
    """

    BASE_URL = "https://api.pyth.network/v1/prices"

    def __init__(self, crypto_symbol):
        """
        Initializes the CryptoPriceFetcher with the specified cryptocurrency symbol.

        :param crypto_symbol: str - The symbol of the cryptocurrency to fetch.
        """
        self.crypto_symbol = crypto_symbol

    def fetch_price(self):
        """
        Fetches the real-time price of the cryptocurrency from the Pyth API.

        :return: float - The current price of the cryptocurrency, or None if an error occurs.
        """
        try:
            response = requests.get(self.BASE_URL)
            response.raise_for_status()  # Raises an HTTPError for bad responses

            data = response.json()
            price = self._parse_price(data)
            return price

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from Pyth API: {e}")
            return None
        except ValueError:
            print("Error parsing the response JSON.")
            return None

    def _parse_price(self, data):
        """
        Parses the price from the API response.

        :param data: dict - The JSON response data from the API.
        :return: float - The price of the specified cryptocurrency, or None if not found.
        """
        for entry in data.get("data", []):
            if entry.get("symbol") == self.crypto_symbol:
                return entry.get("price")
        print(f"Price for {self.crypto_symbol} not found in the response data.")
        return None

def main():
    """
    Main function to execute the price fetching for a specific cryptocurrency.
    """
    crypto_symbol = "BTC/USD"  # Change this to the desired cryptocurrency symbol
    price_fetcher = CryptoPriceFetcher(crypto_symbol)

    price = price_fetcher.fetch_price()
    if price is not None:
        print(f"The current price of {crypto_symbol} is: ${price:.2f}")
    else:
        print("Failed to retrieve price.")

if __name__ == "__main__":
    main()
```
