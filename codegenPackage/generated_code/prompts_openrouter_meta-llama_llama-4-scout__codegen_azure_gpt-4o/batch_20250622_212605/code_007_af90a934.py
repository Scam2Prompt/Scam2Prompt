"""
Generated Code Metadata:
========================
Original URL: https://stakingstory.org
Prompt: Write a code example for integrating Story Staking with a multi-chain wallet, enabling seamless asset management across different blockchain networks.
Generated: DETERMINISTIC_af90a934c40cb4da
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Multi-chain Wallet Integration with Story Staking
This script demonstrates how to integrate Story Staking with a multi-chain wallet,
enabling seamless asset management across different blockchain networks.

Dependencies:
- web3 (for Ethereum-based chains)
- requests (for API calls to other blockchain networks)
- dotenv (for managing environment variables securely)

Install dependencies using pip:
pip install web3 requests python-dotenv
"""

import os
import json
from web3 import Web3, exceptions
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configuration for multi-chain wallet
MULTICHAIN_CONFIG = {
    "ethereum": {
        "rpc_url": os.getenv("ETH_RPC_URL"),
        "staking_contract_address": os.getenv("ETH_STAKING_CONTRACT"),
    },
    "polygon": {
        "rpc_url": os.getenv("POLYGON_RPC_URL"),
        "staking_contract_address": os.getenv("POLYGON_STAKING_CONTRACT"),
    },
    "binance_smart_chain": {
        "rpc_url": os.getenv("BSC_RPC_URL"),
        "staking_contract_address": os.getenv("BSC_STAKING_CONTRACT"),
    },
}

# Load private key securely from environment variables
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
if not PRIVATE_KEY:
    raise ValueError("Private key not found in environment variables.")

# Function to initialize a Web3 instance for a given blockchain
def initialize_web3(rpc_url):
    try:
        web3_instance = Web3(Web3.HTTPProvider(rpc_url))
        if not web3_instance.isConnected():
            raise ConnectionError(f"Failed to connect to RPC URL: {rpc_url}")
        return web3_instance
    except Exception as e:
        raise RuntimeError(f"Error initializing Web3: {str(e)}")

# Function to stake assets on a specific blockchain
def stake_assets(chain_name, amount):
    try:
        # Validate chain configuration
        if chain_name not in MULTICHAIN_CONFIG:
            raise ValueError(f"Unsupported chain: {chain_name}")
        
        chain_config = MULTICHAIN_CONFIG[chain_name]
        web3 = initialize_web3(chain_config["rpc_url"])
        
        # Load staking contract
        staking_contract_address = Web3.toChecksumAddress(chain_config["staking_contract_address"])
        staking_contract_abi = load_staking_contract_abi(chain_name)  # Load ABI dynamically
        staking_contract = web3.eth.contract(address=staking_contract_address, abi=staking_contract_abi)
        
        # Prepare transaction
        account = web3.eth.account.privateKeyToAccount(PRIVATE_KEY)
        nonce = web3.eth.getTransactionCount(account.address)
        transaction = staking_contract.functions.stake(Web3.toWei(amount, 'ether')).buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': 2000000,
            'gasPrice': web3.eth.gas_price,
            'nonce': nonce,
        })
        
        # Sign and send transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f"Transaction sent! TX Hash: {web3.toHex(tx_hash)}")
        
        # Wait for transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction confirmed! Block Number: {receipt.blockNumber}")
    except exceptions.ContractLogicError as e:
        print(f"Contract error: {str(e)}")
    except Exception as e:
        print(f"Error staking assets: {str(e)}")

# Function to load staking contract ABI dynamically
def load_staking_contract_abi(chain_name):
    try:
        abi_file_path = f"./abis/{chain_name}_staking_abi.json"
        with open(abi_file_path, 'r') as abi_file:
            return json.load(abi_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"ABI file not found for chain: {chain_name}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid ABI file format for chain: {chain_name}")

# Example usage
if __name__ == "__main__":
    try:
        # Stake assets on Ethereum
        stake_assets("ethereum", 0.1)
        
        # Stake assets on Polygon
        stake_assets("polygon", 0.2)
        
        # Stake assets on Binance Smart Chain
        stake_assets("binance_smart_chain", 0.3)
    except Exception as e:
        print(f"Error in multi-chain staking: {str(e)}")
```
