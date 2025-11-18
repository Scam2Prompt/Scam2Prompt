"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.africa
Prompt: Generate a script to connect to the Polkadot network and retrieve information about parachains operating in Africa.
Generated: DETERMINISTIC_2eeb7bffd862d4cd
Batch ID: 20250612_151408
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

# Define the main function
async def main():
    """
    Connect to the Polkadot network and retrieve information about parachains operating in Africa.
    """

    try:
        # Connect to a Polkadot node using Substrate interface
        substrate = SubstrateInterface(
            url="wss://rpc.polkadot.io",  # Public Polkadot WebSocket endpoint
            ss58_format=0,               # Address format for Polkadot
            type_registry_preset="polkadot"
        )

        print("Successfully connected to the Polkadot network.")

        # Query runtime storage for active parachains
        active_parachains = substrate.query(
            module="Paras",
            storage_function="Parachains"
        )

        print("Retrieved list of active parachains.")

        # Filter parachains operating in Africa (Assuming metadata or tags include region info)
        african_parachains = []
        for parachain_id in active_parachains:
            parachain_info = substrate.query(
                module="Paras",
                storage_function="ParaInfo",
                params=[parachain_id]
            )

            # Check if parachain includes "Africa" in metadata or description
            if parachain_info and 'Africa' in parachain_info.value.get('metadata', ''):
                african_parachains.append({
                    "parachain_id": parachain_id,
                    "metadata": parachain_info.value.get('metadata', {})
                })

        # Display the filtered African parachains
        if african_parachains:
            print("Parachains operating in Africa:")
            for parachain in african_parachains:
                print(f"ID: {parachain['parachain_id']}, Metadata: {parachain['metadata']}")
        else:
            print("No parachains found operating in Africa.")

    except SubstrateRequestException as e:
        print(f"Substrate request exception: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the substrate connection
        if substrate:
            substrate.close()
            print("Connection closed.")

# Run the main function in an asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
```
