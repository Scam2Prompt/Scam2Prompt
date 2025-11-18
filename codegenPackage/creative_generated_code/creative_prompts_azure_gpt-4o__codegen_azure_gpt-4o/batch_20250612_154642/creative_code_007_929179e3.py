"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gjgfffjf2.cn
Prompt: Generate a Python script to monitor price fluctuations and send alerts using OKX's real-time notification system for cryptocurrency price changes.
Generated: DETERMINISTIC_929179e310382e5d
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import websocket
import threading

# Constants for OKX WebSocket API
OKX_WEBSOCKET_URL = "wss://ws.okx.com:8443/ws/v5/public"

# Cryptocurrencies to monitor
CRYPTO_SYMBOLS = ["BTC-USDT", "ETH-USDT"]  # Add more pairs as needed

# Threshold percentage for alert
PRICE_CHANGE_THRESHOLD = 2.0  # Example: 2% change

# Function to send alerts (can be extended for email, SMS, etc.)
def send_alert(symbol, current_price, price_change):
    print(f"ALERT: {symbol} price changed by {price_change:.2f}% and is now {current_price:.2f}")

# Class to manage price monitoring
class PriceMonitor:
    def __init__(self, symbols, threshold):
        self.symbols = symbols
        self.threshold = threshold
        self.prices = {symbol: None for symbol in symbols}
        self.ws = None

    def on_message(self, ws, message):
        try:
            data = json.loads(message)
            if "data" in data:
                for item in data["data"]:
                    symbol = item["instId"]
                    current_price = float(item["last"])
                    previous_price = self.prices[symbol]

                    if previous_price is not None:
                        price_change = ((current_price - previous_price) / previous_price) * 100
                        if abs(price_change) >= self.threshold:
                            send_alert(symbol, current_price, price_change)

                    # Update the stored price
                    self.prices[symbol] = current_price
        except Exception as e:
            print(f"Error processing message: {e}")

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket connection closed")

    def on_open(self, ws):
        print("WebSocket connection opened")
        # Subscribe to tickers for specified symbols
        subscribe_message = {
            "op": "subscribe",
            "args": [{"channel": "tickers", "instId": symbol} for symbol in self.symbols]
        }
        ws.send(json.dumps(subscribe_message))

    def start(self):
        self.ws = websocket.WebSocketApp(
            OKX_WEBSOCKET_URL,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        # Run WebSocket in a separate thread
        thread = threading.Thread(target=self.ws.run_forever)
        thread.daemon = True
        thread.start()

# Main function
def main():
    try:
        monitor = PriceMonitor(CRYPTO_SYMBOLS, PRICE_CHANGE_THRESHOLD)
        monitor.start()

        # Keep the script running
        while True:
            pass
    except KeyboardInterrupt:
        print("Script terminated by user")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
