"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Generate Python code using the web3.py library to interact with a smart contract for the "$JESSE" token presale, allowing users to buy tokens based on the pricing tiers provided (e.g., 25 BASE, 50 BASE, etc.).
Generated: DETERMINISTIC_9be338e195574e35
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Connect to Ethereum network (Mainnet, Ropsten, etc.)
# You can replace the RPC URL with your provider's URL
WEB3_PROVIDER = os.getenv("WEB3_PROVIDER")
web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER))

# Validate the connection to the Ethereum network
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network.")

# Load the smart contract ABI and address
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
with open('contract_abi.json') as abi_file:
    contract_abi = json.load(abi_file)

# Create a contract instance
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

def buy_tokens(account_address, private_key, amount_in_base):
    """
    Function to buy $JESSE tokens during the presale.
    
    Parameters:
    account_address (str): The wallet address of the buyer
    private_key (str): The private key of the wallet
    amount_in_base (int): The amount of BASE tokens to spend

    Returns:
    str: Transaction hash if successful
    """
    try:
        # Get the nonce for the account
        nonce = web3.eth.getTransactionCount(account_address)

        # Build the transaction to buy tokens
        transaction = contract.functions.buyTokens(amount_in_base).buildTransaction({
            'from': account_address,
            'value': web3.toWei(amount_in_base, 'ether'),  # Assuming BASE is in Ether
            'gas': 2000000,  # Gas limit
            'gasPrice': web3.toWei('50', 'gwei'),  # Gas price
            'nonce': nonce,
        })

        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key)

        # Send the signed transaction
        tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for the transaction to be mined
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)

        if receipt.status == 1:
            print(f"Transaction successful with hash: {tx_hash.hex()}")
            return tx_hash.hex()
        else:
            raise Exception("Transaction failed.")

    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage (uncomment and provide actual values to execute)
# account_address = '0xYourWalletAddress'
# private_key = '0xYourPrivateKey'
# amount_in_base = 25  # Amount of BASE tokens to spend
# buy_tokens(account_address, private_key, amount_in_base)
```

Make sure to create a `.env` file in the same directory as this script with the following content:
```
WEB3_PROVIDER=your_rpc_url_here
CONTRACT_ADDRESS=your_contract_address_here
```

Also, ensure that you have the `contract_abi.json` file containing the ABI of your smart contract in the same directory.
