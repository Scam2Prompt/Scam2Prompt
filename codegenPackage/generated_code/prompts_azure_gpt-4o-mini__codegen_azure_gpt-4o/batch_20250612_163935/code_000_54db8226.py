"""
Generated Code Metadata:
========================
Original URL: https://polkadotindia.org
Prompt: Generate a Python script that utilizes Polkadot's governance-allocated parachains for a common-good project, as discussed on Polkadot India.
Generated: DETERMINISTIC_54db8226d26e7287
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to interact with Polkadot's governance-allocated parachains for a common-good project.
This script demonstrates how to query parachain information and submit a proposal for a common-good project.
"""

import asyncio
from substrateinterface import SubstrateInterface, Keypair, SubstrateRequestException

# Constants
POLKADOT_NODE_URL = "wss://rpc.polkadot.io"  # Polkadot node URL
COMMON_GOOD_PROJECT_DESCRIPTION = "Proposal for a common-good project to benefit the Polkadot ecosystem."
PROPOSAL_AMOUNT = 1000  # Amount in DOT for the proposal
MNEMONIC = "your mnemonic phrase here"  # Replace with your wallet's mnemonic phrase

async def main():
    try:
        # Connect to the Polkadot node
        substrate = SubstrateInterface(
            url=POLKADOT_NODE_URL,
            ss58_format=0,  # Polkadot address format
            type_registry_preset='polkadot'
        )
        print("Connected to Polkadot node.")

        # Generate keypair from mnemonic
        keypair = Keypair.create_from_mnemonic(MNEMONIC)
        print(f"Keypair generated for address: {keypair.ss58_address}")

        # Query governance-allocated parachains
        parachains = substrate.query(
            module='Parachains',
            storage_function='Parachains'
        )
        print("Governance-allocated parachains:")
        for parachain in parachains.value:
            print(f"Parachain ID: {parachain}")

        # Submit a proposal for a common-good project
        call = substrate.compose_call(
            call_module='Democracy',
            call_function='propose',
            call_params={
                'proposal_hash': substrate.generate_storage_hash(
                    module='System',
                    storage_function='Account',
                    params=[keypair.ss58_address]
                ),
                'value': PROPOSAL_AMOUNT * 10**10  # Convert DOT to Planck
            }
        )

        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        print(f"Proposal submitted successfully. Extrinsic hash: {receipt.extrinsic_hash}")

    except SubstrateRequestException as e:
        print(f"Error interacting with the Polkadot node: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'substrate' in locals():
            substrate.close()
            print("Connection to Polkadot node closed.")

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
```
