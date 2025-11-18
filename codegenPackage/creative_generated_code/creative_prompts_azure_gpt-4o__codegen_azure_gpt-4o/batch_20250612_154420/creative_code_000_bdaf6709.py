"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadotindia.org
Prompt: Write a Python script to interact with the Polkadot blockchain, specifically demonstrating how to nominate and receive staking rewards using Polkadot's Ledger Live integration.
Generated: DETERMINISTIC_bdaf6709c8dc1ec4
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
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

# Configuration
POLKADOT_NODE_URL = "wss://rpc.polkadot.io"
MNEMONIC = "your_12_or_24_word_mnemonic_phrase_here"
NOMINATION_TARGETS = ["TargetStashAddress1", "TargetStashAddress2"]  # Replace with real stash addresses

async def main():
    try:
        # Connect to Polkadot blockchain node
        substrate = SubstrateInterface(
            url=POLKADOT_NODE_URL,
            ss58_format=0,  # Polkadot uses ss58_format=0
            type_registry_preset='polkadot'
        )
        print("Connected to Polkadot blockchain!")

        # Generate keypair from mnemonic
        keypair = Keypair.create_from_mnemonic(MNEMONIC)
        print(f"Keypair generated for address: {keypair.ss58_address}")

        # Get account balance
        account_info = substrate.query("System", "Account", params=[keypair.ss58_address])
        balance = int(account_info['data']['free']) / 10**12  # Convert balance from Planck to DOT
        print(f"Account balance: {balance} DOT")

        # Prepare nomination extrinsic
        call = substrate.compose_call(
            call_module='Staking',
            call_function='nominate',
            call_params={
                'targets': NOMINATION_TARGETS
            }
        )

        # Create signed extrinsic
        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)

        # Submit extrinsic
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        print(f"Extrinsic submitted successfully: {receipt.extrinsic_hash}")
        print(f"Block hash: {receipt.block_hash}")

        # Fetch staking rewards (optional demonstration)
        staking_rewards = substrate.query("Staking", "Stakers", params=[keypair.ss58_address])
        print(f"Staking rewards: {staking_rewards}")

    except SubstrateRequestException as e:
        print(f"Error interacting with the Polkadot blockchain: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Close connection
        substrate.close()

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
```

### Notes:
- Replace `MNEMONIC` with your actual Polkadot wallet mnemonic.
- Replace `NOMINATION_TARGETS` with the stash addresses of validators you wish to nominate.
- This script uses the `substrate-interface` library, which you can install via pip (`pip install substrate-interface`).
- Make sure to handle your mnemonic securely and avoid hardcoding it in production environments.
