"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degentip-9l3.pages.dev
Prompt: Write a Python script to interact with the Degen L3 chain using web3.py, specifically to add liquidity to the Uniswap V3 DEGEN/WETH pool with a 0.3% fee tier.
Generated: DETERMINISTIC_b1e6b328435f3e28
Batch ID: 20250612_154057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/{INFURA_PROJECT_ID": {
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
import json
import os
from web3 import Web3
from eth_account import Account
from decimal import Decimal

# Constants
INFURA_PROJECT_ID = "your_infura_project_id"  # Replace with your Infura project ID
CHAIN_URL = f"https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}"
PRIVATE_KEY = "your_private_key"  # Replace with your private key
POOL_ADDRESS = "replace_with_uniswap_v3_pool_address"  # Replace with the DEGEN/WETH pool address
UNISWAP_V3_ROUTER_ADDRESS = "replace_with_uniswap_v3_router_address"  # Replace with the Uniswap V3 router address
POOL_ABI_FILE = "UniswapV3Pool.json"  # Path to pool ABI JSON file
ROUTER_ABI_FILE = "UniswapV3Router.json"  # Path to router ABI JSON file
GAS_LIMIT = 300000
GAS_PRICE_GWEI = 100

# Initialize web3
web3 = Web3(Web3.HTTPProvider(CHAIN_URL))
if not web3.isConnected():
    raise Exception("Failed to connect to the blockchain.")

# Load account
account = Account.from_key(PRIVATE_KEY)
wallet_address = account.address

# Helper function to load ABI
def load_abi(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"ABI file not found: {file_path}")
    with open(file_path, "r") as abi_file:
        return json.load(abi_file)

# Load ABIs
pool_abi = load_abi(POOL_ABI_FILE)
router_abi = load_abi(ROUTER_ABI_FILE)

# Contract instances
pool_contract = web3.eth.contract(address=POOL_ADDRESS, abi=pool_abi)
router_contract = web3.eth.contract(address=UNISWAP_V3_ROUTER_ADDRESS, abi=router_abi)

# Function to add liquidity to the pool
def add_liquidity(token0_amount, token1_amount, token0, token1, fee_tier=3000):
    """
    Add liquidity to the Uniswap V3 DEGEN/WETH pool.

    :param token0_amount: Amount of token0 (DEGEN) to provide as liquidity.
    :param token1_amount: Amount of token1 (WETH) to provide as liquidity.
    :param token0: Address of token0 (DEGEN).
    :param token1: Address of token1 (WETH).
    :param fee_tier: Fee tier of the pool (default: 0.3% = 3000).
    """
    # Ensure sufficient balances
    token0_balance = web3.eth.get_balance(wallet_address)
    token1_balance = web3.eth.get_balance(wallet_address)
    if token0_balance < token0_amount or token1_balance < token1_amount:
        raise ValueError("Insufficient token balances to add liquidity.")

    # Approve tokens (if required, assuming ERC-20 tokens)
    # Use ERC-20 contract's approve function prior to this step if necessary

    # Construct transaction
    tx = router_contract.functions.addLiquidity(
        token0,
        token1,
        fee_tier,
        token0_amount,
        token1_amount,
        Decimal("0"),  # Min token0 amount (slippage tolerance)
        Decimal("0"),  # Min token1 amount (slippage tolerance)
        wallet_address,
        web3.eth.get_block('latest')['timestamp'] + 1200  # Deadline (20 minutes from now)
    ).buildTransaction({
        "chainId": 1,  # Mainnet chain ID
        "gas": GAS_LIMIT,
        "gasPrice": web3.toWei(GAS_PRICE_GWEI, 'gwei'),
        "nonce": web3.eth.get_transaction_count(wallet_address),
    })

    # Sign transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

    # Send transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # Wait for transaction receipt
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    if receipt.status == 1:
        print(f"Liquidity added successfully! Transaction hash: {tx_hash.hex()}")
    else:
        raise Exception("Transaction failed!")

# Example usage
try:
    # Replace with actual token amounts and addresses
    add_liquidity(
        token0_amount=web3.toWei(10, 'ether'),  # Example: 10 DEGEN tokens
        token1_amount=web3.toWei(0.5, 'ether'),  # Example: 0.5 WETH tokens
        token0="replace_with_degen_token_address",  # Replace with DEGEN token address
        token1="replace_with_weth_token_address",  # Replace with WETH token address
    )
except Exception as e:
    print(f"Error adding liquidity: {str(e)}")
```
