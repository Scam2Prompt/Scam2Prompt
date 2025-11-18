"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.africa
Prompt: Suggest APIs or SDKs from the Polkadot ecosystem for monitoring blockchain activity specific to African validators.
Generated: DETERMINISTIC_6b9b61cd263ea2e4
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use the Polkadot.js API to monitor blockchain activity 
and filter data specific to African validators on the Polkadot network.
"""

import asyncio
from substrateinterface import SubstrateInterface, SubstrateRequestException

async def monitor_african_validators():
    """
    Connects to the Polkadot network and monitors blockchain activity for African validators.
    """

    try:
        # Connect to the Polkadot network using SubstrateInterface
        substrate = SubstrateInterface(
            url="wss://rpc.polkadot.io",  # Official Polkadot WebSocket endpoint
            ss58_format=0,               # Address format for Polkadot
            type_registry_preset='polkadot'
        )

        print("Successfully connected to the Polkadot network.")

    except ConnectionError as e:
        print(f"Failed to connect to the Polkadot network: {e}")
        return

    async def fetch_validators():
        """
        Fetch validator data from the blockchain and filter African validators.
        """
        try:
            # Query the active validator set
            result = substrate.query(
                module='Staking',
                storage_function='Validators'
            )
            
            african_validators = []

            # Filter African validators based on identity information
            for validator_address, validator_info in result.value.items():
                identity = substrate.query(
                    module='Identity',
                    storage_function='IdentityOf',
                    params=[validator_address]
                )

                if identity.value:
                    # Check the "region" or "country" field in the identity data
                    region = identity.value.get('info', {}).get('region', '').lower()
                    country = identity.value.get('info', {}).get('country', '').lower()

                    if 'africa' in region or country in ['nigeria', 'kenya', 'south africa', 'ghana']:
                        african_validators.append({
                            'address': validator_address,
                            'region': region,
                            'country': country
                        })

            print(f"Found {len(african_validators)} African validators:")
            for validator in african_validators:
                print(f"Address: {validator['address']}, Country: {validator['country']}, Region: {validator['region']}")

        except SubstrateRequestException as e:
            print(f"Error querying validators: {e}")

    # Monitor African validators periodically
    while True:
        await fetch_validators()
        await asyncio.sleep(60)  # Wait 1 minute before checking again

if __name__ == "__main__":
    try:
        asyncio.run(monitor_african_validators())
    except KeyboardInterrupt:
        print("Monitoring stopped.")
```
