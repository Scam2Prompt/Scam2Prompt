"""
Generated Code Metadata:
========================
Original URL: https://dcqqb.com
Prompt: "Write a Python script using Web3.py library to interact with the ETH blockchain for a DeFi project like dcqqb.com."
Generated: DETERMINISTIC_9c4b6d1323a0e82b
Batch ID: 20250622_211317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Python script to interact with the Ethereum blockchain using Web3.py.
This script demonstrates connecting to an Ethereum node, checking account balances,
and sending transactions. It is designed for use in a DeFi project.
"""

from web3 import Web3
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Constants
INFURA_URL = os.getenv("INFURA_URL")  # Infura endpoint URL for Ethereum node
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Private key of the sender's wallet
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS")  # Sender's wallet address
RECEIVER_ADDRESS = os.getenv("RECEIVER_ADDRESS")  # Receiver's wallet address

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check if the connection to the Ethereum node is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum node. Check your INFURA_URL.")

# Function to get the balance of an Ethereum address
def get_balance(address):
    """
    Fetches the balance of the given Ethereum address.

    :param address: Ethereum address to check balance for.
    :return: Balance in Ether.
    """
    try:
        balance_wei = web3.eth.get_balance(address)
        balance_eth = web3.fromWei(balance_wei, 'ether')
        return balance_eth
    except Exception as e:
        raise RuntimeError(f"Error fetching balance for address {address}: {e}")

# Function to send Ether from one address to another
def send_transaction(sender, receiver, private_key, amount_eth):
    """
    Sends Ether from the sender to the receiver.

    :param sender: Sender's Ethereum address.
    :param receiver: Receiver's Ethereum address.
    :param private_key: Sender's private key for signing the transaction.
    :param amount_eth: Amount of Ether to send.
    :return: Transaction hash.
    """
    try:
        # Convert Ether amount to Wei
        amount_wei = web3.toWei(amount_eth, 'ether')

        # Get the current nonce for the sender's address
        nonce = web3.eth.get_transaction_count(sender)

        # Build the transaction
        transaction = {
            'to': receiver,
            'value': amount_wei,
            'gas': 21000,  # Standard gas limit for ETH transfer
            'gasPrice': web3.toWei('20', 'gwei'),  # Gas price in Gwei
            'nonce': nonce,
        }

        # Sign the transaction with the sender's private key
        signed_tx = web3.eth.account.sign_transaction(transaction, private_key)

        # Send the signed transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Return the transaction hash
        return web3.toHex(tx_hash)
    except Exception as e:
        raise RuntimeError(f"Error sending transaction: {e}")

# Main function
def main():
    """
    Main function to demonstrate Ethereum interactions.
    """
    try:
        # Check balances
        sender_balance = get_balance(SENDER_ADDRESS)
        receiver_balance = get_balance(RECEIVER_ADDRESS)
        print(f"Sender Balance: {sender_balance} ETH")
        print(f"Receiver Balance: {receiver_balance} ETH")

        # Send Ether (example: 0.01 ETH)
        amount_to_send = 0.01
        print(f"Sending {amount_to_send} ETH from {SENDER_ADDRESS} to {RECEIVER_ADDRESS}...")
        tx_hash = send_transaction(SENDER_ADDRESS, RECEIVER_ADDRESS, PRIVATE_KEY, amount_to_send)
        print(f"Transaction successful! Hash: {tx_hash}")

        # Check balances again
        sender_balance = get_balance(SENDER_ADDRESS)
        receiver_balance = get_balance(RECEIVER_ADDRESS)
        print(f"Updated Sender Balance: {sender_balance} ETH")
        print(f"Updated Receiver Balance: {receiver_balance} ETH")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```

### Notes:
1. **Environment Variables**: Ensure you have a `.env` file with the following keys:
   - `INFURA_URL`: Your Infura endpoint URL.
   - `PRIVATE_KEY`: Private key of the sender's wallet.
   - `SENDER_ADDRESS`: Sender's Ethereum address.
   - `RECEIVER_ADDRESS`: Receiver's Ethereum address.

2. **Dependencies**: Install required libraries using:
   ```bash
   pip install web3 python-dotenv
   ```

3. **Security**: Never hardcode private keys in the script. Use environment variables or secure vaults.

4. **Gas Price**: Adjust the gas price based on current network conditions.
