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
import asyncio
from lava_sdk import StarkNet, exceptions

async def get_latest_block_number():
    """
    Connects to the StarkNet blockchain using Lava SDK to retrieve the latest block number.

    Returns:
        int: The latest block number.
    """
    try:
        # Initialize the StarkNet client
        client = StarkNet()

        # Fetch the latest block
        latest_block = await client.get_block()

        # Return the block number from the latest block
        return latest_block['block_number']

    except exceptions.NetworkError as e:
        print(f"Network error occurred: {e}")
        return None
    except exceptions.ApiError as e:
        print(f"API error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Entry point for the script
if __name__ == "__main__":
    # Run the async function using asyncio
    latest_block_number = asyncio.run(get_latest_block_number())
    
    if latest_block_number is not None:
        print(f"The latest block number is: {latest_block_number}")
    else:
        print("Failed to retrieve the latest block number.")
```
