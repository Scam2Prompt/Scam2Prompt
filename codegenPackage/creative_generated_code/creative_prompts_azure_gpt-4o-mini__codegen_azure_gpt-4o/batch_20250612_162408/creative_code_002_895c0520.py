"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portalfridge.com
Prompt: What are the steps to select a source wallet and execute a transaction using the Portal Token Bridge?
Generated: DETERMINISTIC_895c0520b917d434
Batch ID: 20250612_162408
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://portal.tokenbridge/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY": {
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
import requests
import json
from web3 import Web3, HTTPProvider
from eth_account import Account
from decimal import Decimal

# Constants and configuration
TOKEN_BRIDGE_URL = "https://portal.tokenbridge/api"
INFURA_ENDPOINT = "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY"
PRIVATE_KEY = "your-private-key-here"  # Private key for source wallet (keep secure!)
DESTINATION_ADDRESS = "0xDestinationWalletAddress"  # Wallet address to send tokens
TOKEN_CONTRACT_ADDRESS = "0xTokenContractAddress"  # Token contract address
AMOUNT_TO_TRANSFER = Decimal("10")  # Amount of tokens to transfer
GAS_LIMIT = 100000  # Gas limit for the transaction
GAS_PRICE = Web3.toWei("10", "gwei")  # Gas price in gwei

# Initialize Web3 connection
web3 = Web3(HTTPProvider(INFURA_ENDPOINT))

# Ensure the connection to the Ethereum network is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Load wallet and address from private key
account = Account.from_key(PRIVATE_KEY)
source_address = account.address

# Verify sufficient balance for gas fees
eth_balance = web3.eth.get_balance(source_address)
if eth_balance < GAS_LIMIT * GAS_PRICE:
    raise ValueError("Insufficient ETH balance to cover gas fees.")

# Function to get the token balance of the source wallet
def get_token_balance(address, contract_address):
    contract_abi = [
        # ABI snippet for ERC20 balanceOf function
        {
            "constant": True,
            "inputs": [{"name": "_owner", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"name": "balance", "type": "uint256"}],
            "type": "function",
        }
    ]

    # Initialize the token contract
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    # Query the balance
    balance = contract.functions.balanceOf(address).call()

    return Decimal(balance) / Decimal(10**18)  # Convert from Wei to token units

# Check token balance
token_balance = get_token_balance(source_address, TOKEN_CONTRACT_ADDRESS)
if token_balance < AMOUNT_TO_TRANSFER:
    raise ValueError("Insufficient token balance for this transaction.")

# Function to execute the token transfer
def execute_transaction():
    contract_abi = [
        # ABI snippet for ERC20 transfer function
        {
            "constant": False,
            "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
            "name": "transfer",
            "outputs": [{"name": "", "type": "bool"}],
            "type": "function",
        }
    ]

    # Initialize the token contract
    contract = web3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=contract_abi)

    # Convert the token amount to Wei
    token_amount_wei = int(AMOUNT_TO_TRANSFER * 10**18)

    # Build the transaction
    transaction = contract.functions.transfer(DESTINATION_ADDRESS, token_amount_wei).buildTransaction({
        "chainId": 1,  # Mainnet chain ID
        "gas": GAS_LIMIT,
        "gasPrice": GAS_PRICE,
        "nonce": web3.eth.get_transaction_count(source_address),
    })

    # Sign the transaction
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

    # Send the transaction
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    return tx_hash

# Execute the transaction and print the transaction hash
try:
    tx_hash = execute_transaction()
    print(f"Transaction successful with hash: {tx_hash.hex()}")
except Exception as e:
    print(f"Error executing transaction: {e}")
```
