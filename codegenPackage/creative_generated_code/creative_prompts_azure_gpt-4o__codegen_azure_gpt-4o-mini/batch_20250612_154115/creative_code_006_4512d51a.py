"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pc.bigwhales.com
Prompt: Develop a script to automate investment tracking for cryptocurrencies and Forex using APIs similar to Bigwhales.
Generated: DETERMINISTIC_4512d51a108ead28
Batch ID: 20250612_154115
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/forex": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/crypto": {
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
import pandas as pd
import time
import logging
from typing import Dict, Any

# Configure logging for better tracking of the application's behavior
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentTracker:
    def __init__(self, crypto_api_url: str, forex_api_url: str):
        """
        Initialize the InvestmentTracker with the API URLs.

        :param crypto_api_url: API URL for cryptocurrency data
        :param forex_api_url: API URL for Forex data
        """
        self.crypto_api_url = crypto_api_url
        self.forex_api_url = forex_api_url
        self.investments = {
            'crypto': {},
            'forex': {}
        }

    def fetch_data(self, api_url: str) -> Dict[str, Any]:
        """
        Fetch data from the given API URL.

        :param api_url: The URL to fetch data from
        :return: Parsed JSON response from the API
        """
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            logging.info(f"Data fetched successfully from {api_url}")
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching data from {api_url}: {e}")
            return {}

    def track_crypto(self, coin: str) -> None:
        """
        Track a specific cryptocurrency.

        :param coin: The cryptocurrency symbol to track (e.g., 'BTC', 'ETH')
        """
        api_url = f"{self.crypto_api_url}/ticker/{coin}"
        data = self.fetch_data(api_url)
        if data:
            self.investments['crypto'][coin] = data
            logging.info(f"Tracked cryptocurrency: {coin} - {data}")

    def track_forex(self, pair: str) -> None:
        """
        Track a specific Forex pair.

        :param pair: The Forex pair to track (e.g., 'EUR/USD', 'GBP/JPY')
        """
        api_url = f"{self.forex_api_url}/ticker/{pair}"
        data = self.fetch_data(api_url)
        if data:
            self.investments['forex'][pair] = data
            logging.info(f"Tracked Forex pair: {pair} - {data}")

    def display_investments(self) -> None:
        """
        Display the current tracked investments in a tabular format.
        """
        logging.info("Current Investments:")
        crypto_df = pd.DataFrame(self.investments['crypto']).T
        forex_df = pd.DataFrame(self.investments['forex']).T
        
        if not crypto_df.empty:
            print("\nCryptocurrency Investments:\n", crypto_df)
        
        if not forex_df.empty:
            print("\nForex Investments:\n", forex_df)

    def run(self, interval: int = 60) -> None:
        """
        Run the investment tracker at specified intervals.

        :param interval: Time interval (in seconds) to fetch new data
        """
        try:
            while True:
                # Example tracking
                self.track_crypto('BTC')
                self.track_forex('EUR/USD')
                self.display_investments()
                time.sleep(interval)
        except KeyboardInterrupt:
            logging.info("Investment tracking stopped by user.")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

# Configuration for APIs
CRYPTO_API_URL = 'https://api.example.com/crypto'  # Replace with actual cryptocurrency API
FOREX_API_URL = 'https://api.example.com/forex'    # Replace with actual Forex API

# Entry point of the script
if __name__ == "__main__":
    tracker = InvestmentTracker(CRYPTO_API_URL, FOREX_API_URL)
    tracker.run(interval=300)  # Run the tracker every 5 minutes
```
