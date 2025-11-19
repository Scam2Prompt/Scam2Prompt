"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.house
Prompt: What libraries are recommended for integrating with StarkNet's blockchain?
Generated: DETERMINISTIC_e9c06b323a4dc394
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to integrate with StarkNet's blockchain using two popular Python libraries:
1. `starknet.py`: A lightweight library for interacting with StarkNet.
2. `starkware`: The official library for low-level StarkNet interactions.

Make sure to install the required dependencies before running the script:
pip install starknet.py starkware-crypto
"""

import asyncio
from starknet_py.net.client import Client
from starknet_py.net.models import InvokeFunction
from starknet_py.net.account.account import Account
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.models import Call
from starknet_py.net.models.transaction import DeployAccountTransaction
from starknet_py.transaction_execution_objects import TransactionExecutionStatus, TransactionExecutionInfo

# Constants
STARKNET_NETWORK = "testnet"  # Use "mainnet" for production
DEPLOYED_CONTRACT_ADDRESS = "0x0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
ACCOUNT_PRIVATE_KEY = "0xYOUR_PRIVATE_KEY_HERE"
ACCOUNT_PUBLIC_KEY = "0xYOUR_PUBLIC_KEY_HERE"

async def main():
    """
    Main function demonstrating basic StarkNet integration tasks:
    - Connecting to StarkNet's testnet
    - Interacting with a deployed contract
    - Sending transactions using an account
    """
    try:
        # Initialize the GatewayClient for interacting with the network
        client = GatewayClient(net=STARKNET_NETWORK)

        # Example: Fetching contract information
        print("Fetching contract data...")
        result = await client.call_contract(
            Call(
                to_addr=DEPLOYED_CONTRACT_ADDRESS,
                selector="get_balance",
                calldata=[],
            )
        )
        print(f"Contract balance: {result}")

        # Example: Sending a transaction (requires an account)
        print("Sending transaction...")
        account = Account(
            client=client,
            address="0xACCOUNT_ADDRESS",
            private_key=int(ACCOUNT_PRIVATE_KEY, 16),
            public_key=int(ACCOUNT_PUBLIC_KEY, 16),
        )

        invoke_function = InvokeFunction(
            contract_address=DEPLOYED_CONTRACT_ADDRESS,
            entry_point_selector="transfer",
            calldata=[...],  # Fill in calldata parameters
        )

        tx_execution_info: TransactionExecutionInfo = await account.execute(invoke_function)
        print(f"Transaction status: {tx_execution_info.status.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function within an asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
```
