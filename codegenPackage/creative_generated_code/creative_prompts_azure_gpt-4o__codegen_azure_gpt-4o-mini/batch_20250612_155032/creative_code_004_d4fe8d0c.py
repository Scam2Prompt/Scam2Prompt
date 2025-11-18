"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kantor-usdc.com
Prompt: Create a Python script to track cryptocurrency exchange rates (USDC, Bitcoin, Ethereum) in real-time for a service like Kantor USDC Białystok.
Generated: DETERMINISTIC_d4fe8d0c16ad2301
Batch ID: 20250612_155032
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
import time
import json
from datetime import datetime

class CryptoTracker:
    """
    A class to track cryptocurrency exchange rates for USDC, Bitcoin, and Ethereum.
    """

    def __init__(self):
        self.api_url = "https://api.coingecko.com/api/v3/simple/price"
        self.currencies = ["usd", "bitcoin", "ethereum"]
        self.target_currency = "usd"
        self.refresh_interval = 60  # Refresh every 60 seconds

    def fetch_exchange_rates(self):
        """
        Fetch the current exchange rates for the specified cryptocurrencies.
        Returns a dictionary with currency names and their respective rates.
        """
        # Define the parameters for the API request
        params = {
            'ids': ','.join(self.currencies),
            'vs_currencies': self.target_currency
        }

        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            return None

    def display_rates(self, rates):
        """
        Display the fetched exchange rates in a formatted manner.
        """
        if not rates:
            print("No rates to display.")
            return

        print(f"\nExchange Rates at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:")
        for currency, data in rates.items():
            print(f"{currency.capitalize()}: {data[self.target_currency]} {self.target_currency.upper()}")

    def run(self):
        """
        Continuously fetch and display exchange rates at defined intervals.
        """
        print("Starting cryptocurrency exchange rate tracker...\n")
        try:
            while True:
                rates = self.fetch_exchange_rates()
                self.display_rates(rates)
                time.sleep(self.refresh_interval)
        except KeyboardInterrupt:
            print("\nTracker stopped by user.")

if __name__ == "__main__":
    tracker = CryptoTracker()
    tracker.run()
```
