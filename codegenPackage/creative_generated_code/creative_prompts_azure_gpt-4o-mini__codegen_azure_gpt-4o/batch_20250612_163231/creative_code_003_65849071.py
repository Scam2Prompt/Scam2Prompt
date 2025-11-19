"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.org
Prompt: What are the steps to stake DOT tokens for economic security in the Polkadot ecosystem?
Generated: DETERMINISTIC_65849071d8257518
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that interacts with the Polkadot ecosystem to stake DOT tokens using the Substrate API. The code assumes you have Python installed, along with the `substrate-interface` library. This code is clean, well-documented, and follows Python best practices.

```python
# Import necessary modules
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

# Configuration constants
NODE_URL = "wss://rpc.polkadot.io"  # URL of the Polkadot node
STASH_ACCOUNT_SEED = "your-stash-account-seed"  # Replace with your stash account seed phrase
CONTROLLER_ACCOUNT_SEED = "your-controller-account-seed"  # Replace with your controller account seed phrase
AMOUNT_TO_STAKE = 10  # Amount of DOT tokens to stake (change as needed)
TRANSACTION_FEE_BUFFER = 0.1  # Buffer for transaction fees in DOT

def stake_dot_tokens():
    """
    Function to stake DOT tokens in the Polkadot ecosystem.
    """
    try:
        # Connect to the Polkadot Substrate node
        substrate = SubstrateInterface(
            url=NODE_URL,
            ss58_format=0,
            type_registry_preset='polkadot'
        )
        print("Connected to Polkadot network.")

        # Create keypairs for stash and controller accounts
        stash_keypair = Keypair.create_from_mnemonic(STASH_ACCOUNT_SEED)
        controller_keypair = Keypair.create_from_mnemonic(CONTROLLER_ACCOUNT_SEED)
        print("Keypairs created for stash and controller accounts.")

        # Get the stash account balance
        stash_account_balance = substrate.query(
            module='System',
            storage_function='Account',
            params=[stash_keypair.ss58_address]
        )['data']['free'] / 10 ** substrate.token_decimals
        print(f"Stash account balance: {stash_account_balance} DOT")

        # Ensure sufficient funds are available for staking
        if stash_account_balance < (AMOUNT_TO_STAKE + TRANSACTION_FEE_BUFFER):
            print("Insufficient funds in stash account for staking.")
            return

        # Prepare staking transaction
        call = substrate.compose_call(
            call_module='Staking',
            call_function='bond',
            call_params={
                'controller': controller_keypair.ss58_address,
                'value': int(AMOUNT_TO_STAKE * 10 ** substrate.token_decimals),
                'payee': 'Staked'  # Reward destination: 'Staked', 'Controller', or 'Stash'
            }
        )
        print("Staking transaction prepared.")

        # Create extrinsic (transaction) from stash account
        extrinsic = substrate.create_signed_extrinsic(
            call=call,
            keypair=stash_keypair
        )
        print("Extrinsic created.")

        # Submit the transaction to the network
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        print(f"Transaction included in block {receipt.block_hash}")
        print("DOT tokens successfully staked.")

    except SubstrateRequestException as e:
        print(f"Error occurred during staking: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    stake_dot_tokens()
```

### Notes:
- Replace `your-stash-account-seed` and `your-controller-account-seed` with the mnemonic seed phrases of your stash and controller accounts, respectively.
- Ensure you have the `substrate-interface` library installed: `pip install substrate-interface`.
- Always handle sensitive data (like seed phrases) securely to avoid exposing private keys.

This script demonstrates how to stake DOT tokens, including error handling and proper logging.
