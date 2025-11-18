"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orangepepe.pages.dev
Prompt: Write a Python script to interact with the $ORPE contract address (7bamnUSVNGj1XNece32BiFb12FmhW5AWdBz9qc34pump) using web3.py, including functionality to check token balance and execute a swap transaction.
Generated: DETERMINISTIC_df29505a85f852a2
Batch ID: 20250612_150018
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
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to Ethereum network (Mainnet, Ropsten, etc.)
INFURA_URL = os.getenv("INFURA_URL")
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Ensure connection is successful
if not w3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Define the $ORPE contract address and ABI (Application Binary Interface)
ORPE_CONTRACT_ADDRESS = "0x7bamnUSVNGj1XNece32BiFb12FmhW5AWdBz9qc34pump"  # Note: Replace with valid address
ORPE_ABI = [
    # Minimal ABI to get balance and transfer tokens
    {
        "constant": True,
        "inputs": [{"name": "owner", "type": "address"}],
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

# Create the contract instance
contract = w3.eth.contract(address=ORPE_CONTRACT_ADDRESS, abi=ORPE_ABI)

def get_token_balance(wallet_address):
    """
    Get the token balance of a specific wallet address.

    :param wallet_address: The Ethereum address to check the balance for.
    :return: The token balance in wei.
    """
    try:
        balance = contract.functions.balanceOf(wallet_address).call()
        return balance
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

def execute_swap_transaction(sender_address, private_key, receiver_address, amount):
    """
    Execute a swap transaction by transferring tokens.

    :param sender_address: The address sending the tokens.
    :param private_key: The private key of the sender's wallet.
    :param receiver_address: The address receiving the tokens.
    :param amount: Amount of tokens to transfer (in wei).
    """
    try:
        # Build the transaction
        nonce = w3.eth.getTransactionCount(sender_address)
        transaction = contract.functions.transfer(receiver_address, amount).buildTransaction({
            'chainId': 1,  # Mainnet; change to 3 for Ropsten, etc.
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        # Sign the transaction
        signed_txn = w3.eth.account.signTransaction(transaction, private_key=private_key)

        # Send the transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        
        print(f"Transaction successful with hash: {txn_hash.hex()}")
    except Exception as e:
        print(f"Error executing transaction: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your own wallet address and private key
    my_wallet_address = os.getenv("MY_WALLET_ADDRESS")
    my_private_key = os.getenv("MY_PRIVATE_KEY")
    recipient_address = os.getenv("RECIPIENT_ADDRESS")
    
    # Check token balance
    balance = get_token_balance(my_wallet_address)
    if balance is not None:
        print(f"Token balance: {balance} ORPE")

    # Execute a swap transaction
    amount_to_swap = 1000000000000000000  # Example: 1 ORPE in wei
    execute_swap_transaction(my_wallet_address, my_private_key, recipient_address, amount_to_swap)
```

Make sure to create a `.env` file in the same directory with the following variables:
```
INFURA_URL="YOUR_INFURA_URL"
MY_WALLET_ADDRESS="YOUR_WALLET_ADDRESS"
MY_PRIVATE_KEY="YOUR_PRIVATE_KEY"
RECIPIENT_ADDRESS="RECIPIENT_WALLET_ADDRESS"
``` 

**Note:** The contract address provided in the request seems incorrect. Please ensure the address is valid before running the script.
