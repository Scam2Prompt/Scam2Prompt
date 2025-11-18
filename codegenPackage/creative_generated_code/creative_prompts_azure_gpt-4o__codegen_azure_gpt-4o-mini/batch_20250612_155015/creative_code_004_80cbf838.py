"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythcloud.com
Prompt: Write code to fetch and display real-time market data from Pyth Network's price feed oracles using Python.
Generated: DETERMINISTIC_80cbf838c181ccaa
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
import time

class PythNetworkClient:
    """
    A client to fetch real-time market data from Pyth Network's price feed oracles.
    """

    BASE_URL = "https://api.pyth.network/v1"

    def __init__(self):
        """
        Initializes the PythNetworkClient.
        """
        self.price_feed_url = f"{self.BASE_URL}/price_feeds"

    def fetch_price_data(self):
        """
        Fetches price data from the Pyth Network API.

        Returns:
            dict: Parsed JSON response containing price data.
        """
        try:
            response = requests.get(self.price_feed_url)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            return response.json()  # Return the JSON response as a dictionary

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None  # Return None on failure

    def display_price_data(self, price_data):
        """
        Displays the price data in a readable format.

        Args:
            price_data (dict): The price data to display.
        """
        if price_data is None:
            print("No price data available.")
            return

        print("Real-Time Market Data:")
        for feed in price_data.get("data", []):
            symbol = feed.get("symbol", "N/A")
            price = feed.get("price", "N/A")
            conf = feed.get("conf", "N/A")
            print(f"Symbol: {symbol}, Price: {price}, Confidence: {conf}")

def main():
    """
    Main function to run the client and fetch market data periodically.
    """
    client = PythNetworkClient()

    while True:
        # Fetch and display price data
        price_data = client.fetch_price_data()
        client.display_price_data(price_data)

        # Sleep for a specified interval before the next fetch
        time.sleep(60)  # Fetch new data every 60 seconds

if __name__ == "__main__":
    main()
```
