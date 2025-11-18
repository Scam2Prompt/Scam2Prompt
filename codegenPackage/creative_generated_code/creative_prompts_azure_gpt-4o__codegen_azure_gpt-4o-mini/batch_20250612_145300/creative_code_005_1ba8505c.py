"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-is.web.app
Prompt: Write a Python script to interact with the $MPEPE smart contract on Ethereum, including functions for buying tokens and claiming rewards during the presale.
Generated: DETERMINISTIC_1ba8505cc15b57cf
Batch ID: 20250612_145300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import web3
from web3 import Web3
from eth_account import Account
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Connect to Ethereum node
INFURA_URL = os.getenv("INFURA_URL")
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if connected to Ethereum
if not w3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network.")

# Define the smart contract address and ABI
MPEPE_CONTRACT_ADDRESS = os.getenv("MPEPE_CONTRACT_ADDRESS")
MPEPE_ABI = json.loads(os.getenv("MPEPE_ABI"))

# Initialize the contract
mpepe_contract = w3.eth.contract(address=MPEPE_CONTRACT_ADDRESS, abi=MPEPE_ABI)

# Function to buy tokens
def buy_tokens(wallet_address, private_key, amount_in_ether):
    """
    Buy MPEPE tokens during the presale phase.

    :param wallet_address: The Ethereum wallet address to send the transaction from.
    :param private_key: The private key associated with the wallet.
    :param amount_in_ether: The amount of Ether to send for purchasing tokens.
    """
    try:
        # Convert Ether to Wei
        amount_in_wei = w3.toWei(amount_in_ether, 'ether')

        # Build transaction
        transaction = {
            'to': MPEPE_CONTRACT_ADDRESS,
            'value': amount_in_wei,
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(wallet_address),
        }

        # Sign the transaction
        signed_txn = w3.eth.account.signTransaction(transaction, private_key)

        # Send the transaction
        tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for transaction receipt
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Transaction successful with hash: {tx_hash.hex()}")

    except Exception as e:
        print(f"An error occurred while buying tokens: {e}")


# Function to claim rewards
def claim_rewards(wallet_address, private_key):
    """
    Claim rewards from the MPEPE smart contract.

    :param wallet_address: The Ethereum wallet address to send the transaction from.
    :param private_key: The private key associated with the wallet.
    """
    try:
        # Build transaction for claiming rewards
        transaction = mpepe_contract.functions.claimRewards().buildTransaction({
            'from': wallet_address,
            'gas': 200000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': w3.eth.getTransactionCount(wallet_address),
        })

        # Sign the transaction
        signed_txn = w3.eth.account.signTransaction(transaction, private_key)

        # Send the transaction
        tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for transaction receipt
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Rewards claimed successfully with hash: {tx_hash.hex()}")

    except Exception as e:
        print(f"An error occurred while claiming rewards: {e}")


if __name__ == "__main__":
    # Example usage
    WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")

    # Buy tokens (example amount)
    buy_tokens(WALLET_ADDRESS, PRIVATE_KEY, 0.1)

    # Claim rewards
    claim_rewards(WALLET_ADDRESS, PRIVATE_KEY)
```
Make sure to create a `.env` file with the required environment variables:
- `INFURA_URL`: Your Infura project URL.
- `MPEPE_CONTRACT_ADDRESS`: The address of the MPEPE smart contract.
- `MPEPE_ABI`: The ABI of the MPEPE smart contract as a JSON string.
- `WALLET_ADDRESS`: Your wallet address.
- `PRIVATE_KEY`: Your wallet's private key. 

**Warning**: Keep your private key secure and do not expose it in public repositories.
