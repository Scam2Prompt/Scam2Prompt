"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tensr-dao.web.app
Prompt: Write a function that integrates Solana's blockchain API to display live updates of NFT trading metrics, including floor price and sell price, as shown on Tensor's platform.
Generated: DETERMINISTIC_8497624f6d65b55c
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import websockets
import json
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for Solana blockchain API and Tensor platform's WebSocket
SOLANA_API_WS = "wss://api.mainnet-beta.solana.com/v1"
TENSOR_WS = "wss://ws.tensor.trade"

async def fetch_nft_trading_metrics():
    """
    Connects to Tensor's WebSocket to display live updates of NFT trading metrics,
    including floor price and sell price.

    The function listens for incoming data, parses the NFT trading metrics, and
    displays the updates in real-time.
    """
    try:
        # Establish WebSocket connection with Tensor's platform
        async with websockets.connect(TENSOR_WS) as websocket:
            logging.info("Connected to Tensor WebSocket API")

            # Subscribe to NFT trading metrics stream (example payload - adjust based on actual API)
            subscribe_payload = {
                "action": "subscribe",
                "channel": "nft_trading_metrics"  # Replace with the correct channel name
            }
            await websocket.send(json.dumps(subscribe_payload))
            logging.info("Subscription request sent: %s", subscribe_payload)

            # Listen for incoming messages from the WebSocket stream
            while True:
                message = await websocket.recv()
                data = json.loads(message)

                # Parse and display NFT trading metrics
                # Ensure proper fields exist in the response
                if "floor_price" in data and "sell_price" in data:
                    floor_price = data["floor_price"]
                    sell_price = data["sell_price"]
                    logging.info("Floor Price: %s, Sell Price: %s", floor_price, sell_price)
                else:
                    logging.warning("Unexpected data format received: %s", data)

    except websockets.ConnectionClosed as e:
        logging.error("WebSocket connection closed: %s", e)
    except Exception as e:
        logging.error("An error occurred: %s", e)

# Entry point of the script
if __name__ == "__main__":
    try:
        asyncio.run(fetch_nft_trading_metrics())
    except KeyboardInterrupt:
        logging.info("Script terminated by user.")
    except Exception as e:
        logging.error("Unexpected error: %s", e)
```

This code assumes Tensor has a WebSocket API for fetching NFT trading metrics. Replace `"channel": "nft_trading_metrics"` and other details with the actual API specifications provided by Tensor's platform.
