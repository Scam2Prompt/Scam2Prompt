"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet.pages.dev
Prompt: Write a code snippet using LavaSDK to fetch the block details for a specific block number on the Osmosis Mainnet RPC.
Generated: DETERMINISTIC_088b7d4daf1d823e
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries from LavaSDK
from lava_sdk import LavaSDK
import asyncio

async def fetch_block_details(block_number):
    """
    Fetch block details for a specific block number on the Osmosis Mainnet RPC using LavaSDK.

    Args:
        block_number (int): The specific block number to fetch details for.

    Returns:
        dict: The block details if successful.
    """
    try:
        # Initialize LavaSDK client for Osmosis Mainnet RPC
        client = LavaSDK("osmosis-mainnet")

        # Build the query parameters for fetching block details
        query_params = {
            "block": block_number
        }

        # Execute the RPC call to fetch block details
        block_details = await client.request("block", query_params)

        # Return the fetched block details
        return block_details

    except Exception as e:
        # Handle any errors that occur during the RPC call
        print(f"An error occurred while fetching the block details: {e}")
        return None
    finally:
        # Close the SDK client to release resources
        await client.close()

# Main execution block
if __name__ == "__main__":
    # Define the block number to fetch details for
    block_number_to_fetch = 123456  # Replace with the desired block number

    # Run the async function to fetch block details
    asyncio.run(fetch_block_details(block_number_to_fetch))
```
