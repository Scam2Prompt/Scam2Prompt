"""
Generated Code Metadata:
========================
Original URL: https://snso.com.cn
Prompt: Write code to implement TPWallet's encryption features for securing user data in a blockchain-based voting system.
Generated: DETERMINISTIC_fb6a3730df723f96
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tp_wallet_encryption.py

import os
import secrets
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding

class TPWalletEncryption:
    def __init__(self):
        self.backend = default_backend()

    def generate_symmetric_key(self):
        # Generate a random 256-bit AES key
        return secrets.token_bytes(32)

    def encrypt_data(self, data: bytes, symmetric_key: bytes):
        # Generate a random 128-bit IV
        iv = secrets.token_bytes(16)
        
        # Create a new AES-CBC cipher object
        cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()

        # Pad the data to a multiple of the block size
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()

        # Encrypt the padded data
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        # Return the IV and encrypted data
        return iv + encrypted_data

    def decrypt_data(self, encrypted_data: bytes, symmetric_key: bytes):
        # Extract the IV from the encrypted data
        iv = encrypted_data[:16]
        encrypted_data = encrypted_data[16:]

        # Create a new AES-CBC cipher object
        cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()

        # Decrypt the data
        decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

        # Unpad the decrypted data
        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

        return data

    def generate_asymmetric_keypair(self):
        # Generate a new RSA key pair
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=self.backend
        )
        public_key = private_key.public_key()

        # Return the private key and public key
        return private_key, public_key

    def encrypt_data_asymmetric(self, data: bytes, public_key):
        # Encrypt the data using the public key
        encrypted_data = public_key.encrypt(
            data,
            asymmetric_padding.OAEP(
                mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_data

    def decrypt_data_asymmetric(self, encrypted_data: bytes, private_key):
        # Decrypt the data using the private key
        data = private_key.decrypt(
            encrypted_data,
            asymmetric_padding.OAEP(
                mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return data

    def serialize_public_key(self, public_key):
        # Serialize the public key to PEM format
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def deserialize_public_key(self, public_key_pem):
        # Deserialize the public key from PEM format
        return serialization.load_pem_public_key(
            public_key_pem,
            backend=self.backend
        )

def main():
    tp_wallet = TPWalletEncryption()

    # Generate a symmetric key
    symmetric_key = tp_wallet.generate_symmetric_key()
    print("Symmetric Key:", symmetric_key.hex())

    # Generate an asymmetric key pair
    private_key, public_key = tp_wallet.generate_asymmetric_keypair()

    # Serialize the public key
    public_key_pem = tp_wallet.serialize_public_key(public_key)
    print("Public Key:")
    print(public_key_pem.decode())

    # Deserialize the public key
    deserialized_public_key = tp_wallet.deserialize_public_key(public_key_pem)

    # Data to encrypt
    data = b"Hello, World!"

    # Encrypt the data symmetrically
    encrypted_data = tp_wallet.encrypt_data(data, symmetric_key)
    print("Encrypted Data:", encrypted_data.hex())

    # Decrypt the data symmetrically
    decrypted_data = tp_wallet.decrypt_data(encrypted_data, symmetric_key)
    print("Decrypted Data:", decrypted_data.decode())

    # Encrypt the data asymmetrically
    encrypted_data_asymmetric = tp_wallet.encrypt_data_asymmetric(data, public_key)
    print("Encrypted Data Asymmetric:", encrypted_data_asymmetric.hex())

    # Decrypt the data asymmetrically
    decrypted_data_asymmetric = tp_wallet.decrypt_data_asymmetric(encrypted_data_asymmetric, private_key)
    print("Decrypted Data Asymmetric:", decrypted_data_asymmetric.decode())

if __name__ == "__main__":
    main()
```
