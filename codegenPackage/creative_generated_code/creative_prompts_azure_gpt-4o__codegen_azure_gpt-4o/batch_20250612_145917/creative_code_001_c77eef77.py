"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-wallet.org
Prompt: Create a script that generates a SegWit Bitcoin address and retrieves its associated private key, as explained on bitcoin-wallet.org.
Generated: DETERMINISTIC_c77eef7766dc7d6f
Batch ID: 20250612_145917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import ecdsa
import base58

# Generate a SegWit Bitcoin address and corresponding private key

def generate_private_key():
    """
    Generate a 32-byte private key.
    """
    return os.urandom(32)

def private_key_to_wif(private_key):
    """
    Convert a private key to Wallet Import Format (WIF).
    """
    # Add prefix 0x80 for mainnet
    prefix = b'\x80'
    extended_key = prefix + private_key
    
    # Perform double SHA-256 hashing and append checksum
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    wif = base58.b58encode(extended_key + checksum)
    return wif.decode()

def private_key_to_public_key(private_key):
    """
    Derive the public key from a private key.
    """
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    # Add prefix 0x02 or 0x03 for compressed public key based on the sign of the y-coordinate
    public_key = b'\x02' + vk.to_string()[:32] if vk.to_string()[32] % 2 == 0 else b'\x03' + vk.to_string()[:32]
    return public_key

def public_key_to_segwit_address(public_key):
    """
    Convert a public key to a SegWit Bitcoin address.
    """
    # Perform SHA-256 followed by RIPEMD-160 to get the hash of the public key
    sha256_hash = hashlib.sha256(public_key).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    
    # Create SegWit address using bech32 encoding (P2WPKH)
    # Add prefix for mainnet (0x00) and encode using base58
    prefix = b'\x00'
    extended_key = prefix + ripemd160_hash
    
    # Perform double SHA-256 hashing and append checksum
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    segwit_address = base58.b58encode(extended_key + checksum)
    return segwit_address.decode()

def main():
    """
    Main function to generate a SegWit Bitcoin address and retrieve its private key.
    """
    try:
        # Step 1: Generate private key
        private_key = generate_private_key()
        print("Private Key (hex):", private_key.hex())
        
        # Step 2: Convert private key to Wallet Import Format (WIF)
        wif = private_key_to_wif(private_key)
        print("Private Key (WIF):", wif)
        
        # Step 3: Derive public key from private key
        public_key = private_key_to_public_key(private_key)
        print("Public Key (hex):", public_key.hex())
        
        # Step 4: Create SegWit Bitcoin address from public key
        segwit_address = public_key_to_segwit_address(public_key)
        print("SegWit Bitcoin Address:", segwit_address)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
