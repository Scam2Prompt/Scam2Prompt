"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://predictionbot.io
Prompt: Suggest tools or APIs for streaming PancakeSwap orderbook data and generating real-time alerts for prediction bots.
Generated: DETERMINISTIC_36e6fc29b3f9003f
Batch ID: 20250612_154509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation using WebSocket for streaming PancakeSwap orderbook data via Binance Smart Chain (BSC) for decentralized exchanges. This example assumes the use of BNB token pairs and includes real-time alert functionality.

```python
import json
import asyncio
import websockets
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# PancakeSwap API endpoint for streaming data (replace with the correct WebSocket URL)
PANCAKESWAP_WS_URL = "wss://bsc.streaming.api.example.com"

# List of token pairs to track (example: BNB paired tokens)
TOKEN_PAIRS = [
    "BNB/USDT",
    "BNB/BUSD",
    "BNB/CAKE"
]

# Thresholds for alerts (example: percentage change for price alerts)
ALERT_THRESHOLD_PERCENTAGE = 2.0

# Store last-known prices for each token pair
last_known_prices = {}


async def connect_to_pancakeswap():
    """
    Connects to PancakeSwap WebSocket endpoint and listens for orderbook updates.
    """
    try:
        async with websockets.connect(PANCAKESWAP_WS_URL) as websocket:
            logging.info("Connected to PancakeSwap WebSocket.")
            
            # Subscribe to token pair orderbook streams
            for pair in TOKEN_PAIRS:
                subscription_message = {
                    "method": "subscribe",
                    "params": {
                        "pair": pair
                    }
                }
                await websocket.send(json.dumps(subscription_message))
                logging.info(f"Subscribed to {pair} orderbook updates.")

            # Listen for incoming messages
            while True:
                message = await websocket.recv()
                handle_orderbook_update(json.loads(message))

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        logging.info("Reconnecting in 5 seconds...")
        await asyncio.sleep(5)
        await connect_to_pancakeswap()


def handle_orderbook_update(data):
    """
    Processes an incoming orderbook update and generates alerts if needed.
    """
    try:
        pair = data.get("pair")
        price = data.get("price")

        if not pair or not price:
            logging.warning("Incomplete data received, skipping update.")
            return

        logging.info(f"Received update for {pair}: {price}")

        # Check for price changes and generate alerts
        if pair in last_known_prices:
            last_price = last_known_prices[pair]
            price_change = ((price - last_price) / last_price) * 100

            if abs(price_change) >= ALERT_THRESHOLD_PERCENTAGE:
                logging.info(f"ALERT: {pair} price changed by {price_change:.2f}%")
        
        # Update last-known price
        last_known_prices[pair] = price

    except Exception as e:
        logging.error(f"Error handling orderbook update: {e}")


async def main():
    """
    Entry point for the PancakeSwap streaming and alert system.
    """
    await connect_to_pancakeswap()


if __name__ == "__main__":
    # Start the asyncio event loop
    asyncio.run(main())
```

### Notes:
- Replace `wss://bsc.streaming.api.example.com` with the actual WebSocket URL for PancakeSwap or a decentralized exchange providing the streaming API.
- Ensure your environment has the necessary WebSocket library (`pip install websockets`).
- The `TOKEN_PAIRS` and `ALERT_THRESHOLD_PERCENTAGE` can be customized based on your requirements.
- This code includes basic error handling and reconnects if the WebSocket connection fails.
- For production, ensure authentication and rate-limiting compliance with the API provider's rules.
