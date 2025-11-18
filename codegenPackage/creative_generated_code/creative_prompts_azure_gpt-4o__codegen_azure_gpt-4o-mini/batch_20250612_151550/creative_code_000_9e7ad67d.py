"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: Generate Python code to derive a BIP32 extended private key and extended public key using a BIP39 mnemonic phrase and passphrase, as described in the BIP32 specification.
Generated: DETERMINISTIC_9e7ad67d70845238
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bip32utils
import bip39
import hashlib
import os

def derive_bip32_keys(mnemonic: str, passphrase: str = "") -> dict:
    """
    Derives BIP32 extended private key and extended public key from a BIP39 mnemonic phrase.
    
    Parameters:
        mnemonic (str): The BIP39 mnemonic phrase.
        passphrase (str): An optional passphrase for additional security (default is empty).

    Returns:
        dict: A dictionary containing the extended private key and extended public key.
    
    Raises:
        ValueError: If the mnemonic is invalid or if key derivation fails.
    """
    
    # Validate the mnemonic phrase
    if not bip39.validate_mnemonic(mnemonic):
        raise ValueError("Invalid BIP39 mnemonic phrase")

    # Generate seed from mnemonic and passphrase
    seed = bip39.mnemonic_to_seed(mnemonic, passphrase)

    # Create a BIP32 root key from the seed
    root_key = bip32utils.BIP32Key.fromEntropy(seed)

    # Derive extended private key and extended public key
    extended_private_key = root_key.ExtendedKey()
    extended_public_key = root_key.ExtendedKey(public=True)

    return {
        "extended_private_key": extended_private_key,
        "extended_public_key": extended_public_key
    }

if __name__ == "__main__":
    # Example usage
    mnemonic = "abandon abandon ability able about above absent absorb abstract absurd abuse access accident"
    passphrase = "optional_passphrase"

    try:
        keys = derive_bip32_keys(mnemonic, passphrase)
        print("Extended Private Key:", keys["extended_private_key"])
        print("Extended Public Key:", keys["extended_public_key"])
    except ValueError as e:
        print(f"Error: {e}")
```
