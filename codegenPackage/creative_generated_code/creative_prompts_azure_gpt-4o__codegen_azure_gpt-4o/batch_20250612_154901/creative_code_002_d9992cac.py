"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensys-demos.vercel.app
Prompt: Provide code to subscribe to an Ethereum address and receive notifications for transactions using the Infura API.
Generated: DETERMINISTIC_d9992cacf3f62117
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import json
import websockets

# Constants
INFURA_PROJECT_ID = "your-infura-project-id"  # Replace with your Infura project ID
ETHEREUM_ADDRESS_TO_MONITOR = "0xYourEthereumAddress"  # Replace with the Ethereum address to monitor

# Infura WebSocket endpoint
INFURA_WS_URL = f"wss://mainnet.infura.io/ws/v3/{INFURA_PROJECT_ID}"

async def subscribe_to_address(address):
    """
    Subscribes to real-time events for a particular Ethereum address using the Infura WebSocket API.
    """
    try:
        async with websockets.connect(INFURA_WS_URL) as websocket:
            # Construct the subscription payload to monitor transactions involving the address
            subscription_payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "eth_subscribe",
                "params": ["logs", {"address": address}]
            }
            
            # Send the subscription request
            await websocket.send(json.dumps(subscription_payload))
            response = await websocket.recv()
            subscription_response = json.loads(response)

            # Check for subscription success
            if "result" not in subscription_response:
                raise Exception(f"Subscription failed: {subscription_response}")

            print(f"Subscribed successfully. Subscription ID: {subscription_response['result']}")

            # Listen for events
            while True:
                try:
                    message = await websocket.recv()
                    event = json.loads(message)
                    
                    # Handle incoming logs (event data)
                    if "params" in event and "result" in event["params"]:
                        print(f"Transaction notification received: {json.dumps(event['params']['result'], indent=2)}")
                except json.JSONDecodeError:
                    print(f"Received malformed message: {message}")
                except Exception as e:
                    print(f"Error while processing message: {str(e)}")

    except websockets.exceptions.ConnectionClosedError as e:
        print(f"WebSocket connection closed: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Entry point
if __name__ == "__main__":
    print(f"Starting subscription to Ethereum address: {ETHEREUM_ADDRESS_TO_MONITOR}")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(subscribe_to_address(ETHEREUM_ADDRESS_TO_MONITOR))
```

### Notes:
1. Replace `your-infura-project-id` and `0xYourEthereumAddress` with appropriate values.
2. Ensure that the `websockets` library is installed (`pip install websockets`).
3. Use appropriate logging mechanisms for production-grade applications instead of `print` statements.
