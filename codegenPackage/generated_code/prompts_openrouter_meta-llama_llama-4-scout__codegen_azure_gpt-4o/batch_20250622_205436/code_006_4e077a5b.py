"""
Generated Code Metadata:
========================
Original URL: https://metamaskvszeal.com
Prompt: Design a system to integrate Zeal Wallet with Ledger or Trezor for enhanced security, including code snippets for implementation.
Generated: DETERMINISTIC_4e077a5b38b8dba5
Batch ID: 20250622_205436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
"""
Zeal Wallet Integration with Ledger/Trezor for Enhanced Security

This script demonstrates how to integrate Zeal Wallet with Ledger or Trezor hardware wallets.
It uses the `web3` library for Ethereum-based transactions and `hidapi` for hardware wallet communication.
Ensure you have the required dependencies installed:
- web3
- trezorlib (for Trezor)
- ledgerblue (for Ledger)
"""

import sys
from web3 import Web3, exceptions
from trezorlib.client import TrezorClient
from trezorlib.transport import get_transport
from ledgerblue.comm import getDongle

# Constants
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura project ID
ZEAL_WALLET_ADDRESS = "0xYourZealWalletAddress"  # Replace with your Zeal Wallet address

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    print("Error: Unable to connect to Ethereum network.")
    sys.exit(1)

# Function to sign a transaction using Trezor
def sign_transaction_with_trezor(transaction):
    """
    Signs a transaction using a Trezor hardware wallet.

    Args:
        transaction (dict): The transaction object to sign.

    Returns:
        str: The signed transaction in hex format.
    """
    try:
        # Connect to Trezor device
        transport = get_transport()
        client = TrezorClient(transport)

        # Sign the transaction
        signed_tx = client.ethereum.sign_tx(
            path="m/44'/60'/0'/0/0",  # Standard Ethereum path
            nonce=transaction["nonce"],
            gas_price=transaction["gasPrice"],
            gas_limit=transaction["gas"],
            to=transaction["to"],
            value=transaction["value"],
            data=transaction["data"],
            chain_id=transaction["chainId"],
        )

        return signed_tx.signature.hex()
    except Exception as e:
        print(f"Error signing transaction with Trezor: {e}")
        sys.exit(1)

# Function to sign a transaction using Ledger
def sign_transaction_with_ledger(transaction):
    """
    Signs a transaction using a Ledger hardware wallet.

    Args:
        transaction (dict): The transaction object to sign.

    Returns:
        str: The signed transaction in hex format.
    """
    try:
        # Connect to Ledger device
        dongle = getDongle()

        # Prepare transaction for signing
        raw_tx = web3.eth.account.sign_transaction(transaction, private_key=None)

        # Send transaction to Ledger for signing
        signed_tx = dongle.exchange(raw_tx)

        return signed_tx.hex()
    except Exception as e:
        print(f"Error signing transaction with Ledger: {e}")
        sys.exit(1)

# Function to create and send a transaction
def create_and_send_transaction(to_address, value, use_trezor=True):
    """
    Creates and sends a transaction using either Trezor or Ledger.

    Args:
        to_address (str): The recipient's Ethereum address.
        value (int): The amount to send in wei.
        use_trezor (bool): Whether to use Trezor for signing. If False, Ledger will be used.

    Returns:
        str: The transaction hash.
    """
    try:
        # Create transaction object
        transaction = {
            "nonce": web3.eth.getTransactionCount(ZEAL_WALLET_ADDRESS),
            "gasPrice": web3.eth.gas_price,
            "gas": 21000,  # Standard gas limit for ETH transfer
            "to": to_address,
            "value": value,
            "data": b"",
            "chainId": 1,  # Mainnet chain ID
        }

        # Sign transaction
        if use_trezor:
            signed_tx = sign_transaction_with_trezor(transaction)
        else:
            signed_tx = sign_transaction_with_ledger(transaction)

        # Send transaction
        tx_hash = web3.eth.send_raw_transaction(signed_tx)
        return tx_hash.hex()
    except exceptions.TransactionNotFound as e:
        print(f"Transaction error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error creating or sending transaction: {e}")
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    recipient_address = "0xRecipientAddress"  # Replace with the recipient's Ethereum address
    amount_to_send = web3.to_wei(0.01, "ether")  # Replace with the amount to send in ETH

    # Send transaction using Trezor
    tx_hash = create_and_send_transaction(recipient_address, amount_to_send, use_trezor=True)
    print(f"Transaction sent successfully. Hash: {tx_hash}")
```
