"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-disperse.vercel.app
Prompt: Write a script to automate token distribution on Starknet, using concepts from Starknet Disperse.
Generated: DETERMINISTIC_9f2cd1c310a3d22a
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from starknet_py.net.account.account_client import AccountClient
from starknet_py.net.networks import MAINNET
from starknet_py.transaction_exceptions import TransactionFailedError
from starknet_py.contract import Contract
from starknet_py.net.models import StarknetChainId

# Constants
CONTRACT_ADDRESS = "0x123..."  # Replace with the actual token contract address
PRIVATE_KEY = "0xabc..."  # Replace with your private key
RECIPIENTS = [
    {"address": "0xRecipient1...", "amount": 100},
    {"address": "0xRecipient2...", "amount": 200},
    {"address": "0xRecipient3...", "amount": 300},
]  # Replace with actual recipient addresses and amounts
TRANSFER_FUNCTION_NAME = "transfer"  # ERC-20 transfer function name

async def distribute_tokens():
    """
    Automates the distribution of tokens to multiple recipients on Starknet.
    """

    try:
        # Initialize the account client
        account_client = AccountClient(
            net=MAINNET,
            address="0xYourAccountAddress...",  # Replace with your account address
            private_key=PRIVATE_KEY,
            chain=StarknetChainId.MAINNET,
        )

        # Declare the contract instance
        contract = await Contract.from_address(CONTRACT_ADDRESS, account_client)

        # List to hold transaction promises
        transactions = []

        # Prepare the transactions for each recipient
        for recipient in RECIPIENTS:
            recipient_address = recipient["address"]
            amount = recipient["amount"]

            # Build the transfer transaction
            tx = contract.functions[TRANSFER_FUNCTION_NAME].prepare(
                recipient_address, amount
            )

            # Add the transaction promise to the list
            transactions.append(account_client.execute(tx))

        # Execute all transactions concurrently
        results = await asyncio.gather(*transactions, return_exceptions=True)

        # Evaluate results
        for result, recipient in zip(results, RECIPIENTS):
            if isinstance(result, TransactionFailedError):
                print(
                    f"Failed to transfer {recipient['amount']} tokens to {recipient['address']}: {result}"
                )
            else:
                print(
                    f"Successfully transferred {recipient['amount']} tokens to {recipient['address']}"
                )

    except Exception as e:
        print(f"An error occurred during token distribution: {e}")


# Entry point for the script
if __name__ == "__main__":
    asyncio.run(distribute_tokens())
```
