"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainguild.pages.dev
Prompt: Provide code to build a "Balancy playground" for testing blockchain-based tasks and campaigns, as described on the Guildhall Guild website.
Generated: DETERMINISTIC_be5a76bcb10a0a06
Batch ID: 20250612_153224
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
import json
import os

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # Get Infura URL from environment variable
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the account, retrieved securely
PUBLIC_ADDRESS = os.getenv("PUBLIC_ADDRESS")  # Public address of the account
CONTRACT_ABI_PATH = "contract_abi.json"  # Path to your contract ABI JSON file
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # Address of the deployed smart contract

# Ensure environment variables are set
if not INFURA_URL or not PRIVATE_KEY or not PUBLIC_ADDRESS or not CONTRACT_ADDRESS:
    raise EnvironmentError("Missing required environment variables.")

# Connect to the blockchain
web3_provider = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3_provider.isConnected():
    raise ConnectionError("Failed to connect to the blockchain.")

# Load the contract ABI
try:
    with open(CONTRACT_ABI_PATH, "r") as abi_file:
        contract_abi = json.load(abi_file)
except FileNotFoundError:
    raise FileNotFoundError(f"ABI file not found at {CONTRACT_ABI_PATH}.")
except json.JSONDecodeError:
    raise ValueError(f"Failed to decode the ABI JSON file at {CONTRACT_ABI_PATH}.")

# Initialize the contract
contract = web3_provider.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

# Function to check the balance of a given account
def get_balance(address):
    """
    Retrieves the current balance of the specified Ethereum address.
    
    :param address: Ethereum address to check balance for.
    :return: Balance in Ether.
    """
    try:
        balance_wei = web3_provider.eth.get_balance(address)
        balance_ether = web3_provider.fromWei(balance_wei, 'ether')
        return balance_ether
    except Exception as e:
        raise RuntimeError(f"Failed to fetch balance for address {address}: {e}")

# Function to send Ether
def send_ether(to_address, amount):
    """
    Sends Ether from the user's account to the specified address.
    
    :param to_address: Ethereum address to send Ether to.
    :param amount: Amount of Ether to send (in Ether, not Wei).
    :return: Transaction hash.
    """
    try:
        nonce = web3_provider.eth.get_transaction_count(PUBLIC_ADDRESS)
        transaction = {
            'to': to_address,
            'value': web3_provider.toWei(amount, 'ether'),
            'gas': 21000,
            'gasPrice': web3_provider.toWei('50', 'gwei'),
            'nonce': nonce
        }
        signed_txn = web3_provider.eth.account.sign_transaction(transaction, PRIVATE_KEY)
        txn_hash = web3_provider.eth.send_raw_transaction(signed_txn.rawTransaction)
        return web3_provider.toHex(txn_hash)
    except Exception as e:
        raise RuntimeError(f"Failed to send Ether to {to_address}: {e}")

# Sample function to interact with a smart contract
def execute_contract_function(function_name, *args):
    """
    Executes a specified function in the smart contract.

    :param function_name: Name of the contract function to call.
    :param args: Arguments to pass to the contract function.
    :return: Response from the contract function.
    """
    try:
        contract_function = contract.functions[function_name](*args)
        nonce = web3_provider.eth.get_transaction_count(PUBLIC_ADDRESS)
        transaction = contract_function.buildTransaction({
            'chainId': 1,  # Mainnet chain ID
            'gas': 300000,
            'gasPrice': web3_provider.toWei('50', 'gwei'),
            'nonce': nonce
        })
        signed_txn = web3_provider.eth.account.sign_transaction(transaction, PRIVATE_KEY)
        txn_hash = web3_provider.eth.send_raw_transaction(signed_txn.rawTransaction)
        return web3_provider.toHex(txn_hash)
    except Exception as e:
        raise RuntimeError(f"Failed to execute contract function '{function_name}': {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Check balance
        print(f"Balance of {PUBLIC_ADDRESS}: {get_balance(PUBLIC_ADDRESS)} Ether")
        
        # Send Ether (example: sending 0.01 Ether)
        recipient_address = "0xRecipientAddressHere"  # Replace with actual recipient address
        txn_hash = send_ether(recipient_address, 0.01)
        print(f"Transaction hash for Ether transfer: {txn_hash}")
        
        # Interact with contract (example: calling 'startCampaign' function)
        campaign_id = 12345  # Example campaign ID
        txn_hash = execute_contract_function("startCampaign", campaign_id)
        print(f"Transaction hash for contract function call: {txn_hash}")
    except Exception as e:
        print(f"Error: {e}")
```
