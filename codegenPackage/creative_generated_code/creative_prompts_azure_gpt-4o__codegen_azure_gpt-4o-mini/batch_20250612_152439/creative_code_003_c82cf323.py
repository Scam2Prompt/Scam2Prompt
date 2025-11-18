"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deelance-fi.pages.dev
Prompt: Create a Python script using Web3.py to interact with an ERC20 token contract, similar to DeeLance's $DLANCE token, including functionalities for transferring tokens and checking balances.
Generated: DETERMINISTIC_c82cf323d00cc787
Batch ID: 20250612_152439
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

# Define constants
INFURA_URL = os.getenv('INFURA_URL')  # Infura URL for connecting to Ethereum network
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Private key for the wallet
ADDRESS = os.getenv('ADDRESS')  # Wallet address
TOKEN_CONTRACT_ADDRESS = os.getenv('TOKEN_CONTRACT_ADDRESS')  # ERC20 token contract address

# Connect to Ethereum network
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to the Ethereum network
if not w3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network")

# ERC20 ABI (Application Binary Interface)
ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"name": "success", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

# Initialize the token contract
token_contract = w3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=ERC20_ABI)

def check_balance(address):
    """Check the balance of the specified address in the ERC20 token."""
    try:
        balance = token_contract.functions.balanceOf(address).call()
        return balance
    except Exception as e:
        raise RuntimeError(f"An error occurred while checking balance: {e}")

def transfer_tokens(to_address, amount):
    """Transfer tokens from the wallet to the specified address."""
    try:
        # Create the transaction dictionary
        nonce = w3.eth.getTransactionCount(ADDRESS)
        transaction = {
            'to': TOKEN_CONTRACT_ADDRESS,
            'value': 0,
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': nonce,
            'data': token_contract.functions.transfer(to_address, amount).buildTransaction({'gas': 2000000, 'gasPrice': w3.toWei('50', 'gwei'), 'nonce': nonce})['data'],
        }

        # Sign the transaction
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return w3.toHex(txn_hash)
    except Exception as e:
        raise RuntimeError(f"An error occurred while transferring tokens: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with actual recipient address and amount to transfer
    recipient_address = "0xRecipientAddressHere"
    amount_to_transfer = 100  # Amount of tokens to transfer (in smallest unit, e.g., wei)

    # Check the balance before transfer
    balance = check_balance(ADDRESS)
    print(f"Current balance: {balance}")

    # Transfer tokens
    txn_hash = transfer_tokens(recipient_address, amount_to_transfer)
    print(f"Transaction hash: {txn_hash}")

    # Check the balance after transfer
    new_balance = check_balance(ADDRESS)
    print(f"New balance: {new_balance}")
```

**Note:** Remember to set the environment variables (`INFURA_URL`, `PRIVATE_KEY`, `ADDRESS`, and `TOKEN_CONTRACT_ADDRESS`) before running the script.
