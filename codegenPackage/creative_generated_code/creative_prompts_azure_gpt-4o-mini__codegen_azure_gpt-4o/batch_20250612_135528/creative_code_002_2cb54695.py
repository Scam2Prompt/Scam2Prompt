"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-multisig.vercel.app
Prompt: Can you provide an example of code for implementing a multisig functionality on StarkNet with Starsign?
Generated: DETERMINISTIC_2cb54695d360d442
Batch ID: 20250612_135528
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://alpha4.starknet.io": {
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
# starknet_multisig.py

from starknet_py.net.account.account import Account
from starknet_py.net.models import StarknetChainId
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.contract import Contract
from starknet_py.transaction_exceptions import TransactionRejectedError
from starknet_py.net.signer import StarkCurveSigner
from starkware.crypto.signature.signature import sign
import asyncio

# Configuration constants
RPC_URL = "https://alpha4.starknet.io"
CHAIN_ID = StarknetChainId.TESTNET  # Change to MAINNET for production
MULTISIG_CONTRACT_ADDRESS = "<MULTISIG_CONTRACT_ADDRESS>"  # Replace with your contract address
PRIVATE_KEYS = [
    "<PRIVATE_KEY_1>",
    "<PRIVATE_KEY_2>",
    "<PRIVATE_KEY_3>",
]  # List of private keys for signers

NUM_SIGNATURES_REQUIRED = 2  # Update based on your multisig threshold

# Initialize StarkNet client
client = GatewayClient(RPC_URL)

# Function to initialize accounts for signing
def initialize_accounts():
    accounts = []
    for private_key in PRIVATE_KEYS:
        # Generate signer and account
        signer = StarkCurveSigner(
            private_key=int(private_key, 16),  # Private key should be in hex format
            account_address=MULTISIG_CONTRACT_ADDRESS,
            chain_id=CHAIN_ID,
        )
        account = Account(
            client=client,
            address=MULTISIG_CONTRACT_ADDRESS,
            signer=signer,
        )
        accounts.append(account)
    return accounts

# Function to prepare and execute a multisig transaction
async def execute_multisig_transaction():
    try:
        # Load the multisig contract
        contract = await Contract.from_address(MULTISIG_CONTRACT_ADDRESS, client)

        # Example method call on the multisig contract
        method_name = "transfer_funds"  # Replace with your contract's method name
        method_arguments = [123456, "<RECIPIENT_ADDRESS>"]  # Replace with your method arguments

        # Prepare the transaction
        call = contract.functions[method_name].prepare_call(
            *method_arguments
        )

        accounts = initialize_accounts()

        # Collect signatures
        signatures = []
        for account in accounts[:NUM_SIGNATURES_REQUIRED]:
            # Sign the transaction
            signature = sign(account.signer.private_key, call.calldata_hash)
            signatures.append(signature)

        # Execute the transaction with collected signatures
        invocation = await call.invoke(
            max_fee=10**16,  # Adjust max fee as needed
            signatures=signatures,
        )

        # Wait for transaction to complete
        await invocation.wait_for_acceptance()
        print(f"Transaction successful: {invocation.transaction_hash}")

    except TransactionRejectedError as e:
        print(f"Transaction rejected: {e.message}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Main entry point
if __name__ == "__main__":
    # Execute the transaction
    asyncio.run(execute_multisig_transaction())
```
