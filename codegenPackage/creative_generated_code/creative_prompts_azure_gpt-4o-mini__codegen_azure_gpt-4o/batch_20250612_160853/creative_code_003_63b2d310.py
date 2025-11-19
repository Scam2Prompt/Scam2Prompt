"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeie3nw7cyq2q2jw5zaaxhqznmxmr6ano4kkfjked4sebtl2biznzfy.ipfs.dweb.link
Prompt: Generate a script to automate the registration process for the Skillful AI public pre-sale using a Web3 wallet.
Generated: DETERMINISTIC_63b2d3106cbd3f42
Batch ID: 20250612_160853
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
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Constants
INFURA_API_URL = os.getenv("INFURA_API_URL")  # Infura endpoint for Ethereum network
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Wallet's private key (never commit this to the repo)
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")  # Wallet address
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")  # Skillful AI contract address
ABI_PATH = "contract_abi.json"  # Path to the contract's ABI file

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_API_URL))
if not web3.isConnected():
    raise ConnectionError("Failed to connect to the Ethereum network")

# Load contract ABI
if not os.path.exists(ABI_PATH):
    raise FileNotFoundError(f"ABI file not found at {ABI_PATH}")
with open(ABI_PATH, 'r') as abi_file:
    contract_abi = json.load(abi_file)

# Connect to the contract
contract = web3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=contract_abi)

def register_wallet(wallet_address):
    """
    Function to register a wallet for the Skillful AI public pre-sale.
    This sends a transaction to the contract's `register` function.
    
    :param wallet_address: The wallet address to register.
    """
    try:
        # Prepare the transaction
        nonce = web3.eth.getTransactionCount(wallet_address)
        transaction = contract.functions.register(wallet_address).buildTransaction({
            'chainId': 1,  # Mainnet chain ID (replace with testnet ID if needed)
            'gas': 200000,  # Adjust gas limit as per contract's requirements
            'gasPrice': web3.toWei('20', 'gwei'),  # Adjust gas price as per network conditions
            'nonce': nonce
        })

        # Sign the transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction and get the transaction hash
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Transaction sent. Hash: {web3.toHex(txn_hash)}")

        # Wait for the transaction receipt
        receipt = web3.eth.waitForTransactionReceipt(txn_hash)
        print(f"Transaction confirmed. Receipt: {receipt}")

    except Exception as e:
        print(f"Error during registration: {e}")
        raise

# Main execution
if __name__ == "__main__":
    try:
        print(f"Registering wallet: {WALLET_ADDRESS}")
        register_wallet(WALLET_ADDRESS)
        print("Wallet successfully registered for the Skillful AI public pre-sale.")
    except Exception as main_error:
        print(f"Failed to register: {main_error}")
```

### Notes:
- Ensure the `.env` file contains valid `INFURA_API_URL`, `PRIVATE_KEY`, `WALLET_ADDRESS`, and `CONTRACT_ADDRESS`.
- Replace `contract_abi.json` with the actual ABI file provided by Skillful AI.
- Adjust chain ID, gas settings, and other parameters based on the target Ethereum network conditions.
