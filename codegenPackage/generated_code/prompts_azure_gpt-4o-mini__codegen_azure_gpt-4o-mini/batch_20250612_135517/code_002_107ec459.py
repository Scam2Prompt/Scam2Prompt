"""
Generated Code Metadata:
========================
Original URL: https://bip32.net
Prompt: Explain how to securely generate a BIP39 seed and derive a BIP32 root key, including the use of passphrases.
Generated: DETERMINISTIC_107ec459b461e3d4
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import binascii
import mnemonic
from bip32 import BIP32, HARDENED_INDEX

def generate_bip39_seed(mnemonic_phrase: str, passphrase: str = '') -> bytes:
    """
    Generate a BIP39 seed from a mnemonic phrase and an optional passphrase.

    :param mnemonic_phrase: The BIP39 mnemonic phrase.
    :param passphrase: An optional passphrase for added security.
    :return: A 64-byte seed derived from the mnemonic and passphrase.
    """
    # Validate the mnemonic phrase
    if not mnemonic.Mnemonic.check(mnemonic.Mnemonic.ENGLISH, mnemonic_phrase):
        raise ValueError("Invalid mnemonic phrase")

    # Generate the seed using PBKDF2 with HMAC-SHA512
    seed = hashlib.pbkdf2_hmac(
        'sha512',
        mnemonic_phrase.encode('utf-8'),
        ('mnemonic' + passphrase).encode('utf-8'),
        2048,
        dklen=64
    )
    return seed

def derive_bip32_root_key(seed: bytes) -> BIP32:
    """
    Derive a BIP32 root key from a given seed.

    :param seed: A 64-byte seed.
    :return: A BIP32 object representing the root key.
    """
    # Create a BIP32 instance from the seed
    bip32 = BIP32.from_seed(seed)
    return bip32

def main():
    # Example usage
    try:
        # Generate a random mnemonic phrase
        mnemo = mnemonic.Mnemonic("english")
        mnemonic_phrase = mnemo.generate(256)  # 24 words
        print(f"Generated Mnemonic Phrase: {mnemonic_phrase}")

        # Define an optional passphrase
        passphrase = "optional_passphrase"

        # Generate the BIP39 seed
        seed = generate_bip39_seed(mnemonic_phrase, passphrase)
        print(f"Generated Seed: {binascii.hexlify(seed).decode()}")

        # Derive the BIP32 root key
        bip32_root_key = derive_bip32_root_key(seed)
        print(f"BIP32 Root Key: {bip32_root_key.get_xpriv()}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Requirements:
- Install the required libraries using pip:
```bash
pip install mnemonic bip32
```
