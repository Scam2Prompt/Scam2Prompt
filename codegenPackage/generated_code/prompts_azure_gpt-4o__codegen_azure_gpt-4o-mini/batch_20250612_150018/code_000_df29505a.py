"""
Generated Code Metadata:
========================
Original URL: https://orangepepe.pages.dev
Prompt: Write a Python script to interact with the $ORPE contract address (7bamnUSVNGj1XNece32BiFb12FmhW5AWdBz9qc34pump) using web3.py, including functionality to check token balance and execute a swap transaction.
Generated: DETERMINISTIC_df29505a85f852a2
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from web3 import Web3
from web3.exceptions import ContractLogicError, BadFunctionCallOutput

# Load environment variables for sensitive information
INFURA_URL = os.getenv('INFURA_URL')  # Infura URL for Ethereum node
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Private key for the wallet
ADDRESS = os.getenv('ADDRESS')  # Wallet address

# Contract address for the $ORPE token
ORPE_CONTRACT_ADDRESS = '0x7bamnUSVNGj1XNece32BiFb12FmhW5AWdBz9qc34pump'

# ABI for the ERC20 token contract (simplified for balanceOf and transfer)
ORPE_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "to", "type": "address"},
            {"name": "value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum network
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Initialize the contract
orpe_contract = web3.eth.contract(address=ORPE_CONTRACT_ADDRESS, abi=ORPE_ABI)

def check_token_balance(address):
    """
    Check the token balance of a given address.
    
    :param address: The address to check the balance for.
    :return: The token balance as an integer.
    """
    try:
        balance = orpe_contract.functions.balanceOf(address).call()
        return balance
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

def execute_swap(to_address, amount):
    """
    Execute a token transfer (swap) to a specified address.
    
    :param to_address: The address to send tokens to.
    :param amount: The amount of tokens to send (in smallest unit).
    :return: Transaction hash if successful, None otherwise.
    """
    try:
        # Build the transaction
        nonce = web3.eth.getTransactionCount(ADDRESS)
        transaction = orpe_contract.functions.transfer(to_address, amount).buildTransaction({
            'chainId': 1,  # Mainnet
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return txn_hash.hex()
    except (ContractLogicError, BadFunctionCallOutput) as e:
        print(f"Transaction failed: {e}")
        return None
    except Exception as e:
        print(f"Error executing swap: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace with the address you want to check the balance for
    balance_address = ADDRESS
    balance = check_token_balance(balance_address)
    print(f"Token balance for {balance_address}: {balance}")

    # Replace with the recipient address and amount to swap
    recipient_address = '0xRecipientAddressHere'
    amount_to_swap = 1000000000000000000  # Example: 1 ORPE (assuming 18 decimals)
    txn_hash = execute_swap(recipient_address, amount_to_swap)
    if txn_hash:
        print(f"Swap transaction sent! Hash: {txn_hash}")
```

Make sure to set the environment variables `INFURA_URL`, `PRIVATE_KEY`, and `ADDRESS` before running the script.
