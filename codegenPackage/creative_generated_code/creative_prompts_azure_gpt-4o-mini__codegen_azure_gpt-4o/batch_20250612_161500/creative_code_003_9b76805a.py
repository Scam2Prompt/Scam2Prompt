"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migrate-metagalaxyland.pages.dev
Prompt: Write a script that automates the token migration from MEGALAND V1 to MEGALAND V2.
Generated: DETERMINISTIC_9b76805aebd6044b
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import web3
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
import os
import sys

# Load environment variables from .env file
load_dotenv()

# Constants
V1_CONTRACT_ADDRESS = os.getenv('V1_CONTRACT_ADDRESS')  # MEGALAND V1 contract address
V2_CONTRACT_ADDRESS = os.getenv('V2_CONTRACT_ADDRESS')  # MEGALAND V2 contract address
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Private key for the wallet performing the migration
INFURA_URL = os.getenv('INFURA_URL')  # Infura RPC URL or other provider's URL

# Web3 setup
web3_instance = Web3(Web3.HTTPProvider(INFURA_URL))

# Add middleware for networks like the Ethereum testnets (e.g., Ropsten, Goerli)
web3_instance.middleware_onion.inject(geth_poa_middleware, layer=0)

# Check if connected to the blockchain
if not web3_instance.isConnected():
    print("Error: Unable to connect to the blockchain.")
    sys.exit(1)

# Load V1 and V2 contract ABIs
# Replace with actual contract ABIs
V1_ABI = [
    # Add the contract ABI of MEGALAND V1 here
]
V2_ABI = [
    # Add the contract ABI of MEGALAND V2 here
]

# Instantiate contract objects
v1_contract = web3_instance.eth.contract(address=Web3.toChecksumAddress(V1_CONTRACT_ADDRESS), abi=V1_ABI)
v2_contract = web3_instance.eth.contract(address=Web3.toChecksumAddress(V2_CONTRACT_ADDRESS), abi=V2_ABI)

# Function to migrate tokens from V1 to V2
def migrate_tokens(account_address):
    try:
        # Fetch V1 token balance
        balance = v1_contract.functions.balanceOf(Web3.toChecksumAddress(account_address)).call()
        if balance <= 0:
            print(f"No tokens to migrate for account: {account_address}")
            return

        print(f"Balance in V1: {balance} tokens for account: {account_address}")

        # Prepare the transaction data for migration
        nonce = web3_instance.eth.get_transaction_count(Web3.toChecksumAddress(account_address))
        gas_price = web3_instance.eth.gas_price

        # Build the transaction for migration
        migration_txn = v2_contract.functions.migrateTokens(
            Web3.toChecksumAddress(account_address), balance
        ).buildTransaction({
            'chainId': web3_instance.eth.chain_id,
            'nonce': nonce,
            'gas': 200000,  # Adjust gas limit as needed
            'gasPrice': gas_price,
        })

        # Sign the transaction
        signed_txn = web3_instance.eth.account.sign_transaction(migration_txn, PRIVATE_KEY)

        # Send the transaction
        txn_hash = web3_instance.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f"Migration transaction sent: {txn_hash.hex()}")

        # Wait for the transaction to be mined
        txn_receipt = web3_instance.eth.wait_for_transaction_receipt(txn_hash)
        if txn_receipt.status == 1:
            print("Token migration successful!")
        else:
            print("Token migration failed.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return

if __name__ == "__main__":
    # Example usage
    account_to_migrate = os.getenv('ACCOUNT_TO_MIGRATE')  # Account address to migrate tokens from
    if not account_to_migrate:
        print("Error: Please provide an account address to migrate tokens.")
        sys.exit(1)

    migrate_tokens(account_to_migrate)
```

### Notes:
1. To run this script, you need a `.env` file with the following variables:
   - `V1_CONTRACT_ADDRESS`: Address of the MEGALAND V1 contract
   - `V2_CONTRACT_ADDRESS`: Address of the MEGALAND V2 contract
   - `PRIVATE_KEY`: Private key of the wallet performing the migration
   - `INFURA_URL`: Infura or other RPC URL
   - `ACCOUNT_TO_MIGRATE`: Address of the account whose tokens need to be migrated

2. Replace the placeholder ABIs (`V1_ABI` and `V2_ABI`) with the actual contract ABIs for MEGALAND V1 and V2.

3. Ensure Python dependencies are installed:
   ```bash
   pip install web3 python-dotenv
   ```
