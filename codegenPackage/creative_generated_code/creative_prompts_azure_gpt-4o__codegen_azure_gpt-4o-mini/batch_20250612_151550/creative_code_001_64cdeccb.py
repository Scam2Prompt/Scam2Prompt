"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: Write a function in Python that uses HMAC SHA512 to implement the Child Key Derivation (CKD) function for generating hardened and normal keys, based on the BIP32 standard.
Generated: DETERMINISTIC_64cdeccb248ea0f4
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hmac
import hashlib
from typing import Tuple

def hmac_sha512(key: bytes, data: bytes) -> bytes:
    """
    Generate HMAC SHA512 hash.

    :param key: The secret key used for HMAC.
    :param data: The message to be hashed.
    :return: HMAC SHA512 hash as bytes.
    """
    return hmac.new(key, data, hashlib.sha512).digest()

def ckd(key: bytes, index: int, hardened: bool = False) -> bytes:
    """
    Child Key Derivation (CKD) function based on BIP32 standard.

    :param key: The parent key (master or child key).
    :param index: The index for deriving the child key. 
                  If hardened is True, the index must be greater than or equal to 0x80000000.
    :param hardened: Boolean flag for hardened key derivation.
    :return: Derived child key as bytes.
    """
    # Validate index for hardened derivation
    if hardened and index < 0x80000000:
        raise ValueError("Hardened index must be >= 0x80000000")
    
    # Convert index to bytes (4 bytes)
    index_bytes = index.to_bytes(4, byteorder='big')
    
    # If deriving a hardened key, concatenate the key with the index
    if hardened:
        # For hardened keys, prepend the byte 0x00 (indicating private key) to the key
        data = b'\x00' + key + index_bytes
    else:
        # For non-hardened keys, simply append the index to the key
        data = key + index_bytes

    # Generate the child key using HMAC SHA512
    child_key = hmac_sha512(key, data)
    
    return child_key

# Example usage:
if __name__ == "__main__":
    master_key = b'my_super_secret_master_key'
    index = 0x80000001  # Example hardened index
    try:
        child_key_hardened = ckd(master_key, index, hardened=True)
        print("Hardened Child Key:", child_key_hardened.hex())
        
        child_key_normal = ckd(master_key, 1, hardened=False)
        print("Normal Child Key:", child_key_normal.hex())
    except ValueError as e:
        print(f"Error: {e}")
```
