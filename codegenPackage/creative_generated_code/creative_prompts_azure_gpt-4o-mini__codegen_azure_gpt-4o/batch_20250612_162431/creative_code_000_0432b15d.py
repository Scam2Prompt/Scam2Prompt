"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coingenius.org
Prompt: How can I use the Coingenius Websocket API to automate my cryptocurrency arbitrage trading strategies?
Generated: DETERMINISTIC_0432b15d49b0cab9
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import websocket
import json
import time
import threading

# Constants
COINGENIUS_WS_URL = "wss://api.coingenius.ai/v1/ws"
ARBITRAGE_THRESHOLD = 0.01  # Minimum percentage difference for arbitrage (e.g., 1%)

# Global variables to store price data
price_data = {}

# Function to handle WebSocket messages
def on_message(ws, message):
    try:
        # Parse the incoming WebSocket message
        data = json.loads(message)
        
        # Extract relevant price data (example format depends on API documentation)
        pair = data.get("pair")
        price = data.get("price")
        
        # Store the price data
        if pair and price:
            price_data[pair] = price
        
        # Perform arbitrage check
        check_arbitrage()
    except Exception as e:
        print(f"Error processing message: {e}")

# Function to handle WebSocket errors
def on_error(ws, error):
    print(f"WebSocket error: {error}")

# Function to handle WebSocket connection closure
def on_close(ws, close_status_code, close_msg):
    print(f"WebSocket connection closed: {close_msg}")

# Function to handle WebSocket connection opening
def on_open(ws):
    # Subscribe to cryptocurrency price updates
    # Example subscription format depends on API documentation
    subscription_message = {
        "action": "subscribe",
        "channels": ["price_updates"]
    }
    ws.send(json.dumps(subscription_message))
    print("WebSocket connection opened and subscription message sent.")

# Function to check for arbitrage opportunities
def check_arbitrage():
    # Example: Compare prices between trading pairs
    # This logic should be customized based on the available trading pairs
    # and the structure of the price_data dictionary

    trading_pairs = list(price_data.keys())
    for i in range(len(trading_pairs)):
        for j in range(i + 1, len(trading_pairs)):
            pair1 = trading_pairs[i]
            pair2 = trading_pairs[j]
            price1 = price_data[pair1]
            price2 = price_data[pair2]
            
            # Calculate percentage difference
            if price1 and price2:
                percentage_diff = abs(price1 - price2) / min(price1, price2)
                if percentage_diff >= ARBITRAGE_THRESHOLD:
                    print(f"Arbitrage opportunity detected!")
                    print(f"Buy {pair1} at {price1} and sell {pair2} at {price2}")
                    # Execute arbitrage strategy (implementation depends on trading platform API)
                    execute_arbitrage(pair1, pair2, price1, price2)

# Placeholder function to execute an arbitrage trade
def execute_arbitrage(pair1, pair2, price1, price2):
    try:
        # Implement trade logic here (depends on trading platform API)
        print(f"Executing arbitrage trade between {pair1} and {pair2}")
    except Exception as e:
        print(f"Error executing trade: {e}")

# Function to start the WebSocket client
def start_websocket_client():
    ws = websocket.WebSocketApp(
        COINGENIUS_WS_URL,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open
    )
    ws.run_forever()

# Main entry point
if __name__ == "__main__":
    # Run WebSocket client in a separate thread
    client_thread = threading.Thread(target=start_websocket_client)
    client_thread.start()
    
    # Keep the main thread alive
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting...")
            break
```
