"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cointaap.com
Prompt: Provide a step-by-step guide to integrate NFT purchase functionality into a crypto trading app similar to Cointaap.
Generated: DETERMINISTIC_c18991a9ae9143ce
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
NFT Purchase Integration for a Crypto Trading App.

This script provides an implementation for integrating NFT purchase functionality
into a crypto trading app. It adheres to best practices, includes error handling,
and is well-documented for production readiness.

Requirements:
- Python 3.7+
- A web3 provider (e.g., Infura or Alchemy)
- A crypto wallet with sufficient funds for gas fees and purchase

Dependencies:
Install the following Python libraries before running this script:
- web3: `pip install web3`
"""

from web3 import Web3, HTTPProvider
import json
import os

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

# Constants for the NFT contract and blockchain network
INFURA_API_URL = os.getenv("INFURA_API_URL")  # Ethereum network provider URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # User's private wallet key
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # User's wallet address
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # NFT smart contract address
CONTRACT_ABI_FILE = "contract_abi.json"  # JSON file containing the contract's ABI

# Initialize Web3 provider
web3 = Web3(HTTPProvider(INFURA_API_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to the blockchain network. Check your provider URL.")

# Verify wallet address is valid
if not web3.isAddress(WALLET_ADDRESS):
    raise ValueError("Invalid wallet address. Ensure your wallet address is correct.")

# Load contract ABI
try:
    with open(CONTRACT_ABI_FILE, 'r') as abi_file:
        contract_abi = json.load(abi_file)
except FileNotFoundError:
    raise FileNotFoundError("Contract ABI file not found. Ensure 'contract_abi.json' exists in the working directory.")

# Initialize the NFT contract
nft_contract = web3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=contract_abi)

def purchase_nft(token_id: int, wallet_address: str, private_key: str):
    """
    Facilitates the purchase of an NFT.

    Args:
        token_id (int): The unique identifier of the NFT to purchase.
        wallet_address (str): The user's wallet address.
        private_key (str): Private key associated with the wallet address.

    Returns:
        dict: Transaction receipt if the purchase is successful.
    """
    try:
        # Get the NFT price
        nft_price = nft_contract.functions.getPrice(token_id).call()
        print(f"NFT Price: {web3.fromWei(nft_price, 'ether')} ETH")

        # Build transaction
        transaction = nft_contract.functions.purchase(token_id).buildTransaction({
            "from": wallet_address,
            "value": nft_price,  # Pass the price of the NFT
            "gas": 200000,  # Set gas limit (adjust based on contract requirements)
            "gasPrice": web3.toWei('20', 'gwei'),  # Set gas price
            "nonce": web3.eth.getTransactionCount(wallet_address),
        })

        # Sign transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)

        # Send transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Transaction Hash: {txn_hash.hex()}")

        # Wait for transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
        print("Transaction successful. Receipt:", receipt)

        return receipt
    except Exception as e:
        print(f"Error during NFT purchase: {str(e)}")
        return {"error": str(e)}

# Example Usage
if __name__ == "__main__":
    TOKEN_ID = 1  # Replace with the actual token ID of the NFT you want to purchase

    print(f"Attempting to purchase NFT with token ID {TOKEN_ID}...")
    result = purchase_nft(TOKEN_ID, wallet_address=WALLET_ADDRESS, private_key=PRIVATE_KEY)

    if "error" in result:
        print("NFT purchase failed:", result["error"])
    else:
        print("NFT purchase completed successfully.")
```

Make sure to replace placeholder values (`PRIVATE_KEY`, `WALLET_ADDRESS`, etc.) with actual data from your environment. Ensure you install dependencies (`web3`, `dotenv`) before running the script.
