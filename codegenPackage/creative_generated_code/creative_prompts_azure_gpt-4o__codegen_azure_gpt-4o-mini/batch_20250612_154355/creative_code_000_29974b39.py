"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sage-croissant-c13d3b.netlify.app
Prompt: Write a Python script to integrate Tether's USD₮ stablecoin into a blockchain application using the Ethereum ERC20 transport protocol. Ensure the script includes functionality for sending and receiving USD₮ tokens.
Generated: DETERMINISTIC_29974b3998e48412
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # Ethereum node URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Your Ethereum wallet private key
USD_T_CONTRACT_ADDRESS = os.getenv("USD_T_CONTRACT_ADDRESS")  # USD₮ contract address on Ethereum

# Initialize web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if the connection to Ethereum node is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum node")

# USD₮ Token ABI (simplified for send/receive functionality)
USD_T_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "to", "type": "address"},
            {"name": "value", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

# Create a contract instance for USD₮
usd_t_contract = web3.eth.contract(address=USD_T_CONTRACT_ADDRESS, abi=USD_T_ABI)

def get_balance(address):
    """
    Get the USD₮ balance of a given Ethereum address.
    
    :param address: Ethereum address to check the balance
    :return: USD₮ balance as a float
    """
    balance = usd_t_contract.functions.balanceOf(address).call()
    return web3.fromWei(balance, 'mwei')  # USD₮ has 6 decimals

def send_usdt(to_address, amount):
    """
    Send USD₮ tokens to a specified Ethereum address.
    
    :param to_address: The address to send USD₮ to
    :param amount: The amount of USD₮ to send
    :raises ValueError: If the amount is negative or there's an error in transaction
    """
    if amount < 0:
        raise ValueError("Amount must be non-negative")

    # Convert amount to proper unit (USD₮ has 6 decimal places)
    amount_in_wei = web3.toWei(amount, 'mwei')

    # Build the transaction
    nonce = web3.eth.getTransactionCount(Account.from_key(PRIVATE_KEY).address)
    transaction = {
        'to': USD_T_CONTRACT_ADDRESS,
        'value': 0,
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
        'data': usd_t_contract.functions.transfer(to_address, amount_in_wei).buildTransaction({'chainId': 1})['data']
    }

    # Sign the transaction
    signed_txn = web3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)

    # Send the transaction
    try:
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Transaction successful with hash: {web3.toHex(txn_hash)}")
    except Exception as e:
        raise RuntimeError(f"Transaction failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    recipient_address = "<RECIPIENT_ADDRESS>"  # Replace with actual recipient address
    amount_to_send = 10  # Amount in USD₮ to send

    try:
        print(f"Current balance: {get_balance(Account.from_key(PRIVATE_KEY).address)} USD₮")
        send_usdt(recipient_address, amount_to_send)
    except Exception as e:
        print(f"Error: {str(e)}")
``` 

Make sure to replace `"<RECIPIENT_ADDRESS>"` with the actual Ethereum address you want to send USD₮ to. Also, ensure that your `.env` file contains the required information (INFURA_URL, PRIVATE_KEY, USD_T_CONTRACT_ADDRESS) before running this script.
