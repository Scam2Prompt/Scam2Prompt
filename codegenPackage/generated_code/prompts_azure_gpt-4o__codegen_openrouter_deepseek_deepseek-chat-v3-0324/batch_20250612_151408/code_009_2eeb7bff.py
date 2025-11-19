"""
Generated Code Metadata:
========================
Original URL: https://polkadot.africa
Prompt: Generate a script to connect to the Polkadot network and retrieve information about parachains operating in Africa.
Generated: DETERMINISTIC_2eeb7bffd862d4cd
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from substrateinterface import SubstrateInterface
from substrateinterface.exceptions import SubstrateRequestException

async def get_africa_parachains():
    """
    Connects to the Polkadot network and retrieves parachains operating in Africa.
    """
    try:
        # Connect to Polkadot network
        substrate = SubstrateInterface(
            url="wss://rpc.polkadot.io",
            type_registry_preset='polkadot'
        )
        
        print("Connected to Polkadot network successfully")
        
        # Get current parachains
        parachains = substrate.query(
            module='Paras',
            storage_function='Parachains',
            params=[]
        )
        
        if not parachains:
            print("No parachains found")
            return []
        
        print(f"Found {len(parachains)} parachains")
        
        africa_parachains = []
        
        # Check each parachain for Africa-related information
        for para_id in parachains:
            # Get parachain metadata
            metadata = substrate.query(
                module='Paras',
                storage_function='ParaLifecycles',
                params=[para_id]
            )
            
            # In a real implementation, you would check metadata for Africa-related info
            # This is a placeholder for the actual Africa detection logic
            # You might check for specific on-chain data, geolocation tags, etc.
            if metadata and "Africa" in str(metadata):
                africa_parachains.append({
                    'para_id': para_id,
                    'metadata': metadata
                })
        
        return africa_parachains
        
    except SubstrateRequestException as e:
        print(f"Error connecting to Polkadot network: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
    finally:
        if 'substrate' in locals():
            substrate.close()

async def main():
    africa_parachains = await get_africa_parachains()
    if africa_parachains:
        print("\nParachains operating in Africa:")
        for chain in africa_parachains:
            print(f"Parachain ID: {chain['para_id']}")
            print(f"Metadata: {chain['metadata']}\n")
    else:
        print("No parachains operating in Africa found")

if __name__ == "__main__":
    asyncio.run(main())
```
