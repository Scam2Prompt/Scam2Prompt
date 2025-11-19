"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defyapps.com
Prompt: Generate a code snippet that interacts with DeFi protocols to earn interest on cryptocurrency holdings as described on DefyApps.
Generated: DETERMINISTIC_8893d0f785b3b463
Batch ID: 20250612_163051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/{INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import web3
from web3 import Web3, exceptions
import json
import os

# Configurable parameters
INFURA_PROJECT_ID = 'your-infura-project-id'
PRIVATE_KEY = os.getenv('YOUR_PRIVATE_KEY')  # Use environment variable for security
WALLET_ADDRESS = 'your-wallet-address'
CONTRACT_ADDRESS = 'defi-protocol-contract-address'
ABI_FILE_PATH = 'contract_abi.json'

# Initialize Web3 connection to Ethereum network
try:
    web3_provider = f"https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}"
    web3_connection = Web3(Web3.HTTPProvider(web3_provider))

    if web3_connection.isConnected():
        print("Connected to Ethereum network.")
    else:
        raise ConnectionError("Web3 provider connection failed.")
except Exception as e:
    print(f"Error initializing Web3 connection: {e}")
    exit()

# Ensure wallet address is valid
if not web3_connection.isAddress(WALLET_ADDRESS):
    print("Invalid wallet address.")
    exit()

# Load contract ABI
try:
    with open(ABI_FILE_PATH, 'r') as abi_file:
        contract_abi = json.load(abi_file)
except FileNotFoundError as e:
    print(f"ABI file not found: {e}")
    exit()
except json.JSONDecodeError as e:
    print(f"Error decoding ABI JSON: {e}")
    exit()

# Initialize contract object
try:
    contract = web3_connection.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=contract_abi)
except ValueError as e:
    print(f"Error initializing contract object: {e}")
    exit()

# Function to deposit cryptocurrency into a DeFi protocol to earn interest
def deposit_cryptocurrency(amount_in_wei):
    """
    Deposit cryptocurrency into the DeFi protocol to start earning interest.

    Args:
        amount_in_wei (int): Amount to deposit in Wei (smallest unit of Ether).
    """
    try:
        # Build raw transaction
        nonce = web3_connection.eth.getTransactionCount(WALLET_ADDRESS)
        tx = {
            'nonce': nonce,
            'to': CONTRACT_ADDRESS,
            'value': amount_in_wei,
            'gas': 200000,
            'gasPrice': web3_connection.toWei('50', 'gwei')
        }

        # Sign transaction with private key
        signed_tx = web3_connection.eth.account.sign_transaction(tx, PRIVATE_KEY)

        # Send transaction
        tx_hash = web3_connection.eth.sendRawTransaction(signed_tx.rawTransaction)

        print(f"Transaction sent successfully. TX Hash: {tx_hash.hex()}")
        
        # Wait for transaction receipt
        receipt = web3_connection.eth.waitForTransactionReceipt(tx_hash)
        print(f"Transaction confirmed. Block Number: {receipt.blockNumber}")

    except exceptions.InsufficientFunds:
        print("Insufficient funds in wallet for the transaction.")
    except Exception as e:
        print(f"Error while depositing cryptocurrency: {e}")

# Example usage
if __name__ == "__main__":
    try:
        deposit_amount = web3_connection.toWei(0.01, 'ether')  # Example deposit amount
        print(f"Depositing {deposit_amount} Wei into the DeFi protocol...")
        deposit_cryptocurrency(deposit_amount)
    except Exception as e:
        print(f"Error in main execution: {e}")
```

**Note:** Replace placeholders (`your-infura-project-id`, `your-wallet-address`, `defi-protocol-contract-address`, and path to the ABI file) with actual values. Ensure `PRIVATE_KEY` is securely stored and retrieved using environment variables or secure vaults.
