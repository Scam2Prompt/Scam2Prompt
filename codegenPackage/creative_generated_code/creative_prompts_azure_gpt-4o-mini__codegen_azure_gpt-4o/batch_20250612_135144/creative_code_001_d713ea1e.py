"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disperse-starknet.vercel.app
Prompt: Provide a code snippet for integrating wallet connection with Disperse Starknet.
Generated: DETERMINISTIC_d713ea1e9da31794
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from starknet_py.net.account.account import Account
from starknet_py.net.client import Client
from starknet_py.net.networks import MAINNET
from starknet_py.contract import Contract
from starknet_py.net.models.transaction import InvokeFunction
from starknet_py.exceptions import StarkException

# Constants
WALLET_PRIVATE_KEY = "your_wallet_private_key_here"  # Replace with your wallet's private key
WALLET_ADDRESS = "your_wallet_address_here"  # Replace with your wallet's public address
DISPERSE_CONTRACT_ADDRESS = "disperse_contract_address_here"  # Replace with the Disperse contract address
STARKNET_NETWORK = MAINNET  # Change to TESTNET if you're testing

async def main():
    """
    Main function to connect wallet and interact with Disperse Starknet contract.
    """

    try:
        # Initialize StarkNet client for specified network
        client = Client(STARKNET_NETWORK)

        # Connect wallet using the private key
        wallet = Account(
            address=WALLET_ADDRESS,
            key=WALLET_PRIVATE_KEY,
            chain=STARKNET_NETWORK,
            client=client
        )

        # Load the Disperse contract
        disperse_contract = await Contract.from_address(
            address=DISPERSE_CONTRACT_ADDRESS,
            client=client
        )

        # Example transaction: Disperse tokens to multiple addresses
        recipients = [
            {"address": "recipient_address_1", "amount": 1000},
            {"address": "recipient_address_2", "amount": 2000}
        ]

        # Prepare calldata for the contract's disperse function
        calldata = []
        for recipient in recipients:
            calldata.extend([recipient["address"], recipient["amount"]])

        # Invoke the disperse function
        invoke_transaction = InvokeFunction(
            contract_address=DISPERSE_CONTRACT_ADDRESS,
            entry_point_selector="disperse",
            calldata=calldata
        )

        # Sign and send the transaction using the wallet
        response = await wallet.sign_and_send_transaction(invoke_transaction)

        # Check transaction status
        print(f"Transaction sent with hash: {response.transaction_hash}")

    except StarkException as e:
        # Handle StarkNet-specific errors
        print(f"Error interacting with StarkNet: {e}")
    except Exception as e:
        # Handle general errors
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```
