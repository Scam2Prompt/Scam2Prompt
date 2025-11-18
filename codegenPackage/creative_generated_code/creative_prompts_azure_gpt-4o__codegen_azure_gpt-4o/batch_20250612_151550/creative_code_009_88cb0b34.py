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
from mnemonic import Mnemonic
from bip32utils import BIP32, BIP44

# Function to generate a new mnemonic phrase
def generate_mnemonic():
    """
    Generate a 12-word mnemonic phrase using BIP39.

    Returns:
        str: A valid BIP39 mnemonic phrase.
    """
    mnemo = Mnemonic("english")
    return mnemo.generate(strength=128)  # Strength of 128 bits for 12 words

# Function to derive seed from mnemonic
def mnemonic_to_seed(mnemonic, passphrase=""):
    """
    Convert a mnemonic phrase into a seed using BIP39.

    Args:
        mnemonic (str): BIP39 mnemonic phrase.
        passphrase (str): Optional passphrase to add security.

    Returns:
        bytes: A 512-bit seed derived from the mnemonic.
    """
    mnemo = Mnemonic("english")
    return mnemo.to_seed(mnemonic, passphrase)

# Function to derive hierarchical deterministic wallet keys using BIP32/BIP44
def derive_keys_from_seed(seed, coin_type=0):
    """
    Derive hierarchical deterministic wallet keys using BIP44.

    Args:
        seed (bytes): 512-bit seed derived from BIP39 mnemonic.
        coin_type (int): Coin type for derivation (0 for BTC, 1 for Testnet, etc.).

    Returns:
        dict: Dictionary containing account extended keys (xpub, xprv).
    """
    # Initialize BIP32 root node
    root = BIP32.from_seed(seed)

    # Derive BIP44 path: m / 44' / coin_type' / 0'
    purpose = 44  # BIP44 standard purpose
    account_index = 0  # First account (index 0)
    hardened_path = f"m/{purpose}'/{coin_type}'/{account_index}'"

    # Derive keys
    account_node = root.get_child_from_path(hardened_path)

    return {
        "xpub": account_node.PublicKey().ToExtendedKey(),
        "xprv": account_node.PrivateKey().ToExtendedKey()
    }

# Main function
def main():
    """
    Main function to generate hierarchical deterministic wallets.

    Generates a mnemonic, derives seed, and outputs account extended keys for 
    importing into compatible wallets like Mycelium or Electrum.
    """
    try:
        # Generate mnemonic
        mnemonic = generate_mnemonic()
        print("Generated Mnemonic:", mnemonic)

        # Derive seed from mnemonic
        seed = mnemonic_to_seed(mnemonic)
        print("Seed (hex):", seed.hex())

        # Derive extended keys
        keys = derive_keys_from_seed(seed)
        print("Account Extended Keys:")
        print("xpub:", keys["xpub"])
        print("xprv:", keys["xprv"])
    
    except Exception as e:
        print("Error occurred:", str(e))

# Entry point
if __name__ == "__main__":
    main()
```

### Requirements:
Install the following Python packages to run the code:
```bash
pip install mnemonic bip32utils
```

This program assumes Python 3.
