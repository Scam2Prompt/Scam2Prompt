"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polypredict.fun
Prompt: Create a program that tracks live market movements and price changes in real-time, inspired by PolyPredict's professional-grade analytics features.
Generated: DETERMINISTIC_b29e4ca7d72504cf
Batch ID: 20250612_154708
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for a program that tracks live market movements and price changes in real-time using the `websocket` and `requests` libraries. This code is designed to connect to a public cryptocurrency WebSocket API (such as Binance) for real-time updates.

```python
import websocket
import json
import logging
from datetime import datetime

# Set up logging for monitoring and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

class MarketTracker:
    """
    A class to track live market movements and price changes in real-time.
    """

    def __init__(self, symbol="btcusdt"):
        """
        Initialize the MarketTracker instance.

        :param symbol: The trading pair symbol (e.g., 'btcusdt' for Bitcoin/USDT).
        """
        self.symbol = symbol
        self.websocket_url = f"wss://stream.binance.com:9443/ws/{self.symbol}@trade"
        self.ws = None

    def on_message(self, ws, message):
        """
        Callback executed when a message is received from the WebSocket server.

        :param ws: The WebSocketApp instance.
        :param message: The message received from the WebSocket server.
        """
        try:
            data = json.loads(message)
            price = float(data["p"])
            quantity = float(data["q"])
            trade_time = datetime.fromtimestamp(data["T"] / 1000).strftime('%Y-%m-%d %H:%M:%S')
            logging.info(f"Price: {price} | Quantity: {quantity} | Time: {trade_time}")
        except Exception as e:
            logging.error(f"Error processing message: {e}")

    def on_error(self, ws, error):
        """
        Callback executed when an error occurs.

        :param ws: The WebSocketApp instance.
        :param error: The error message.
        """
        logging.error(f"WebSocket error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        """
        Callback executed when the WebSocket connection is closed.

        :param ws: The WebSocketApp instance.
        :param close_status_code: The close status code.
        :param close_msg: The close message.
        """
        logging.info("WebSocket connection closed.")

    def on_open(self, ws):
        """
        Callback executed when the WebSocket connection is opened.

        :param ws: The WebSocketApp instance.
        """
        logging.info(f"Connected to WebSocket for symbol: {self.symbol}")

    def start_tracking(self):
        """
        Start tracking live market movements by connecting to the WebSocket API.
        """
        logging.info("Starting market tracking...")
        self.ws = websocket.WebSocketApp(
            self.websocket_url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ws.on_open = self.on_open
        self.ws.run_forever()


if __name__ == "__main__":
    try:
        # Initialize the tracker for a specific symbol (e.g., Bitcoin/USDT)
        tracker = MarketTracker(symbol="btcusdt")
        tracker.start_tracking()
    except KeyboardInterrupt:
        logging.info("Market tracking stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```

### Requirements:
- Install the `websocket-client` library using `pip install websocket-client`.
- Replace `btcusdt` with the desired trading pair symbol for tracking.

This code connects to Binance's WebSocket API, receives real-time trading data for the specified symbol, and logs price updates, trade quantities, and timestamps. Proper error handling, logging, and best practices are followed to ensure production readiness.
