"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.org
Prompt: Write a Python script using the Aave Protocol's open-source smart contracts to supply liquidity to a pool and earn interest. Include functionality for tracking the Health Factor of borrow positions.
Generated: DETERMINISTIC_cfee657c68074c07
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # Infura endpoint for Ethereum network
USER_PRIVATE_KEY = os.getenv("USER_PRIVATE_KEY")  # Your Ethereum private key
USER_ADDRESS = os.getenv("USER_ADDRESS")  # Your Ethereum address
AAVE_POOL_ADDRESS = "0x794a61358d6845594F94Dc1d0d55Ce3A628d7c0e"  # Aave V3 Pool contract address
ERC20_ABI_PATH = "erc20_abi.json"  # Path to the ERC20 ABI file
AAVE_POOL_ABI_PATH = "aave_pool_abi.json"  # Path to the Aave Pool ABI file

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)  # Use middleware for PoA chains if needed

# Load ABIs
with open(ERC20_ABI_PATH, 'r') as file:
    erc20_abi = json.load(file)

with open(AAVE_POOL_ABI_PATH, 'r') as file:
    aave_pool_abi = json.load(file)

# Initialize contract
aave_pool_contract = web3.eth.contract(address=AAVE_POOL_ADDRESS, abi=aave_pool_abi)

# Function to supply liquidity
def supply_liquidity(token_address, amount):
    """
    Supplies liquidity to an Aave pool.

    Args:
        token_address (str): The address of the ERC20 token to supply.
        amount (int): The amount of tokens to supply, in smallest unit (e.g., wei for ETH).

    Returns:
        str: Transaction hash of the supply transaction.
    """
    # Initialize token contract
    token_contract = web3.eth.contract(address=token_address, abi=erc20_abi)
    
    # Approve the Aave Pool contract to spend tokens
    nonce = web3.eth.get_transaction_count(USER_ADDRESS)
    approve_txn = token_contract.functions.approve(AAVE_POOL_ADDRESS, amount).build_transaction({
        'chainId': web3.eth.chain_id,
        'gas': 200000,
        'gasPrice': web3.eth.gas_price,
        'nonce': nonce
    })
    signed_approve_txn = web3.eth.account.sign_transaction(approve_txn, private_key=USER_PRIVATE_KEY)
    approve_tx_hash = web3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(approve_tx_hash)

    # Supply tokens to the Aave pool
    nonce += 1
    supply_txn = aave_pool_contract.functions.supply(
        token_address, amount, USER_ADDRESS, 0  # Supply mode 0: no referral
    ).build_transaction({
        'chainId': web3.eth.chain_id,
        'gas': 300000,
        'gasPrice': web3.eth.gas_price,
        'nonce': nonce
    })
    signed_supply_txn = web3.eth.account.sign_transaction(supply_txn, private_key=USER_PRIVATE_KEY)
    supply_tx_hash = web3.eth.send_raw_transaction(signed_supply_txn.rawTransaction)
    return supply_tx_hash.hex()

# Function to track Health Factor
def get_health_factor():
    """
    Retrieves the Health Factor of the user's borrow positions.

    Returns:
        float: The Health Factor value.
    """
    user_account_data = aave_pool_contract.functions.getUserAccountData(USER_ADDRESS).call()
    health_factor = user_account_data[5]  # Health factor is the sixth return value
    return health_factor

# Example usage
if __name__ == "__main__":
    try:
        # Token address and supply amount (example: USDC)
        token_address = "0xA0b86991c6218B36c1d19D4a2e9Eb0CE3606EB48"  # USDC token address
        supply_amount = web3.to_wei(100, 'mwei')  # 100 USDC (USDC uses 'mwei' denomination)

        print("Supplying liquidity...")
        tx_hash = supply_liquidity(token_address, supply_amount)
        print(f"Supply transaction successful! Tx Hash: {tx_hash}")

        print("Fetching Health Factor...")
        health_factor = get_health_factor()
        print(f"Current Health Factor: {health_factor}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
