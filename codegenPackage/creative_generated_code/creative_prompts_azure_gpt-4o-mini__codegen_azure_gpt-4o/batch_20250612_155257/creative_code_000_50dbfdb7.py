"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-dapp.vercel.app
Prompt: How can I create a decentralized application (dApp) using StarkNet?
Generated: DETERMINISTIC_50dbfdb714014b2f
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a simple example of creating a decentralized application (dApp) using StarkNet written in Python. The code demonstrates deploying and interacting with a basic smart contract using StarkNet's Python SDK (`starknet.py`). Ensure you install the StarkNet Python SDK (`pip install starknet.py`) before running this code.

```python
# Import required modules from StarkNet Python SDK
from starknet_py.contract import Contract
from starknet_py.net.account.account import Account
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import TESTNET
from starknet_py.net.signer.stark_curve_signer import KeyPair, StarkCurveSigner
from starknet_py.net.models import StarknetChainId
from starknet_py.common import create_compiled_contract

# Constants
CONTRACT_PATH = "contract/counter.json"  # Path to compiled Cairo contract
PRIVATE_KEY = "0xYOUR_PRIVATE_KEY"  # Replace with your private key
ACCOUNT_ADDRESS = "0xYOUR_ACCOUNT_ADDRESS"  # Replace with your account address

async def main():
    # Initialize StarkNet client for testnet
    client = GatewayClient(TESTNET)

    # Set up account and signer
    key_pair = KeyPair.from_private_key(PRIVATE_KEY)
    signer = StarkCurveSigner(
        account_address=ACCOUNT_ADDRESS,
        key_pair=key_pair,
        chain_id=StarknetChainId.TESTNET
    )
    account = Account(
        client=client,
        address=ACCOUNT_ADDRESS,
        signer=signer
    )

    # Deploy a smart contract
    with open(CONTRACT_PATH, "r") as file:
        compiled_contract = file.read()

    deployment_transaction = await Contract.deploy(
        account=account,
        compiled_contract=compiled_contract
    )
    print("Deploying contract...")
    await deployment_transaction.wait_for_acceptance()
    contract_address = deployment_transaction.deployed_contract.address
    print(f"Contract deployed at address: {contract_address}")

    # Interact with the contract
    contract = await Contract.from_address(contract_address, client)

    # Call function to get the counter value
    print("Calling contract to get current counter value...")
    counter_value = await contract.functions["get_counter"].call()
    print(f"Counter value: {counter_value}")

    # Invoke function to increment the counter
    print("Sending transaction to increment the counter...")
    invocation = await account.execute(
        calls=[
            {
                "to": contract_address,
                "selector": "increment_counter",
                "calldata": []
            }
        ]
    )
    await invocation.wait_for_acceptance()
    print("Counter incremented successfully.")

    # Verify the counter value after incrementing
    print("Calling contract to verify updated counter value...")
    counter_value_after = await contract.functions["get_counter"].call()
    print(f"Counter value after increment: {counter_value_after}")

# Run the async main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

### Notes:
1. Replace `CONTRACT_PATH`, `PRIVATE_KEY`, and `ACCOUNT_ADDRESS` with your actual values.
2. The above code assumes a compiled Cairo contract (`contract/counter.json`) with `get_counter` and `increment_counter` functions. You'll need to implement the corresponding Cairo contract.
3. For production use, ensure the private key is securely stored and never hard-coded directly into the script.
