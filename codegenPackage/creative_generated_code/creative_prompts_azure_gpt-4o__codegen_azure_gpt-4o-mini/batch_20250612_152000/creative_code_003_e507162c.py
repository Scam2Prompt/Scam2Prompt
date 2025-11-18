"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rtt23423.pages.dev
Prompt: Create a Python script using web3.py to interact with a smart contract that supports tokenized real-world assets, inspired by Ondo Finance's ecosystem.
Generated: DETERMINISTIC_e507162c5c27f389
Batch ID: 20250612_152000
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
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Connect to Ethereum network (Infura, Alchemy, or local node)
INFURA_URL = os.getenv('INFURA_URL')  # Set your Infura URL in .env
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum network
if not web3.isConnected():
    raise Exception("Failed to connect to the Ethereum network. Please check your Infura URL.")

# Load the smart contract ABI and address
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')  # Set your smart contract address in .env
ABI_FILE_PATH = 'contract_abi.json'  # Path to the ABI JSON file

try:
    with open(ABI_FILE_PATH) as abi_file:
        contract_abi = json.load(abi_file)
except FileNotFoundError:
    raise Exception(f"ABI file not found at {ABI_FILE_PATH}. Please provide the correct file path.")

# Create a contract instance
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

# Function to interact with the smart contract, for example, fetching the token balance
def get_token_balance(wallet_address):
    """
    Fetch the token balance of a specified wallet address.
    
    :param wallet_address: The Ethereum address to check the token balance of.
    :return: The token balance as a float.
    """
    try:
        balance = contract.functions.balanceOf(wallet_address).call()
        return web3.fromWei(balance, 'ether')  # Assuming the token uses 18 decimals
    except Exception as e:
        print(f"Error fetching balance for {wallet_address}: {str(e)}")
        return None

# Function to transfer tokens
def transfer_tokens(sender_private_key, recipient_address, amount):
    """
    Transfer tokens from one address to another.
    
    :param sender_private_key: The private key of the sender's wallet.
    :param recipient_address: The Ethereum address to send tokens to.
    :param amount: The amount of tokens to send (in Ether).
    :return: Transaction hash of the transfer.
    """
    try:
        account = web3.eth.account.from_key(sender_private_key)
        nonce = web3.eth.getTransactionCount(account.address)

        # Prepare the transaction details
        transaction = contract.functions.transfer(
            recipient_address, 
            web3.toWei(amount, 'ether')  # Convert amount to Wei
        ).buildTransaction({
            'chainId': 1,  # Mainnet chain ID
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return tx_hash.hex()  # Return the transaction hash as a hex string
    except Exception as e:
        print(f"Error transferring tokens: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    wallet_address = os.getenv('WALLET_ADDRESS')  # The wallet address to check balance
    sender_private_key = os.getenv('SENDER_PRIVATE_KEY')  # The private key for sending tokens
    recipient_address = os.getenv('RECIPIENT_ADDRESS')  # The recipient's wallet address
    amount = 0.1  # Amount to transfer

    # Fetch and print the token balance
    balance = get_token_balance(wallet_address)
    print(f"Token balance of {wallet_address}: {balance}")

    # Transfer tokens and print the transaction hash
    tx_hash = transfer_tokens(sender_private_key, recipient_address, amount)
    if tx_hash:
        print(f"Transaction successful with hash: {tx_hash}")
```

Make sure to create a `.env` file containing the required environment variables:
```
INFURA_URL=<your_infura_url>
CONTRACT_ADDRESS=<your_contract_address>
WALLET_ADDRESS=<your_wallet_address>
SENDER_PRIVATE_KEY=<your_sender_private_key>
RECIPIENT_ADDRESS=<recipient_wallet_address>
``` 

Also, ensure that the ABI of your contract is saved in `contract_abi.json`.
