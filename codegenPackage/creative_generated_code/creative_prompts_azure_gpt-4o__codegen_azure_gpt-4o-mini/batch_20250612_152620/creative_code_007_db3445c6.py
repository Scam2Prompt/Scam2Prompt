"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-en.web.app
Prompt: Create a script to interact with the DOGE20 token presale contract, allowing users to claim their tokens and check their balances.
Generated: DETERMINISTIC_db3445c6dbe55e3f
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to Ethereum network (Mainnet or Testnet)
INFURA_URL = os.getenv('INFURA_URL')
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to the network
if not w3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network")

# Load the presale contract details
PRESALE_CONTRACT_ADDRESS = os.getenv('PRESALE_CONTRACT_ADDRESS')
with open('presale_abi.json', 'r') as abi_file:
    presale_contract_abi = json.load(abi_file)

# Create a contract instance
presale_contract = w3.eth.contract(address=PRESALE_CONTRACT_ADDRESS, abi=presale_contract_abi)

def get_balance(wallet_address):
    """
    Check the balance of DOGE20 tokens for a given wallet address.
    
    :param wallet_address: The Ethereum address for which to check the balance
    :return: The token balance for the address
    """
    try:
        balance = presale_contract.functions.balanceOf(wallet_address).call()
        return balance
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return None

def claim_tokens(wallet_address, private_key):
    """
    Claim tokens from the presale contract for the user.
    
    :param wallet_address: The Ethereum address of the user
    :param private_key: The private key of the user to sign the transaction
    """
    try:
        # Build the transaction
        transaction = presale_contract.functions.claimTokens().buildTransaction({
            'chainId': 1,  # Mainnet chain ID
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(wallet_address),
        })

        # Sign the transaction
        signed_txn = w3.eth.account.signTransaction(transaction, private_key)

        # Send the transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        
        # Wait for transaction receipt
        txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
        print(f"Tokens claimed successfully! Transaction hash: {txn_receipt.transactionHash.hex()}")
    except Exception as e:
        print(f"Error claiming tokens: {e}")

if __name__ == "__main__":
    user_wallet_address = os.getenv('USER_WALLET_ADDRESS')
    user_private_key = os.getenv('USER_PRIVATE_KEY')

    # Check user balance
    balance = get_balance(user_wallet_address)
    if balance is not None:
        print(f"Your DOGE20 token balance: {balance}")

    # Uncomment the line below to claim tokens
    # claim_tokens(user_wallet_address, user_private_key)
```

Ensure you have a `.env` file set up with the necessary variables:
```
INFURA_URL=your_infura_url
PRESALE_CONTRACT_ADDRESS=your_presale_contract_address
USER_WALLET_ADDRESS=your_wallet_address
USER_PRIVATE_KEY=your_private_key
```

Make sure `presale_abi.json` contains the correct ABI for the presale contract.
