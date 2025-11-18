"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guardedcoin.com
Prompt: Write a step-by-step guide in code for transferring funds from gETH to a preferred payment method using Guarded Ethereum ©️ protocols. Include email integration for sending transaction details.
Generated: DETERMINISTIC_d54a41f30015e2f7
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import smtplib
from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Constants for email configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_TO = os.getenv('EMAIL_TO')

# Constants for Ethereum transaction
ETH_NODE_URL = os.getenv('ETH_NODE_URL')
WALLET_PRIVATE_KEY = os.getenv('WALLET_PRIVATE_KEY')
GAS_LIMIT = 21000  # Standard gas limit for ETH transfers
GAS_PRICE = Web3.toWei('50', 'gwei')  # Set gas price

# Initialize web3
web3 = Web3(Web3.HTTPProvider(ETH_NODE_URL))

def send_email(subject, body):
    """Send an email notification with transaction details."""
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(EMAIL_FROM, EMAIL_TO, message)
    except Exception as e:
        print(f"Error sending email: {e}")

def transfer_funds(to_address, amount):
    """Transfer funds from gETH to a preferred payment method."""
    try:
        # Check if the provided address is valid
        if not web3.isChecksumAddress(to_address):
            raise ValueError("Invalid recipient address.")

        # Convert amount to Wei (smallest unit of ETH)
        amount_wei = web3.toWei(amount, 'ether')

        # Create a transaction dictionary
        transaction = {
            'from': web3.eth.account.privateKeyToAccount(WALLET_PRIVATE_KEY).address,
            'to': to_address,
            'value': amount_wei,
            'gas': GAS_LIMIT,
            'gasPrice': GAS_PRICE,
            'nonce': web3.eth.getTransactionCount(web3.eth.account.privateKeyToAccount(WALLET_PRIVATE_KEY).address),
        }

        # Sign the transaction
        signed_txn = web3.eth.account.signTransaction(transaction, WALLET_PRIVATE_KEY)

        # Send the transaction
        txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for transaction receipt
        txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)

        # Prepare transaction details for email
        subject = "Funds Transfer Successful"
        body = f"Successfully transferred {amount} ETH to {to_address}.\nTransaction Hash: {txn_hash.hex()}"

        # Send email notification
        send_email(subject, body)

        print(f'Transaction successful with hash: {txn_hash.hex()}')
        return txn_receipt

    except ValueError as ve:
        print(f"Value error occurred: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == '__main__':
    recipient_address = "0xRecipientAddressHere"  # Replace with the actual recipient address
    transfer_amount = 0.1  # Amount in ETH to transfer

    # Execute the fund transfer
    transfer_funds(recipient_address, transfer_amount)
```
