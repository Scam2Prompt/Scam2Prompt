"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperliquidfaucet.com
Prompt: Generate code to interact with the HyperEVM testnet using HYPE tokens after bridging from mock USDC.
Generated: DETERMINISTIC_42591dd352adb385
Batch ID: 20250612_155705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import requests
from web3 import Web3, HTTPProvider
from decouple import config

# Load environment variables
INFURA_URL = config("INFURA_URL")  # Infura URL for the HyperEVM testnet
PRIVATE_KEY = config("PRIVATE_KEY")  # User's wallet private key
WALLET_ADDRESS = config("WALLET_ADDRESS")  # User's wallet address

# Constants
HYPE_TOKEN_CONTRACT_ADDRESS = "0xYourHypeTokenContractAddress"  # Replace with real HYPE token contract address
USDC_TOKEN_CONTRACT_ADDRESS = "0xYourUSDCContractAddress"  # Replace with real mock USDC contract address
BRIDGE_CONTRACT_ADDRESS = "0xYourBridgeContractAddress"  # Replace with real bridge contract address
GAS_LIMIT = 200000  # Set appropriate gas limit
GAS_PRICE = Web3.toWei("10", "gwei")  # Set appropriate gas price

# Initialize Web3
web3 = Web3(HTTPProvider(INFURA_URL))
if not web3.isConnected():
    raise Exception("Failed to connect to HyperEVM testnet.")

# Load ABI data (replace these file paths with actual ABI file locations)
with open("hype_token_abi.json", "r") as hype_abi_file:
    HYPE_ABI = json.load(hype_abi_file)

with open("usdc_token_abi.json", "r") as usdc_abi_file:
    USDC_ABI = json.load(usdc_abi_file)

with open("bridge_contract_abi.json", "r") as bridge_abi_file:
    BRIDGE_ABI = json.load(bridge_abi_file)

# Instantiate contract objects
hype_token_contract = web3.eth.contract(address=HYPE_TOKEN_CONTRACT_ADDRESS, abi=HYPE_ABI)
usdc_token_contract = web3.eth.contract(address=USDC_TOKEN_CONTRACT_ADDRESS, abi=USDC_ABI)
bridge_contract = web3.eth.contract(address=BRIDGE_CONTRACT_ADDRESS, abi=BRIDGE_ABI)

# Helper function to send transactions
def send_transaction(transaction):
    try:
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt
    except Exception as e:
        print(f"Error during transaction: {e}")
        return None

# Step 1: Approve the transfer of mock USDC to the bridge contract
def approve_usdc_transfer(amount):
    amount_in_wei = Web3.toWei(amount, "ether")  # Assumes USDC has 18 decimals
    approve_txn = usdc_token_contract.functions.approve(
        BRIDGE_CONTRACT_ADDRESS, amount_in_wei
    ).build_transaction({
        "from": WALLET_ADDRESS,
        "gas": GAS_LIMIT,
        "gasPrice": GAS_PRICE,
        "nonce": web3.eth.get_transaction_count(WALLET_ADDRESS),
    })
    receipt = send_transaction(approve_txn)
    if receipt:
        print(f"USDC transfer approved. Transaction hash: {receipt.transactionHash.hex()}")
    else:
        print("Failed to approve USDC transfer.")

# Step 2: Bridge USDC tokens to HYPE tokens
def bridge_usdc_to_hype(amount):
    amount_in_wei = Web3.toWei(amount, "ether")  # Assumes USDC has 18 decimals
    bridge_txn = bridge_contract.functions.bridgeTokens(
        USDC_TOKEN_CONTRACT_ADDRESS, amount_in_wei
    ).build_transaction({
        "from": WALLET_ADDRESS,
        "gas": GAS_LIMIT,
        "gasPrice": GAS_PRICE,
        "nonce": web3.eth.get_transaction_count(WALLET_ADDRESS),
    })
    receipt = send_transaction(bridge_txn)
    if receipt:
        print(f"USDC tokens bridged to HYPE tokens. Transaction hash: {receipt.transactionHash.hex()}")
    else:
        print("Failed to bridge USDC to HYPE tokens.")

# Step 3: Check HYPE token balance
def check_hype_balance():
    balance = hype_token_contract.functions.balanceOf(WALLET_ADDRESS).call()
    balance_in_hype = Web3.fromWei(balance, "ether")
    print(f"HYPE Token Balance: {balance_in_hype} HYPE")

# Main execution
if __name__ == "__main__":
    try:
        # Example usage:
        usdc_amount = 100  # Amount in USDC to bridge
        print("Approving USDC transfer...")
        approve_usdc_transfer(usdc_amount)

        print("Bridging USDC to HYPE tokens...")
        bridge_usdc_to_hype(usdc_amount)

        print("Checking HYPE token balance...")
        check_hype_balance()
    except Exception as e:
        print(f"An error occurred: {e}")
```
