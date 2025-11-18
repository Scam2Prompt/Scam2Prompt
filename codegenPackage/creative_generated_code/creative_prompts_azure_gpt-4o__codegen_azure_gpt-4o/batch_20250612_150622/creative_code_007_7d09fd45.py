"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://to-ousd.pages.dev
Prompt: Write code to interact with the Morpho Aave protocol for lending USDC via OUSD, ensuring efficient matching of lenders and borrowers.
Generated: DETERMINISTIC_7d09fd4520bacab7
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: morpho_aave_lending.py

"""
This script interacts with the Morpho Aave protocol to lend USDC via OUSD.
It ensures efficient matching of lenders and borrowers on the Morpho platform.
"""

from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_utils import to_wei
import json
import os

# Constants
RPC_URL = os.getenv("RPC_URL")  # Replace with your Ethereum RPC URL or specify via an environment variable
USDC_CONTRACT_ADDRESS = "0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"  # USDC ERC20 contract address
MORPHO_AAVE_ADDRESS = "0x1234567890abcdef1234567890abcdef12345678"  # Replace with actual Morpho Aave contract address
OUSD_CONTRACT_ADDRESS = "0x2A8D4DDFA0B4a8E3eA8DA48a526cDE702bC104D8"  # Replace with actual OUSD contract address

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(RPC_URL))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

if not web3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum RPC")

# Helper function to load ABI files
def load_abi(file_path):
    """Load contract ABI from a JSON file."""
    with open(file_path, 'r') as abi_file:
        return json.load(abi_file)

# Load ABIs
usdc_abi = load_abi("usdc_abi.json")  # Ensure correct file path
morpho_aave_abi = load_abi("morpho_aave_abi.json")  # Ensure correct file path
ousd_abi = load_abi("ousd_abi.json")  # Ensure correct file path

# Contract instances
usdc_contract = web3.eth.contract(address=USDC_CONTRACT_ADDRESS, abi=usdc_abi)
morpho_aave_contract = web3.eth.contract(address=MORPHO_AAVE_ADDRESS, abi=morpho_aave_abi)
ousd_contract = web3.eth.contract(address=OUSD_CONTRACT_ADDRESS, abi=ousd_abi)

# Account setup
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Replace with your private key or specify via an environment variable
ACCOUNT_ADDRESS = web3.eth.account.privateKeyToAccount(PRIVATE_KEY).address

# Function to approve USDC transfers
def approve_usdc(amount):
    """
    Approves the transfer of USDC tokens to the Morpho Aave contract.
    :param amount: Amount of USDC to approve (in tokens, not Wei).
    """
    try:
        # Convert USDC amount to smallest denomination
        usdc_amount = int(amount * (10 ** 6))  # USDC has 6 decimal places
        approve_tx = usdc_contract.functions.approve(MORPHO_AAVE_ADDRESS, usdc_amount).build_transaction({
            'from': ACCOUNT_ADDRESS,
            'gas': 100000,
            'gasPrice': web3.toWei('10', 'gwei'),
            'nonce': web3.eth.get_transaction_count(ACCOUNT_ADDRESS)
        })

        # Sign and send the transaction
        signed_tx = web3.eth.account.sign_transaction(approve_tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Approve transaction sent. TX hash: {tx_hash.hex()}")
        web3.eth.wait_for_transaction_receipt(tx_hash)

    except Exception as e:
        raise RuntimeError(f"Error approving USDC: {e}")

# Function to supply USDC via Morpho Aave
def supply_usdc(amount):
    """
    Supplies USDC to the Morpho Aave protocol for lending via OUSD.
    :param amount: Amount of USDC to supply (in tokens, not Wei).
    """
    try:
        # Convert USDC amount to smallest denomination
        usdc_amount = int(amount * (10 ** 6))  # USDC has 6 decimal places
        supply_tx = morpho_aave_contract.functions.supply(USDC_CONTRACT_ADDRESS, ACCOUNT_ADDRESS, usdc_amount).build_transaction({
            'from': ACCOUNT_ADDRESS,
            'gas': 200000,
            'gasPrice': web3.toWei('10', 'gwei'),
            'nonce': web3.eth.get_transaction_count(ACCOUNT_ADDRESS)
        })

        # Sign and send the transaction
        signed_tx = web3.eth.account.sign_transaction(supply_tx, PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Supply transaction sent. TX hash: {tx_hash.hex()}")
        web3.eth.wait_for_transaction_receipt(tx_hash)

    except Exception as e:
        raise RuntimeError(f"Error supplying USDC: {e}")

# Main function
def main():
    """
    Main function to approve and supply USDC.
    """
    try:
        usdc_amount_to_lend = 1000  # Example amount: 1000 USDC
        print(f"Approving {usdc_amount_to_lend} USDC...")
        approve_usdc(usdc_amount_to_lend)

        print(f"Supplying {usdc_amount_to_lend} USDC via Morpho Aave...")
        supply_usdc(usdc_amount_to_lend)

        print("USDC lending completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```

**Note**:  
- Replace placeholder values like `MORPHO_AAVE_ADDRESS`, `OUSD_CONTRACT_ADDRESS`, and ABI file paths (`usdc_abi.json`, `morpho_aave_abi.json`, `ousd_abi.json`) with correct values.
- Ensure the necessary ABIs are available as JSON files for the script to run correctly.
- This script assumes gas price is statically set at 10 gwei; you may want to use dynamic gas pricing for production.
- Handle environment variables securely for RPC URL and private key (e.g., `.env` files).
