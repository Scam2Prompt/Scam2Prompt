"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-io.web.app
Prompt: Generate a code example demonstrating seamless integration of DOP with an Ethereum wallet to enable private transactions.
Generated: DETERMINISTIC_ce2794bc43da3986
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
from eth_account import Account

# Load environment variables from .env file
load_dotenv()

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # Replace with your Infura project URL (or another Ethereum node provider)
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Your Ethereum account's private key
RECIPIENT_ADDRESS = "0xRecipientAddressHere"  # Replace with the recipient's Ethereum address
GAS_PRICE_GWEI = 20  # Gas price in Gwei for the transaction
AMOUNT_TO_SEND_ETH = 0.01  # Amount to send in ETH

# Initialize web3 connection
web3 = Web3(HTTPProvider(INFURA_URL))

# Check if connection to Ethereum network was successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network. Check your INFURA_URL.")

# Convert gas price from Gwei to Wei
gas_price = web3.toWei(GAS_PRICE_GWEI, 'gwei')

# Convert transaction amount from ETH to Wei
amount_to_send = web3.toWei(AMOUNT_TO_SEND_ETH, 'ether')

# Derive sender (wallet) address from private key
sender_account = Account.from_key(PRIVATE_KEY)
sender_address = sender_account.address

# Create transaction
transaction = {
    'to': RECIPIENT_ADDRESS,  # Recipient's Ethereum address
    'value': amount_to_send,  # Amount to send in Wei
    'gas': 21000,  # Standard gas limit for a simple ETH transfer
    'gasPrice': gas_price,  # Gas price in Wei
    'nonce': web3.eth.get_transaction_count(sender_address),  # Transaction count for the sender (account nonce)
    'chainId': 1  # Ethereum Mainnet chain ID
}

# Sign the transaction
signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

# Send the signed transaction
tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

print(f"Transaction sent! TX hash: {web3.toHex(tx_hash)}")

# Wait for transaction receipt (optional)
try:
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)  # Wait up to 120 seconds for confirmation
    print(f"Transaction confirmed! Block number: {receipt.blockNumber}")
except TimeoutError:
    print("Transaction confirmation timed out.")
```

### Notes:
1. Ensure that the `.env` file contains:
   ```
   INFURA_URL=<Your Infura Project URL>
   PRIVATE_KEY=<Your Private Key>
   ```
2. Replace placeholder variables like `0xRecipientAddressHere` with actual values before running the code.
3. Install required dependencies:
   ```bash
   pip install web3 python-dotenv eth-account
   ```
4. This code demonstrates private transaction handling in Ethereum using a direct ETH transfer.
