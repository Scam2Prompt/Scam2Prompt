"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.morpo.org
Prompt: Write a script using the Morpho Bundler API to bundle multiple actions into one transaction, such as using wstETH as collateral to borrow USDC and then supplying USDC into a vault.
Generated: DETERMINISTIC_36bdd51e7a08fd8a
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables for sensitive information
load_dotenv()

# Constants and configuration
RPC_URL = os.getenv("RPC_URL")  # Ethereum RPC endpoint URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the user
MORPHO_BUNDLER_CONTRACT_ADDRESS = os.getenv("MORPHO_BUNDLER_CONTRACT_ADDRESS")  # Morpho Bundler contract address
WSTETH_ADDRESS = os.getenv("WSTETH_ADDRESS")  # Address of wstETH (wrapped staked ETH)
USDC_ADDRESS = os.getenv("USDC_ADDRESS")  # Address of USDC token
VAULT_ADDRESS = os.getenv("VAULT_ADDRESS")  # Address of the target vault

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(RPC_URL))
if not web3.isConnected():
    raise RuntimeError("Failed to connect to Ethereum RPC")

# Load user account from private key
account = Account.from_key(PRIVATE_KEY)
sender_address = account.address

# Morpho Bundler ABI (note: this is a placeholder; you'll need the actual ABI from the Morpho team)
MORPHO_BUNDLER_ABI = [
    # Add the ABI definition here
]

# Initialize Morpho Bundler contract
morpho_bundler_contract = web3.eth.contract(address=MORPHO_BUNDLER_CONTRACT_ADDRESS, abi=MORPHO_BUNDLER_ABI)

# Helper function to build individual actions
def build_action(action_type, params):
    """
    Build an individual action to be bundled.
    
    Args:
        action_type (str): The type of the action.
        params (list): Action-specific parameters.
    
    Returns:
        dict: The action formatted for the bundler.
    """
    return {"actionType": action_type, "params": params}

# Define actions
actions = [
    # Action 1: Supply wstETH as collateral
    build_action("SUPPLY_COLLATERAL", [WSTETH_ADDRESS, web3.toWei(1, 'ether')]),  # Example: 1 wstETH
    
    # Action 2: Borrow USDC
    build_action("BORROW_ASSET", [USDC_ADDRESS, web3.toWei(1000, 'mwei')]),  # Example: 1000 USDC (USDC uses 6 decimals)
    
    # Action 3: Supply USDC into a vault
    build_action("SUPPLY_ASSET_TO_VAULT", [VAULT_ADDRESS, USDC_ADDRESS, web3.toWei(1000, 'mwei')]),  # Example: 1000 USDC
]

# Encode the bundle
bundle_data = morpho_bundler_contract.functions.bundle(actions).build_transaction({
    'from': sender_address,
    'nonce': web3.eth.get_transaction_count(sender_address),
    'gas': 500000,  # Estimate gas limit (you might need to adjust this)
    'gasPrice': web3.eth.gas_price,
})

# Sign the transaction
signed_tx = web3.eth.account.sign_transaction(bundle_data, private_key=PRIVATE_KEY)

# Send the transaction
try:
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Transaction sent successfully. Tx Hash: {tx_hash.hex()}")
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Transaction confirmed. Block Number: {receipt.blockNumber}")
except Exception as e:
    print(f"Error sending transaction: {str(e)}")
```
