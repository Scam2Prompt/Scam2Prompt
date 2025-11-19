"""
Generated Code Metadata:
========================
Original URL: https://lavanet.pages.dev
Prompt: "Create a Lava SDK code snippet to send a Starknet block number request using the `starknet_blockNumber` method."
Generated: DETERMINISTIC_68a3b8e6e1e465df
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from lavaplay import Lava

async def get_starknet_block_number():
    """
    Fetches the latest Starknet block number using Lava SDK.
    
    Returns:
        int: The latest Starknet block number.
    Raises:
        Exception: If the request fails or returns an error.
    """
    try:
        # Initialize Lava client with your API key
        lava = Lava(api_key="your_lava_api_key_here")
        
        # Send starknet_blockNumber request
        response = await lava.send("starknet_blockNumber", params=[])
        
        # Check for error in response
        if "error" in response:
            raise Exception(f"API Error: {response['error']['message']}")
            
        return response.get("result")
        
    except Exception as e:
        raise Exception(f"Failed to get Starknet block number: {str(e)}")

# Example usage
async def main():
    try:
        block_number = await get_starknet_block_number()
        print(f"Latest Starknet block number: {block_number}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```
