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
import hashlib
import hmac
import binascii
from typing import Tuple
from mnemonic import Mnemonic
from coincurve import PrivateKey

# Constants for BIP32
HARDENED_OFFSET = 0x80000000
BIP32_SEED_KEY = b'Bitcoin seed'

def mnemonic_to_seed(mnemonic: str, passphrase: str = "") -> bytes:
    """
    Generates a BIP39 seed from a mnemonic phrase and optional passphrase.
    """
    # PBKDF2 with HMAC-SHA512
    mnemonic_norm = mnemonic.strip()
    passphrase_norm = f"mnemonic{passphrase.strip()}"
    return hashlib.pbkdf2_hmac('sha512', mnemonic_norm.encode(), passphrase_norm.encode(), 2048)

def hmac_sha512(key: bytes, data: bytes) -> bytes:
    """
    Performs HMAC-SHA512 hashing.
    """
    return hmac.new(key, data, hashlib.sha512).digest()

def derive_child_key(parent_private_key: bytes, parent_chain_code: bytes, index: int) -> Tuple[bytes, bytes]:
    """
    Derives a child key using the Child Key Derivation (CKD) function (BIP32).
    """
    if index >= HARDENED_OFFSET:
        # Hardened derivation: include private key in input
        data = b'\x00' + parent_private_key + index.to_bytes(4, 'big')
    else:
        # Normal derivation: include public key in input
        parent_public_key = PrivateKey(parent_private_key).public_key.format(compressed=True)
        data = parent_public_key + index.to_bytes(4, 'big')
    
    # Generate HMAC-SHA512 digest
    digest = hmac_sha512(parent_chain_code, data)
    
    # Split digest into left (key) and right (chain code)
    left_part = digest[:32]
    right_part = digest[32:]
    
    # Add left part to parent private key to derive child private key
    child_private_key = (int.from_bytes(left_part, 'big') + int.from_bytes(parent_private_key, 'big')) % PrivateKey.curve.order
    return child_private_key.to_bytes(32, 'big'), right_part

def generate_bip32_extended_key(mnemonic: str, passphrase: str = "") -> Tuple[str, str]:
    """
    Generates the BIP32 extended private key from a BIP39 mnemonic phrase.
    """
    # Step 1: Generate seed from mnemonic
    seed = mnemonic_to_seed(mnemonic, passphrase)
    
    # Step 2: Generate master private key and chain code
    master_key_material = hmac_sha512(BIP32_SEED_KEY, seed)
    master_private_key = master_key_material[:32]
    master_chain_code = master_key_material[32:]
    
    # Step 3: Format extended private key (xpriv)
    extended_key = binascii.hexlify(master_private_key).decode()
    chain_code = binascii.hexlify(master_chain_code).decode()
    return extended_key, chain_code

# Example usage
if __name__ == "__main__":
    # Example mnemonic phrase (Do NOT use this in production; generate securely!)
    example_mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
    example_passphrase = ""  # Optional passphrase
    
    # Generate BIP32 extended private key
    extended_key, chain_code = generate_bip32_extended_key(example_mnemonic, example_passphrase)
    print(f"Extended Private Key: {extended_key}")
    print(f"Chain Code: {chain_code}")
```

**Note**: To run the code, ensure you have installed the required dependencies:
```bash
pip install mnemonic coincurve
```
