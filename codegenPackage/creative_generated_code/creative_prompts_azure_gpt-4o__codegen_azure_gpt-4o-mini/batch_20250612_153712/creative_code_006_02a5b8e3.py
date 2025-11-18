"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wildhorse-llc.com
Prompt: Provide code to implement end-to-end encryption for user data on Wildhorse LLC's platform, leveraging hybrid encryption algorithms.
Generated: DETERMINISTIC_02a5b8e3bdb2a590
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import base64
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

# Constants for encryption
AES_KEY_SIZE = 32  # 256 bits
AES_BLOCK_SIZE = AES.block_size
SALT_SIZE = 16
ITERATIONS = 100000
PUBLIC_KEY_PATH = "public.pem"  # Path to the public key
PRIVATE_KEY_PATH = "private.pem"  # Path to the private key

def generate_rsa_keypair():
    """Generate RSA public and private key pair."""
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open(PRIVATE_KEY_PATH, "wb") as priv_file:
        priv_file.write(private_key)

    with open(PUBLIC_KEY_PATH, "wb") as pub_file:
        pub_file.write(public_key)

def load_public_key():
    """Load the RSA public key from a file."""
    with open(PUBLIC_KEY_PATH, "rb") as pub_file:
        public_key = RSA.import_key(pub_file.read())
    return public_key

def load_private_key():
    """Load the RSA private key from a file."""
    with open(PRIVATE_KEY_PATH, "rb") as priv_file:
        private_key = RSA.import_key(priv_file.read())
    return private_key

def encrypt_data(data: bytes, public_key: RSA.RsaKey) -> dict:
    """
    Encrypt data using hybrid encryption (AES + RSA).
    
    Parameters:
    data (bytes): Data to encrypt
    public_key (RSA.RsaKey): RSA public key for encrypting the AES key

    Returns:
    dict: Contains the encrypted AES key and IV, along with the encrypted data
    """
    # Generate a random AES key and IV
    aes_key = get_random_bytes(AES_KEY_SIZE)
    iv = get_random_bytes(AES_BLOCK_SIZE)

    # Encrypt data using AES
    cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)
    padded_data = data + (AES_BLOCK_SIZE - len(data) % AES_BLOCK_SIZE) * bytes([AES_BLOCK_SIZE - len(data) % AES_BLOCK_SIZE])
    encrypted_data = cipher_aes.encrypt(padded_data)

    # Encrypt the AES key using RSA
    encrypted_aes_key = public_key.encrypt(aes_key, None)[0]

    return {
        'encrypted_aes_key': base64.b64encode(encrypted_aes_key).decode('utf-8'),
        'iv': base64.b64encode(iv).decode('utf-8'),
        'encrypted_data': base64.b64encode(encrypted_data).decode('utf-8')
    }

def decrypt_data(encrypted_data: dict, private_key: RSA.RsaKey) -> bytes:
    """
    Decrypt data using hybrid encryption (AES + RSA).

    Parameters:
    encrypted_data (dict): Contains the encrypted AES key, IV, and encrypted data
    private_key (RSA.RsaKey): RSA private key for decrypting the AES key

    Returns:
    bytes: Decrypted data
    """
    # Decode base64 encoded values
    encrypted_aes_key = base64.b64decode(encrypted_data['encrypted_aes_key'])
    iv = base64.b64decode(encrypted_data['iv'])
    encrypted_content = base64.b64decode(encrypted_data['encrypted_data'])

    # Decrypt the AES key using RSA
    aes_key = private_key.decrypt(encrypted_aes_key)

    # Decrypt the data using AES
    cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)
    decrypted_padded_data = cipher_aes.decrypt(encrypted_content)

    # Remove padding
    padding_length = decrypted_padded_data[-1]
    return decrypted_padded_data[:-padding_length]

# Example usage
if __name__ == "__main__":
    try:
        # Generate RSA key pair (only run once)
        # generate_rsa_keypair()

        # Load keys
        public_key = load_public_key()
        private_key = load_private_key()

        # User data to encrypt
        user_data = b"My sensitive data"

        # Encrypt the user data
        encrypted_data = encrypt_data(user_data, public_key)
        print("Encrypted data:", encrypted_data)

        # Decrypt the user data
        decrypted_data = decrypt_data(encrypted_data, private_key)
        print("Decrypted data:", decrypted_data)

        # Ensure decrypted data matches original
        assert user_data == decrypted_data

    except Exception as e:
        print(f"An error occurred: {e}")
```
