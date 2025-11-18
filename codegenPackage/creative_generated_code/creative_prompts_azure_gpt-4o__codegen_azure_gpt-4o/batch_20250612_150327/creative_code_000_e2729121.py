"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disperse-starknet.vercel.app
Prompt: Write a Python script to interact with the "Disperse StarkNet" tool for distributing tokens using the StarkNet blockchain. Include wallet connection functionality as described in the GitHub repository.
Generated: DETERMINISTIC_e27291215d672534
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse
import asyncio
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.signer.stark_curve_signer import KeyPair, StarkCurveSigner
from starknet_py.net.account.account import Account
from starknet_py.contract import Contract
from starknet_py.transaction_exceptions import TransactionFailed

# Constants
DISPERSE_CONTRACT_ADDRESS = "0x..."  # Replace with the actual Disperse contract address
STARKNET_NETWORK = "mainnet"  # Use "testnet" for the testnet environment

# Helper function to load private key
def load_private_key(file_path: str) -> str:
    """
    Load the private key from a given file.
    The file should contain the private key as a string.
    """
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Private key file not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error loading private key: {str(e)}")

# Connect to StarkNet
async def connect_to_starknet(private_key: str, address: str) -> Account:
    """
    Connect to the StarkNet blockchain using the provided private key and account address.
    """
    try:
        client = GatewayClient(net=STARKNET_NETWORK)
        key_pair = KeyPair.from_private_key(private_key)
        signer = StarkCurveSigner(
            account_address=int(address, 16), key_pair=key_pair, chain_id=STARKNET_NETWORK
        )
        account = Account(
            address=int(address, 16),
            client=client,
            signer=signer,
        )
        return account
    except Exception as e:
        raise Exception(f"Error connecting to StarkNet: {str(e)}")

# Disperse tokens
async def disperse_tokens(
    account: Account, recipients: list, amounts: list, token_address: str
):
    """
    Distributes tokens to multiple recipients using the Disperse contract.

    Parameters:
    - account: Account object representing the user's wallet.
    - recipients: A list of recipient addresses.
    - amounts: A list of token amounts corresponding to each recipient.
    - token_address: The address of the token to be dispersed.
    """
    try:
        disperse_contract = await Contract.from_address(
            DISPERSE_CONTRACT_ADDRESS, account.client
        )

        # Prepare the invocation of the disperse function
        call = disperse_contract.functions["disperse_tokens"].prepare(
            token_address=int(token_address, 16),
            recipients=[int(addr, 16) for addr in recipients],
            amounts=amounts,
        )

        # Execute the transaction
        tx = await account.execute(call, max_fee=int(1e16))  # Adjust max_fee as needed
        await account.client.wait_for_tx(tx.transaction_hash)

        print(f"Transaction successful: {tx.transaction_hash}")
    except TransactionFailed as tf:
        raise Exception(f"Transaction failed: {str(tf)}")
    except Exception as e:
        raise Exception(f"Error during token dispersion: {str(e)}")

# Entry point
async def main():
    parser = argparse.ArgumentParser(
        description="Distribute tokens using the Disperse StarkNet tool."
    )
    parser.add_argument(
        "--private_key_file",
        required=True,
        help="Path to the private key file for your StarkNet wallet.",
    )
    parser.add_argument(
        "--address",
        required=True,
        help="Your StarkNet wallet address.",
    )
    parser.add_argument(
        "--token_address",
        required=True,
        help="Address of the token to be distributed.",
    )
    parser.add_argument(
        "--recipients",
        required=True,
        nargs="+",
        help="List of recipient addresses.",
    )
    parser.add_argument(
        "--amounts",
        required=True,
        nargs="+",
        type=int,
        help="List of amounts corresponding to each recipient address.",
    )
    args = parser.parse_args()

    if len(args.recipients) != len(args.amounts):
        raise ValueError("Mismatch: Number of recipients must equal number of amounts.")

    # Load the private key
    private_key = load_private_key(args.private_key_file)

    # Connect to StarkNet
    account = await connect_to_starknet(private_key, args.address)

    # Disperse tokens
    await disperse_tokens(account, args.recipients, args.amounts, args.token_address)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"Error: {str(error)}")
```
