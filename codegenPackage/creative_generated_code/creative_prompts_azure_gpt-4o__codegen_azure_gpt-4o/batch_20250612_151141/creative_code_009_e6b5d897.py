"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bsclayer.com
Prompt: Write code to subscribe to live blockchain events on Binance Smart Chain using BSC Layer APIs.
Generated: DETERMINISTIC_e6b5d89758aa1c2c
Batch ID: 20250612_151141
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

# Binance Smart Chain WebSocket endpoint for live events
BSC_WEB_SOCKET_URL = "wss://bsc.getblock.io/mainnet/?api_key=YOUR_API_KEY"

# Subscribe to blockchain events
async def subscribe_to_bsc_events():
    """
    Connects to Binance Smart Chain WebSocket endpoint and listens to live blockchain events.
    """
    try:
        async with websockets.connect(BSC_WEB_SOCKET_URL) as websocket:
            print("Connected to Binance Smart Chain WebSocket endpoint.")

            # Create the subscription payload
            subscription_payload = {
                "jsonrpc": "2.0",
                "method": "eth_subscribe",
                "params": ["newHeads"],  # Subscribe to new block headers
                "id": 1
            }

            # Send subscription request
            await websocket.send(json.dumps(subscription_payload))
            print("Subscription request sent.")

            # Handle the subscription confirmation response
            response = await websocket.recv()
            response_data = json.loads(response)
            if "result" in response_data:
                subscription_id = response_data["result"]
                print(f"Subscribed successfully! Subscription ID: {subscription_id}")
            else:
                print("Failed to subscribe. Response:", response_data)
                return
            
            # Listen for incoming blockchain events
            print("Listening for new block headers...")
            while True:
                try:
                    event = await websocket.recv()
                    event_data = json.loads(event)
                    print("Received new block header event:", event_data)
                except json.JSONDecodeError:
                    print("Error decoding incoming event.")
                except Exception as e:
                    print(f"Error handling event: {e}")
                    break

    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed unexpectedly: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    print("Starting Binance Smart Chain event listener...")
    try:
        asyncio.run(subscribe_to_bsc_events())
    except KeyboardInterrupt:
        print("Program interrupted manually. Exiting...")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

**Note:**
1. Replace `"YOUR_API_KEY"` with your actual API key obtained from the Binance Smart Chain provider like GetBlock.
2. Make sure you have the `websockets` Python package installed (`pip install websockets`).
3. This code subscribes to new block headers (`newHeads`) as an example event; you can modify the `params` field to subscribe to other types of events.
