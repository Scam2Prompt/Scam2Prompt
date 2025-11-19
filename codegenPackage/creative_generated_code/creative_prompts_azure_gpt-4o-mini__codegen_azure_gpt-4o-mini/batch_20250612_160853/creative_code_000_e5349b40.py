"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: Generate a Python script to interact with the Zushi $ZUSHI token using the BSC20 contract address 0xE9C...d392b3 for transactions.
Generated: DETERMINISTIC_e5349b40a0a86550
Batch ID: 20250612_160853
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
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Constants
BSC_NODE_URL = os.getenv('BSC_NODE_URL')  # URL of the BSC node (e.g., Infura, Alchemy)
TOKEN_CONTRACT_ADDRESS = '0xE9C...d392b3'  # Replace with the full BSC20 contract address for $ZUSHI
GAS_PRICE = 5 * 10**9  # Gas price in wei, can be adjusted based on network conditions

# Initialize the Web3 connection
web3 = Web3(Web3.HTTPProvider(BSC_NODE_URL))

# Check if connected to BSC
if not web3.isConnected():
    raise ConnectionError("Unable to connect to the Binance Smart Chain node.")

# Load the token contract ABI
def load_contract_abi():
    """ Load the contract ABI from a JSON file. """
    with open('zushi_abi.json', 'r') as abi_file:
        return json.load(abi_file)

# Initialize the token contract
token_abi = load_contract_abi()
contract = web3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=token_abi)

def get_token_balance(address):
    """ Get the token balance of a given address. """
    balance = contract.functions.balanceOf(address).call()
    return web3.fromWei(balance, 'ether')

def transfer_tokens(private_key, to_address, amount):
    """ Transfer tokens from the sender to the specified address. """
    # Create an account object
    account = Account.from_key(private_key)
    
    # Prepare the transaction
    nonce = web3.eth.getTransactionCount(account.address)
    amount_in_wei = web3.toWei(amount, 'ether')
    transaction = contract.functions.transfer(to_address, amount_in_wei).buildTransaction({
        'chainId': 56,  # BSC Mainnet chain ID
        'gas': 200000,  # Customize as per requirement
        'gasPrice': GAS_PRICE,
        'nonce': nonce,
    })

    # Sign the transaction
    signed_txn = web3.eth.account.signTransaction(transaction, private_key)

    # Send the transaction
    try:
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return web3.toHex(txn_hash)
    except Exception as e:
        raise RuntimeError(f"Transaction failed: {str(e)}")

if __name__ == "__main__":
    # Example usage
    user_private_key = os.getenv('USER_PRIVATE_KEY')  # Load user's private key from environment
    recipient_address = '0xRecipientAddressHere'  # Replace with the recipient address
    amount_to_transfer = 1.0  # Amount of $ZUSHI to transfer

    # Check balance before transfer
    user_address = Account.from_key(user_private_key).address
    balance_before = get_token_balance(user_address)
    print(f"Balance before transfer: {balance_before} $ZUSHI")

    # Perform transfer
    try:
        txn_hash = transfer_tokens(user_private_key, recipient_address, amount_to_transfer)
        print(f"Transaction successful with hash: {txn_hash}")
    except Exception as e:
        print(f"Error during transaction: {str(e)}")

    # Check balance after transfer
    balance_after = get_token_balance(user_address)
    print(f"Balance after transfer: {balance_after} $ZUSHI")
```

**Note**: Ensure to replace `'0xE9C...d392b3'` with the full BSC20 contract address for the $ZUSHI token and provide the correct ABI file path in the code. Additionally, please set up your `.env` file with your private key and BSC node URL.
