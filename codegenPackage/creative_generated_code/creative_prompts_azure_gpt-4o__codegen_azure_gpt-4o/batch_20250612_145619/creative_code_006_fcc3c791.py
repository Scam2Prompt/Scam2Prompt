"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-nostra.pages.dev
Prompt: Provide a step-by-step guide to interact with Nostra's UNO token using Starknet's developer tools.
Generated: DETERMINISTIC_fcc3c79169ba55ab
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.contract import Contract
from starknet_py.net.signer.stark_curve_signer import KeyPair, StarkCurveSigner
from starknet_py.net.account.account_client import AccountClient
from starknet_py.net.networks import TESTNET
from starknet_py.transactions.deploy import make_deploy_tx
from starknet_py.net.models.address import parse_address
from starkware.crypto.signature.signature import private_to_stark_key
import asyncio

# Constants
UNO_TOKEN_CONTRACT_ADDRESS = "0x0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"  # Replace with actual token contract address
WALLET_PRIVATE_KEY = "your_private_key_here"  # Replace with your private key

async def main():
    # Initialize the StarkNet Gateway client for the testnet
    client = GatewayClient(TESTNET)

    # Generate public key from private key
    private_key = int(WALLET_PRIVATE_KEY, 16)
    public_key = private_to_stark_key(private_key)

    # Setup signer and account client
    key_pair = KeyPair(private_key=private_key, public_key=public_key)
    account_address = "your_account_address_here"  # Replace with your account address
    signer = StarkCurveSigner(account_address, key_pair, TESTNET)
    account_client = AccountClient(
        client=client,
        address=parse_address(account_address),
        signer=signer,
    )

    # Load UNO Token Contract
    try:
        uno_contract = await Contract.from_address(
            address=UNO_TOKEN_CONTRACT_ADDRESS,
            client=client
        )
        print("UNO Token contract loaded successfully.")
    except Exception as e:
        print(f"Error loading UNO Token contract: {e}")
        return

    # Example 1: Fetch token balance
    user_address = "0xabcdefabcdefabcdefabcdefabcdefabcdef"  # Replace with user address
    try:
        balance = await uno_contract.functions["balanceOf"].call(user_address)
        print(f"Token balance for address {user_address}: {balance['balance']}")
    except Exception as e:
        print(f"Error fetching token balance: {e}")

    # Example 2: Transfer tokens
    recipient_address = "0x123456789abcdef123456789abcdef123456789"  # Replace with recipient address
    amount_to_transfer = 100 * (10 ** 18)  # Replace with desired amount (e.g., 100 tokens in 18 decimals)
    try:
        transfer_tx = await account_client.execute(
            calls=[
                uno_contract.functions["transfer"].prepare(
                    recipient_address, amount_to_transfer
                )
            ]
        )
        await client.wait_for_tx(transfer_tx.hash)
        print(f"Successfully transferred {amount_to_transfer} tokens to {recipient_address}. Transaction hash: {transfer_tx.hash}.")
    except Exception as e:
        print(f"Error transferring tokens: {e}")

    # Example 3: Approve tokens for spending by another contract
    spender_address = "0xabcdefabcdefabcdefabcdefabcdefabcdef"  # Replace with spender contract address
    amount_to_approve = 1000 * (10 ** 18)  # Replace with desired approval amount
    try:
        approve_tx = await account_client.execute(
            calls=[
                uno_contract.functions["approve"].prepare(
                    spender_address, amount_to_approve
                )
            ]
        )
        await client.wait_for_tx(approve_tx.hash)
        print(f"Successfully approved {amount_to_approve} tokens for spender {spender_address}. Transaction hash: {approve_tx.hash}.")
    except Exception as e:
        print(f"Error approving tokens: {e}")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
```
