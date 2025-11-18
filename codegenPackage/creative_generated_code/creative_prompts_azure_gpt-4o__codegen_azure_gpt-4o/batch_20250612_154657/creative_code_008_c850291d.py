"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storyprotocols.com
Prompt: Write a program to automate the process of uploading intellectual property to the "Story IP Blockchain" for tokenization.
Generated: DETERMINISTIC_c850291dff7f4ac5
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import requests
from web3 import Web3, exceptions
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants - Replace with your actual values
BLOCKCHAIN_URL = os.getenv("BLOCKCHAIN_URL")  # URL of the blockchain node
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # Smart Contract address
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # User's private key for signing transactions
ACCOUNT_ADDRESS = os.getenv("ACCOUNT_ADDRESS")  # User's public wallet address
ABI_PATH = os.getenv("ABI_PATH")  # Path to the ABI JSON file

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(BLOCKCHAIN_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to the blockchain node.")

# Load Smart Contract ABI
try:
    with open(ABI_PATH, "r") as abi_file:
        contract_abi = json.load(abi_file)
except FileNotFoundError:
    raise FileNotFoundError("ABI file not found. Please check the ABI_PATH environment variable.")
except json.JSONDecodeError:
    raise ValueError("Invalid ABI file format. Please ensure the ABI file is a valid JSON.")

# Initialize Smart Contract
contract = web3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=contract_abi)

def upload_ip_to_blockchain(ip_title, ip_description, ip_file_path):
    """
    Uploads intellectual property metadata to the blockchain for tokenization.

    Args:
        ip_title (str): Title of the intellectual property.
        ip_description (str): Description of the intellectual property.
        ip_file_path (str): Path to the intellectual property file.

    Returns:
        str: Transaction hash of the upload process.
    """
    try:
        # Validate input
        if not os.path.exists(ip_file_path):
            raise FileNotFoundError(f"The file '{ip_file_path}' does not exist.")
        
        # Read the file content
        with open(ip_file_path, "rb") as file:
            file_content = file.read()
        
        # Generate a unique hash for the file content
        file_hash = web3.sha3(file_content).hex()

        # Construct transaction data
        nonce = web3.eth.getTransactionCount(ACCOUNT_ADDRESS)
        transaction = contract.functions.tokenizeIP(
            ip_title, ip_description, file_hash
        ).buildTransaction({
            'gas': 300000,  # Set appropriate gas limit
            'gasPrice': web3.toWei('20', 'gwei'),
            'nonce': nonce,
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

        # Send transaction to the blockchain
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Return the transaction hash
        return tx_hash.hex()

    except exceptions.SolidityError as e:
        raise RuntimeError(f"Smart Contract Error: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to handle user input and upload IP to the blockchain.
    """
    print("Welcome to the Story IP Blockchain Tokenization System.")
    ip_title = input("Enter the title of the Intellectual Property: ").strip()
    ip_description = input("Enter the description of the Intellectual Property: ").strip()
    ip_file_path = input("Enter the file path of the Intellectual Property: ").strip()

    try:
        tx_hash = upload_ip_to_blockchain(ip_title, ip_description, ip_file_path)
        print(f"Transaction successful! Transaction hash: {tx_hash}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
