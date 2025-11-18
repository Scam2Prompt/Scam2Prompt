"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-git-update-doc-419labs.vercel.app
Prompt: Write Python code to interact with a DeFi project running on StarkNet Layer 2, using APIs or tools mentioned in the StarkNet ecosystem documentation.
Generated: DETERMINISTIC_b78a3cb2f8e01d99
Batch ID: 20250612_145430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.client_models import Call
from starknet_py.net.signer.stark_curve_signer import StarkCurveSigner
from starknet_py.net.account.account_client import AccountClient
from starknet_py.net.models import StarknetChainId
from starknet_py.contract import Contract
from starknet_py.net.networks import MAINNET, TESTNET

# Define constants
PRIVATE_KEY = "your_private_key_here"  # Replace with your private key
ACCOUNT_ADDRESS = "your_account_address_here"  # Replace with your account address
CONTRACT_ADDRESS = "deployed_contract_address_here"  # Replace with the DeFi contract address
NETWORK = TESTNET  # Change to MAINNET for production use
CHAIN_ID = StarknetChainId.TESTNET  # Change to StarknetChainId.MAINNET for production use

async def main():
    # Initialize GatewayClient for network interaction
    client = GatewayClient(net=NETWORK)

    # Create a signer with private key and chain ID
    signer = StarkCurveSigner(
        account_address=ACCOUNT_ADDRESS,
        key_pair=(int(PRIVATE_KEY, 16),),
        chain_id=CHAIN_ID
    )

    # Initialize the account with signer and client
    account = AccountClient(
        address=ACCOUNT_ADDRESS,
        client=client,
        signer=signer
    )

    # Fetch the contract
    contract = await Contract.from_address(CONTRACT_ADDRESS, client)

    # Example function call to interact with the DeFi contract
    try:
        # Replace "function_name" and "function_args" with actual function details
        call = Call(
            to_addr=CONTRACT_ADDRESS,
            selector=contract.functions["function_name"].get_selector(),
            calldata=[arg1, arg2]  # Add appropriate arguments
        )
        
        # Execute the call
        result = await account.execute(call)
        
        # Log transaction hash for debugging
        print(f"Transaction sent successfully. Tx Hash: {result.transaction_hash}")
    except Exception as e:
        # Catch and log any errors
        print(f"An error occurred: {e}")

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
```
