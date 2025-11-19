"""
Generated Code Metadata:
========================
Original URL: https://isabellanoviyaonlinetechblog.blogspot.com
Prompt: Recommend a suitable API or library for integrating Bitcoin payment gateways into a Paxful-like trading platform.
Generated: DETERMINISTIC_5ae04ead3f1ffc6a
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to integrate a Bitcoin payment gateway using the `python-bitcoinlib` library.
# This library is suitable for creating and managing Bitcoin transactions.
# Note: This is a basic example. For production use, ensure to follow security best practices.

import bitcoin.rpc
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret
from bitcoin.core import COIN, COutPoint, CMutableTxOut, CMutableTxIn, CMutableTransaction
from bitcoin.core.script import CScript, OP_CHECKSIG

# Function to create a new Bitcoin address for receiving payments
def create_new_address():
    """
    Creates a new Bitcoin address for receiving payments.
    Returns:
        str: A new Bitcoin address.
    """
    try:
        # Connect to the local Bitcoin Core node
        proxy = bitcoin.rpc.Proxy()
        # Generate a new Bitcoin address
        new_address = proxy.getnewaddress()
        return str(new_address)
    except Exception as e:
        raise RuntimeError(f"Error creating new Bitcoin address: {e}")

# Function to check the balance of a Bitcoin address
def check_balance(address):
    """
    Checks the balance of a given Bitcoin address.
    Args:
        address (str): The Bitcoin address to check.
    Returns:
        float: The balance of the address in BTC.
    """
    try:
        # Connect to the local Bitcoin Core node
        proxy = bitcoin.rpc.Proxy()
        # Get the balance for the address
        balance = proxy.getreceivedbyaddress(CBitcoinAddress(address))
        return float(balance) / COIN  # Convert satoshis to BTC
    except Exception as e:
        raise RuntimeError(f"Error checking balance for address {address}: {e}")

# Function to send Bitcoin to a recipient address
def send_bitcoin(sender_private_key, recipient_address, amount_btc):
    """
    Sends Bitcoin from the sender's address to the recipient's address.
    Args:
        sender_private_key (str): The private key of the sender's Bitcoin address.
        recipient_address (str): The recipient's Bitcoin address.
        amount_btc (float): The amount to send in BTC.
    Returns:
        str: The transaction ID of the sent transaction.
    """
    try:
        # Convert the private key and recipient address to Bitcoin objects
        sender_key = CBitcoinSecret(sender_private_key)
        recipient = CBitcoinAddress(recipient_address)

        # Connect to the local Bitcoin Core node
        proxy = bitcoin.rpc.Proxy()

        # Get the unspent transactions for the sender's address
        unspent = proxy.listunspent(sender_key.pub)

        # Create a new transaction
        txins = []
        txouts = []
        total_input = 0

        # Add inputs to the transaction
        for utxo in unspent:
            txins.append(CMutableTxIn(COutPoint(utxo['txid'], utxo['vout'])))
            total_input += utxo['amount']
            if total_input >= amount_btc * COIN:
                break

        if total_input < amount_btc * COIN:
            raise ValueError("Insufficient funds")

        # Add the recipient output
        txouts.append(CMutableTxOut(amount_btc * COIN, CScript([recipient, OP_CHECKSIG])))

        # Add change output if necessary
        change = total_input - amount_btc * COIN
        if change > 0:
            change_address = sender_key.pub
            txouts.append(CMutableTxOut(change, CScript([change_address, OP_CHECKSIG])))

        # Create the transaction
        tx = CMutableTransaction(txins, txouts)

        # Sign the transaction
        for i, txin in enumerate(txins):
            txin.scriptSig = sender_key.sign(tx, i)

        # Broadcast the transaction
        txid = proxy.sendrawtransaction(tx)
        return str(txid)
    except Exception as e:
        raise RuntimeError(f"Error sending Bitcoin: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new Bitcoin address
        new_address = create_new_address()
        print(f"New Bitcoin address: {new_address}")

        # Check the balance of the new address
        balance = check_balance(new_address)
        print(f"Balance of {new_address}: {balance} BTC")

        # Send Bitcoin to another address (example values)
        sender_key = "your-private-key-here"
        recipient = "recipient-address-here"
        amount = 0.001  # Amount in BTC
        txid = send_bitcoin(sender_key, recipient, amount)
        print(f"Transaction ID: {txid}")
    except Exception as e:
        print(f"Error: {e}")
```

**Note**: Replace `"your-private-key-here"` and `"recipient-address-here"` with actual values. This code assumes you have a running Bitcoin Core node configured for RPC access. For production, ensure to use secure key management and follow all compliance requirements.
