"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbinu.app
Prompt: Write a Python script that interacts with the Arbinu token on the Arbitrum network, allowing users to check their token balance and transaction history.
Generated: DETERMINISTIC_2c8d9c5607c491e7
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import os
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Constants
ARBITRUM_RPC_URL = os.getenv("ARBITRUM_RPC_URL")  # Arbitrum RPC URL from .env
ARBINU_TOKEN_ADDRESS = os.getenv("ARBINU_TOKEN_ADDRESS")  # Arbinu token contract address from .env
USER_WALLET_ADDRESS = os.getenv("USER_WALLET_ADDRESS")  # User's wallet address from .env

# Connect to the Arbitrum RPC
try:
    web3 = Web3(Web3.HTTPProvider(ARBITRUM_RPC_URL))
    if not web3.isConnected():
        raise ConnectionError("Failed to connect to Arbitrum network")
except Exception as e:
    print(f"Error connecting to Arbitrum network: {e}")
    sys.exit(1)

# ABI of the Arbinu token contract (ERC20 standard functions)
ARBINU_TOKEN_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "_from", "type": "address"}, {"name": "_to", "type": "address"}],
        "name": "transfer",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "_address", "type": "address"}],
        "name": "getPastTransactions",
        "outputs": [{"name": "transactions", "type": "array"}],
        "paybad
