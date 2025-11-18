"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.eu
Prompt: Provide a Python example for interacting with StarkNet, including querying contract state and sending transactions.
Generated: DETERMINISTIC_8af65150b87f6f78
Batch ID: 20250612_150342
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://alpha-mainnet.starknet.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries from starknet_py
from starknet_py.net import AccountClient, KeyPair, StarknetProvider
from starknet_py.net.networks import MAINNET
from starknet_py.contract import Contract
from starknet_py.utils.crypto.facade import generate_random_private_key
from starknet_py.constants import TRANSACTION_STATUS, DEFAULT_ACCOUNT_CONTRACT

# Configuration
NODE_URL = "https://alpha-mainnet.starknet.io"  # Replace with your StarkNet node URL
ACCOUNT_PRIVATE_KEY = generate_random_private_key()  # Replace with your actual private key
ACCOUNT_ADDRESS = "0x123..."  # Replace with your actual account address
CONTRACT_ADDRESS = "0x456..."  # Replace with your contract address

async def main():
    try:
        # Set up the account client
        key_pair = KeyPair.from_private_key(ACCOUNT_PRIVATE_KEY)
        account_client = AccountClient(
            address=ACCOUNT_ADDRESS,
            key_pair=key_pair,
            provider=StarknetProvider(node_url=NODE_URL),
        )

        # Deploy a contract client
        contract = await Contract.from_address(
            contract_address=CONTRACT_ADDRESS,
            provider=account_client.provider,
        )

        # Query contract data (example: fetching a variable named `get_balance`)
        query_result = await contract.functions["get_balance"].call()
        print(f"Contract Balance: {query_result['amount']}")

        # Send a transaction (example: updating balance using `set_balance`)
        transaction_response = await contract.functions["set_balance"].invoke(
            amount=1000, max_fee=int(1e16)  # Replace with values appropriate for your contract
        )

        # Wait for transaction to be confirmed
        await account_client.provider.wait_for_tx(transaction_response.transaction_hash)
        print(f"Transaction successful! Hash: {transaction_response.transaction_hash}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the async main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```
