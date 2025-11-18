"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradegpt360-evix.com
Prompt: Create a Python script to generate trade signals for Bitcoin and Ethereum based on real-time market scans, inspired by the TradeGPT 360 Evix app's features.
Generated: DETERMINISTIC_ec8b35d608915bbf
Batch ID: 20250612_150843
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/market": {
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
import numpy as np
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradeSignalGenerator:
    """
    A class to generate trade signals for Bitcoin and Ethereum based on real-time market data.
    """

    def __init__(self, api_url, threshold=0.02):
        """
        Initializes the TradeSignalGenerator with API endpoint and trade signal threshold.

        :param api_url: The API endpoint for fetching cryptocurrency market data.
        :param threshold: The percentage threshold for generating buy/sell signals.
        """
        self.api_url = api_url
        self.threshold = threshold

    def fetch_market_data(self):
        """
        Fetches market data for Bitcoin and Ethereum from the specified API.

        :return: A dictionary containing market data for Bitcoin and Ethereum.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            market_data = response.json()
            return market_data
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching market data: {e}")
            return None

    def calculate_trade_signal(self, market_data):
        """
        Calculates trade signals based on market data.

        :param market_data: The market data dictionary.
        :return: A dictionary with trade signals for Bitcoin and Ethereum.
        """
        try:
            signals = {}
            for coin in ['BTC', 'ETH']:
                price = market_data[coin]['price']
                prev_price = market_data[coin]['prevPrice']
                change = (price - prev_price) / prev_price
                
                if change > self.threshold:
                    signals[coin] = 'BUY'
                elif change < -self.threshold:
                    signals[coin] = 'SELL'
                else:
                    signals[coin] = 'HOLD'
            return signals
        except KeyError as e:
            logging.error(f"Error calculating trade signals: Missing key {e}")
            return None

    def generate_signals(self):
        """
        Main method to fetch market data and generate trade signals.
        
        :return: A dictionary with trade signals for Bitcoin and Ethereum or None if an error occurs.
        """
        market_data = self.fetch_market_data()
        if market_data:
            return self.calculate_trade_signal(market_data)
        logging.error("Failed to generate signals due to market data fetch error.")
        return None

def main():
    """
    Main function to execute the trade signal generator.
    """
    API_URL = 'https://api.example.com/market'  # Replace with actual API endpoint
    signal_generator = TradeSignalGenerator(api_url=API_URL)

    while True:
        signals = signal_generator.generate_signals()
        if signals:
            logging.info(f"Trade Signals: {signals}")
        time.sleep(60)  # Fetch data every 60 seconds

if __name__ == "__main__":
    main()
```
