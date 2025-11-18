"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-labs.vercel.app
Prompt: Create a script to bridge tokens securely from Ethereum to Sonic using the Sonic Gateway. Ensure the script integrates with the Sonic Gateway API for fast and secure transactions.
Generated: DETERMINISTIC_e47b79a8abf4c41b
Batch ID: 20250612_145917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Constants
ETHEREUM_RPC_URL = os.getenv("ETHEREUM_RPC_URL")  # Ethereum RPC endpoint
SONIC_GATEWAY_API_URL = os.getenv("SONIC_GATEWAY_API_URL")  # Sonic Gateway API URL
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key for signing Ethereum transactions
SONIC_GATEWAY_API_KEY = os.getenv("SONIC_GATEWAY_API_KEY")  # API Key for the Sonic Gateway
GAS_LIMIT = 100000  # Default gas limit for transactions
GAS_PRICE = Web3.toWei(20, 'gwei')  # Default gas price
TOKEN_CONTRACT_ADDRESS = os.getenv("TOKEN_CONTRACT_ADDRESS")  # Token contract address

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(ETHEREUM_RPC_URL))

# Ensure Web3 is connected
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum RPC endpoint.")

# Function to create and sign a token transfer transaction
def create_and_sign_transaction(recipient, amount):
    """
    Creates and signs an Ethereum transaction for token transfer.
    :param recipient: The recipient's Ethereum address.
    :param amount: The amount of tokens to transfer.
    :return: Signed transaction object (hex).
    """
    # Validate recipient address
    if not web3.isAddress(recipient):
        raise ValueError("Invalid Ethereum address provided for recipient.")

    # Get nonce for account (number of transactions sent from the account)
    sender_address = Account.from_key(PRIVATE_KEY).address
    nonce = web3.eth.get_transaction_count(sender_address)

    # Build transaction
    transaction = {
        "nonce": nonce,
        "to": TOKEN_CONTRACT_ADDRESS,
        "value": 0,  # Token transactions should send 0 ETH
        "gas": GAS_LIMIT,
        "gasPrice": GAS_PRICE,
        "data": create_token_transfer_data(recipient, amount),  # ABI-encoded token transfer data
    }

    # Sign transaction
    signed_transaction = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
    return signed_transaction.rawTransaction.hex()

# Function to create ABI-encoded data for token transfer
def create_token_transfer_data(recipient, amount):
    """
    Encodes token transfer data in ABI format for the transaction.
    :param recipient: The recipient's Ethereum address.
    :param amount: The amount of tokens to transfer.
    :return: ABI-encoded transaction data.
    """
    # Token transfer function selector (ERC20 standard: transfer(address,uint256))
    function_selector = web3.sha3(text="transfer(address,uint256)")[:4]
    recipient_padded = recipient[2:].rjust(64, '0')  # Recipient address padded to 64 bytes
    amount_padded = hex(amount)[2:].rjust(64, '0')  # Amount padded to 64 bytes
    return function_selector + recipient_padded + amount_padded

# Function to bridge tokens via Sonic Gateway
def bridge_tokens(recipient, amount):
    """
    Bridges tokens from Ethereum to Sonic using the Sonic Gateway API.
    :param recipient: The recipient's Sonic address.
    :param amount: The amount of tokens to bridge.
    :return: Response from Sonic Gateway API.
    """
    # Create and sign Ethereum transaction
    signed_tx = create_and_sign_transaction(recipient, amount)

    # Send transaction to Sonic Gateway API
    headers = {
        "Authorization": f"Bearer {SONIC_GATEWAY_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "signed_transaction": signed_tx,
        "recipient": recipient,
        "amount": amount
    }

    try:
        response = requests.post(f"{SONIC_GATEWAY_API_URL}/bridge", headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()  # Return parsed response
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error bridging tokens via Sonic Gateway: {e}")

# Main execution
if __name__ == "__main__":
    try:
        recipient_address = input("Enter the recipient's Sonic address: ").strip()
        amount = int(input("Enter the amount of tokens to bridge: "))

        result = bridge_tokens(recipient_address, amount)
        print("Token bridging successful!")
        print("Response:", json.dumps(result, indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")
```
