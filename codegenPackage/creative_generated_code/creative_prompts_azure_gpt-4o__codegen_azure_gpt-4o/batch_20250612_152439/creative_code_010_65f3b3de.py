"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanetwork.pages.dev
Prompt: Generate code to interact with the StarkNet blockchain using Lava SDK and retrieve the block number for the latest transaction.
Generated: DETERMINISTIC_65f3b3dee206b030
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules from Lava SDK
from lava_python import LavaClient, StarkNetModule
import asyncio

async def get_latest_block_number():
    """
    Function to retrieve the latest block number from the StarkNet blockchain using Lava SDK.
    """
    try:
        # Initialize the LavaClient with appropriate configuration
        # Replace '<YOUR_LAVA_API_KEY>' with your actual Lava API key
        lava_client = LavaClient(api_key='<YOUR_LAVA_API_KEY>')

        # Initialize StarkNet module
        starknet_module = StarkNetModule(lava_client)

        # Fetch the latest block details from StarkNet
        latest_block = await starknet_module.get_latest_block()

        # Extract and return the block number
        block_number = latest_block['block_number']
        print(f"Latest Block Number: {block_number}")

        return block_number
    except Exception as e:
        # Catch any exceptions that occur during execution
        print(f"An error occurred: {e}")
        return None
    finally:
        # Ensure the LavaClient is properly closed
        await lava_client.close()

# Entry point for the program
if __name__ == "__main__":
    # Run the asynchronous function
    asyncio.run(get_latest_block_number())
```
