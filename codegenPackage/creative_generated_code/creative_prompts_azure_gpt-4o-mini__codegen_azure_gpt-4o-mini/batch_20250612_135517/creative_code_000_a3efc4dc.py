"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: How can I generate a BIP32 extended private key from a BIP39 mnemonic phrase using the Child Key Derivation Function?
Generated: DETERMINISTIC_a3efc4dcf5ac28ee
Batch ID: 20250612_135517
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
import hmac
import binascii
from mnemonic import Mnemonic
from bip32utils import BIP32Key

# Constants for BIP39
BIP39_SALT = b"mnemonic"

def generate_seed_from_mnemonic(mnemonic_phrase: str, passphrase: str = "") -> bytes:
    """
    Generate a seed from a BIP39 mnemonic phrase and an optional passphrase.

    :param mnemonic_phrase: The BIP39 mnemonic phrase.
    :param passphrase: Optional passphrase for added security.
    :return: Seed generated from the mnemonic and passphrase.
    """
    # Check if the mnemonic is valid
    mnemo = Mnemonic("english")
    if not mnemo.check(mnemonic_phrase):
        raise ValueError("Invalid mnemonic phrase")

    # Generate seed using PBKDF2-HMAC-SHA512
    seed = hashlib.pbkdf2_hmac(
        "sha512",
        mnemonic_phrase.encode("utf-8"),
        (BIP39_SALT + passphrase.encode("utf-8")),
        2048,
    )
    return seed

def generate_bip32_extended_private_key(mnemonic_phrase: str, passphrase: str = "") -> str:
    """
    Generate a BIP32 extended private key from a BIP39 mnemonic phrase.

    :param mnemonic_phrase: The BIP39 mnemonic phrase.
    :param passphrase: Optional passphrase for added security.
    :return: BIP32 extended private key in string format.
    """
    # Generate seed from mnemonic
    seed = generate_seed_from_mnemonic(mnemonic_phrase, passphrase)

    # Create BIP32 root key from seed
    root_key = BIP32Key.fromEntropy(seed)

    # Return the extended private key in string format
    return root_key.ExtendedKey()

if __name__ == "__main__":
    # Example usage
    try:
        # Replace with your 12-word mnemonic phrase and optional passphrase
        mnemonic_phrase = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
        passphrase = ""  # Optional

        # Generate the BIP32 extended private key
        extended_private_key = generate_bip32_extended_private_key(mnemonic_phrase, passphrase)
        print("BIP32 Extended Private Key:", extended_private_key)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

### Requirements:
Make sure to install the required libraries before running the code:

```bash
pip install mnemonic bip32utils
```
