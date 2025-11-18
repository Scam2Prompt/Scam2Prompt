"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot-live.app
Prompt: Provide an example of how to use the Polkadot Live desktop client to query network statistics programmatically.
Generated: DETERMINISTIC_575ec2afc04fe48c
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
Example Python code for querying network statistics using the Polkadot Live desktop client.
This code demonstrates how to connect to the Polkadot network and retrieve basic statistics
like the block number, finalized block, and network health.

Dependencies:
- Install the 'substrate-interface' Python package to interact with the Polkadot network.
  You can install it via pip:
  `pip install substrate-interface`
"""

from substrateinterface import SubstrateInterface, SubstrateRequestException

def query_network_statistics():
    try:
        # Establish connection to a Polkadot node
        # Replace '<NODE_URL>' with the URL of your Polkadot Live desktop client node (e.g., ws://127.0.0.1:9944)
        substrate = SubstrateInterface(
            url="<NODE_URL>",
            ss58_format=0,
            type_registry_preset='polkadot'
        )
        print("Successfully connected to the Polkadot network.")

        # Query latest block number
        latest_block_hash = substrate.get_block_hash()
        latest_block = substrate.get_block(latest_block_hash)
        print(f"Latest Block Number: {latest_block['header']['number']}")

        # Query finalized block number
        finalized_block_hash = substrate.get_finalized_head()
        finalized_block = substrate.get_block(finalized_block_hash)
        print(f"Finalized Block Number: {finalized_block['header']['number']}")

        # Query network health
        network_health = substrate.rpc_request("system_health", [])
        print("Network Health:")
        print(f"Peers Connected: {network_health['peers']}")
        print(f"Is Syncing: {network_health['isSyncing']}")
        print(f"Should Have Peers: {network_health['shouldHavePeers']}")

    except SubstrateRequestException as e:
        print(f"An error occurred while querying the Polkadot network: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Finished querying network statistics.")

if __name__ == "__main__":
    query_network_statistics()
```
