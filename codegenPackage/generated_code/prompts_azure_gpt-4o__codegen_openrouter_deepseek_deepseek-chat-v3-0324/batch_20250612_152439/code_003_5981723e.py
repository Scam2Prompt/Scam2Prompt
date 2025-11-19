"""
Generated Code Metadata:
========================
Original URL: https://lavanet.pages.dev
Prompt: Provide a code example that demonstrates how to use LavaSDK to connect to multiple blockchain networks, including Avalanche, Axelar, and StarkNet.
Generated: DETERMINISTIC_5981723e8a3667a5
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from lavasdk.client import LavaSDK
from lavasdk.exceptions import LavaSDKError

# Initialize LavaSDK with configuration for multiple networks
def initialize_lava_sdk():
    try:
        # Configuration for Avalanche
        avalanche_config = {
            "network": "avalanche",
            "api_key": os.getenv("AVALANCHE_API_KEY"),
            "chain_id": "43114",
            "rpc_url": os.getenv("AVALANCHE_RPC_URL")
        }

        # Configuration for Axelar
        axelar_config = {
            "network": "axelar",
            "api_key": os.getenv("AXELAR_API_KEY"),
            "chain_id": "axelar-dojo-1",
            "rpc_url": os.getenv("AXELAR_RPC_URL")
        }

        # Configuration for StarkNet
        starknet_config = {
            "network": "starknet",
            "api_key": os.getenv("STARKNET_API_KEY"),
            "chain_id": "SN_MAIN",
            "rpc_url": os.getenv("STARKNET_RPC_URL")
        }

        # Initialize clients for each network
        avalanche_client = LavaSDK(avalanche_config)
        axelar_client = LavaSDK(axelar_config)
        starknet_client = LavaSDK(starknet_config)

        return {
            "avalanche": avalanche_client,
            "axelar": axelar_client,
            "starknet": starknet_client
        }

    except LavaSDKError as e:
        print(f"Error initializing LavaSDK: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

# Example usage to query block height from each network
def query_block_heights(clients):
    try:
        # Query Avalanche
        avalanche_height = clients["avalanche"].get_block_height()
        print(f"Avalanche block height: {avalanche_height}")

        # Query Axelar
        axelar_height = clients["axelar"].get_block_height()
        print(f"Axelar block height: {axelar_height}")

        # Query StarkNet
        starknet_height = clients["starknet"].get_block_height()
        print(f"StarkNet block height: {starknet_height}")

    except LavaSDKError as e:
        print(f"Error querying block heights: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Main execution
if __name__ == "__main__":
    try:
        # Initialize clients
        clients = initialize_lava_sdk()
        
        # Query block heights
        query_block_heights(clients)

    except Exception as e:
        print(f"Application error: {e}")
```
