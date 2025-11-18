"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanet.pages.dev
Prompt: Provide a code example that demonstrates how to use LavaSDK to connect to multiple blockchain networks, including Avalanche, Axelar, and StarkNet.
Generated: DETERMINISTIC_5981723e8a3667a5
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
from lav_sdk import LavaSDK, Network

# Initialize the LavaSDK client
lava_sdk = LavaSDK()

async def connect_to_networks():
    try:
        # Define the networks to connect to
        networks = {
            'avalanche': Network.AVALANCHE,
            'axelar': Network.AXELAR,
            'starknet': Network.STARKNET
        }

        # Create a connection to each network
        for name, network in networks.items():
            print(f"Connecting to {name} network...")
            connection = await lava_sdk.connect(network)
            print(f"Successfully connected to {name} network: {connection}")

            # Optionally perform a simple operation on the network
            # For example, we could get the network height or balance
            result = await connection.get_network_height()
            print(f"{name.capitalize()} network height: {result}")

            # Disconnect when done
            await lava_sdk.disconnect(connection)
            print(f"Disconnected from {name} network.")

    except Exception as e:
        # Handle any exceptions that occur during connection
        print(f"An error occurred while connecting to the networks: {str(e)}")

if __name__ == "__main__":
    # Run the asynchronous connection function
    asyncio.run(connect_to_networks())
```

### Requirements:
- Ensure that `lav_sdk` is installed and correctly configured in your environment. 
- Adjust the code if necessary based on the actual API provided by LavaSDK, as this is a hypothetical example.
