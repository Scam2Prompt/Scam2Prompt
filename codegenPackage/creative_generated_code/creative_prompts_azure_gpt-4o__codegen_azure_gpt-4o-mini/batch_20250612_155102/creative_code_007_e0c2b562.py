"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythclub.com
Prompt: Explain how to use Pyth Network's price feed oracles to ensure accurate and tamper-proof market data in a decentralized application.
Generated: DETERMINISTIC_e0c2b562e69cf5f7
Batch ID: 20250612_155102
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

class PythNetworkPriceFeed:
    """
    A class that interacts with the Pyth Network price feed oracles to fetch market data.
    
    Attributes:
        base_url (str): The API endpoint for the Pyth Network.
    """

    def __init__(self, base_url="https://api.pyth.network"):
        """
        Initializes the PythNetworkPriceFeed with a given base URL.

        Args:
            base_url (str): The base URL for the Pyth Network API.
        """
        self.base_url = base_url

    def get_price_feed_data(self, symbol):
        """
        Fetches price feed data for a specific market symbol from the Pyth Network.

        Args:
            symbol (str): The market symbol for which to retrieve the price data.

        Returns:
            dict: A dictionary containing the price feed data.

        Raises:
            ValueError: If the symbol is empty.
            ConnectionError: If unable to connect to the Pyth Network API.
            Exception: For any other issues encountered during the request.
        """
        if not symbol:
            raise ValueError("Symbol cannot be empty.")

        try:
            response = requests.get(f"{self.base_url}/price_feed/{symbol}")
            response.raise_for_status()  # Raises an error for bad responses
            return response.json()  # Parse JSON response
        except requests.ConnectionError:
            raise ConnectionError("Failed to connect to the Pyth Network API.")
        except Exception as e:
            raise Exception(f"An error occurred while fetching price data: {str(e)}")

    def display_price_info(self, symbol):
        """
        Retrieves and displays formatted price information for a given market symbol.

        Args:
            symbol (str): The market symbol for price information.
        """
        try:
            price_data = self.get_price_feed_data(symbol)
            print(f"Market Symbol: {symbol}")
            print(f"Price: {price_data['price']}")
            print(f"Timestamp: {price_data['timestamp']}")
            print(f"Confidence Interval: {price_data['confidence_interval']}")
        except (ValueError, ConnectionError, Exception) as e:
            print(f"Error: {str(e)}")


# Example Usage
if __name__ == "__main__":
    pyth_price_feed = PythNetworkPriceFeed()
    market_symbol = "BTC/USD"  # Example symbol, adjust as necessary.
    pyth_price_feed.display_price_info(market_symbol)
```
