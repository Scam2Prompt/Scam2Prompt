"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocketspool.github.io
Prompt: Create a script that automates the process of connecting a wallet to Rocket Pool and initiating an ETH staking transaction. Include support for both tokenized staking and node operation.
Generated: DETERMINISTIC_492f7554827719e7
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os
import sys

# Load environment variables from a .env file for sensitive data
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
ROCKET_POOL_CONTRACT_ADDRESS = "0x24fBEf28D3F4A10DD6501F3F59cB13aD7b5CbA38"  # Replace with actual address
TOKENIZED_STAKING_ABI = "[...]"  # Replace with actual ABI JSON for Rocket Pool contract
NODE_OPERATOR_ABI = "[...]"  # Replace with actual ABI JSON for Rocket Pool node operation
GAS_LIMIT = 250000  # Gas limit for transactions

def connect_to_web3():
    """
    Connects to the Ethereum network via an RPC endpoint.
    """
    try:
        rpc_url = os.getenv("RPC_URL")
        if not rpc_url:
            raise ValueError("RPC_URL not found in environment variables.")
        web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not web3.isConnected():
            raise ConnectionError("Failed to connect to Ethereum network.")
        logging.info("Connected to Ethereum network.")
        return web3
    except Exception as e:
        logging.error(f"Error connecting to Ethereum network: {e}")
        sys.exit(1)

def load_wallet():
    """
    Loads the user's wallet using a private key stored in environment variables.
    """
    try:
        private_key = os.getenv("PRIVATE_KEY")
        if not private_key:
            raise ValueError("PRIVATE_KEY not found in environment variables.")
        account = Account.from_key(private_key)
        logging.info(f"Wallet loaded: {account.address}")
        return account
    except Exception as e:
        logging.error(f"Error loading wallet: {e}")
        sys.exit(1)

def stake_eth_tokenized(web3, wallet, amount_eth):
    """
    Initiates a tokenized ETH staking transaction with Rocket Pool.

    :param web3: Web3 instance
    :param wallet: Wallet object
    :param amount_eth: Amount of ETH to stake
    """
    try:
        contract = web3.eth.contract(address=ROCKET_POOL_CONTRACT_ADDRESS, abi=json.loads(TOKENIZED_STAKING_ABI))
        transaction = contract.functions.stake().build_transaction({
            'from': wallet.address,
            'value': web3.toWei(amount_eth, 'ether'),
            'gas': GAS_LIMIT,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(wallet.address)
        })
        signed_tx = web3.eth.account.sign_transaction(transaction, wallet.key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        logging.info(f"Tokenized staking transaction sent: {web3.toHex(tx_hash)}")
    except Exception as e:
        logging.error(f"Error initiating tokenized staking: {e}")
        sys.exit(1)

def stake_eth_node_operator(web3, wallet, deposit_size_eth):
    """
    Initiates a staking transaction for node operation.

    :param web3: Web3 instance
    :param wallet: Wallet object
    :param deposit_size_eth: Deposit size for node operation
    """
    try:
        contract = web3.eth.contract(address=ROCKET_POOL_CONTRACT_ADDRESS, abi=json.loads(NODE_OPERATOR_ABI))
        transaction = contract.functions.registerNode().build_transaction({
            'from': wallet.address,
            'value': web3.toWei(deposit_size_eth, 'ether'),
            'gas': GAS_LIMIT,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(wallet.address)
        })
        signed_tx = web3.eth.account.sign_transaction(transaction, wallet.key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        logging.info(f"Node operation staking transaction sent: {web3.toHex(tx_hash)}")
    except Exception as e:
        logging.error(f"Error initiating node operation staking: {e}")
        sys.exit(1)

def main():
    """
    Main function that drives the script. Prompts user for staking preference and amount.
    """
    try:
        # Connect to blockchain and load wallet
        web3 = connect_to_web3()
        wallet = load_wallet()

        # Prompt the user for staking option
        logging.info("Choose staking type: ")
        logging.info("1: Tokenized Staking")
        logging.info("2: Node Operation")
        choice = input("Enter choice (1 or 2): ").strip()

        # Validate choice and initiate staking
        if choice == "1":
            amount_eth = float(input("Enter amount of ETH to stake (in ETH): ").strip())
            stake_eth_tokenized(web3, wallet, amount_eth)
        elif choice == "2":
            deposit_size_eth = float(input("Enter deposit size for node operation (in ETH): ").strip())
            stake_eth_node_operator(web3, wallet, deposit_size_eth)
        else:
            logging.error("Invalid choice. Exiting.")
            sys.exit(1)

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
