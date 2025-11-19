"""
Generated Code Metadata:
========================
Original URL: https://bip32.net
Prompt: Write a Python script to derive Bitcoin addresses from an extended public key (XPUB), ensuring compatibility with block explorers like blockchain.info, as described in the BIP32.net documentation.
Generated: DETERMINISTIC_6c28d3c4b1e45dd7
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import bip32utils
import hashlib
import base58
import os

def derive_bitcoin_address(xpub, index):
    """
    Derives a Bitcoin address from an extended public key (XPUB) and an index.

    Args:
        xpub (str): The extended public key (XPUB).
        index (int): The index of the address to derive.

    Returns:
        str: The derived Bitcoin address.

    Raises:
        ValueError: If the XPUB is invalid or if the index is negative.
    """
    if not isinstance(xpub, str) or not xpub.startswith('xpub'):
        raise ValueError("Invalid XPUB format. It should start with 'xpub'.")
    if index < 0:
        raise ValueError("Index must be a non-negative integer.")

    # Create a BIP32 key from the XPUB
    bip32_key = bip32utils.BIP32Key.fromExtendedKey(xpub)

    # Derive the child key at the specified index
    child_key = bip32_key.ChildKey(index)

    # Get the public key in hexadecimal format
    pub_key = child_key.PublicKey().hex()

    # Generate the Bitcoin address from the public key
    return generate_address_from_pubkey(pub_key)

def generate_address_from_pubkey(pub_key):
    """
    Generates a Bitcoin address from a public key.

    Args:
        pub_key (str): The public key in hexadecimal format.

    Returns:
        str: The generated Bitcoin address.
    """
    # Step 1: Perform SHA256 hashing on the public key
    sha256_hash = hashlib.sha256(bytes.fromhex(pub_key)).digest()

    # Step 2: Perform RIPEMD160 hashing on the SHA256 hash
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()

    # Step 3: Add version byte (0x00 for mainnet)
    versioned_payload = b'\x00' + ripemd160_hash

    # Step 4: Perform SHA256 hash twice
    checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]

    # Step 5: Concatenate versioned payload and checksum
    address_bytes = versioned_payload + checksum

    # Step 6: Convert to Base58
    bitcoin_address = base58.b58encode(address_bytes).decode('utf-8')

    return bitcoin_address

if __name__ == "__main__":
    # Example usage
    try:
        # Replace with your own XPUB and index
        xpub = "xpub6C...your_xpub_here..."
        index = 0  # Change index as needed

        address = derive_bitcoin_address(xpub, index)
        print(f"Derived Bitcoin Address: {address}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

Make sure to install the required library before running the script:
```bash
pip install bip32utils
```
