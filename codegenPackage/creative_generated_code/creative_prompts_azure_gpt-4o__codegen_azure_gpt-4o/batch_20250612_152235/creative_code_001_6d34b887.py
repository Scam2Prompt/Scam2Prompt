"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roost-ai.pages.dev
Prompt: Create a Python script using Web3.py to connect a Metamask wallet, bridge ETH to the Base blockchain, and swap ETH for $ROOST tokens on Uniswap using the contract address provided on the Roost website.
Generated: DETERMINISTIC_6d34b887362943c9
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Metamask wallet private key (NEVER expose this in production code)
PRIVATE_KEY = os.getenv("METAMASK_PRIVATE_KEY")
# Infura or Alchemy URL for Ethereum Mainnet
ETH_PROVIDER_URL = os.getenv("ETH_PROVIDER_URL")
# Base Chain RPC URL
BASE_PROVIDER_URL = os.getenv("BASE_PROVIDER_URL")
# Uniswap Router Address
UNISWAP_ROUTER_ADDRESS = os.getenv("UNISWAP_ROUTER_ADDRESS")
# $ROOST Token Contract Address
ROOST_CONTRACT_ADDRESS = os.getenv("ROOST_CONTRACT_ADDRESS")

# Connect to Ethereum Mainnet
web3_eth = Web3(Web3.HTTPProvider(ETH_PROVIDER_URL))
assert web3_eth.isConnected(), "Failed to connect to Ethereum Mainnet."

# Connect to Base Chain
web3_base = Web3(Web3.HTTPProvider(BASE_PROVIDER_URL))
assert web3_base.isConnected(), "Failed to connect to Base Blockchain."

# Create Web3 account object from private key
account = Account.from_key(PRIVATE_KEY)
wallet_address = account.address

# Load Uniswap router ABI
with open('uniswap_router_abi.json', 'r') as file:
    uniswap_router_abi = json.load(file)

# Load ERC-20 token ABI
with open('erc20_abi.json', 'r') as file:
    erc20_abi = json.load(file)

# Initialize Uniswap contract
uniswap_router = web3_eth.eth.contract(
    address=Web3.to_checksum_address(UNISWAP_ROUTER_ADDRESS),
    abi=uniswap_router_abi
)

# Initialize $ROOST token contract
roost_token = web3_eth.eth.contract(
    address=Web3.to_checksum_address(ROOST_CONTRACT_ADDRESS),
    abi=erc20_abi
)


def check_balance():
    """
    Check ETH balance of the user's wallet.
    """
    balance = web3_eth.eth.get_balance(wallet_address)
    eth_balance = web3_eth.fromWei(balance, 'ether')
    print(f"Wallet {wallet_address} balance: {eth_balance:.8f} ETH")
    return eth_balance


def bridge_eth_to_base(amount_eth):
    """
    Bridge ETH to the Base blockchain. Assumes a bridging mechanism is implemented.
    For production, integrate with a specific bridge API (e.g., Hop Protocol, Synapse).
    """
    # Placeholder for bridging logic
    print(f"Bridging {amount_eth:.8f} ETH to Base blockchain...")
    # Implement bridging logic with the chosen bridge provider's API
    pass


def swap_eth_for_roost(amount_eth_in, token_out_address):
    """
    Swap ETH for $ROOST tokens using Uniswap.
    """
    try:
        # Minimum amount of $ROOST tokens to receive (set slippage tolerance)
        amount_out_min = 0  # Replace with calculated value

        # Deadline for the transaction (e.g., 2 minutes from now)
        deadline = int(web3_eth.eth.get_block('latest')['timestamp']) + 120

        # Path: ETH -> $ROOST
        path = [
            Web3.to_checksum_address(web3_eth.to_checksum_address(web3_eth.get_address
