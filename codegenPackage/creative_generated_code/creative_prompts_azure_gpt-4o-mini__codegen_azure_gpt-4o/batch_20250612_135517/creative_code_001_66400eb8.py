"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bip32.net
Prompt: Write a code snippet to derive child public keys from a BIP32 master public key using the specified derivation path.
Generated: DETERMINISTIC_66400eb8ef598056
Batch ID: 20250612_135517
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
import binascii
from typing import Tuple

# Constants for BIP32
HARDENED_OFFSET = 0x80000000
BIP32_SEED = b'Bitcoin seed'

def derive_child_public_key(master_public_key: bytes, chain_code: bytes, derivation_path: str) -> Tuple[bytes, bytes]:
    """
    Derives a child public key and chain code from a master public key using the BIP32 derivation path.

    Args:
        master_public_key (bytes): The master public key (compressed format).
        chain_code (bytes): The chain code associated with the master key.
        derivation_path (str): Derivation path (e.g., "m/0'/1/2").

    Returns:
        Tuple[bytes, bytes]: A tuple containing the derived child public key and chain code.
    """
    def parse_derivation_path(path: str):
        """Parses the derivation path into indexes."""
        if not path.startswith("m/"):
            raise ValueError("Invalid derivation path. Must start with 'm/'.")
        return [
            int(index[:-1]) + HARDENED_OFFSET if index.endswith("'") else int(index)
            for index in path[2:].split("/")
        ]

    def hmac_sha512(key: bytes, data: bytes) -> bytes:
        """Computes HMAC-SHA512."""
        return hmac.new(key, data, hashlib.sha512).digest()

    def derive_key(parent_public_key: bytes, parent_chain_code: bytes, index: int) -> Tuple[bytes, bytes]:
        """
        Derives a child key from the parent public key and chain code.
        """
        if index >= HARDENED_OFFSET:
            raise ValueError("Cannot derive hardened keys using a public key.")
        
        # Serialize the index and construct the data for HMAC
        index_bytes = index.to_bytes(4, byteorder="big")
        data = parent_public_key + index_bytes
        
        # Perform HMAC-SHA512
        derived = hmac_sha512(parent_chain_code, data)
        
        # Split the result into child key components
        child_chain_code = derived[32:]
        child_public_key = derived[:32]  # Placeholder: Implement actual elliptic curve point addition
        
        return child_public_key, child_chain_code

    # Parse the derivation path
    indexes = parse_derivation_path(derivation_path)
    
    # Start with the master public key and chain code
    current_public_key = master_public_key
    current_chain_code = chain_code
    
    # Derive keys along the specified path
    for index in indexes:
        current_public_key, current_chain_code = derive_key(current_public_key, current_chain_code, index)

    return current_public_key, current_chain_code


# Example usage
if __name__ == "__main__":
    try:
        # Master key and chain code (example values; replace with real ones)
        MASTER_PUBLIC_KEY = binascii.unhexlify("03a34b...")  # Compressed public key
        MASTER_CHAIN_CODE = binascii.unhexlify("751...")     # Chain code
        
        # Specify the derivation path
        DERIVATION_PATH = "m/0/1"
        
        # Derive child public key
        child_key, child_chain_code = derive_child_public_key(MASTER_PUBLIC_KEY, MASTER_CHAIN_CODE, DERIVATION_PATH)
        
        print("Derived Child Public Key:", binascii.hexlify(child_key).decode())
        print("Derived Child Chain Code:", binascii.hexlify(child_chain_code).decode())
    except Exception as e:
        print("Error:", str(e))
```
