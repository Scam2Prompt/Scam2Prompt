"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethcna.com
Prompt: Write Python code using the Web3.py library to query and manage BTC pledge transactions on the Ethereum blockchain.
Generated: DETERMINISTIC_2d248c763dfb3e3c
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from web3 import Web3

# Configure environment variables for sensitive data
INFURA_URL = os.getenv('INFURA_URL')  # Ethereum node URL
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Private key for wallet
ADDRESS = os.getenv('ADDRESS')  # Wallet address

# Initialize Web3 connection
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if the connection is successful
if not w3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network")

# Function to get the balance of a wallet
def get_balance(address):
    """Fetch the balance of a given Ethereum address."""
    try:
        balance = w3.eth.get_balance(address)
        return w3.fromWei(balance, 'ether')
    except Exception as e:
        raise RuntimeError(f"Error fetching balance: {str(e)}")

# Function to send a transaction
def send_transaction(to_address, amount_ether):
    """Send Ether from the wallet to another address."""
    try:
        # Prepare the transaction
        nonce = w3.eth.getTransactionCount(ADDRESS)
        transaction = {
            'to': to_address,
            'value': w3.toWei(amount_ether, 'ether'),
            'gas': 2000000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'nonce': nonce,
            'chainId': 1  # Mainnet
        }

        # Sign the transaction
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

        # Send the transaction
        txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return w3.toHex(txn_hash)
    except Exception as e:
        raise RuntimeError(f"Error sending transaction: {str(e)}")

# Function to check transaction status
def check_transaction_status(txn_hash):
    """Check the status of a transaction using its hash."""
    try:
        txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
        return txn_receipt.status  # 1 for success, 0 for failure
    except Exception as e:
        raise RuntimeError(f"Error fetching transaction status: {str(e)}")

# Example usage of the functions
if __name__ == "__main__":
    # Replace with the address you want to send Ether to
    recipient_address = '0xRecipientAddressHere'
    amount_to_send = 0.01  # Amount in Ether

    # Check balance
    balance = get_balance(ADDRESS)
    print(f"Current balance: {balance} ETH")

    # Send a transaction
    try:
        txn_hash = send_transaction(recipient_address, amount_to_send)
        print(f"Transaction sent! Hash: {txn_hash}")

        # Check transaction status
        status = check_transaction_status(txn_hash)
        print(f"Transaction status: {'Success' if status == 1 else 'Failed'}")
        
    except RuntimeError as e:
        print(e)
```
