"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frax-finances.pages.dev
Prompt: Create a Python script using web3.py to interact with Fraxlend, allowing users to lend and borrow between two ERC20 tokens in an isolated market.
Generated: DETERMINISTIC_a90d596c9c29e258
Batch ID: 20250612_150327
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
from web3.middleware import geth_poa_middleware
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configuration variables (replace these with your actual values)
INFURA_URL = os.getenv("INFURA_URL")  # Infura or another provider's endpoint
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Your wallet private key
FRAXLEND_CONTRACT_ADDRESS = os.getenv("FRAXLEND_CONTRACT_ADDRESS")  # Fraxlend contract address
ERC20_TOKEN_A_ADDRESS = os.getenv("ERC20_TOKEN_A_ADDRESS")  # Address of the first ERC20 token
ERC20_TOKEN_B_ADDRESS = os.getenv("ERC20_TOKEN_B_ADDRESS")  # Address of the second ERC20 token
CHAIN_ID = int(os.getenv("CHAIN_ID", 1))  # Chain ID of the network (e.g., 1 for Ethereum Mainnet)

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Add PoA middleware for networks like Ropsten with Proof of Authority
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Ensure the connection is successful
if not web3.isConnected():
    raise Exception("Failed to connect to the Ethereum network.")

# Load the Fraxlend contract ABI
with open("fraxlend_abi.json", "r") as abi_file:
    FRAXLEND_ABI = json.load(abi_file)

# Initialize the Fraxlend contract
fraxlend_contract = web3.eth.contract(
    address=Web3.to_checksum_address(FRAXLEND_CONTRACT_ADDRESS),
    abi=FRAXLEND_ABI
)

# Load ERC20 token contract ABI
with open("erc20_abi.json", "r") as abi_file:
    ERC20_ABI = json.load(abi_file)

# Initialize ERC20 token contract instances
token_a_contract = web3.eth.contract(
    address=Web3.to_checksum_address(ERC20_TOKEN_A_ADDRESS),
    abi=ERC20_ABI
)
token_b_contract = web3.eth.contract(
    address=Web3.to_checksum_address(ERC20_TOKEN_B_ADDRESS),
    abi=ERC20_ABI
)

# Function to approve tokens for lending/borrowing
def approve_tokens(account_address, token_contract, spender_contract_address, amount):
    try:
        # Build the transaction
        tx = token_contract.functions.approve(
            spender_contract_address, amount
        ).build_transaction({
            "chainId": CHAIN_ID,
            "gas": 200000,
            "gasPrice": web3.to_wei("20", "gwei"),
            "nonce": web3.eth.get_transaction_count(account_address)
        })

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

        # Send the transaction and wait for receipt
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        print(f"Transaction successful with hash: {tx_hash.hex()}")
        return receipt
    except Exception as e:
        print(f"Error approving tokens: {e}")
        return None

# Function to lend tokens
def lend_tokens(account_address, amount_a, amount_b):
    try:
        # Build the transaction for lending
        tx = fraxlend_contract.functions.lend(
            Web3.to_checksum_address(ERC20_TOKEN_A_ADDRESS),
            Web3.to_checksum_address(ERC20_TOKEN_B_ADDRESS),
            amount_a,
            amount_b
        ).build_transaction({
            "chainId": CHAIN_ID,
            "gas": 300000,
            "gasPrice": web3.to_wei("20", "gwei"),
            "nonce": web3.eth.get_transaction_count(account_address)
        })

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

        # Send the transaction and wait for receipt
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        print(f"Lending transaction successful with hash: {tx_hash.hex()}")
        return receipt
    except Exception as e:
        print(f"Error lending tokens: {e}")
        return None

# Function to borrow tokens
def borrow_tokens(account_address, amount_to_borrow):
    try:
        # Build the transaction for borrowing
        tx = fraxlend_contract.functions.borrow(
            Web3.to_checksum_address(ERC20_TOKEN_B_ADDRESS),
            amount_to_borrow
        ).build_transaction({
            "chainId": CHAIN_ID,
            "gas": 300000,
            "gasPrice": web3.to_wei("20", "gwei"),
            "nonce": web3.eth.get_transaction_count(account_address)
        })

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)

        # Send the transaction and wait for receipt
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        print(f"Borrowing transaction successful with hash: {tx_hash.hex()}")
        return receipt
    except Exception as e:
        print(f"Error borrowing tokens: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Ensure PRIVATE_KEY is valid and corresponds to your account
    user_account = Account.privateKeyToAccount(PRIVATE_KEY).address
    print(f"Using account: {user_account}")

    # Example values for lending and borrowing
    lend_amount_a = web3.to_wei(100, "ether")  # Replace with actual lending amount
    lend_amount_b = web3.to_wei(50, "ether")  # Replace with actual lending amount
    borrow_amount = web3.to_wei(20, "ether")  # Replace with actual borrowing amount

    # Approve tokens for Fraxlend contract first
    approve_tokens(user_account, token_a_contract, FRAXLEND_CONTRACT_ADDRESS, lend_amount_a)
    approve_tokens(user_account, token_b_contract, FRAXLEND_CONTRACT_ADDRESS, lend_amount_b)

    # Lend tokens
    lend_tokens(user_account, lend_amount_a, lend_amount_b)

    # Borrow tokens
    borrow_tokens(user_account, borrow_amount)
```

### Note:
1. Replace file paths (`fraxlend_abi.json` and `erc20_abi.json`) with the actual paths to the ABI files.
2. Update `.env` file with the required environment variables.
3. Ensure `web3.py` and other necessary libraries are installed (`pip install web3 pycryptodome python-dotenv`).
