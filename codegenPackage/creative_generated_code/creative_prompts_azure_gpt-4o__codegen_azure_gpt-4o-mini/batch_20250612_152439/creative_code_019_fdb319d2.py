"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet.pages.dev
Prompt: Write a code snippet using LavaSDK to connect to the Filecoin blockchain and retrieve block data.
Generated: DETERMINISTIC_fdb319d2469806dc
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from lavapool import LavaPool  # Assuming LavaSDK is structured similarly to Lavapool
from lavapool.exceptions import LavaError

async def get_block_data(block_height):
    """
    Connects to the Filecoin blockchain and retrieves block data for the given block height.

    Args:
        block_height (int): The height of the block to retrieve data for.

    Returns:
        dict: A dictionary containing block data.

    Raises:
        ValueError: If block_height is not a positive integer.
        LavaError: If there is an error retrieving block data from the blockchain.
    """
    if not isinstance(block_height, int) or block_height < 0:
        raise ValueError("block_height must be a non-negative integer")

    # Initialize the LavaPool with the appropriate Filecoin network configuration
    lava_pool = LavaPool(network='filecoin-mainnet')

    try:
        # Connect to the blockchain
        await lava_pool.connect()

        # Retrieve block data
        block_data = await lava_pool.get_block(block_height)

        return block_data  # Return the retrieved block data

    except LavaError as e:
        # Handle errors specific to LavaSDK
        print(f"Error retrieving block data: {e}")
        raise  # Re-raise the exception for further handling if necessary

    finally:
        # Ensure the connection is closed after retrieval
        await lava_pool.disconnect()

# Example of running get_block_data in an asynchronous context
if __name__ == "__main__":
    block_height_to_retrieve = 1000  # Example block height
    try:
        block_data = asyncio.run(get_block_data(block_height_to_retrieve))
        print(block_data)  # Print the retrieved block data
    except Exception as e:
        print(f"An error occurred: {e}")
```
