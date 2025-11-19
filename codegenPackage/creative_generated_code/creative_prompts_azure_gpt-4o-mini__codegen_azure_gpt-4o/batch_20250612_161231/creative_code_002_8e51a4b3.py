"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsconnectonline.com
Prompt: Write a script that connects to a blockchain to automate financial transactions without centralized intermediaries.
Generated: DETERMINISTIC_8e51a4b358befef0
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configuration: Blockchain Node URL and Private Key
BLOCKCHAIN_NODE_URL = os.getenv("BLOCKCHAIN_NODE_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Your wallet address
RECIPIENT_ADDRESS = os.getenv("RECIPIENT_ADDRESS")  # Recipient wallet address
TRANSACTION_AMOUNT = os.getenv("TRANSACTION_AMOUNT")  # Amount in Ether to send

# Initialize Web3 connection
try:
    web3 = Web3(HTTPProvider(BLOCKCHAIN_NODE_URL))
    if web3.isConnected():
        print("Successfully connected to the blockchain.")
    else:
        raise Exception("Failed to connect to the blockchain node.")
except Exception as e:
    print(f"Error connecting to blockchain: {e}")
    exit(1)

# Ensure valid Wallet Address format
if not web3.isAddress(WALLET_ADDRESS) or not web3.isAddress(RECIPIENT_ADDRESS):
    print("Invalid wallet or recipient address.")
    exit(1)

# Convert Ether amount to Wei (smallest unit in Ethereum)
try:
    transaction_value = web3.toWei(float(TRANSACTION_AMOUNT), "ether")
except Exception as e:
    print(f"Error converting transaction amount: {e}")
    exit(1)

# Build, sign, and send the transaction
try:
    # Fetch the current nonce (transaction count for account)
    nonce = web3.eth.getTransactionCount(WALLET_ADDRESS)

    # Create a transaction dictionary
    transaction = {
        "nonce": nonce,
        "to": RECIPIENT_ADDRESS,
        "value": transaction_value,
        "gas": 21000,  # Gas limit for basic transactions
        "gasPrice": web3.toWei("20", "gwei"),  # Adjust gas price as needed
        "chainId": web3.eth.chainId
    }

    # Sign the transaction with the private key
    signed_transaction = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

    # Send the signed transaction
    tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

    # Print the transaction hash
    print(f"Transaction sent successfully. Hash: {web3.toHex(tx_hash)}")

except Exception as e:
    print(f"Error during transaction: {e}")
    exit(1)

# Verify transaction status
try:
    # Wait for the transaction receipt
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    if tx_receipt.status == 1:  # 1 indicates success
        print("Transaction confirmed successfully.")
    else:
        print("Transaction failed.")
except Exception as e:
    print(f"Error verifying transaction status: {e}")
    exit(1)
```
