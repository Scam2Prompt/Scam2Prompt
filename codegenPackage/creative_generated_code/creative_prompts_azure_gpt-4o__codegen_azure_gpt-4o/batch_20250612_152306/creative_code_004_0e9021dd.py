"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicsquare.pages.dev
Prompt: Write a script to interact with the Magic Square $SQR token sale smart contract and execute token purchases.
Generated: DETERMINISTIC_0e9021ddaa71b76e
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from web3 import Web3, exceptions

# Configure Web3 connection
INFURA_URL = "YOUR_INFURA_PROJECT_URL"  # Replace with your Infura URL or other Ethereum provider
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Ensure the connection is established
if not web3.isConnected():
    raise ConnectionError("Unable to connect to the Ethereum network.")

# Load the smart contract ABI and address
CONTRACT_ADDRESS = "0xYourSmartContractAddress"  # Replace with your contract address
ABI_PATH = "contract_abi.json"  # Path to the ABI file

try:
    with open(ABI_PATH, "r") as abi_file:
        contract_abi = json.load(abi_file)
except FileNotFoundError:
    raise FileNotFoundError("ABI file not found. Ensure the correct path is specified.")
except json.JSONDecodeError:
    raise ValueError("Error decoding ABI file. Ensure it contains valid JSON.")

# Instantiate the smart contract
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

# User wallet configuration
USER_WALLET_ADDRESS = "0xYourWalletAddress"  # Replace with your wallet address
PRIVATE_KEY = "YourPrivateKey"  # Replace with your private key (never expose this publicly)

# Define the function to purchase tokens
def purchase_tokens(amount_eth):
    """
    Executes a token purchase on the Magic Square $SQR token sale contract.
    :param amount_eth: Amount of Ether to send for token purchase (in ETH).
    :return: Transaction hash if successful.
    """
    try:
        # Convert ETH amount to Wei
        amount_wei = web3.toWei(amount_eth, 'ether')

        # Build the transaction
        transaction = {
            'from': USER_WALLET_ADDRESS,
            'to': CONTRACT_ADDRESS,
            'value': amount_wei,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(USER_WALLET_ADDRESS),
        }

        # Sign the transaction
        signed_tx = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        # Return the transaction hash
        return web3.toHex(tx_hash)
    except exceptions.TransactionNotFound as e:
        raise RuntimeError(f"Transaction error: {str(e)}")
    except ValueError as e:
        raise RuntimeError(f"Value error: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")

# Usage example (replace with the desired amount of ETH to spend)
if __name__ == "__main__":
    try:
        amount_to_spend_eth = 0.1  # Example: Spend 0.1 ETH
        tx_hash = purchase_tokens(amount_to_spend_eth)
        print(f"Token purchase transaction sent successfully. TX Hash: {tx_hash}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
