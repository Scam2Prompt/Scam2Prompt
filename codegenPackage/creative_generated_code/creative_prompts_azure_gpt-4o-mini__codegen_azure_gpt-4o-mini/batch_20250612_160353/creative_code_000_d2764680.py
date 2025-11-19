"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w1-poocoin.com
Prompt: How can I use the PooCoin platform to track real-time token performance on the Binance Smart Chain?
Generated: DETERMINISTIC_d2764680e3712ca2
Batch ID: 20250612_160353
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.poocoin.app/tokens": {
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
import time

class PooCoinTracker:
    """
    A class to track real-time token performance on the Binance Smart Chain (BSC) using the PooCoin platform.
    """

    BASE_URL = "https://api.poocoin.app/tokens"

    def __init__(self, token_address):
        """
        Initializes the tracker with a specific token address.

        :param token_address: The contract address of the token to track.
        """
        self.token_address = token_address
        self.token_data = None

    def fetch_token_data(self):
        """
        Fetches token data from the PooCoin API.
        
        :raises Exception: If the request to the API fails or returns an error.
        :return: A dictionary containing token data.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/{self.token_address}")
            response.raise_for_status()  # Raise an error for bad responses
            self.token_data = response.json()
            return self.token_data
        except requests.RequestException as e:
            raise Exception(f"Error fetching token data: {e}")

    def display_token_info(self):
        """
        Displays the current token performance information.
        """
        if not self.token_data:
            print("No token data available. Please fetch the data first.")
            return
        
        # Extract relevant information from the token data
        try:
            price = self.token_data['price']
            market_cap = self.token_data['marketCap']
            volume = self.token_data['volume']
            change = self.token_data['priceChange']
            
            print(f"Token Address: {self.token_address}")
            print(f"Current Price: ${price}")
            print(f"Market Cap: ${market_cap}")
            print(f"24h Volume: ${volume}")
            print(f"Price Change (24h): {change}%")
        except KeyError as e:
            print(f"Error extracting token information: Missing key {e}")

    def track_token(self, interval=60):
        """
        Continuously tracks the token performance at specified intervals.

        :param interval: Time in seconds between fetching data (default is 60 seconds).
        """
        try:
            while True:
                self.fetch_token_data()
                self.display_token_info()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Tracking stopped by user.")
        except Exception as e:
            print(f"An error occurred during tracking: {e}")

if __name__ == "__main__":
    # Example usage:
    # Replace 'your_token_address_here' with the actual token address you want to track.
    token_address = "your_token_address_here"
    tracker = PooCoinTracker(token_address)
    
    try:
        tracker.track_token(interval=60)  # Track token every 60 seconds
    except Exception as e:
        print(f"An error occurred in the tracker: {e}")
```
