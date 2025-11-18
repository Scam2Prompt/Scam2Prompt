"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holdstationexchange.app
Prompt: Write a script to convert esHOLD tokens into HOLD tokens using the vesting feature described on the Holdstation Exchange website.
Generated: DETERMINISTIC_0635e54d1b220e2b
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import web3
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound
import json
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment Variables
INFURA_URL = os.getenv("INFURA_URL")  # Infura endpoint URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the user
ES_HOLD_TOKEN_ADDRESS = os.getenv("ES_HOLD_TOKEN_ADDRESS")  # Address of the esHOLD token contract
HOLD_TOKEN_ADDRESS = os.getenv("HOLD_TOKEN_ADDRESS")  # Address of the HOLD token contract
VESTING_CONTRACT_ADDRESS = os.getenv("VESTING_CONTRACT_ADDRESS")  # Address of the vesting contract

# Connect to Ethereum node
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    print("Failed to connect to Ethereum node.")
    sys.exit(1)

# Get the account address from private key
account = web3.eth.account.from_key(PRIVATE_KEY)
account_address = account.address

# Load ABI files (Replace with actual ABI JSON paths)
try:
    with open("es_hold_token_abi.json", "r") as file:
        es_hold_abi = json.load(file)
    with open("hold_token_abi.json", "r") as file:
        hold_abi = json.load(file)
    with open("vesting_contract_abi.json", "r") as file:
        vesting_abi = json.load(file)
except FileNotFoundError as e:
    print(f"ABI file not found: {e}")
    sys.exit(1)

# Initialize contract instances
es_hold_contract = web3.eth.contract(address=ES_HOLD_TOKEN_ADDRESS, abi=es_hold_abi)
hold_contract = web3.eth.contract(address=HOLD_TOKEN_ADDRESS, abi=hold_abi)
vesting_contract = web3.eth.contract(address=VESTING_CONTRACT_ADDRESS, abi=vesting_abi)

def check_balance():
    """
    Check the balance of esHOLD tokens for the current account.
    """
    try:
        balance = es_hold_contract.functions.balanceOf(account_address).call()
        return balance
    except ContractLogicError as e:
        print(f"Error checking balance: {e}")
        return 0

def approve_es_hold_transfer(amount):
    """
    Approve the transfer of esHOLD tokens to the vesting contract.
    :param amount: Amount of esHOLD tokens to approve
    """
    try:
        nonce = web3.eth.getTransactionCount(account_address)
        approve_txn = es_hold_contract.functions.approve(VESTING_CONTRACT_ADDRESS, amount).buildTransaction({
            "chainId": web3.eth.chain_id,
            "gas": 200000,
            "gasPrice": web3.toWei("20", "gwei"),
            "nonce": nonce
        })
        signed_txn = web3.eth.account.sign_transaction(approve_txn, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f"Approve transaction sent, waiting for confirmation. Tx Hash: {tx_hash.hex()}")
        return tx_hash.hex()
    except Exception as e:
        print(f"Error approving esHOLD transfer: {e}")
        return None

def convert_es_hold_to_hold(amount):
    """
    Convert esHOLD tokens to HOLD tokens using the vesting contract.
    :param amount: Amount of esHOLD tokens to convert
    """
    try:
        nonce = web3.eth.getTransactionCount(account_address)
        convert_txn = vesting_contract.functions.convertEsHoldToHold(amount).buildTransaction({
            "chainId": web3.eth.chain_id,
            "gas": 300000,
            "gasPrice": web3.toWei("20", "gwei"),
            "nonce": nonce
        })
        signed_txn = web3.eth.account.sign_transaction(convert_txn, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f"Convert transaction sent, waiting for confirmation. Tx Hash: {tx_hash.hex()}")
        return tx_hash.hex()
    except Exception as e:
        print(f"Error converting esHOLD to HOLD: {e}")
        return None

def main():
    """
    Main function to execute the conversion process.
    """
    print("Checking esHOLD token balance...")
    balance = check_balance()
    print(f"esHOLD Balance: {balance}")

    if balance <= 0:
        print("No esHOLD tokens available for conversion.")
        return

    print("Approving esHOLD token transfer...")
    approve_txn = approve_es_hold_transfer(balance)
    if not approve_txn:
        print("Failed to approve esHOLD token transfer.")
        return

    print("Converting esHOLD tokens to HOLD tokens...")
    convert_txn = convert_es_hold_to_hold(balance)
    if not convert_txn:
        print("Failed to convert esHOLD tokens to HOLD tokens.")
        return

    print("Conversion process completed successfully.")

if __name__ == "__main__":
    main()
```
