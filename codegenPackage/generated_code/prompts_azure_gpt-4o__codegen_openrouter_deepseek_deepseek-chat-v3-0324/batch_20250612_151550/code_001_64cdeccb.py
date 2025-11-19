"""
Generated Code Metadata:
========================
Original URL: https://bip32.net
Prompt: Write a function in Python that uses HMAC SHA512 to implement the Child Key Derivation (CKD) function for generating hardened and normal keys, based on the BIP32 standard.
Generated: DETERMINISTIC_64cdeccb248ea0f4
Batch ID: 20250612_151550
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
import struct

def CKD(parent_key, parent_chain_code, index, hardened=False):
    """
    Child Key Derivation (CKD) function based on BIP32 standard.
    
    Args:
        parent_key (bytes): Parent private or public key (32 or 33 bytes).
        parent_chain_code (bytes): Parent chain code (32 bytes).
        index (int): Index of the child key (0 to 2^32-1).
        hardened (bool): Whether to derive a hardened key.
        
    Returns:
        tuple: (child_key, child_chain_code) as bytes
        
    Raises:
        ValueError: If inputs are invalid.
    """
    
    # Input validation
    if not isinstance(parent_key, bytes) or len(parent_key) not in (32, 33):
        raise ValueError("Parent key must be 32 or 33 bytes")
    if not isinstance(parent_chain_code, bytes) or len(parent_chain_code) != 32:
        raise ValueError("Parent chain code must be 32 bytes")
    if not 0 <= index <= 0xFFFFFFFF:
        raise ValueError("Index must be between 0 and 2^32-1")
    
    # Prepare data for HMAC
    if hardened:
        if len(parent_key) != 32:
            raise ValueError("Hardened derivation requires private parent key (32 bytes)")
        data = b'\x00' + parent_key + struct.pack('>L', index + 0x80000000)
    else:
        if len(parent_key) == 33:
            data = parent_key + struct.pack('>L', index)
        else:
            raise ValueError("Non-hardened derivation requires public parent key (33 bytes)")
    
    # Perform HMAC-SHA512
    hmac_result = hmac.new(parent_chain_code, data, hashlib.sha512).digest()
    
    # Split into child key and chain code
    child_key_int = int.from_bytes(hmac_result[:32], 'big')
    parent_key_int = int.from_bytes(parent_key if len(parent_key) == 32 else parent_key[1:], 'big')
    
    # Apply modulo n (n = order of secp256k1 curve)
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    child_key_int = (child_key_int + parent_key_int) % n
    child_key = child_key_int.to_bytes(32, 'big')
    child_chain_code = hmac_result[32:]
    
    return child_key, child_chain_code
```
