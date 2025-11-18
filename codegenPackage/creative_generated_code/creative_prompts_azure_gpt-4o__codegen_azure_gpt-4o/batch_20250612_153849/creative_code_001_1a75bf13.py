"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-live.app
Prompt: Generate code to connect to the Polkadot Live desktop client and fetch live updates about the Polkadot network.
Generated: DETERMINISTIC_1a75bf13527422ac
Batch ID: 20250612_153849
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

# Constants for the Polkadot websocket endpoint
POLKADOT_WS_URL = "wss://rpc.polkadot.io"  # Replace this with the correct endpoint if necessary.

async def connect_to_polkadot():
    """
    Connects to the Polkadot WebSocket endpoint and fetches live updates.
    """
    try:
        # Establish WebSocket connection to Polkadot node
        async with websockets.connect(POLKADOT_WS_URL) as websocket:
            print("Connected to Polkadot WebSocket endpoint.")

            # Subscribe to system health updates as a sample request
            subscription_request = {
                "id": 1,
                "jsonrpc": "2.0",
                "method": "system_health",
                "params": []
            }
            
            # Send subscription request
            await websocket.send(json.dumps(subscription_request))
            print("Subscription request sent.")

            # Continuously listen for messages from the WebSocket
            while True:
                try:
                    response = await websocket.recv()
                    parsed_response = json.loads(response)
                    
                    # Print or process the live updates
                    print("Received update:", json.dumps(parsed_response, indent=4))
                except json.JSONDecodeError:
                    print("Failed to parse JSON response.")
                except Exception as e:
                    print(f"Error while receiving data: {e}")

    except websockets.exceptions.ConnectionError as e:
        print(f"WebSocket connection error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Run the asynchronous connection function
    asyncio.run(connect_to_polkadot())
```
