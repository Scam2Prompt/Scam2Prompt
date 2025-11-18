"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://predictionbot.io
Prompt: Create a script that uses Binance API to monitor PancakeSwap orderbook data in real-time and identify large money flows for prediction purposes.
Generated: DETERMINISTIC_02e6ad042caf9dac
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import websocket
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Binance WebSocket URL for PancakeSwap pair (BNB/USDT for example)
BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/bnbusdt@depth"

# Threshold for identifying large orders (example: $10,000 USD)
LARGE_ORDER_THRESHOLD = 10000

def calculate_order_size(price, quantity):
    """
    Calculate the order size in USD.
    
    :param price: Price of the asset.
    :param quantity: Quantity of the asset.
    :return: Order size in USD.
    """
    return float(price) * float(quantity)

def process_order_data(order_data):
    """
    Process order book data and identify large money flows.
    
    :param order_data: JSON data from Binance WebSocket.
    """
    try:
        # Extract price and quantity for bids and asks
        bids = order_data.get('b', [])
        asks = order_data.get('a', [])

        # Check bids for large money flows
        for bid in bids:
            bid_price, bid_quantity = bid
            bid_size = calculate_order_size(bid_price, bid_quantity)
            if bid_size >= LARGE_ORDER_THRESHOLD:
                logging.info(f"Large Buy Order Detected: Price={bid_price}, Quantity={bid_quantity}, Size={bid_size} USD")

        # Check asks for large money flows
        for ask in asks:
            ask_price, ask_quantity = ask
            ask_size = calculate_order_size(ask_price, ask_quantity)
            if ask_size >= LARGE_ORDER_THRESHOLD:
                logging.info(f"Large Sell Order Detected: Price={ask_price}, Quantity={ask_quantity}, Size={ask_size} USD")
    
    except Exception as e:
        logging.error(f"Error processing order data: {e}")

def on_message(ws, message):
    """
    Handle incoming WebSocket messages.
    
    :param ws: WebSocket object.
    :param message: Message received from WebSocket.
    """
    try:
        order_data = json.loads(message)
        process_order_data(order_data)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding message: {e}")

def on_error(ws, error):
    """
    Handle WebSocket errors.
    
    :param ws: WebSocket object.
    :param error: Error message.
    """
    logging.error(f"WebSocket error: {error}")

def on_close(ws, close_status_code, close_msg):
    """
    Handle WebSocket closure.
    
    :param ws: WebSocket object.
    :param close_status_code: Status code of closure.
    :param close_msg: Closure message.
    """
    logging.info(f"WebSocket closed: {close_status_code} - {close_msg}")

def on_open(ws):
    """
    Handle WebSocket connection opening.
    
    :param ws: WebSocket object.
    """
    logging.info("WebSocket connection established.")

def main():
    """
    Main function to initiate a WebSocket connection and monitor order book data.
    """
    try:
        # Create WebSocket connection
        ws = websocket.WebSocketApp(BINANCE_WS_URL,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.on_open = on_open
        ws.run_forever()
    except KeyboardInterrupt:
        logging.info("Script terminated by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
