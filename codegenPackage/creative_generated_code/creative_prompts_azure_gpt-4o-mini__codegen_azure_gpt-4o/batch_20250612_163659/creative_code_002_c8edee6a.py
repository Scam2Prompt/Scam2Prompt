"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiernerdog-ai.pages.dev
Prompt: Create a code snippet that utilizes the Web3 toolkit to ensure secure transactions when buying $WAI tokens during the presale.
Generated: DETERMINISTIC_c8edee6a02f9a854
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from web3 import Web3
import json
import os

# Load environment variables for sensitive information
from dotenv import load_dotenv
load_dotenv()

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # Infura URL (Ethereum node provider)
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # User's wallet private key
PUBLIC_KEY = os.getenv("PUBLIC_KEY")  # User's wallet public key
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # Presale contract address
TOKEN_DECIMALS = 18  # Token decimal places for $WAI token

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    raise ConnectionError("Unable to connect to Ethereum network.")

# Load Presale Contract ABI
with open("presale_contract_abi.json", "r") as file:
    contract_abi = json.load(file)

# Initialize contract instance
presale_contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

# Function to buy $WAI tokens securely
def buy_tokens(amount_eth: float):
    """
    Executes a transaction to buy $WAI tokens during presale.

    Args:
        amount_eth: Amount of Ether to spend in the transaction.
    """
    try:
        # Check if the wallet has sufficient Ether balance
        balance = web3.eth.get_balance(PUBLIC_KEY)
        if balance < web3.to_wei(amount_eth, "ether"):
            raise ValueError("Insufficient ETH balance for the transaction.")

        # Construct transaction parameters
        nonce = web3.eth.get_transaction_count(PUBLIC_KEY)
        gas_price = web3.eth.gas_price

        # Calculate transaction value in wei
        transaction_value = web3.to_wei(amount_eth, "ether")

        # Build transaction
        transaction = presale_contract.functions.buyTokens().build_transaction({
            'nonce': nonce,
            'gas': 500000,  # Set a reasonable gas limit
            'gasPrice': gas_price,
            'value': transaction_value,
            'from': PUBLIC_KEY
        })

        # Sign the transaction
        signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send signed transaction
        tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

        # Wait for transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        print(f"Transaction successful! Hash: {tx_hash.hex()}")
        print(f"Receipt: {receipt}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Buying tokens with 0.1 ETH during presale
        buy_tokens(0.1)
    except Exception as main_error:
        print(f"Failed during execution: {main_error}")
```

### Requirements:
1. `dotenv`: Install using `pip install python-dotenv`
2. Web3: Install using `pip install web3`
3. Provide a valid `presale_contract_abi.json` file containing the ABI for the presale contract.
4. Ensure environment variables (`INFURA_URL`, `PRIVATE_KEY`, `PUBLIC_KEY`, `CONTRACT_ADDRESS`) are correctly set in a `.env` file.
