"""
Generated Code Metadata:
========================
Original URL: https://hjiihhhgg.pages.dev
Prompt: Generate a code example for a cross-chain bridge to facilitate asset swapping between Avalanche and Fantom networks, using a decentralized protocol.
Generated: DETERMINISTIC_a11484bc4270d55d
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import os

# Load environment variables for private keys and RPC URLs
AVALANCHE_RPC_URL = os.getenv("AVALANCHE_RPC_URL")
FANTOM_RPC_URL = os.getenv("FANTOM_RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
AVALANCHE_BRIDGE_CONTRACT_ADDRESS = os.getenv("AVALANCHE_BRIDGE_CONTRACT_ADDRESS")
FANTOM_BRIDGE_CONTRACT_ADDRESS = os.getenv("FANTOM_BRIDGE_CONTRACT_ADDRESS")

# Load ABI files for the bridge contracts
with open("avalanche_bridge_abi.json", "r") as f:
    AVALANCHE_BRIDGE_ABI = json.load(f)

with open("fantom_bridge_abi.json", "r") as f:
    FANTOM_BRIDGE_ABI = json.load(f)

# Initialize Web3 instances for Avalanche and Fantom networks
avalanche_web3 = Web3(Web3.HTTPProvider(AVALANCHE_RPC_URL))
fantom_web3 = Web3(Web3.HTTPProvider(FANTOM_RPC_URL))

# Add middleware for networks using Proof of Authority (if applicable)
avalanche_web3.middleware_onion.inject(geth_poa_middleware, layer=0)
fantom_web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Ensure connections are established
if not avalanche_web3.isConnected():
    raise ConnectionError("Failed to connect to Avalanche network.")
if not fantom_web3.isConnected():
    raise ConnectionError("Failed to connect to Fantom network.")

# Load bridge contract instances
avalanche_bridge_contract = avalanche_web3.eth.contract(
    address=Web3.toChecksumAddress(AVALANCHE_BRIDGE_CONTRACT_ADDRESS),
    abi=AVALANCHE_BRIDGE_ABI
)

fantom_bridge_contract = fantom_web3.eth.contract(
    address=Web3.toChecksumAddress(FANTOM_BRIDGE_CONTRACT_ADDRESS),
    abi=FANTOM_BRIDGE_ABI
)

# Function to swap assets from Avalanche to Fantom
def swap_assets_avalanche_to_fantom(amount, recipient_address):
    """
    Swap assets from Avalanche to Fantom using the bridge contract.

    :param amount: Amount of tokens to swap (in smallest unit, e.g., wei).
    :param recipient_address: Address on Fantom network to receive the tokens.
    """
    try:
        # Build transaction for Avalanche bridge contract
        nonce = avalanche_web3.eth.getTransactionCount(avalanche_web3.eth.defaultAccount)
        tx = avalanche_bridge_contract.functions.swapToFantom(
            amount, Web3.toChecksumAddress(recipient_address)
        ).buildTransaction({
            'chainId': 43114,  # Avalanche chain ID
            'gas': 200000,
            'gasPrice': avalanche_web3.eth.gas_price,
            'nonce': nonce
        })

        # Sign and send the transaction
        signed_tx = avalanche_web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = avalanche_web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        print(f"Transaction sent. Avalanche TX Hash: {tx_hash.hex()}")
        return tx_hash.hex()

    except Exception as e:
        print(f"Error during asset swap: {e}")
        raise

# Function to swap assets from Fantom to Avalanche
def swap_assets_fantom_to_avalanche(amount, recipient_address):
    """
    Swap assets from Fantom to Avalanche using the bridge contract.

    :param amount: Amount of tokens to swap (in smallest unit, e.g., wei).
    :param recipient_address: Address on Avalanche network to receive the tokens.
    """
    try:
        # Build transaction for Fantom bridge contract
        nonce = fantom_web3.eth.getTransactionCount(fantom_web3.eth.defaultAccount)
        tx = fantom_bridge_contract.functions.swapToAvalanche(
            amount, Web3.toChecksumAddress(recipient_address)
        ).buildTransaction({
            'chainId': 250,  # Fantom chain ID
            'gas': 200000,
            'gasPrice': fantom_web3.eth.gas_price,
            'nonce': nonce
        })

        # Sign and send the transaction
        signed_tx = fantom_web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = fantom_web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        print(f"Transaction sent. Fantom TX Hash: {tx_hash.hex()}")
        return tx_hash.hex()

    except Exception as e:
        print(f"Error during asset swap: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Set default account for Web3 instances
    avalanche_web3.eth.defaultAccount = avalanche_web3.eth.account.privateKeyToAccount(PRIVATE_KEY).address
    fantom_web3.eth.defaultAccount = fantom_web3.eth.account.privateKeyToAccount(PRIVATE_KEY).address

    # Swap assets from Avalanche to Fantom
    try:
        avalanche_tx_hash = swap_assets_avalanche_to_fantom(
            amount=1000000000000000000,  # 1 token (assuming 18 decimals)
            recipient_address="0xRecipientAddressOnFantomNetwork"
        )
        print(f"Avalanche to Fantom swap successful. TX Hash: {avalanche_tx_hash}")
    except Exception as e:
        print(f"Failed to swap assets from Avalanche to Fantom: {e}")

    # Swap assets from Fantom to Avalanche
    try:
        fantom_tx_hash = swap_assets_fantom_to_avalanche(
            amount=1000000000000000000,  # 1 token (assuming 18 decimals)
            recipient_address="0xRecipientAddressOnAvalancheNetwork"
        )
        print(f"Fantom to Avalanche swap successful. TX Hash: {fantom_tx_hash}")
    except Exception as e:
        print(f"Failed to swap assets from Fantom to Avalanche: {e}")
```

### Notes:
- Replace placeholder values (e.g., `AVALANCHE_RPC_URL`, `FANTOM_RPC_URL`, `PRIVATE_KEY`, contract addresses, and ABIs) with actual values.
- Ensure ABI files (`avalanche_bridge_abi.json` and `fantom_bridge_abi.json`) are correctly formatted and match the deployed contracts.
- This code assumes the bridge contracts have `swapToFantom` and `swapToAvalanche` functions implemented. Adjust function names and parameters as needed based on the actual contract implementation.
