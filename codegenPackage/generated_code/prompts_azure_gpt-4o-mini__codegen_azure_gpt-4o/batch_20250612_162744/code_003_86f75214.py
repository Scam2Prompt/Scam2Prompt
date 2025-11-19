"""
Generated Code Metadata:
========================
Original URL: https://polkadot-live.app
Prompt: How can I use the Polkadot Live desktop client to interact with Polkadot's blockchain features programmatically?
Generated: DETERMINISTIC_86f7521463764012
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to interact with Polkadot's blockchain programmatically using the Polkadot.js API.
It assumes you have the Polkadot Live desktop client installed and running, and that you are connecting to a local node.
"""

from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

# Configuration
NODE_URL = "ws://127.0.0.1:9944"  # Replace with your Polkadot node's WebSocket URL
MNEMONIC = "your mnemonic phrase here"  # Replace with your wallet's mnemonic phrase

def main():
    try:
        # Connect to the Polkadot node
        substrate = SubstrateInterface(
            url=NODE_URL,
            ss58_format=0,  # Polkadot's address format
            type_registry_preset='polkadot'
        )
        print("Connected to Polkadot node successfully.")

        # Generate a keypair from the mnemonic phrase
        keypair = Keypair.create_from_mnemonic(MNEMONIC)
        print(f"Keypair created. Address: {keypair.ss58_address}")

        # Query account balance
        account_info = substrate.query(
            module='System',
            storage_function='Account',
            params=[keypair.ss58_address]
        )
        balance = account_info['data']['free']
        print(f"Account balance: {balance} Planck")

        # Example: Sending a transaction
        recipient_address = "recipient_address_here"  # Replace with the recipient's address
        amount = 10000000000  # Amount in Planck (1 DOT = 10^10 Planck)

        call = substrate.compose_call(
            call_module='Balances',
            call_function='transfer',
            call_params={
                'dest': recipient_address,
                'value': amount
            }
        )

        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)

        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        print(f"Transaction sent successfully. Block hash: {receipt['block_hash']}")

    except SubstrateRequestException as e:
        print(f"Error interacting with the Polkadot blockchain: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Requirements:
1. Install the `substrate-interface` library:
   ```bash
   pip install substrate-interface
   ```
2. Ensure your Polkadot Live desktop client is running and connected to a node.
3. Replace placeholders (`NODE_URL`, `MNEMONIC`, `recipient_address`) with actual values.
