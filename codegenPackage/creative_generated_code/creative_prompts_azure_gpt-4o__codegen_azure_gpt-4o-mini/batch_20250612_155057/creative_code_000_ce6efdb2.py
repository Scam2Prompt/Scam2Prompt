"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom237.com
Prompt: Write a Python script to simulate a cryptocurrency price tracker for PHANTOM237 ($PHTM), including features for fetching real-time data from a public API and displaying price changes over time.
Generated: DETERMINISTIC_ce6efdb23eec1446
Batch ID: 20250612_155057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1/prices/phtm": {
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
import json

class CryptocurrencyPriceTracker:
    """
    A class to track the price of a cryptocurrency ($PHTM) using a public API.
    """

    def __init__(self, api_url):
        """
        Initializes the CryptocurrencyPriceTracker with the given API URL.

        :param api_url: str - The URL of the public API for fetching cryptocurrency prices.
        """
        self.api_url = api_url
        self.price_history = []

    def fetch_price(self):
        """
        Fetches the current price of $PHTM from the API.

        :return: float - The current price of $PHTM.
        :raises Exception: If the API request fails.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            current_price = data['price']  # Adjust the key based on the actual API response
            return float(current_price)
        except requests.RequestException as e:
            raise Exception(f"Error fetching price data: {e}") from e
        except (KeyError, ValueError) as e:
            raise Exception(f"Error parsing price data: {e}") from e

    def track_price(self, interval=60, duration=3600):
        """
        Tracks the price of $PHTM over a specified duration.

        :param interval: int - Time in seconds between price fetches.
        :param duration: int - Total time in seconds to track the price.
        """
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                current_price = self.fetch_price()
                self.price_history.append(current_price)
                print(f"Current $PHTM Price: ${current_price:.2f}")
                time.sleep(interval)
            except Exception as e:
                print(e)
                time.sleep(interval)  # Wait before retrying in case of an error

    def display_price_changes(self):
        """
        Displays the price changes over time.
        """
        if not self.price_history:
            print("No price data available.")
            return
        
        for i in range(1, len(self.price_history)):
            change = self.price_history[i] - self.price_history[i - 1]
            percentage_change = (change / self.price_history[i - 1]) * 100
            print(f"Change from {self.price_history[i - 1]:.2f} to {self.price_history[i]:.2f}: {change:.2f} ({percentage_change:.2f}%)")

if __name__ == "__main__":
    # Example API URL (replace with actual API)
    API_URL = "https://api.example.com/v1/prices/phtm"
    
    tracker = CryptocurrencyPriceTracker(API_URL)
    
    # Track price for 1 hour, fetching every 60 seconds
    tracker.track_price(interval=60, duration=3600)
    
    # Display price changes after tracking
    tracker.display_price_changes()
```
