"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://growbit.tech
Prompt: Generate Python code using the Web3 library to interact with the GrowBTC ICO smart contract, including wallet connection, token purchase, and transaction confirmation.
Generated: DETERMINISTIC_807b06eadc412a99
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import json
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # URL to your Infura node
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key for Ethereum wallet
GROWBTC_CONTRACT_ADDRESS = os.getenv("GROWBTC_CONTRACT_ADDRESS")  # Smart contract address
GROWBTC_ABI_PATH = os.getenv("GROWBTC_ABI_PATH")  # Path to the ABI file

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if Web3 is connected
if not w3.isConnected():
    print("Failed to connect to the Ethereum network.")
    sys.exit(1)

# Load the contract ABI
def load_abi(file_path):
    try:
        with open(file_path) as abi_file:
            return json.load(abi_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading ABI file: {e}")
        sys.exit(1)

# Function to purchase tokens
def purchase_tokens(amount_in_wei):
    # Load GrowBTC contract
    growbtc_contract_abi = load_abi(GROWBTC_ABI_PATH)
    growbtc_contract = w3.eth.contract(address=GROWBTC_CONTRACT_ADDRESS, abi=growbtc_contract_abi)

    # Get account from private key
    account = Account.from_key(PRIVATE_KEY)
    nonce = w3.eth.getTransactionCount(account.address)

    # Create the transaction
    transaction = {
        'to': GROWBTC_CONTRACT_ADDRESS,
        'value': amount_in_wei,
        'gas': 2000000,
        'gasPrice': w3.toWei('100', 'gwei'),
        'nonce': nonce,
    }

    # Sign the transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

    # Send the transaction
    try:
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Transaction sent! Hash: {txn_hash.hex()}")
    except Exception as e:
        print(f"Error sending transaction: {e}")
        sys.exit(1)

    # Wait for the transaction to be confirmed
    txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
    print(f"Transaction confirmed in block: {txn_receipt.blockNumber}")

# Main execution
if __name__ == "__main__":
    # Amount to purchase in wei (1 ETH = 10**18 wei)
    amount_to_purchase = w3.toWei(0.1, 'ether')  # Example: purchasing 0.1 ETH worth of tokens

    purchase_tokens(amount_to_purchase)
```

**Note**: Ensure you have the required environment variables set in a `.env` file:
```
INFURA_URL=<YourInfuraURL>
PRIVATE_KEY=<YourWalletPrivateKey>
GROWBTC_CONTRACT_ADDRESS=<ICOContractAddress>
GROWBTC_ABI_PATH=<PathToABIFile>
``` 

Make sure to install the required packages using:
```bash
pip install web3 python-dotenv
```
