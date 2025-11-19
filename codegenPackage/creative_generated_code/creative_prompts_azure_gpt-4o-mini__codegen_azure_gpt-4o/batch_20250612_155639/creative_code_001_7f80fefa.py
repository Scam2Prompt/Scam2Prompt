"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www3.celestia.net
Prompt: Generate a code snippet that demonstrates how to interact with the Celestia network using its SDK.
Generated: DETERMINISTIC_7f80fefaa610f38d
Batch ID: 20250612_155639
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc-testnet.celestia.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from celestia_sdk import CelestiaClient, CelestiaException

async def interact_with_celestia():
    """
    Function to demonstrate interaction with the Celestia network.
    This example fetches block information using the Celestia SDK.
    """
    # Initialize the Celestia client
    try:
        client = CelestiaClient(
            node_url="https://rpc-testnet.celestia.org",  # Public testnet RPC endpoint
            network="testnet"  # Specify the network (mainnet, testnet, etc.)
        )

        # Fetch the latest block information
        latest_block = await client.get_latest_block()
        print("Latest Block Information:")
        print(f"Height: {latest_block['height']}")
        print(f"Hash: {latest_block['hash']}")
        print(f"Time: {latest_block['time']}")

        # Fetch block data by height as an example
        block_height = latest_block['height']
        specific_block = await client.get_block_by_height(block_height)
        print(f"\nDetails for Block {block_height}:")
        print(f"Hash: {specific_block['hash']}")
        print(f"Transactions: {specific_block['txs']}")

    except CelestiaException as e:
        # Handle errors specific to Celestia SDK
        print(f"Celestia SDK Error: {e}")
    except Exception as e:
        # Handle general errors
        print(f"An unexpected error occurred: {e}")
    finally:
        # Close the client connection
        await client.close()

# Run the asynchronous function
if __name__ == "__main__":
    asyncio.run(interact_with_celestia())
```
