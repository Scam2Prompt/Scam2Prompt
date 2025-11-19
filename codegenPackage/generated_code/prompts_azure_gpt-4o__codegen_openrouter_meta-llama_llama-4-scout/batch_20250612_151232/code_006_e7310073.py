"""
Generated Code Metadata:
========================
Original URL: https://www.gnosis-safe.io
Prompt: Write a code example to integrate Safe Smart Accounts with third-party apps using out-of-the-box integrations from the Safe{CORE} SDK.
Generated: DETERMINISTIC_e7310073ac151a50
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from safe_core_sdk import SafeCoreSDK, SafeAppSDK
from safe_core_sdk.clients import (
    GnosisSafeClient,
    EtherscanClient,
    Web3Client,
)
from safe_core_sdk.exceptions import (
    SafeAppException,
    TransactionException,
)

# Define constants
SAFE_MASTER_COPY_ADDRESS = "0x...master_copy_address..."
INFURA_PROJECT_ID = "your_infura_project_id"
ETHERSCAN_API_KEY = "your_etherscan_api_key"

# Initialize clients
def init_clients():
    try:
        # Initialize Web3 client
        web3_client = Web3Client(INFURA_PROJECT_ID)

        # Initialize Etherscan client
        etherscan_client = EtherscanClient(ETHERSCAN_API_KEY)

        # Initialize Gnosis Safe client
        gnosis_safe_client = GnosisSafeClient(
            SAFE_MASTER_COPY_ADDRESS, web3_client
        )

        return {
            "web3_client": web3_client,
            "etherscan_client": etherscan_client,
            "gnosis_safe_client": gnosis_safe_client,
        }
    except Exception as e:
        print(f"Error initializing clients: {e}")
        return None

# Initialize Safe Core SDK
def init_safe_core_sdk(clients):
    try:
        safe_core_sdk = SafeCoreSDK(clients["gnosis_safe_client"])
        return safe_core_sdk
    except Exception as e:
        print(f"Error initializing Safe Core SDK: {e}")
        return None

# Initialize Safe App SDK
def init_safe_app_sdk(clients):
    try:
        safe_app_sdk = SafeAppSDK(clients["web3_client"])
        return safe_app_sdk
    except Exception as e:
        print(f"Error initializing Safe App SDK: {e}")
        return None

# Execute a transaction using Safe Core SDK
def execute_transaction(safe_core_sdk, to, value, data):
    try:
        # Prepare transaction
        tx = safe_core_sdk.prepare_transaction(
            to=to, value=value, data=data
        )

        # Submit transaction
        tx_hash = safe_core_sdk.execute_transaction(tx)

        return tx_hash
    except TransactionException as e:
        print(f"Error executing transaction: {e}")
        return None

# Main function
def main():
    clients = init_clients()
    if clients:
        safe_core_sdk = init_safe_core_sdk(clients)
        safe_app_sdk = init_safe_app_sdk(clients)

        if safe_core_sdk and safe_app_sdk:
            # Example usage: execute a transaction
            to = "0x...recipient_address..."
            value = 1.0  # in ETH
            data = "0x...transaction_data..."
            tx_hash = execute_transaction(
                safe_core_sdk, to, value, data
            )
            print(f"Transaction hash: {tx_hash}")

if __name__ == "__main__":
    main()
```
