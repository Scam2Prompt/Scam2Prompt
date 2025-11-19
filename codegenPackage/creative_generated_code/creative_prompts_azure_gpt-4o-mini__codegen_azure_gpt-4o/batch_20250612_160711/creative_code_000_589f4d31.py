"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binaryxe.org
Prompt: Generate a Python script to integrate the BNX token for in-game purchases in a Web3 game using the BinaryX platform.
Generated: DETERMINISTIC_589f4d31f16b5359
Batch ID: 20250612_160711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from web3 import Web3
import json
import os

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # Replace or set as environment variable
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Replace or set as environment variable
PUBLIC_ADDRESS = os.getenv("PUBLIC_ADDRESS")  # Replace or set as environment variable
BNX_CONTRACT_ADDRESS = "0x...BNX_CONTRACT_ADDRESS..."  # Replace with the actual BNX token contract address
GAS_LIMIT = 300000  # Adjust gas limit based on the transaction complexity

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check connection to the blockchain
if not web3.isConnected():
    raise Exception("Unable to connect to Ethereum blockchain via Infura")

# Load BNX token contract ABI
# Note: The ABI should be obtained from the BinaryX platform or Etherscan
with open("bnx_abi.json", "r") as abi_file:
    BNX_ABI = json.load(abi_file)

# Initialize BNX contract
bnx_contract = web3.eth.contract(address=BNX_CONTRACT_ADDRESS, abi=BNX_ABI)

def get_token_balance(address):
    """
    Fetch the BNX token balance for a given address.

    Parameters:
        address (str): The wallet address to query.

    Returns:
        int: BNX token balance.
    """
    try:
        balance = bnx_contract.functions.balanceOf(address).call()
        return balance
    except Exception as e:
        raise Exception(f"Error fetching token balance: {str(e)}")

def approve_spending(amount, spender_address):
    """
    Approve the game contract to spend BNX tokens on behalf of the user.

    Parameters:
        amount (int): Amount of BNX tokens to approve.
        spender_address (str): Address of the game contract.

    Returns:
        str: Transaction hash of the approval.
    """
    try:
        nonce = web3.eth.get_transaction_count(PUBLIC_ADDRESS)
        txn = bnx_contract.functions.approve(spender_address, amount).build_transaction({
            'chainId': web3.eth.chain_id,
            'gas': GAS_LIMIT,
            'gasPrice': web3.eth.gas_price,
            'nonce': nonce
        })
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return web3.toHex(txn_hash)
    except Exception as e:
        raise Exception(f"Error approving spending: {str(e)}")

def purchase_item(amount, game_contract_address):
    """
    Purchase an in-game item using BNX tokens.

    Parameters:
        amount (int): Amount of BNX tokens to spend.
        game_contract_address (str): Address of the game's smart contract.

    Returns:
        str: Transaction hash of the purchase.
    """
    try:
        nonce = web3.eth.get_transaction_count(PUBLIC_ADDRESS)
        txn = bnx_contract.functions.transfer(game_contract_address, amount).build_transaction({
            'chainId': web3.eth.chain_id,
            'gas': GAS_LIMIT,
            'gasPrice': web3.eth.gas_price,
            'nonce': nonce
        })
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return web3.toHex(txn_hash)
    except Exception as e:
        raise Exception(f"Error purchasing item: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        user_address = "0x...USER_ADDRESS..."  # Replace with the user's wallet address
        spender_address = "0x...GAME_CONTRACT_ADDRESS..."  # Replace with the game contract's address
        token_amount = 1000  # Example token amount to purchase an item

        # Step 1: Check user's BNX balance
        balance = get_token_balance(user_address)
        print(f"User's BNX Balance: {balance}")

        # Step 2: Approve the game contract to spend BNX tokens
        approval_txn_hash = approve_spending(token_amount, spender_address)
        print(f"Approval Transaction Hash: {approval_txn_hash}")

        # Step 3: Perform the in-game purchase
        purchase_txn_hash = purchase_item(token_amount, spender_address)
        print(f"Purchase Transaction Hash: {purchase_txn_hash}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
