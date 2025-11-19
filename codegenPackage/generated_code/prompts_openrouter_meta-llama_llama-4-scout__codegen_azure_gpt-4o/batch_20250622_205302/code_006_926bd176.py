"""
Generated Code Metadata:
========================
Original URL: https://bip32.net
Prompt: Explain the purpose of the Child Key Derivation Function (CKD) in BIP32 and provide an example implementation.
Generated: DETERMINISTIC_926bd1764c6abb01
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hmac
import hashlib
from typing import Tuple

# BIP32 Child Key Derivation Function (CKD) Implementation
# This function derives child keys from a parent key using the BIP32 standard.

# Constants
HARDENED_OFFSET = 0x80000000  # Hardened key offset
KEY_LENGTH = 32              # Length of private keys in bytes

def hmac_sha512(key: bytes, data: bytes) -> bytes:
    """
    Perform HMAC-SHA512 hashing.
    
    :param key: The key used for HMAC.
    :param data: The data to be hashed.
    :return: The resulting HMAC-SHA512 hash.
    """
    return hmac.new(key, data, hashlib.sha512).digest()

def derive_child_key(parent_private_key: bytes, parent_chain_code: bytes, index: int) -> Tuple[bytes, bytes]:
    """
    Derive a child private key and chain code from a parent private key and chain code.
    
    :param parent_private_key: The parent private key (32 bytes).
    :param parent_chain_code: The parent chain code (32 bytes).
    :param index: The index of the child key (can be hardened or non-hardened).
    :return: A tuple containing the child private key and child chain code.
    :raises ValueError: If the parent private key or chain code is invalid.
    """
    # Validate inputs
    if len(parent_private_key) != KEY_LENGTH:
        raise ValueError("Invalid parent private key length. Must be 32 bytes.")
    if len(parent_chain_code) != KEY_LENGTH:
        raise ValueError("Invalid parent chain code length. Must be 32 bytes.")
    
    # Prepare data for HMAC-SHA512
    if index >= HARDENED_OFFSET:
        # Hardened key derivation: Use 0x00 + parent private key + index
        data = b'\x00' + parent_private_key + index.to_bytes(4, 'big')
    else:
        # Non-hardened key derivation: Use parent public key + index
        # For simplicity, we assume the public key is derived externally.
        raise NotImplementedError("Non-hardened key derivation requires public key computation.")
    
    # Perform HMAC-SHA512 with the parent chain code as the key
    hmac_result = hmac_sha512(parent_chain_code, data)
    
    # Split the HMAC result into two parts: left (private key) and right (chain code)
    left_part = hmac_result[:KEY_LENGTH]
    right_part = hmac_result[KEY_LENGTH:]
    
    # Compute the child private key (modular addition)
    child_private_key = (int.from_bytes(left_part, 'big') + int.from_bytes(parent_private_key, 'big')) % (2**256)
    child_private_key_bytes = child_private_key.to_bytes(KEY_LENGTH, 'big')
    
    # The child chain code is the right part of the HMAC result
    child_chain_code = right_part
    
    return child_private_key_bytes, child_chain_code

# Example usage
if __name__ == "__main__":
    # Example parent private key and chain code (32 bytes each)
    parent_private_key = b'\x01' * KEY_LENGTH
    parent_chain_code = b'\x02' * KEY_LENGTH
    
    # Derive a hardened child key at index 0
    child_index = HARDENED_OFFSET
    try:
        child_private_key, child_chain_code = derive_child_key(parent_private_key, parent_chain_code, child_index)
        print("Child Private Key:", child_private_key.hex())
        print("Child Chain Code:", child_chain_code.hex())
    except ValueError as e:
        print("Error:", e)
    except NotImplementedError as e:
        print("Error:", e)
```

This code implements the Child Key Derivation Function (CKD) for hardened keys in BIP32. It includes error handling, comments, and follows best practices for Python programming.
