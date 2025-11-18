"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centrifuge.onl
Prompt: Generate a tutorial for using Centrifuge's GitHub documentation to build a decentralized application for tokenized financial products.
Generated: DETERMINISTIC_c1a552a7307eb162
Batch ID: 20250612_155000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here’s a sample Python code tutorial using Centrifuge's GitHub documentation to build a decentralized application for tokenized financial products. For simplicity, we'll assume the application interacts with Centrifuge's Tinlake protocol (used for tokenized financial products) via their smart contract APIs.

```python
"""
Tutorial Code: Building a Decentralized Application for Tokenized Financial Products Using Centrifuge

Requirements:
1. Install web3.py for Ethereum smart contract interaction: `pip install web3`
2. Install dotenv for securely managing environment variables: `pip install python-dotenv`
3. Ensure you have access to Centrifuge's smart contract ABI files from their GitHub documentation.
"""

import os
import json
from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
from web3.exceptions import ContractLogicError, TransactionNotFound

# Load environment variables (e.g. Ethereum node URL and private key)
load_dotenv()

# Constants
ETHEREUM_NODE_URL = os.getenv('ETHEREUM_NODE_URL')  # Example: https://mainnet.infura.io/v3/<API_KEY>
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Your Ethereum wallet's private key
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS')  # Your Ethereum wallet address

# Ensure the environment variables are properly set
if not ETHEREUM_NODE_URL or not PRIVATE_KEY or not WALLET_ADDRESS:
    raise EnvironmentError("Please set ETHEREUM_NODE_URL, PRIVATE_KEY, and WALLET_ADDRESS in the environment variables.")

# Connect to Ethereum blockchain
web3 = Web3(HTTPProvider(ETHEREUM_NODE_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum blockchain. Check your ETHEREUM_NODE_URL.")

# Load Centrifuge's Tinlake smart contract ABI
# Make sure to download the required ABI JSON file from Centrifuge's GitHub documentation.
with open("TinlakeContractABI.json", "r") as abi_file:
    contract_abi = json.load(abi_file)

# Define the Tinlake contract address
TINLAKE_CONTRACT_ADDRESS = "0x..."  # Replace with the actual contract address from the Centrifuge documentation.

# Create the smart contract object
tinlake_contract = web3.eth.contract(address=web3.toChecksumAddress(TINLAKE_CONTRACT_ADDRESS), abi=contract_abi)

# Function to fetch tokenized financial products
def get_tokenized_products():
    """
    Fetch tokenized financial products from the Tinlake contract.

    Returns:
        list: A list of tokenized financial products data.
    """
    try:
        # Example method: Fetch total number of products (replace with actual contract method)
        total_products = tinlake_contract.functions.totalProducts().call()
        print(f"Total tokenized financial products: {total_products}")

        products = []
        for product_id in range(total_products):
            # Example method: Fetch product details by ID (replace with actual contract method)
            product = tinlake_contract.functions.getProduct(product_id).call()
            products.append(product)
        
        return products
    except ContractLogicError as e:
        print(f"Error while fetching tokenized products: {e}")
        return []

# Function to invest in tokenized products
def invest_in_product(product_id, investment_amount):
    """
    Invest in a tokenized financial product.

    Args:
        product_id (int): The ID of the tokenized product to invest in.
        investment_amount (float): The amount to invest (in Ether).

    Returns:
        str: Transaction hash if the investment succeeds.
    """
    try:
        # Convert investment amount to Wei (smallest ETH unit)
        amount_in_wei = web3.toWei(investment_amount, 'ether')

        # Build transaction payload
        txn = tinlake_contract.functions.invest(product_id).buildTransaction({
            'from': WALLET_ADDRESS,
            'value': amount_in_wei,
            'gas': 2000000,  # Define a reasonable gas limit
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(WALLET_ADDRESS)
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f"Investment transaction submitted. Tx hash: {web3.toHex(tx_hash)}")

        return web3.toHex(tx_hash)
    except ContractLogicError as e:
        print(f"Error during investment: {e}")
        return None
    except ValueError as e:
        print(f"Transaction error: {e}")
        return None

# Function to check the transaction status
def check_transaction_status(tx_hash):
    """
    Check the status of a transaction on the Ethereum blockchain.

    Args:
        tx_hash (str): Transaction hash.

    Returns:
        str: 'Success' if the transaction was mined successfully, otherwise 'Pending' or 'Failed'.
    """
    try:
        tx_receipt = web3.eth.get_transaction_receipt(tx_hash)
        if tx_receipt and tx_receipt['status'] == 1:
            return "Success"
        else:
            return "Failed"
    except TransactionNotFound:
        return "Pending"

# Example usage
if __name__ == "__main__":
    try:
        # Fetch tokenized products
        products = get_tokenized_products()
        if not products:
            print("No tokenized products found.")
        else:
            print(f"Tokenized Products: {products}")

        # Invest in a tokenized product (example: product ID 1, invest 0.1 ETH)
        tx_hash = invest_in_product(product_id=1, investment_amount=0.1)
        if tx_hash:
            print(f"Checking transaction status for Tx hash: {tx_hash}")
            status = check_transaction_status(tx_hash)
            print(f"Transaction Status: {status}")
    except Exception as e:
        print(f"Error occurred: {e}")
```

### Notes:
1. Replace `TINLAKE_CONTRACT_ADDRESS` and contract methods (`totalProducts`, `getProduct`, `invest`, etc.) with actual values and methods from Centrifuge's GitHub documentation.
2. This code assumes the Tinlake protocol is used; adapt the contract ABI and methods based on the specific Centrifuge product you are working with.
3. Proper error handling and logging are included for production readiness.
4. Safeguard your private key and ensure environment variables are appropriately secured.
