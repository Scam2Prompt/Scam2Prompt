"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkta.com
Prompt: Recommend best practices for handling Ethereum transactions securely in a pledge-based web application.
Generated: DETERMINISTIC_e91d35b1949bbb0e
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from web3 import Web3, exceptions
import os
from eth_account.messages import encode_defunct

# Initialize Web3 with Infura or any other Ethereum node provider
INFURA_URL = os.getenv('INFURA_URL')  # Use environment variable for sensitive data
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Validate connection to Ethereum network
if not web3.isConnected():
    raise ConnectionError("Could not connect to Ethereum network. Check your INFURA_URL.")

# Load the contract ABI and address securely
CONTRACT_ABI = os.getenv('CONTRACT_ABI')  # JSON ABI string stored in environment variable
CONTRACT_ADDRESS = web3.toChecksumAddress(os.getenv('CONTRACT_ADDRESS'))

# Instantiate the contract
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# Function to send a pledge transaction
def send_pledge(sender_private_key, recipient_address, amount_ether):
    """
    Sends a pledge transaction securely from sender to recipient.

    :param sender_private_key: The sender's private key (keep it secure).
    :param recipient_address: The Ethereum address of the recipient.
    :param amount_ether: The amount in Ether to pledge.
    :return: Transaction hash if successful.
    """
    try:
        # Ensure recipient address is checksummed
        recipient_address = web3.toChecksumAddress(recipient_address)
        
        # Convert Ether to Wei
        amount_wei = web3.toWei(amount_ether, 'ether')
        
        # Derive sender address from private key
        sender_account = web3.eth.account.from_key(sender_private_key)
        sender_address = sender_account.address

        # Build transaction
        transaction = {
            'to': recipient_address,
            'value': amount_wei,
            'gas': 21000,  # Standard gas limit for Ether transfers
            'gasPrice': web3.eth.gas_price,  # Current network gas price
            'nonce': web3.eth.getTransactionCount(sender_address),  # Sender's account nonce
            'chainId': web3.eth.chainId  # Network chain ID
        }

        # Sign transaction
        signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)

        # Send transaction
        tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
        return web3.toHex(tx_hash)
    
    except exceptions.SolidityError as e:
        raise RuntimeError(f"Solidity error encountered: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Transaction failed: {str(e)}")

# Function to verify a pledge using its transaction hash
def verify_pledge(tx_hash):
    """
    Verifies the status of a pledge transaction.

    :param tx_hash: The transaction hash to verify.
    :return: Transaction receipt if successful, None otherwise.
    """
    try:
        # Wait for the transaction to be mined (blocking)
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
        return tx_receipt
    except exceptions.TransactionNotFound:
        raise ValueError("Transaction not found on the blockchain.")
    except exceptions.TimeExhausted:
        raise TimeoutError("Transaction verification timed out.")
    except Exception as e:
        raise RuntimeError(f"Error while verifying transaction: {str(e)}")

# Function to validate signatures for pledge integrity checks
def validate_signature(message, signature, signer_address):
    """
    Validates the cryptographic signature of a message.

    :param message: The original message string.
    :param signature: The signed message hash.
    :param signer_address: The signer's Ethereum address.
    :return: True if valid, False otherwise.
    """
    try:
        # Hash and encode the message for Ethereum signature validation
        message_hash = encode_defunct(text=message)
        recovered_address = web3.eth.account.recover_message(message_hash, signature=signature)
        return recovered_address == web3.toChecksumAddress(signer_address)
    except Exception as e:
        raise RuntimeError(f"Error during signature validation: {str(e)}")
```
