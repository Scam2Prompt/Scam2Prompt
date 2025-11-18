"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astertex.com
Prompt: Write a script to fetch real-time trading data for a specific symbol using Aster's Pro Mode API and display advanced order options.
Generated: DETERMINISTIC_9487fe091c613c91
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aster.com/v1": {
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

class AsterAPI:
    def __init__(self, api_key: str):
        """
        Initializes the AsterAPI class with the provided API key.
        
        :param api_key: API key for authenticating requests to the Aster API.
        """
        self.api_key = api_key
        self.base_url = "https://api.aster.com/v1"

    def fetch_trading_data(self, symbol: str) -> dict:
        """
        Fetches real-time trading data for the specified symbol using Aster's Pro Mode API.
        
        :param symbol: The trading symbol for which to fetch data.
        :return: A dictionary containing trading data.
        :raises ValueError: If the symbol is invalid.
        :raises Exception: If an error occurs during the API request.
        """
        if not symbol:
            raise ValueError("Symbol cannot be empty.")

        url = f"{self.base_url}/trading_data/{symbol}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

    def display_order_options(self, trading_data: dict) -> None:
        """
        Displays advanced order options based on the fetched trading data.
        
        :param trading_data: A dictionary containing trading data.
        """
        print("Advanced Order Options:")
        print(f"Symbol: {trading_data.get('symbol')}")
        print(f"Current Price: {trading_data.get('current_price')}")
        print(f"Bid: {trading_data.get('bid')}")
        print(f"Ask: {trading_data.get('ask')}")
        print(f"Volume: {trading_data.get('volume')}")
        print("Available Order Types: Limit, Market, Stop-Loss")

def main():
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    SYMBOL = "AAPL"  # Example symbol for Apple Inc.

    aster_api = AsterAPI(api_key=API_KEY)

    try:
        # Fetch trading data for the specified symbol
        trading_data = aster_api.fetch_trading_data(SYMBOL)
        
        # Display the advanced order options
        aster_api.display_order_options(trading_data)

    except Exception as e:
        print(f"Failed to fetch trading data: {e}")

if __name__ == "__main__":
    main()
```
