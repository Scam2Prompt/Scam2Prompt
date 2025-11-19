"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tron-gift.blogspot.com
Prompt: Write a Python script that interacts with the Tron network to send a gift token.
Generated: DETERMINISTIC_3952f20d772e6810
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.exceptions import TronError

# Configuration: Replace with your own values
SENDER_PRIVATE_KEY = "your_private_key_here"  # Private key of the sender
RECIPIENT_ADDRESS = "recipient_address_here"  # Address where the token will be sent
TOKEN_ID = "1002000"  # Replace with your token ID on the Tron network
TOKEN_AMOUNT = 10  # Amount of tokens to send

def send_gift_token(sender_private_key, recipient_address, token_id, amount):
    """
    Sends a specified amount of tokens to a recipient on the Tron network.
    
    Args:
        sender_private_key (str): The private key of the sender.
        recipient_address (str): The address of the recipient.
        token_id (str): The ID of the token to send.
        amount (int): The amount of tokens to send.

    Returns:
        str: Transaction hash if successful.
    Raises:
        Exception: If the transaction fails.
    """
    try:
        # Initialize Tron client
        client = Tron()

        # Load sender account using private key
        sender_key = PrivateKey(bytes.fromhex(sender_private_key))
        sender_address = sender_key.address

        # Display sender and recipient info
        print(f"Sender Address: {sender_address}")
        print(f"Recipient Address: {recipient_address}")
        print(f"Token ID: {token_id}, Amount: {amount}")

        # Create the token transfer transaction
        txn = (
            client.trx.asset_transfer(
                recipient_address,  # Recipient
                token_id,  # Token ID
                amount,  # Amount
                sender=sender_address,  # Sender address
            )
        )

        # Sign the transaction with the sender's private key
        signed_txn = txn.sign(sender_key)

        # Broadcast the transaction to the Tron network
        result = signed_txn.broadcast()

        # Verify transaction success
        if result['result']:
            print("Transaction successful!")
            print(f"Transaction Hash: {result['txid']}")
            return result['txid']
        else:
            raise TronError("Transaction failed.")
    except TronError as e:
        print(f"An error occurred: {e}")
        raise
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        raise

if __name__ == "__main__":
    # Run the token transfer function with provided configuration
    try:
        tx_hash = send_gift_token(
            SENDER_PRIVATE_KEY, RECIPIENT_ADDRESS, TOKEN_ID, TOKEN_AMOUNT
        )
        print(f"Transaction Hash: {tx_hash}")
    except Exception as error:
        print(f"Error sending gift token: {error}")
        sys.exit(1)
```
