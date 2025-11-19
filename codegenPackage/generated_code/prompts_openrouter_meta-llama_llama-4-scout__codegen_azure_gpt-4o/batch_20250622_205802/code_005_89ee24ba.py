"""
Generated Code Metadata:
========================
Original URL: https://starknet-ecosystem-git-update-doc-419labs.vercel.app
Prompt: Create a basic Payment system using StarkNet L2 and its ecosystem tools.
Generated: DETERMINISTIC_89ee24bac19a3fa4
Batch ID: 20250622_205802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payment_system.py

"""
A basic payment system using StarkNet L2 and its ecosystem tools.
This script demonstrates how to interact with StarkNet to send payments between accounts.
"""

import asyncio
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.account.account import Account
from starknet_py.net.models import InvokeFunction
from starknet_py.net.signer.stark_curve_signer import KeyPair, StarkCurveSigner
from starknet_py.contract import Contract

# Constants
STARKNET_NETWORK = "testnet"  # Use "mainnet" for production
PRIVATE_KEY = "0xYOUR_PRIVATE_KEY"  # Replace with your private key
ACCOUNT_ADDRESS = "0xYOUR_ACCOUNT_ADDRESS"  # Replace with your account address
RECIPIENT_ADDRESS = "0xRECIPIENT_ADDRESS"  # Replace with the recipient's address
CONTRACT_ADDRESS = "0xPAYMENT_CONTRACT_ADDRESS"  # Replace with the deployed payment contract address
AMOUNT = 1000  # Amount to transfer

async def main():
    try:
        # Initialize StarkNet client
        client = GatewayClient(net=STARKNET_NETWORK)

        # Initialize account with signer
        key_pair = KeyPair.from_private_key(int(PRIVATE_KEY, 16))
        signer = StarkCurveSigner(ACCOUNT_ADDRESS, key_pair, client)
        account = Account(address=ACCOUNT_ADDRESS, client=client, signer=signer)

        # Load the payment contract
        payment_contract = await Contract.from_address(CONTRACT_ADDRESS, client)

        # Prepare the payment transaction
        invoke_function = InvokeFunction(
            contract_address=CONTRACT_ADDRESS,
            entry_point_selector="transfer",  # Replace with the actual entry point name
            calldata=[int(RECIPIENT_ADDRESS, 16), AMOUNT]
        )

        # Execute the transaction
        response = await account.execute(invoke_function)
        print(f"Transaction sent successfully. Tx hash: {response.transaction_hash}")

        # Wait for transaction confirmation
        await client.wait_for_tx(response.transaction_hash)
        print("Transaction confirmed.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
```
