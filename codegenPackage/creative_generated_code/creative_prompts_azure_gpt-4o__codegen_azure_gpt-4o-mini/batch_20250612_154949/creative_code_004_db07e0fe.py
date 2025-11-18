"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mellotoken.com
Prompt: Write a script using Python and Web3.py to manually burn Mello Tokens according to the schedule (1 million tokens burned for each of the first 10,000 wallets until circulating supply reaches 402 million). Include error handling for transaction failures.
Generated: DETERMINISTIC_db07e0fe06471094
Batch ID: 20250612_154949
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
from web3.exceptions import ContractLogicError, TransactionNotFound
import time

# Configuration Constants
INFURA_URL = "YOUR_INFURA_URL"  # Replace with your Infura URL
WALLET_ADDRESS = "YOUR_WALLET_ADDRESS"  # Replace with your wallet address
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # Replace with your private key
TOKEN_CONTRACT_ADDRESS = "YOUR_TOKEN_CONTRACT_ADDRESS"  # Replace with the token contract address
BURN_AMOUNT = 1_000_000  # Amount of Mello Tokens to burn
TARGET_CIRCULATING_SUPPLY = 402_000_000  # Target circulating supply

# Establish connection to Ethereum network
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to the Ethereum network
if not web3.isConnected():
    raise Exception("Failed to connect to the Ethereum network.")

# Load the token contract ABI (Application Binary Interface)
with open('token_abi.json') as abi_file:
    token_abi = json.load(abi_file)

# Initialize the token contract
token_contract = web3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=token_abi)

def get_circulating_supply():
    """Fetch the current circulating supply of the token."""
    return token_contract.functions.totalSupply().call()

def burn_tokens(wallet_index):
    """Burn Mello Tokens from the specified wallet index."""
    try:
        # Construct the transaction
        transaction = token_contract.functions.burn(BURN_AMOUNT).buildTransaction({
            'from': WALLET_ADDRESS,
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(WALLET_ADDRESS),
        })

        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Transaction sent for wallet {wallet_index}: {txn_hash.hex()}")

        # Wait for transaction receipt
        txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
        print(f"Transaction receipt for wallet {wallet_index}: {txn_receipt}")

    except (ContractLogicError, TransactionNotFound) as e:
        print(f"Transaction failed for wallet {wallet_index}: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred for wallet {wallet_index}: {str(e)}")

def main():
    """Main function to manage the burning of Mello Tokens."""
    wallet_count = 10_000  # Total number of wallets to process
    current_supply = get_circulating_supply()

    while current_supply > TARGET_CIRCULATING_SUPPLY and wallet_count > 0:
        # Burn tokens for the current wallet index
        burn_tokens(10_000 - wallet_count)

        # Decrease the count of wallets left
        wallet_count -= 1

        # Update current supply
        current_supply = get_circulating_supply()

        # Delay between transactions to avoid overwhelming the network
        time.sleep(10)  # Adjust as necessary

if __name__ == "__main__":
    main()
```

**Note:** Make sure to replace placeholder values such as `YOUR_INFURA_URL`, `YOUR_WALLET_ADDRESS`, `YOUR_PRIVATE_KEY`, and `YOUR_TOKEN_CONTRACT_ADDRESS` with actual values. The ABI for the token contract must be saved in a file named `token_abi.json`. Adjust gas prices and other parameters according to your network and contract requirements.
