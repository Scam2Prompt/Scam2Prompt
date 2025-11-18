"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadotindia.org
Prompt: Generate code to query and display data from Polkadot's parachains, emphasizing common-good system and public utility blockchains.
Generated: DETERMINISTIC_2aa0c98be976808c
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from substrateinterface import SubstrateInterface, SubstrateRequestException

async def fetch_parachain_data():
    """
    Fetch and display data about Polkadot's parachains, emphasizing common-good system
    and public utility blockchains.
    """
    try:
        # Establish connection to Polkadot's main relay chain
        substrate = SubstrateInterface(
            url="wss://rpc.polkadot.io",
            ss58_format=0,
            type_registry_preset='polkadot'
        )
        
        print("Connected to Polkadot Network!")

        # Fetch current parachains from storage key
        parachains_key = substrate.get_storage_key(module="Paras", storage_function="CurrentParachains")
        current_parachains = substrate.get_storage(key=parachains_key)
        
        if current_parachains:
            print("\n--- Current Parachains ---")
            for parachain_id in current_parachains:
                print(f"Parachain ID: {parachain_id}")
            
                # Query information about each parachain
                parachain_meta_key = substrate.get_storage_key(module="Paras", storage_function="ParaLifecycle", params=[parachain_id])
                parachain_meta = substrate.get_storage(key=parachain_meta_key)
                
                print(f"Lifecycle Status: {parachain_meta}")
        else:
            print("\nNo parachains currently registered on the network.")
    
    except SubstrateRequestException as e:
        print(f"Substrate request failed: {str(e)}")

    except Exception as ex:
        print(f"An unexpected error occurred: {str(ex)}")

    finally:
        # Clean up resources or connections if needed
        if 'substrate' in locals():
            substrate.close()

# Run the async function
if __name__ == "__main__":
    asyncio.run(fetch_parachain_data())
```
