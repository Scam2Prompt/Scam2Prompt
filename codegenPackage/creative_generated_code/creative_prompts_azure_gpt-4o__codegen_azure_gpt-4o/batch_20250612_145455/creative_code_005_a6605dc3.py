"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-sophon.xyz
Prompt: Write a function to interact with a blockchain mainnet for uploading and retrieving user-generated content, inspired by Sophon's onchain entertainment model.
Generated: DETERMINISTIC_a6605dc32f369adf
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from web3 import Web3
import json
import os

# Set up environment variables for security
INFURA_URL = os.getenv("INFURA_URL")  # Your Ethereum Mainnet URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # User's private key for signing transactions
ACCOUNT_ADDRESS = os.getenv("ACCOUNT_ADDRESS")  # User's Ethereum address
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # Address of the deployed smart contract
CONTRACT_ABI_PATH = os.getenv("CONTRACT_ABI_PATH")  # Path to the contract's ABI file

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Validate the Web3 connection
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum Mainnet")

# Load the contract ABI
with open(CONTRACT_ABI_PATH, 'r') as abi_file:
    contract_abi = json.load(abi_file)

# Get the contract instance
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

def upload_content(content: str) -> str:
    """
    Upload user-generated content to the blockchain.
    
    Args:
        content (str): The content to upload (e.g., a string of text or metadata).
        
    Returns:
        str: The transaction hash of the upload.
    """
    try:
        # Validate input
        if not content or not isinstance(content, str):
            raise ValueError("Content must be a non-empty string")
        
        # Build the transaction
        transaction = contract.functions.uploadContent(content).build_transaction({
            'from': ACCOUNT_ADDRESS,
            'nonce': web3.eth.get_transaction_count(ACCOUNT_ADDRESS),
            'gas': 2000000,
            'gasPrice': web3.to_wei('50', 'gwei')
        })

        # Sign the transaction with the private key
        signed_tx = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for the transaction receipt
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        if tx_receipt.status != 1:
            raise Exception("Transaction failed")

        return tx_hash.hex()

    except Exception as e:
        raise RuntimeError(f"Failed to upload content: {str(e)}")

def retrieve_content(content_id: int) -> str:
    """
    Retrieve user-generated content from the blockchain.
    
    Args:
        content_id (int): The unique identifier of the content to retrieve.
        
    Returns:
        str: The retrieved content.
    """
    try:
        # Validate input
        if not isinstance(content_id, int) or content_id < 0:
            raise ValueError("content_id must be a non-negative integer")
        
        # Call the contract function to retrieve content
        content = contract.functions.getContent(content_id).call()

        return content

    except Exception as e:
        raise RuntimeError(f"Failed to retrieve content: {str(e)}")

if __name__ == "__main__":
    # Example usage
    try:
        # Upload content
        content_to_upload = "Hello, blockchain world!"
        tx_hash = upload_content(content_to_upload)
        print(f"Content uploaded successfully. Transaction hash: {tx_hash}")

        # Retrieve content
        content_id = 0  # Example ID
        retrieved_content = retrieve_content(content_id)
        print(f"Retrieved content: {retrieved_content}")

    except Exception as main_error:
        print(f"An error occurred: {main_error}")
```
