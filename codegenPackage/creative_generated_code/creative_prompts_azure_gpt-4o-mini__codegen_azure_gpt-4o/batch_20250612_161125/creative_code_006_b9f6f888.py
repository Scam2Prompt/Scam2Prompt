"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geokukt.cn
Prompt: Provide an example of how to handle WebSocket connections with the OKX API for live trade updates.
Generated: DETERMINISTIC_b9f6f888f9a890b5
Batch ID: 20250612_161125
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

# Constants
OKX_WEBSOCKET_URL = "wss://ws.okx.com:8443/ws/v5/public"
TRADE_CHANNEL = "trades"
SYMBOL = "BTC-USDT"

async def connect_to_okx_websocket():
    """
    Connects to the OKX WebSocket API and listens for live trade updates.
    """
    try:
        async with websockets.connect(OKX_WEBSOCKET_URL) as websocket:
            # Subscribe to the trade channel for the specified symbol
            subscribe_message = {
                "op": "subscribe",
                "args": [
                    {
                        "channel": TRADE_CHANNEL,
                        "instId": SYMBOL
                    }
                ]
            }
            await websocket.send(json.dumps(subscribe_message))
            print(f"Subscribed to {TRADE_CHANNEL} for {SYMBOL}")

            # Listen for incoming messages
            async for message in websocket:
                try:
                    data = json.loads(message)
                    # Check if the message contains trade data
                    if "data" in data:
                        for trade in data["data"]:
                            print(f"Trade Update: {trade}")
                    else:
                        print(f"Non-trade message received: {data}")
                except json.JSONDecodeError:
                    print("Failed to decode message from WebSocket.")
                except Exception as e:
                    print(f"Error while processing WebSocket message: {e}")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"WebSocket connection closed: {e}")
    except asyncio.TimeoutError:
        print("WebSocket connection timed out.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

async def main():
    """
    Entry point to start the WebSocket connection.
    """
    await connect_to_okx_websocket()

if __name__ == "__main__":
    # Run the asyncio event loop
    asyncio.run(main())
```
