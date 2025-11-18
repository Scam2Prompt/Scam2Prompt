"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dexmoney.io
Prompt: Write a script to register a domain using the 3DNS system on Optimism, ensuring secure name record updates and instant transfer capabilities.
Generated: DETERMINISTIC_bb5148aa566ca685
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# domain_registration.py

"""
This script allows users to register a domain using the 3DNS system on Optimism.
It ensures secure name record updates and instant transfer capabilities.
"""

import json
import requests
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Constants
OPTIMISM_RPC_URL = os.getenv("OPTIMISM_RPC_URL")  # Optimism RPC URL
DOMAIN_CONTRACT_ADDRESS = os.getenv("DOMAIN_CONTRACT_ADDRESS")  # 3DNS Domain contract address
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # User's private key for signing transactions

# Initialize Web3 connection to Optimism
web3 = Web3(Web3.HTTPProvider(OPTIMISM_RPC_URL))

if not web3.is_connected():
    raise ConnectionError("Unable to connect to Optimism RPC.")

# Load the contract ABI
with open("3dns_abi.json", "r") as abi_file:
    DOMAIN_CONTRACT_ABI = json.load(abi_file)

# Initialize contract instance
domain_contract = web3.eth.contract(address=DOMAIN_CONTRACT_ADDRESS, abi=DOMAIN_CONTRACT_ABI)

def register_domain(domain_name: str, owner_address: str):
    """
    Registers a domain on the 3DNS system.

    Args:
        domain_name (str): The name of the domain to register.
        owner_address (str): The Ethereum address of the new domain owner.

    Returns:
        dict: Transaction receipt containing details of the registration.
    """
    # Ensure valid input
    if not domain_name or not owner_address:
        raise ValueError("Domain name and owner address must be provided.")
    
    if not web3.is_address(owner_address):
        raise ValueError("Invalid Ethereum address.")

    # Build transaction
    nonce = web3.eth.get_transaction_count(web3.eth.account.privateKeyToAccount(PRIVATE_KEY).address)
    tx = domain_contract.functions.registerDomain(domain_name, owner_address).build_transaction({
        "chainId": web3.eth.chain_id,
        "gas": 300000,
        "gasPrice": web3.eth.gas_price,
        "nonce": nonce
    })

    # Sign transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

    # Send transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Transaction sent! TX hash: {tx_hash.hex()}")

    # Wait for transaction receipt
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Transaction confirmed! Block number: {receipt.blockNumber}")

    return receipt

def update_name_record(domain_name: str, record_data: str):
    """
    Updates the name record of an already registered domain.

    Args:
        domain_name (str): The name of the domain to update.
        record_data (str): The new record data for the domain.

    Returns:
        dict: Transaction receipt containing details of the record update.
    """
    # Ensure valid input
    if not domain_name or not record_data:
        raise ValueError("Domain name and record data must be provided.")

    # Build transaction
    nonce = web3.eth.get_transaction_count(web3.eth.account.privateKeyToAccount(PRIVATE_KEY).address)
    tx = domain_contract.functions.updateNameRecord(domain_name, record_data).build_transaction({
        "chainId": web3.eth.chain_id,
        "gas": 300000,
        "gasPrice": web3.eth.gas_price,
        "nonce": nonce
    })

    # Sign transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

    # Send transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Transaction sent! TX hash: {tx_hash.hex()}")

    # Wait for transaction receipt
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Transaction confirmed! Block number: {receipt.blockNumber}")

    return receipt

def transfer_domain(domain_name: str, new_owner_address: str):
    """
    Transfers domain ownership to a new owner.

    Args:
        domain_name (str): The name of the domain to transfer.
        new_owner_address (str): The Ethereum address of the new owner.

    Returns:
        dict: Transaction receipt containing details of the ownership transfer.
    """
    # Ensure valid input
    if not domain_name or not new_owner_address:
        raise ValueError("Domain name and new owner address must be provided.")
    
    if not web3.is_address(new_owner_address):
        raise ValueError("Invalid Ethereum address.")

    # Build transaction
    nonce = web3.eth.get_transaction_count(web3.eth.account.privateKeyToAccount(PRIVATE_KEY).address)
    tx = domain_contract.functions.transferDomain(domain_name, new_owner_address).build_transaction({
        "chainId": web3.eth.chain_id,
        "gas": 300000,
        "gasPrice": web3.eth.gas_price,
        "nonce": nonce
    })

    # Sign transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

    # Send transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Transaction sent! TX hash: {tx_hash.hex()}")

    # Wait for transaction receipt
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Transaction confirmed! Block number: {receipt.blockNumber}")

    return receipt

if __name__ == "__main__":
    # Example usage
    try:
        domain_name = "example.eth"
        owner_address = "0xYourEthereumAddress"

        print("Registering domain...")
        register_receipt = register_domain(domain_name, owner_address)
        print("Domain registered successfully!")

        print("Updating name record...")
        update_receipt = update_name_record(domain_name, "New record data")
        print("Name record updated successfully!")

        print("Transferring domain...")
        transfer_receipt = transfer_domain(domain_name, "0xNewOwnerEthereumAddress")
        print("Domain transferred successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
