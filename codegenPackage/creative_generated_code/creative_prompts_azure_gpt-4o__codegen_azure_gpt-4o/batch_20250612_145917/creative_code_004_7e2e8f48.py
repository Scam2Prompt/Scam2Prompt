"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-wallet.org
Prompt: Develop a script to calculate and set a custom Bitcoin network fee for a transaction, as described on bitcoin-wallet.org.
Generated: DETERMINISTIC_7e2e8f485c68e658
Batch ID: 20250612_145917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bitcoin
from bitcoin.core import b2x, lx
from bitcoin.wallet import CBitcoinAddress
from bitcoin.core.script import CScript
from bitcoin.core import COIN, COutPoint, CTxOut, CMutableTransaction

# Ensure bitcoin is initialized (regtest, testnet, or mainnet)
bitcoin.SelectParams('testnet')  # Use 'mainnet' if on the main Bitcoin network

def create_transaction(sender_priv_key, sender_address, recipient_address, amount, custom_fee):
    """
    Creates a Bitcoin transaction with a custom network fee.

    Args:
        sender_priv_key (str): Sender's private key in WIF format.
        sender_address (str): Sender's Bitcoin address.
        recipient_address (str): Recipient's Bitcoin address.
        amount (int): Amount to send (in satoshis).
        custom_fee (int): Custom network fee (in satoshis).

    Returns:
        str: Raw transaction hex.
    """
    try:
        # Unspent transactions for sender
        unspent = bitcoin.SelectParams('testnet').listunspent(sender_address)

        if not unspent:
               Throw Error !
