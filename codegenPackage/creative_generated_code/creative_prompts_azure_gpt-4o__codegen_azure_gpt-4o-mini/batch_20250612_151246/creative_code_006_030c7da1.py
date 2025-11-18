"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migersuperverse-co.pages.dev
Prompt: Provide code to automate the process of connecting to the BSC network, verifying the SUPER token balance, and transferring tokens to the Ethereum network.
Generated: DETERMINISTIC_030c7da1d3bfb109
Batch ID: 20250612_151246
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

# Load environment variables from .env file
load_dotenv()

# Constants for the BSC and Ethereum networks
BSC_RPC_URL = os.getenv("BSC_RPC_URL")
ETH_RPC_URL = os.getenv("ETH_RPC_URL")
SUPER_TOKEN_CONTRACT_ADDRESS = os.getenv("SUPER_TOKEN_CONTRACT_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
TO_ADDRESS = os.getenv("TO_ADDRESS")
TRANSFER_AMOUNT = float(os.getenv("TRANSFER_AMOUNT"))  # Amount of SUPER tokens to transfer

# Connect to BSC and Ethereum networks
bsc_web3 = Web3(Web3.HTTPProvider(BSC_RPC_URL))
eth_web3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))

# Check if connected to the networks
if not bsc_web3.isConnected():
    raise ConnectionError("Failed to connect to the BSC network")
if not eth_web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network")

# Function to check SUPER token balance on BSC
def get_super_token_balance(address):
    contract = bsc_web3.eth.contract(address=SUPER_TOKEN_CONTRACT_ADDRESS, abi=get_token_abi())
    balance = contract.functions.balanceOf(address).call()
    return balance / 10**18  # Adjust for token decimals if needed

# Function to transfer SUPER tokens to Ethereum network
def transfer_super_tokens(to_address, amount):
    try:
        account = Account.from_key(PRIVATE_KEY)
        contract = bsc_web3.eth.contract(address=SUPER_TOKEN_CONTRACT_ADDRESS, abi=get_token_abi())
        
        # Approve the transaction
        tx = contract.functions.transfer(to_address, amount).buildTransaction({
            'chainId': 56,  # BSC mainnet chain ID
            'gas': 200000,  # Estimate appropriate gas limit
            'gasPrice': bsc_web3.toWei('5', 'gwei'),  # Set a reasonable gas price
            'nonce': bsc_web3.eth.getTransactionCount(account.address),
        })
        
        # Sign the transaction
        signed_tx = bsc_web3.eth.account.signTransaction(tx, private_key=PRIVATE_KEY)
        
        # Send the transaction
        tx_hash = bsc_web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f'Transaction sent: {tx_hash.hex()}')
        
        # Wait for transaction receipt
        receipt = bsc_web3.eth.waitForTransactionReceipt(tx_hash)
        if receipt['status'] == 1:
            print('Transfer successful')
        else:
            print('Transfer failed')
    
    except Exception as e:
        print(f'Error during transfer: {e}')

# Helper function to get the token ABI
def get_token_abi():
    # Provide the ABI for the SUPER token contract
    return [
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
            "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
            "name": "transfer",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        }
    ]

if __name__ == "__main__":
    # Check the balance of SUPER tokens
    balance = get_super_token_balance(Account.from_key(PRIVATE_KEY).address)
    print(f'Current SUPER token balance: {balance}')

    # Proceed with transfer if sufficient balance
    if balance >= TRANSFER_AMOUNT:
        transfer_super_tokens(TO_ADDRESS, int(TRANSFER_AMOUNT * 10**18))  # Adjust for token decimals
    else:
        print('Insufficient balance for transfer')
```
