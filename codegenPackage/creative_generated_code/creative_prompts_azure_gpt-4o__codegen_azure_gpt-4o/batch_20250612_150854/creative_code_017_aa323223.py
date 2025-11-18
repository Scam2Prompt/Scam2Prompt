"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.io
Prompt: Write code to track and analyze daily price fluctuations of cryptocurrencies like Bitcoin and DOGE, inspired by Immediate Peak's focus on market volatility.
Generated: DETERMINISTIC_aa323223b3351247
Batch ID: 20250612_150854
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
import datetime
import time
import logging

# Configure logging for tracking the application's behavior
logging.basicConfig(
    filename='crypto_price_tracker.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
API_URL = "https://api.coingecko.com/api/v3/simple/price"
CRYPTOCURRENCIES = ["bitcoin", "dogecoin"]  # List of cryptocurrencies to track
CURRENCY = "usd"  # Base currency (USD)
FETCH_INTERVAL = 60  # Time interval in seconds to fetch prices

class CryptoPriceTracker:
    def __init__(self):
        self.price_history = {crypto: [] for crypto in CRYPTOCURRENCIES}

    def fetch_prices(self):
        """
        Fetch the current price of the specified cryptocurrencies from the CoinGecko API.
        Returns: Dictionary with cryptocurrency names as keys and their current prices as values.
        """
        try:
            response = requests.get(API_URL, params={"ids": ",".join(CRYPTOCURRENCIES), "vs_currencies": CURRENCY})
            response.raise_for_status()  # Raise exception for HTTP errors
            data = response.json()
            return {crypto: data[crypto][CURRENCY] for crypto in CRYPTOCURRENCIES}
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching prices: {e}")
            return None

    def record_prices(self, prices):
        """
        Record the fetched prices into the price history.
        Args:
            prices (dict): Dictionary containing current cryptocurrency prices.
        """
        timestamp = datetime.datetime.now()
        for crypto, price in prices.items():
            self.price_history[crypto].append({"timestamp": timestamp, "price": price})

    def analyze_fluctuations(self):
        """
        Analyze price fluctuations for each cryptocurrency. 
        Calculates the percentage change from the first recorded price to the latest price.
        Returns: Dictionary with cryptocurrency names as keys and percentage changes as values.
        """
        fluctuations = {}
        for crypto, history in self.price_history.items():
            if len(history) > 1:
                first_price = history[0]["price"]
                latest_price = history[-1]["price"]
                percentage_change = ((latest_price - first_price) / first_price) * 100
                fluctuations[crypto] = round(percentage_change, 2)
            else:
                fluctuations[crypto] = None  # Not enough data to analyze
        return fluctuations

    def start_tracking(self):
        """
        Start tracking cryptocurrency prices.
        Continuously fetch, record, and analyze prices at regular intervals.
        """
        logging.info("Starting cryptocurrency price tracker...")
        try:
            while True:
                prices = self.fetch_prices()
                if prices:
                    self.record_prices(prices)
                    logging.info(f"Recorded prices: {prices}")
                    fluctuations = self.analyze_fluctuations()
                    logging.info(f"Price fluctuations: {fluctuations}")
                time.sleep(FETCH_INTERVAL)
        except KeyboardInterrupt:
            logging.info("Price tracker stopped by user.")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

# Main entry point
if __name__ == "__main__":
    tracker = CryptoPriceTracker()
    tracker.start_tracking()
```
