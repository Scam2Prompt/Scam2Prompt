"""
Generated Code Metadata:
========================
Original URL: https://bip32.net
Prompt: Explain how to use BIP44 derivation path with a BIP32 extended public key to derive addresses for a Bitcoin wallet.
Generated: DETERMINISTIC_dc635642e0004e5f
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import struct
from typing import Tuple

# Constants for BIP44 derivation
HARDENED_OFFSET = 0x80000000
BIP44_PURPOSE = 44
BITCOIN_COIN_TYPE = 0

# Base58 encoding/decoding utilities
BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def base58_encode(data: bytes) -> str:
    """Encodes bytes into a Base58 string."""
    num = int.from_bytes(data, 'big')
    encoded = ""
    while num > 0:
        num, remainder = divmod(num, 58)
        encoded = BASE58_ALPHABET[remainder] + encoded
    # Add '1' for each leading 0 byte
    for byte in data:
        if byte == 0:
            encoded = '1' + encoded
        else:
            break
    return encoded

def hash160(data: bytes) -> bytes:
    """Performs RIPEMD-160(SHA-256(data)) hashing."""
    sha256_hash = hashlib.sha256(data).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_hash)
    return ripemd160.digest()

def derive_child_key(parent_key: bytes, parent_chain_code: bytes, index: int) -> Tuple[bytes, bytes]:
    """
    Derives a child key using the BIP32 algorithm.
    :param parent_key: Parent public key (33 bytes for compressed format).
    :param parent_chain_code: Parent chain code (32 bytes).
    :param index: Child index (integer).
    :return: Tuple of (child_public_key, child_chain_code).
    """
    if index >= HARDENED_OFFSET:
        raise ValueError("Cannot derive hardened keys from an extended public key.")
    
    # Data for HMAC-SHA512: parent_key + index (4 bytes, big-endian)
    data = parent_key + struct.pack(">L", index)
    hmac_result = hmac.new(parent_chain_code, data, hashlib.sha512).digest()
    
    # Split HMAC result into left (key material) and right (chain code)
    key_material = hmac_result[:32]
    child_chain_code = hmac_result[32:]
    
    # Add key material to parent key to derive child key
    # Note: This is simplified and assumes no key overflow
    child_public_key = (int.from_bytes(parent_key, 'big') + int.from_bytes(key_material, 'big')) % (2**256)
    child_public_key_bytes = child_public_key.to_bytes(33, 'big')
    
    return child_public_key_bytes, child_chain_code

def derive_bip44_address(xpub: str, account: int, change: int, address_index: int) -> str:
    """
    Derives a Bitcoin address using BIP44 from an extended public key (xpub).
    :param xpub: Extended public key (Base58 encoded string).
    :param account: Account index (integer).
    :param change: Change index (0 for external, 1 for internal).
    :param address_index: Address index (integer).
    :return: Bitcoin address (Base58 encoded string).
    """
    # Decode xpub (simplified, assumes valid input)
    xpub_bytes = base58_decode(xpub)
    parent_key = xpub_bytes[:33]  # First 33 bytes are the public key
    parent_chain_code = xpub_bytes[33:65]  # Next 32 bytes are the chain code
    
    # Derive account key
    account_index = HARDENED_OFFSET + account
    account_key, account_chain_code = derive_child_key(parent_key, parent_chain_code, account_index)
    
    # Derive change key
    change_key, change_chain_code = derive_child_key(account_key, account_chain_code, change)
    
    # Derive address key
    address_key, _ = derive_child_key(change_key, change_chain_code, address_index)
    
    # Generate Bitcoin address
    pubkey_hash = hash160(address_key)
    version_byte = b'\x00'  # Mainnet version byte
    payload = version_byte + pubkey_hash
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    address = base58_encode(payload + checksum)
    
    return address

# Example usage
if __name__ == "__main__":
    # Replace with a valid xpub for testing
    xpub = "xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKi8Lq9x6XqjVZ5zv5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5X5
