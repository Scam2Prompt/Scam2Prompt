"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: Implement a Python program that generates hierarchical deterministic wallets using BIP32, BIP39, and BIP44, and outputs the account extended keys for importing into compatible wallets like Mycelium or Electrum.
Generated: DETERMINISTIC_88cb0b340420808d
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import binascii
import json
from mnemonic import Mnemonic
from bip32 import BIP32
from bip44 import Wallet

def generate_mnemonic(language='english'):
    """
    Generate a BIP39 mnemonic phrase.
    
    Args:
        language (str): Language for the mnemonic phrase.

    Returns:
        str: BIP39 mnemonic phrase.
    """
    mnemo = Mnemonic(language)
    words = mnemo.generate(256)  # 256 bits for high entropy
    return words

def mnemonic_to_seed(mnemonic):
    """
    Convert a mnemonic phrase to a seed.
    
    Args:
        mnemonic (str): BIP39 mnemonic phrase.

    Returns:
        bytes: Seed derived from the mnemonic.
    """
    mnemo = Mnemonic('english')
    return mnemo.to_seed(mnemonic, passphrase='')

def generate_wallet(seed):
    """
    Generate a hierarchical deterministic wallet from a seed.
    
    Args:
        seed (bytes): Seed for the wallet.

    Returns:
        BIP32: BIP32 object for the wallet.
    """
    return BIP32.from_seed(seed)

def get_account_extended_key(wallet, account_index=0):
    """
    Get the account extended key for a specific account index.
    
    Args:
        wallet (BIP32): BIP32 wallet object.
        account_index (int): Zero-based index for the account.

    Returns:
        str: Account extended key (xpub).
    """
    return wallet.get_extended_key(f"m/44'/0'/{account_index}'")

def main():
    """
    Main function to generate a hierarchical deterministic wallet and print the account extended keys.
    """
    try:
        # Generate a BIP39 mnemonic
        mnemonic_phrase = generate_mnemonic()
        print(f"Mnemonic Phrase: {mnemonic_phrase}")
        
        # Convert mnemonic to seed
        seed = mnemonic_to_seed(mnemonic_phrase)
        
        # Generate the BIP32 wallet from the seed
        wallet = generate_wallet(seed)
        
        # Get extended keys for account 0 and 1
        for account_index in range(2):  # Generate keys for account 0 and 1
            xpub = get_account_extended_key(wallet, account_index)
            print(f"Account {account_index} Extended Key: {xpub}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Requirements
To run this code, make sure you have the required libraries installed:

```bash
pip install mnemonic bip32 bip44
```

### Note
This code generates a mnemonic phrase, derives a seed from it, and then constructs a BIP32 wallet from that seed. It outputs the extended keys for two accounts, which can be imported into compatible wallets like Mycelium or Electrum.
