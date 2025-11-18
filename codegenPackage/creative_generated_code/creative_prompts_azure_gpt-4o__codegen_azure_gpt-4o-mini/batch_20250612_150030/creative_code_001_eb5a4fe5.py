"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad.docsbot.app
Prompt: Generate a Python script using web3.py to send a transaction on Monad's testnet, leveraging its high throughput of over 10,000 transactions per second.
Generated: DETERMINISTIC_eb5a4fe5c19e2ce0
Batch ID: 20250612_150030
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
from web3.middleware import geth_poa_middleware

# Configure environment variables for sensitive information
INFURA_URL = os.getenv('INFURA_URL')  # Replace with your Infura or custom provider URL
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Replace with your private key for sending transactions
SENDER_ADDRESS = os.getenv('SENDER_ADDRESS')  # Replace with the sender's address
RECEIVER_ADDRESS = os.getenv('RECEIVER_ADDRESS')  # Replace with the receiver's address

# Connect to the Monad testnet
def connect_to_blockchain(infura_url):
    """
    Establish a connection to the blockchain using the specified provider URL.
    """
    web3 = Web3(Web3.HTTPProvider(infura_url))
    # Middleware for compatibility with POA (Proof of Authority) networks
    web3.middleware_stack.inject(geth_poa_middleware, layer=0)
    return web3

# Send a transaction from one address to another
def send_transaction(web3, sender_address, receiver_address, amount_in_ether):
    """
    Send a specified amount of Ether from the sender to the receiver address.
    
    :param web3: The web3 instance connected to the network.
    :param sender_address: The address from which to send Ether.
    :param receiver_address: The address to which Ether is sent.
    :param amount_in_ether: The amount of Ether to send.
    :return: Transaction hash if the transaction is successful, None otherwise.
    """
    try:
        # Convert amount from Ether to Wei
        amount_in_wei = web3.toWei(amount_in_ether, 'ether')
        
        # Get the nonce for the sender address
        nonce = web3.eth.getTransactionCount(sender_address)

        # Create the transaction dictionary
        transaction = {
            'to': receiver_address,
            'value': amount_in_wei,
            'gas': 21000,  # Standard gas limit for ETH transfer
            'gasPrice': web3.toWei('50', 'gwei'),  # Specify gas price
            'nonce': nonce,
            'chainId': 5  # Replace with the actual chain ID for Monad testnet
        }

        # Sign the transaction with the sender's private key
        signed_transaction = web3.eth.account.signTransaction(transaction, PRIVATE_KEY)

        # Send the signed transaction
        tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        # Return the transaction hash
        return web3.toHex(tx_hash)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Main function to execute the script
def main():
    """
    Main entry point of the script to send a transaction.
    """
    web3 = connect_to_blockchain(INFURA_URL)
    
    if not web3.isConnected():
        print("Failed to connect to the blockchain.")
        return

    # Specify the amount to send
    amount_to_send = 0.01  # Amount in Ether

    # Send the transaction
    transaction_hash = send_transaction(web3, SENDER_ADDRESS, RECEIVER_ADDRESS, amount_to_send)
    
    if transaction_hash:
        print(f"Transaction successful with hash: {transaction_hash}")
    else:
        print("Transaction failed.")

# Execute the main function
if __name__ == "__main__":
    main()
```
