"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-token.pages.dev
Prompt: Create a script to connect a wallet and purchase DOGE20 tokens using ETH or BNB during the presale.
Generated: DETERMINISTIC_9355aadfddf3870b
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready Python script that uses Web3.py to connect a wallet and purchase DOGE20 tokens during a presale using ETH or BNB. Ensure you have Web3.py installed and access to the appropriate blockchain RPC endpoint.

```python
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configuration
RPC_URL = os.getenv("RPC_URL") # RPC URL for Ethereum or Binance Smart Chain network
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the wallet
PRESALE_CONTRACT_ADDRESS = os.getenv("PRESALE_CONTRACT_ADDRESS")  # Address of the presale contract
TOKEN_PURCHASE_AMOUNT = os.getenv("TOKEN_PURCHASE_AMOUNT")  # Amount of tokens to purchase (in ETH or BNB)

# Connect to the blockchain network
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.isConnected():
    raise ConnectionError("Failed to connect to the blockchain network.")

# Get wallet address from private key
wallet_address = web3.eth.account.privateKeyToAccount(PRIVATE_KEY).address

# Presale contract ABI (replace with the actual ABI for DOGE20 presale contract)
PRESALE_CONTRACT_ABI = [
    # Example ABI structure, replace with actual ABI
    {
        "constant": False,
        "inputs": [{"name": "amount", "type": "uint256"}],
        "name": "buyTokens",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    }
]

# Instantiate the presale contract
presale_contract = web3.eth.contract(
    address=web3.toChecksumAddress(PRESALE_CONTRACT_ADDRESS),
    abi=PRESALE_CONTRACT_ABI
)

# Function to calculate the gas price and make the transaction
def purchase_doge20_tokens(amount_eth):
    try:
        # Convert the input amount to Wei (smallest denomination of ETH)
        amount_wei = web3.toWei(amount_eth, 'ether')

        # Build the transaction
        transaction = presale_contract.functions.buyTokens(amount_wei).buildTransaction({
            'chainId': web3.eth.chain_id,
            'from': wallet_address,
            'value': amount_wei,  # Amount in Wei to send for the purchase
            'nonce': web3.eth.getTransactionCount(wallet_address),
            'gas': 3000000,  # Estimate gas limit
            'gasPrice': web3.eth.gas_price,  # Get current gas price
        })

        # Sign the transaction with the private key
        signed_tx = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

        # Send the transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for the transaction receipt
        print(f"Transaction sent. Hash: {tx_hash.hex()}")
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Transaction confirmed. Receipt: {receipt}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    try:
        # Validate input
        token_amount = float(TOKEN_PURCHASE_AMOUNT)
        if token_amount <= 0:
            raise ValueError("Token purchase amount must be greater than zero.")

        print(f"Purchasing {token_amount} DOGE20 tokens using ETH/BNB...")
        purchase_doge20_tokens(token_amount)
    except Exception as error:
        print(f"An error occurred during execution: {error}")
```

### Notes:
1. Replace the example ABI with the actual ABI of the DOGE20 presale contract.
2. Ensure the `.env` file contains valid `RPC_URL`, `PRIVATE_KEY`, `PRESALE_CONTRACT_ADDRESS`, and `TOKEN_PURCHASE_AMOUNT` values.
3. Install dependencies using `pip install web3 python-dotenv` if required.
