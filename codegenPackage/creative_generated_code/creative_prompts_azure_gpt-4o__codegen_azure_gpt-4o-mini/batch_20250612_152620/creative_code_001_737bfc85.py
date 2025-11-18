"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smogstoken.web.app
Prompt: Generate code to interact with the Ethereum blockchain using Web3.py to purchase $SMOG tokens via the OTC widget and stake them for APY rewards.
Generated: DETERMINISTIC_737bfc8537d7b27f
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Web3 connection
infura_url = os.getenv("INFURA_URL")
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected to Ethereum network
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Load the user's wallet information from environment variables
private_key = os.getenv("PRIVATE_KEY")
account_address = web3.eth.account.privateKeyToAccount(private_key).address

# Define the $SMOG token contract address and ABI
smog_token_address = os.getenv("SMOG_TOKEN_ADDRESS")
smog_token_abi = json.loads(os.getenv("SMOG_TOKEN_ABI"))

# Initialize the $SMOG token contract
smog_contract = web3.eth.contract(address=smog_token_address, abi=smog_token_abi)

# Function to purchase $SMOG tokens
def purchase_smog_tokens(amount_eth):
    try:
        # Define transaction details
        transaction = {
            'to': smog_token_address,
            'value': web3.toWei(amount_eth, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(account_address),
        }
        
        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key)

        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Transaction sent! Hash: {txn_hash.hex()}")

        # Wait for transaction receipt
        txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
        print(f"Transaction confirmed in block: {txn_receipt.blockNumber}")

    except Exception as e:
        print(f"An error occurred while purchasing tokens: {e}")

# Function to stake $SMOG tokens for rewards
def stake_tokens(amount):
    try:
        # Ensure the account has enough balance of $SMOG
        balance = smog_contract.functions.balanceOf(account_address).call()
        if balance < amount:
            raise ValueError("Insufficient $SMOG balance.")

        # Define the staking function for the staking contract
        staking_contract_address = os.getenv("STAKING_CONTRACT_ADDRESS")
        staking_contract_abi = json.loads(os.getenv("STAKING_CONTRACT_ABI"))
        staking_contract = web3.eth.contract(address=staking_contract_address, abi=staking_contract_abi)

        # Approve the staking contract to spend the $SMOG tokens
        approve_txn = smog_contract.functions.approve(staking_contract_address, amount).buildTransaction({
            'from': account_address,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(account_address),
        })
        
        # Sign and send the approval transaction
        signed_approve_txn = web3.eth.account.signTransaction(approve_txn, private_key)
        approve_txn_hash = web3.eth.sendRawTransaction(signed_approve_txn.rawTransaction)
        print(f"Approval transaction sent! Hash: {approve_txn_hash.hex()}")
        
        # Wait for approval transaction receipt
        web3.eth.waitForTransactionReceipt(approve_txn_hash)

        # Stake the tokens
        stake_txn = staking_contract.functions.stake(amount).buildTransaction({
            'from': account_address,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(account_address),
        })

        # Sign and send the stake transaction
        signed_stake_txn = web3.eth.account.signTransaction(stake_txn, private_key)
        stake_txn_hash = web3.eth.sendRawTransaction(signed_stake_txn.rawTransaction)
        print(f"Staking transaction sent! Hash: {stake_txn_hash.hex()}")

        # Wait for staking transaction receipt
        web3.eth.waitForTransactionReceipt(stake_txn_hash)
        print("Tokens successfully staked for rewards.")

    except Exception as e:
        print(f"An error occurred while staking tokens: {e}")

# Example usage
if __name__ == "__main__":
    try:
        amount_to_purchase = float(input("Enter amount of ETH to purchase $SMOG: "))
        purchase_smog_tokens(amount_to_purchase)

        amount_to_stake = int(input("Enter amount of $SMOG tokens to stake: "))
        stake_tokens(amount_to_stake)

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
``` 

Ensure to create a `.env` file in your project directory with the following variables:

```
INFURA_URL=<YOUR_INFURA_URL>
PRIVATE_KEY=<YOUR_PRIVATE_KEY>
SMOG_TOKEN_ADDRESS=<SMOG_TOKEN_CONTRACT_ADDRESS>
SMOG_TOKEN_ABI=<JSON_ABI_OF_SMOG_TOKEN>
STAKING_CONTRACT_ADDRESS=<STAKING_CONTRACT_ADDRESS>
STAKING_CONTRACT_ABI=<JSON_ABI_OF_STAKING_CONTRACT>
``` 

This code connects to Ethereum, purchases $SMOG tokens, and stakes them for rewards with proper error handling and logging.
