"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-disperse.vercel.app
Prompt: Provide an example of a token distribution script using Starknet Disperse.
Generated: DETERMINISTIC_99d50256bf999d4c
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Starknet Token Distribution Script using Disperse
# This script distributes ERC20 tokens to multiple recipients using the Disperse contract.
# Ensure you have Python 3.9+ and the required libraries installed before running.
# pip install starknet.py

from starknet_py.net import AccountClient, KeyPair, StarknetChainId
from starknet_py.net.client import Client
from starknet_py.contract import Contract
from starknet_py.net.models import Address
from starknet_py.transaction_errors import TransactionError

# Constants
DISPERSE_CONTRACT_ADDRESS = "0x0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"  # Replace with actual contract address.
TOKEN_CONTRACT_ADDRESS = "0xFEDCBA9876543210FEDCBA9876543210FEDCBA9876543210FEDCBA9876543210"  # Replace with the token's contract address.
PRIVATE_KEY = "0xYOUR_PRIVATE_KEY_HERE"  # Replace with your private key.
ACCOUNT_ADDRESS = "0xYOUR_ACCOUNT_ADDRESS_HERE"  # Replace with your Account address.
CHAIN_ID = StarknetChainId.TESTNET  # Use StarknetChainId.MAINNET for mainnet.

# Recipients and amounts
RECIPIENTS = [
    {"address": "0x1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF", "amount": 1000},
    {"address": "0xFEDCBA0987654321FEDCBA0987654321FEDCBA0987654321FEDCBA0987654321", "amount": 500},
    {"address": "0x1111111111111111111111111111111111111111111111111111111111111111", "amount": 250},
]

async def distribute_tokens():
    """
    Distributes tokens using the Disperse contract.

    This script assumes:
    - The sender has enough balance of the ERC20 token to cover all distributions.
    - The sender has sufficient Starknet tokens to pay for transaction fees.
    """
    try:
        # Initialize the client
        key_pair = KeyPair.from_private_key(int(PRIVATE_KEY, 16))
        client = AccountClient(
            address=Address.from_hex(ACCOUNT_ADDRESS),
            key_pair=key_pair,
            chain=CHAIN_ID,
        )

        # Fetch Disperse contract
        disperse_contract = await Contract.from_address(DISPERSE_CONTRACT_ADDRESS, client)

        # Prepare calldata
        token_address = int(TOKEN_CONTRACT_ADDRESS, 16)
        recipient_addresses = [int(r["address"], 16) for r in RECIPIENTS]
        amounts = [r["amount"] for r in RECIPIENTS]

        # Call distributeTokens function
        tx_execution = await disperse_contract.functions["distributeTokens"].invoke(
            token_address, recipient_addresses, amounts,
            max_fee=int(1e16)  # Replace with appropriate fee
        )

        print(f"Transaction sent. Hash: {tx_execution.hash}")
        await tx_execution.wait_for_acceptance()
        print("Transaction was successfully accepted on-chain.")

    except TransactionError as e:
        print(f"Transaction failed: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Run the script
if __name__ == "__main__":
    import asyncio
    asyncio.run(distribute_tokens())
```
