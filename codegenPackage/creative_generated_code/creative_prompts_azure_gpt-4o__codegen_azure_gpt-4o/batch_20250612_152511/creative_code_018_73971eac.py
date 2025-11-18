"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanetworks.pages.dev
Prompt: How can I use LavaSDK to query block details from the Juno blockchain? Provide a code example.
Generated: DETERMINISTIC_73971eac352c519c
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary libraries
import asyncio
from lavasdk import LavaSDK

# Define an asynchronous function to query block details
async def query_block_details(chain_id: str, block_height: int):
    """
    Queries block details from the Juno blockchain using LavaSDK.

    Parameters:
        chain_id (str): The chain ID of the target blockchain (e.g., 'juno-1').
        block_height (int): The height of the block to query.

    Returns:
        dict: Block details if successful, or None if an error occurs.
    """
    try:
        # Initialize LavaSDK with the specified chain ID
        lava = LavaSDK(chain_id=chain_id)

        # Construct the query parameters
        query_endpoint = "/cosmos/base/tendermint/v1beta1/blocks/{}".format(block_height)

        # Execute the query
        response = await lava.rpc_call(endpoint=query_endpoint)

        # Return the block details
        return response
    except Exception as e:
        # Handle any errors that occur during the query
        print(f"Error querying block details: {e}")
        return None

# Entry point for the script
if __name__ == "__main__":
    # Define the chain ID and block height to query
    chain_id = "juno-1"  # Juno blockchain's mainnet chain ID
    block_height = 1000  # Example block height

    # Run the query asynchronously
    block_details = asyncio.run(query_block_details(chain_id, block_height))

    # Print the retrieved block details
    if block_details:
        print("Block Details:", block_details)
    else:
        print("Failed to retrieve block details.")
```
