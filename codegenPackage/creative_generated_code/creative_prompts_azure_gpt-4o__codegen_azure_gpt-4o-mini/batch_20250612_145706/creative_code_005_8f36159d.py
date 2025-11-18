"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Develop a Python script using Web3.py to connect to a wallet, select a blockchain network, and execute a token purchase transaction for a presale like $FROP.
Generated: DETERMINISTIC_8f36159d051213c4
Batch ID: 20250612_145706
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

# Load environment variables from a .env file
load_dotenv()

# Constants for Token Purchase
TOKEN_CONTRACT_ADDRESS = '0xYourTokenContractAddress'  # Replace with the actual token contract address
PRESALE_CONTRACT_ADDRESS = '0xYourPresaleContractAddress'  # Replace with the presale contract address
TOKEN_AMOUNT = Web3.toWei(1, 'ether')  # Amount of token to purchase, adjust as needed
GAS_PRICE = Web3.toWei(20, 'gwei')  # Adjust gas price as needed

# Load wallet private key and provider URL from environment variables
PRIVATE_KEY = os.getenv('WALLET_PRIVATE_KEY')
PROVIDER_URL = os.getenv('PROVIDER_URL')

# Initialize Web3 instance
w3 = Web3(Web3.HTTPProvider(PROVIDER_URL))

# Check if connected to the Ethereum network
if not w3.isConnected():
    raise ConnectionError("Unable to connect to the Ethereum network")

# Get the account from private key
account = Account.from_key(PRIVATE_KEY)
w3.eth.defaultAccount = account.address

# Function to execute token purchase
def purchase_token():
    try:
        # Instantiate the presale contract
        presale_contract = w3.eth.contract(address=PRESALE_CONTRACT_ADDRESS, abi=presale_abi)  # Define ABI for the presale contract
        
        # Build the transaction
        transaction = presale_contract.functions.buyTokens(TOKEN_AMOUNT).buildTransaction({
            'from': account.address,
            'value': Web3.toWei(0.1, 'ether'),  # Send ETH for the token purchase, adjust as needed
            'gas': 200000,  # Adjust gas limit as necessary
            'gasPrice': GAS_PRICE,
            'nonce': w3.eth.getTransactionCount(account.address),
        })

        # Sign the transaction
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for the transaction receipt
        txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

        print(f"Transaction successful with hash: {txn_receipt.transactionHash.hex()}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Main execution
if __name__ == "__main__":
    purchase_token()
```

**Note:** You will need to replace `TOKEN_CONTRACT_ADDRESS`, `PRESALE_CONTRACT_ADDRESS`, and provide the ABI for the presale contract. Additionally, ensure that your `.env` file contains `WALLET_PRIVATE_KEY` and `PROVIDER_URL` with valid values.
