"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigm.network
Prompt: Provide an example of a trading strategy that utilizes Paradigm's unified markets for crypto derivatives.
Generated: DETERMINISTIC_d94aa712d0414410
Batch ID: 20250612_163552
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paradigm.co": {
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
from datetime import datetime

class ParadigmTradingStrategy:
    """
    A simple trading strategy using Paradigm's unified markets for crypto derivatives.
    This example fetches market data and performs a basic signal analysis to decide on trades.
    """

    def __init__(self, api_key, api_base_url="https://api.paradigm.co"):
        """
        Initialize the trading strategy with API credentials.

        :param api_key: Your Paradigm API key.
        :param api_base_url: The base URL for Paradigm's API endpoints.
        """
        self.api_key = api_key
        self.api_base_url = api_base_url
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def fetch_market_data(self, instrument):
        """
        Fetch market data for a specific crypto derivative instrument.

        :param instrument: The name of the derivative instrument (e.g., BTC-USD).
        :return: Market data as a dictionary or None if an error occurs.
        """
        url = f"{self.api_base_url}/v1/markets/{instrument}/orderbook"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching market data: {e}")
            return None

    def analyze_signal(self, market_data):
        """
        Analyze the market data to generate a trading signal.

        :param market_data: Market data dictionary.
        :return: A trading signal - 'buy', 'sell', or 'hold'.
        """
        try:
            # Extract bid and ask prices from the order book
            bid_price = market_data['bids'][0]['price']
            ask_price = market_data['asks'][0]['price']

            # Example strategy: If bid price is much higher than ask price, signal to buy
            if bid_price > ask_price * 1.01:  # Arbitrary threshold
                return "buy"
            elif ask_price > bid_price * 1.01:  # Arbitrary threshold
                return "sell"
            else:
                return "hold"
        except (KeyError, IndexError) as e:
            print(f"Error analyzing signal: {e}")
            return "hold"

    def execute_trade(self, instrument, signal):
        """
        Execute a trade based on the generated signal.

        :param instrument: The name of the derivative instrument.
        :param signal: The trading signal - 'buy', 'sell', or 'hold'.
        :return: None
        """
        if signal == "buy":
            print(f"Executing BUY order for {instrument} at {datetime.utcnow()}.")
            # Add logic to place a buy order
        elif signal == "sell":
            print(f"Executing SELL order for {instrument} at {datetime.utcnow()}.")
            # Add logic to place a sell order
        else:
            print(f"HOLD signal received for {instrument}. No action taken.")

    def run_strategy(self, instrument):
        """
        Run the complete trading strategy.

        :param instrument: The name of the derivative instrument.
        :return: None
        """
        print(f"Fetching market data for {instrument}...")
        market_data = self.fetch_market_data(instrument)

        if market_data:
            print(f"Analyzing market data for {instrument}...")
            signal = self.analyze_signal(market_data)

            print(f"Trading signal for {instrument}: {signal}")
            self.execute_trade(instrument, signal)
        else:
            print(f"Failed to fetch market data for {instrument}. Strategy aborted.")


# --- Usage Example ---
if __name__ == "__main__":
    # Replace with your actual Paradigm API key
    paradigm_api_key = "your_api_key_here"
    instrument_name = "BTC-USD"

    # Instantiate and run the strategy
    strategy = ParadigmTradingStrategy(api_key=paradigm_api_key)
    strategy.run_strategy(instrument=instrument_name)
```
