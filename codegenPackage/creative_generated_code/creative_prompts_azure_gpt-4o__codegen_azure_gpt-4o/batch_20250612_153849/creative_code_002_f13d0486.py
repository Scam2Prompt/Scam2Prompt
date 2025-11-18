"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-live.app
Prompt: Recommend libraries or APIs compatible with the Polkadot Live desktop client for building a custom Polkadot monitoring tool.
Generated: DETERMINISTIC_f13d04867c1da680
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a recommendation for libraries/APIs compatible with the Polkadot Live desktop client
and demonstrates how to connect to the Polkadot network, fetch chain data, and monitor network events using the `polkadot-js/api` library.
"""

# Import required libraries
from substrateinterface import SubstrateInterface, SubstrateRequestException

def fetch_chain_data():
    """
    Connect to the Polkadot network and fetch basic chain information.
    Returns: Dictionary containing chain information.
    """
    try:
        # Connect to the Polkadot network
        substrate = SubstrateInterface(
            url="wss://rpc.polkadot.io",  # Polkadot WebSocket endpoint
            ss58_format=0,               # Default SS58 address format for Polkadot
            type_registry_preset="polkadot"  # Registry preset
        )

        # Fetch chain metadata
        chain_name = substrate.chain
        latest_block = substrate.get_chain_head()
        genesis_hash = substrate.get_genesis_block_hash()

        return {
            "chain_name": chain_name,
            "latest_block": latest_block,
            "genesis_hash": genesis_hash
        }

    except SubstrateRequestException as e:
        # Handle API request exceptions
        print(f"Error fetching chain data: {e}")
        return None

    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")
        return None

def monitor_events():
    """
    Subscribes to Polkadot network events and logs them in real-time.
    """
    try:
        # Connect to the Polkadot network
        substrate = SubstrateInterface(
            url="wss://rpc.polkadot.io",
            ss58_format=0,
            type_registry_preset="polkadot"
        )

        # Callback function to handle events
        def event_callback(event_data):
            print(f"New event: {event_data}")

        # Subscribe to events
        substrate.subscribe_events(event_callback)
    
    except SubstrateRequestException as e:
        print(f"Error during event monitoring: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage of the library
    print("Fetching Polkadot chain data...")
    chain_data = fetch_chain_data()

    if chain_data:
        print(f"Chain Name: {chain_data['chain_name']}")
        print(f"Latest Block: {chain_data['latest_block']}")
        print(f"Genesis Hash: {chain_data['genesis_hash']}")

    print("\nMonitoring Polkadot network events...")
    monitor_events()
```

Note:
- Replace the WebSocket endpoint (`wss://rpc.polkadot.io`) with the appropriate endpoint if using a different Polkadot node or network.
- Install the required library `substrate-interface` using `pip install substrate-interface`.
