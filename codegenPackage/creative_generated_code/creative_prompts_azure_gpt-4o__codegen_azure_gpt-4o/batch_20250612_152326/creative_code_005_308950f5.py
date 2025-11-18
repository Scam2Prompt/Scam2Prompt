"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flow-blockchain.com
Prompt: Provide a code example for subscribing to real-time transaction updates on Flow Blockchain using its event API.
Generated: DETERMINISTIC_308950f53428e38a
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from flow_py_sdk import flow_client, events

# Configuration Constants
ACCESS_NODE_URL = "access.mainnet.nodes.onflow.org:9000"  # Flow Access Node URL (Mainnet)
EVENT_TYPE = "flow.AccountCreated"  # Replace with desired event type
START_BLOCK = 0  # Starting block height (0 for latest block)

async def subscribe_to_events():
    """
    Subscribes to real-time transaction updates for the specified event type on the Flow blockchain.
    Uses Flow's Event API to listen for events, starting from the latest block.
    """
    try:
        # Establish a connection to the Flow Access Node
        async with flow_client.FlowClient(ACCESS_NODE_URL) as client:
            print("Connected to Flow Access Node.")

            # Infinite loop to continuously fetch event updates
            while True:
                # Retrieve the latest block height
                latest_block = await client.get_latest_block(is_sealed=True)
                latest_block_height = latest_block.height

                # Fetch events starting from the START_BLOCK up to the latest block height
                event_results = await events.get_events_for_height_range(
                    client,
                    event_type=EVENT_TYPE,
                    start_height=max(START_BLOCK, latest_block_height - 1),
                    end_height=latest_block_height,
                )

                # Process each event result
                for event in event_results:
                    print(f"Event Found: {event.event_type}")
                    print(f"Transaction ID: {event.transaction_id}")
                    print(f"Values: {event.values}")
                    print("-" * 40)

                # To avoid overwhelming the node, add a small delay before the next request
                await asyncio.sleep(2)

    except Exception as e:
        # Handle any errors gracefully
        print(f"Error occurred: {str(e)}")
    finally:
        print("Event subscription terminated.")

# Entry point
if __name__ == "__main__":
    # Run the asyncio event loop to start the subscription
    asyncio.run(subscribe_to_events())
```
