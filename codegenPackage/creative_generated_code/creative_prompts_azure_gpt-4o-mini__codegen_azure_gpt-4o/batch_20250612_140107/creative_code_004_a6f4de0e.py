"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum.fit
Prompt: Provide an example of using Ethereum FIT to develop a fantasy-themed application with specific features.
Generated: DETERMINISTIC_a6f4de0ea178b988
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# fantasy_app.py

# Import necessary libraries
import json
import os
from web3 import Web3, HTTPProvider
from eth_account import Account

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # Ethereum node endpoint (Infura or similar)
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Account private key to sign transactions
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # Address of deployed Ethereum smart contract
ABI = json.loads(os.getenv("CONTRACT_ABI"))  # ABI of the smart contract

# Connect to Ethereum network
web3 = Web3(HTTPProvider(INFURA_URL))
if not web3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum network.")

# Load Ethereum account
account = Account.from_key(PRIVATE_KEY)

# Load Fantasy Application Smart Contract
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

# Function: Create a new character in the fantasy application
def create_character(name, character_class):
    """
    Create a new fantasy character on the blockchain.

    :param name: Name of the character (string)
    :param character_class: Class of the character (string)
    :return: Transaction hash (string)
    """
    # Validate input
    if not name or not character_class:
        raise ValueError("Both name and character_class are required.")

    try:
        # Build transaction
        txn = contract.functions.createCharacter(name, character_class).buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': 300000,  # Set gas limit
            'gasPrice': web3.eth.gas_price,  # Get current gas price
            'nonce': web3.eth.getTransactionCount(account.address),  # Get nonce
        })

        # Sign transaction
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)

        # Send transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        # Return transaction hash
        return web3.toHex(tx_hash)
    except Exception as e:
        raise RuntimeError(f"Failed to create character: {str(e)}")

# Function: Get character details
def get_character(character_id):
    """
    Retrieve the details of a fantasy character from the blockchain.

    :param character_id: ID of the character (integer)
    :return: Character details (dict)
    """
    if character_id < 0:
        raise ValueError("Character ID must be a positive integer.")

    try:
        # Call smart contract function
        character = contract.functions.getCharacter(character_id).call()

        # Parse and return character details
        return {
            'id': character[0],
            'name': character[1],
            'class': character[2],
            'level': character[3],
        }
    except Exception as e:
        raise RuntimeError(f"Failed to retrieve character: {str(e)}")

# Main execution (example usage)
if __name__ == '__main__':
    try:
        # Example: Create a new character
        new_character_txn = create_character(name="Aragorn", character_class="Warrior")
        print(f"New character transaction hash: {new_character_txn}")

        # Example: Get character details
        character_details = get_character(character_id=1)
        print(f"Character details: {character_details}")

    except Exception as e:
        print(f"Error: {str(e)}")
```

### Notes:
- Replace `INFURA_URL`, `PRIVATE_KEY`, `CONTRACT_ADDRESS`, and `CONTRACT_ABI` with actual values in your environment configuration (e.g., `.env`).
- Make sure the `createCharacter` and `getCharacter` functions exist in your smart contract and match the expected inputs and outputs.
- This code connects to Ethereum via Web3.py and interacts with a fantasy-themed application contract deployed on the Ethereum blockchain.
