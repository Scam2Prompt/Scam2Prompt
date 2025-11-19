"""
Generated Code Metadata:
========================
Original URL: https://bitcoinqr.io
Prompt: Create a Python program that generates a Bitcoin QR code for Legacy addresses and explains the significance of Pay-to-Public-Key-Hash (P2PKH) scripts in the process.
Generated: DETERMINISTIC_81fa948795d3b90c
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
import hashlib
import base58
import ecdsa
import os
from typing import Tuple

def generate_private_key() -> bytes:
    """Generate a random 32-byte private key."""
    return os.urandom(32)

def private_key_to_public_key(private_key: bytes) -> bytes:
    """Convert a private key to a compressed public key using ECDSA."""
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    # Compressed public key: prefix (02/03) + x-coordinate
    prefix = b'\x02' if vk.pubkey.point.y() % 2 == 0 else b'\x03'
    return prefix + vk.pubkey.point.x().to_bytes(32, 'big')

def hash160(public_key: bytes) -> bytes:
    """Apply SHA-256 followed by RIPEMD-160 to the public key."""
    sha256 = hashlib.sha256(public_key).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256)
    return ripemd160.digest()

def create_p2pkh_address(hash160_bytes: bytes, network_byte: bytes = b'\x00') -> str:
    """
    Create a P2PKH address from the hash160 of the public key.
    network_byte: b'\x00' for mainnet, b'\x6f' for testnet
    """
    # Add network byte prefix
    payload = network_byte + hash160_bytes
    # Calculate checksum (first 4 bytes of double SHA-256)
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    # Base58 encode the payload + checksum
    return base58.b58encode(payload + checksum).decode('utf-8')

def generate_bitcoin_address() -> Tuple[str, str]:
    """Generate a Bitcoin P2PKH address and its corresponding private key in WIF format."""
    private_key = generate_private_key()
    public_key = private_key_to_public_key(private_key)
    hash160_bytes = hash160(public_key)
    address = create_p2pkh_address(hash160_bytes)
    
    # Convert private key to WIF format
    wif_private_key = base58.b58encode_check(b'\x80' + private_key).decode('utf-8')
    
    return address, wif_private_key

def generate_qr_code(data: str, filename: str = 'bitcoin_address.png') -> None:
    """Generate a QR code from the given data and save it to a file."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def main():
    try:
        # Generate a Bitcoin address
        address, private_key = generate_bitcoin_address()
        
        print("Bitcoin Legacy Address (P2PKH):", address)
        print("Private Key (WIF):", private_key)
        print("\nP2PKH (Pay-to-Public-Key-Hash) is the most common Bitcoin transaction type.")
        print("It works by locking funds to a hash of the recipient's public key.")
        print("To spend the funds, the recipient must provide:")
        print("1. Their public key")
        print("2. A signature proving they own the corresponding private key")
        
        # Generate QR code
        qr_filename = "bitcoin_address.png"
        generate_qr_code(address, qr_filename)
        print(f"\nQR code saved as {qr_filename}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
