"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safepalwallet.hu
Prompt: Develop code to implement EAL 5+ security chip features in a custom cryptocurrency wallet application, inspired by SafePal hardware wallet specifications.
Generated: DETERMINISTIC_ce5bccef88fcd5ea
Batch ID: 20250612_151917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import hmac
import base64
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.exceptions import InvalidSignature

class SecurityChip:
    """
    EAL 5+ Security Chip Emulator for Cryptographic Wallet Features.
    Inspired by SafePal hardware wallet specifications.
    """

    def __init__(self):
        """
        Initialize the security chip emulation with a secure private key.
        """
        self._private_key = ec.generate_private_key(ec.SECP256R1())
        self._public_key = self._private_key.public_key()

    def generate_key_pair(self):
        """
        Generates a new ECDSA key pair.
        """
        private_key = self._private_key
        public_key = self._public_key
        return private_key, public_key

    def sign_transaction(self, transaction_data: str) -> bytes:
        """
        Signs transaction data using the private key.
        :param transaction_data: String data representing the transaction.
        :return: ECDSA signature in bytes.
        """
        try:
            transaction_hash = hashlib.sha256(transaction_data.encode()).digest()
            signature = self._private_key.sign(transaction_hash, ec.ECDSA(SHA256()))
            return signature
        except Exception as e:
            raise ValueError(f"Error signing transaction: {str(e)}")

    def verify_signature(self, transaction_data: str, signature: bytes) -> bool:
        """
        Verifies the ECDSA signature for the given transaction data.
        :param transaction_data: String data representing the transaction.
        :param signature: Signature in bytes to verify.
        :return: True if the signature is valid, False otherwise.
        """
        try:
            transaction_hash = hashlib.sha256(transaction_data.encode()).digest()
            self._public_key.verify(signature, transaction_hash, ec.ECDSA(SHA256()))
            return True
        except InvalidSignature:
            return False
        except Exception as e:
            raise ValueError(f"Error verifying signature: {str(e)}")

    def encrypt_data(self, plaintext: str, key: bytes) -> bytes:
        """
        Encrypts data using AES encryption.
        :param plaintext: The text to encrypt.
        :param key: Symmetric key for encryption (must be 256 bits).
        :return: Encrypted data in bytes.
        """
        if len(key) != 32:  # AES-256 requires a 256-bit key
            raise ValueError("Key must be 256 bits (32 bytes).")

        iv = os.urandom(16)  # Generate a secure random 16-byte IV
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
        encryptor = cipher.encryptor()
        encrypted_data = iv + encryptor.update(plaintext.encode()) + encryptor.finalize()
        return encrypted_data

    def decrypt_data(self, encrypted_data: bytes, key: bytes) -> str:
        """
        Decrypts AES-encrypted data.
        :param encrypted_data: The encrypted data as bytes.
        :param key: Symmetric key for decryption (must be 256 bits).
        :return: Decrypted text as a string.
        """
        if len(key) != 32:  # AES-256 requires a 256-bit key
            raise ValueError("Key must be 256 bits (32 bytes).")

        iv = encrypted_data[:16]  # Extract the IV from the encrypted data
        ciphertext = encrypted_data[16:]
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        return decrypted_data.decode()

    def derive_shared_key(self, peer_public_key_pem: bytes) -> bytes:
        """
        Derives a shared symmetric key using ECDH.
        :param peer_public_key_pem: Peer public key in PEM format.
        :return: Derived shared key (256 bits).
        """
        try:
            peer_public_key = serialization.load_pem_public_key(peer_public_key_pem)
            shared_key = self._private_key.exchange(ec.ECDH(), peer_public_key)
            # Derive a symmetric key using HKDF
            derived_key = HKDF(
                algorithm=SHA256(),
                length=32,
                salt=None,
                info=b'cryptowallet-shared-key'
            ).derive(shared_key)
            return derived_key
        except Exception as e:
            raise ValueError(f"Error deriving shared key: {str(e)}")

# Example Usage:
if __name__ == "__main__":
    # Instantiate the security chip emulator
    security_chip = SecurityChip()

    # Generate a key pair
    private_key, public_key = security_chip.generate_key_pair()

    # Transaction signing and verification
    transaction = "UserA sends 5 BTC to UserB"
    signature = security_chip.sign_transaction(transaction)
    is_valid = security_chip.verify_signature(transaction, signature)
    print(f"Signature valid: {is_valid}")

    # Data encryption and decryption
    aes_key = os.urandom(32)  # Generate a secure random 256-bit AES key
    encrypted_data = security_chip.encrypt_data("Sensitive transaction details", aes_key)
    decrypted_data = security_chip.decrypt_data(encrypted_data, aes_key)
    print(f"Decrypted data: {decrypted_data}")

    # Shared key derivation
    peer_public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    shared_key = security_chip.derive_shared_key(peer_public_key_pem)
    print(f"Derived shared key: {base64.b64encode(shared_key).decode()}")
```
