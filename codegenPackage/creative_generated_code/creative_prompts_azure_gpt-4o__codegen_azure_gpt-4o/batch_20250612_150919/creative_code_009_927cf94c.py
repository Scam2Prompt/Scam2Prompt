"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://40f8af32.blog-a32.pages.dev
Prompt: Generate a tutorial for beginners to register and manage ENS domains, referencing the "A Beginner's Guide to Ethereum and ENS" article.
Generated: DETERMINISTIC_927cf94c9c5b3ab3
Batch ID: 20250612_150919
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
Script: manage_ens_domains.py
Description: A beginner-friendly Python script to register and manage ENS (Ethereum Name Service) domains.
Dependencies: web3.py, eth-account
Prerequisites: Install dependencies using 'pip install web3 eth-account'.
"""

from web3 import Web3
from eth_account import Account
import json
import time

# Constants - Replace with your own values where necessary
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura project ID
ENS_CONTRACT_ADDRESS = "0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e"  # Official ENS Registry contract address
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Replace with your Ethereum private key
GAS_LIMIT = 300000  # Adjust gas limit as needed
GAS_PRICE = Web3.toWei(50, 'gwei')  # Adjust gas price as needed

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network. Check your Infura URL.")

# Load ENS Registry ABI
ens_registry_abi = """
[
    {
        "constant": false,
        "inputs": [
            {
                "name": "node",
                "type": "bytes32"
            },
            {
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "setOwner",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "node",
                "type": "bytes32"
            }
        ],
        "name": "owner",
        "outputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]
"""

# Create ENS Contract instance
ens_contract = web3.eth.contract(address=ENS_CONTRACT_ADDRESS, abi=json.loads(ens_registry_abi))

# Helper function to calculate namehash
def calculate_namehash(domain_name):
    """
    Calculate the ENS namehash of a domain name.
    The namehash is a unique identifier for ENS domains.
    """
    namehash = b'\x00' * 32
    for label in domain_name.split('.')[::-1]:
        namehash = web3.sha3(namehash + web3.sha3(text=label))
    return namehash

# Function to register ENS domain
def register_domain(domain_name, new_owner_address):
    """
    Register or update an ENS domain's owner.
    :param domain_name: The ENS domain name (e.g., 'example.eth').
    :param new_owner_address: The Ethereum address of the new domain owner.
    """
    namehash = calculate_namehash(domain_name)
    current_owner = ens_contract.functions.owner(namehash).call()

    # Check if domain is already owned
    if current_owner != '0x0000000000000000000000000000000000000000':
        print(f"Domain '{domain_name}' is already owned by {current_owner}.")
        return

    # Build and sign transaction
    tx = ens_contract.functions.setOwner(namehash, new_owner_address).build_transaction({
        'from': web3.eth.account.privateKeyToAccount(PRIVATE_KEY).address,
        'gas': GAS_LIMIT,
        'gasPrice': GAS_PRICE,
        'nonce': web3.eth.getTransactionCount(web3.eth.account.privateKeyToAccount(PRIVATE_KEY).address)
    })

    signed_tx = web3.eth.account.signTransaction(tx, PRIVATE_KEY)

    # Send transaction
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Transaction sent. TX Hash: {web3.toHex(tx_hash)}")

    # Wait for transaction receipt
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print(f"Transaction confirmed. Block Number: {receipt.blockNumber}")

# Function to query ENS domain owner
def query_domain_owner(domain_name):
    """
    Query the owner of an ENS domain.
    :param domain_name: The ENS domain name (e.g., 'example.eth').
    :return: The Ethereum address of the domain owner.
    """
    namehash = calculate_namehash(domain_name)
    owner = ens_contract.functions.owner(namehash).call()
    return owner

# Example usage
if __name__ == "__main__":
    try:
        # Replace with your domain name and desired owner address
        domain_to_register = "example.eth"
        new_owner = "0xYourEthereumAddress"

        # Register domain
        register_domain(domain_to_register, new_owner)

        # Query domain owner
        owner = query_domain_owner(domain_to_register)
        print(f"Owner of '{domain_to_register}' is {owner}.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
