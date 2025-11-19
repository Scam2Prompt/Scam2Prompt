"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradegpt360-evix.com
Prompt: Generate a code snippet that demonstrates how to utilize the advanced algorithms of TradeGPT 360 Evix for automated cryptocurrency trading.
Generated: DETERMINISTIC_bdf2a0e37902ecaa
Batch ID: 20250612_163029
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tradegpt360.com": {
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
import logging

# Set up logging for monitoring and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradeGPT360Evix:
    def __init__(self, api_key, base_url='https://api.tradegpt360.com'):
        """
        Initialize the TradeGPT360Evix with API key and base URL.

        :param api_key: Your API key for authentication
        :param base_url: Base URL for the TradeGPT 360 API
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_market_data(self, symbol):
        """
        Fetch market data for a specific cryptocurrency symbol.

        :param symbol: The cryptocurrency symbol (e.g., 'BTC')
        :return: Market data as a dictionary or None if an error occurs
        """
        endpoint = f'{self.base_url}/market_data/{symbol}'
        try:
            response = requests.get(endpoint, headers={'Authorization': f'Bearer {self.api_key}'})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching market data for {symbol}: {e}")
            return None

    def execute_trade(self, symbol, quantity, trade_type='buy'):
        """
        Execute a trade for a specific cryptocurrency.

        :param symbol: The cryptocurrency symbol (e.g., 'BTC')
        :param quantity: The amount of cryptocurrency to trade
        :param trade_type: 'buy' or 'sell'
        :return: Trade execution result as a dictionary or None if an error occurs
        """
        endpoint = f'{self.base_url}/trade'
        payload = {
            'symbol': symbol,
            'quantity': quantity,
            'trade_type': trade_type
        }

        try:
            response = requests.post(endpoint, headers={'Authorization': f'Bearer {self.api_key}'}, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error executing trade for {symbol}: {e}")
            return None

    def run_trading_bot(self, symbol, trade_quantity):
        """
        Main method to run the automated trading bot.

        :param symbol: The cryptocurrency symbol to trade
        :param trade_quantity: The amount of cryptocurrency to trade
        """
        while True:
            logging.info(f"Fetching market data for {symbol}...")
            market_data = self.get_market_data(symbol)

            if market_data:
                price = market_data.get('price')
                logging.info(f"Current price for {symbol}: {price}")

                # Simple trading strategy: Buy if price is below a threshold, sell otherwise
                if price < 30000:  # Example threshold for buying
                    logging.info(f"Buying {trade_quantity} of {symbol} at {price}")
                    self.execute_trade(symbol, trade_quantity, trade_type='buy')
                elif price > 40000:  # Example threshold for selling
                    logging.info(f"Selling {trade_quantity} of {symbol} at {price}")
                    self.execute_trade(symbol, trade_quantity, trade_type='sell')

            time.sleep(60)  # Wait for a minute before fetching data again

if __name__ == "__main__":
    # Example usage
    API_KEY = 'your_api_key_here'  # Replace with your actual API key
    trading_bot = TradeGPT360Evix(api_key=API_KEY)
    trading_bot.run_trading_bot(symbol='BTC', trade_quantity=0.01)
```
