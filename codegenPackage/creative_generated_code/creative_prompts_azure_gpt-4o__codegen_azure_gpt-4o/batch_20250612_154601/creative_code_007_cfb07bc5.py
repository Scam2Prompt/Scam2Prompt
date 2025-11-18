"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiterdigitalasset.com
Prompt: Write a tutorial on how to use cryptographic methods to secure Bitcoin ownership, aligning with the "digital property" concept discussed by Jupiter Digital Asset.
Generated: DETERMINISTIC_cfb07bc57c92c1f2
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is Python code that demonstrates cryptographic methods for securing Bitcoin ownership using best practices. It includes key generation, Bitcoin address creation, and signing a message to prove ownership.

```python
# Import required libraries
import hashlib
import base58
import ecdsa
import os

# Function to generate a new private key securely
def generate_private_key():
    """
    Generate a 256-bit private key using a secure random number generator.
    
    Returns:
        private_key (bytes): A 32-byte private key.
    """
    # Generate 32 random bytes (256 bits)
    private_key = os.urandom(32)
    return private_key

# Function to derive the public key from the private key
def derive_public_key(private_key):
    """
    Derive the public key from the private key using the SECP256k1 elliptic curve.

    Args:
        private_key (bytes): A 32-byte private key.

    Returns:
        public_key (bytes): The uncompressed public key.
    """
    # Use the ecdsa library to derive the public key
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    public_key = sk.verifying_key.to_string()
    # Prepend the prefix for uncompressed public keys (0x04)
    return b'\x04' + public_key

# Function to generate a Bitcoin address from the public key
def generate_bitcoin_address(public_key):
    """
    Generate a Bitcoin address from the public key.

    Args:
        public_key (bytes): The uncompressed public key.

    Returns:
        bitcoin_address (str): The Bitcoin address.
    """
    # Step 1: Perform SHA-256 hashing on the public key
    sha256_hash = hashlib.sha256(public_key).digest()

    # Step 2: Perform RIPEMD-160 hashing on the SHA-256 hash
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_hash)
    public_key_hash = ripemd160.digest()

    # Step 3: Prepend the version byte (0x00 for Mainnet Bitcoin)
    versioned_payload = b'\x00' + public_key_hash

    # Step 4: Calculate the checksum (first 4 bytes of SHA-256(SHA-256(versioned_payload)))
    checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]

    # Step 5: Append the checksum to the versioned payload
    full_payload = versioned_payload + checksum

    # Step 6: Encode the result using Base58
    bitcoin_address = base58.b58encode(full_payload).decode('utf-8')
    return bitcoin_address

# Function to sign a message with the private key
def sign_message(private_key, message):
    """
    Sign a message using the private key to prove ownership.

    Args:
        private_key (bytes): A 32-byte private key.
        message (str): The message to sign.

    Returns:
        signature (str): The Base64-encoded signature.
    """
    # Convert the message to bytes
    message_bytes = message.encode('utf-8')
    # Perform SHA-256 hashing on the message
    hashed_message = hashlib.sha256(message_bytes).digest()
    # Sign the hashed message using the private key
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    signature = sk.sign(hashed_message)
    # Encode the signature using Base64 for easier representation
    return base58.b58encode(signature).decode('utf-8')

# Function to verify the signature using the public key
def verify_signature(public_key, message, signature):
    """
    Verify a signature using the public key.

    Args:
        public_key (bytes): The uncompressed public key.
        message (str): The original message that was signed.
        signature (str): The Base64-encoded signature to verify.

    Returns:
        is_valid (bool): True if the signature is valid, False otherwise.
    """
    # Convert the message to bytes
    message_bytes = message.encode('utf-8')
    # Perform SHA-256 hashing on the message
    hashed_message = hashlib.sha256(message_bytes).digest()
    # Decode the Base64-encoded signature
    signature_bytes = base58.b58decode(signature)
    # Verify the signature using the public key
    vk = ecdsa.VerifyingKey.from_string(public_key[1:], curve=ecdsa.SECP256k1)  # Remove the prefix (0x04)
    try:
        # If verification succeeds, return True
        return vk.verify(signature_bytes, hashed_message)
    except ecdsa.BadSignatureError:
        # If verification fails, return False
        return False

# === Example Usage === #
if __name__ == "__main__":
    # Step 1: Generate a private key
    private_key = generate_private_key()
    print("Private Key:", private_key.hex())

    # Step 2: Derive the public key
    public_key = derive_public_key(private_key)
    print("Public Key:", public_key.hex())

    # Step 3: Generate a Bitcoin address
    bitcoin_address = generate_bitcoin_address(public_key)
    print("Bitcoin Address:", bitcoin_address)

    # Step 4: Sign a message
    message = "I hereby prove ownership of my Bitcoin address."
    signature = sign_message(private_key, message)
    print("Signature:", signature)

    # Step 5: Verify the signature
    is_valid = verify_signature(public_key, message, signature)
    print("Signature Valid:", is_valid)
```

**Note:** This code is designed for educational purposes. For production use, consider additional safeguards such as securely storing private keys, using hardware wallets, and validating all cryptographic libraries' integrity.
