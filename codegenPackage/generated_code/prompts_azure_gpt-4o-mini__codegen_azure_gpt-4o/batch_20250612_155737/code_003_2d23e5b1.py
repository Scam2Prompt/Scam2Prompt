"""
Generated Code Metadata:
========================
Original URL: https://aethiredge.tw
Prompt: Explain how to implement end-to-end encryption for data communication in an Aethir Edge setup.
Generated: DETERMINISTIC_2d23e5b12d42f191
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of end-to-end encryption for data communication in an Aethir Edge setup. The code uses RSA for asymmetric encryption and AES for symmetric encryption.

```python
import os
import rsa
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Generate RSA keys for asymmetric encryption
def generate_rsa_keys():
    """
    Generate RSA public and private keys.
    Returns:
        tuple: (public_key, private_key)
    """
    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key

# Encrypt data using RSA public key
def rsa_encrypt(data, public_key):
    """
    Encrypt data using RSA public key.
    Args:
        data (bytes): Data to encrypt.
        public_key (rsa.PublicKey): RSA public key.
    Returns:
        bytes: Encrypted data.
    """
    try:
        return rsa.encrypt(data, public_key)
    except Exception as e:
        raise ValueError(f"RSA encryption failed: {e}")

# Decrypt data using RSA private key
def rsa_decrypt(encrypted_data, private_key):
    """
    Decrypt data using RSA private key.
    Args:
        encrypted_data (bytes): Encrypted data.
        private_key (rsa.PrivateKey): RSA private key.
    Returns:
        bytes: Decrypted data.
    """
    try:
        return rsa.decrypt(encrypted_data, private_key)
    except Exception as e:
        raise ValueError(f"RSA decryption failed: {e}")

# Generate AES key for symmetric encryption
def generate_aes_key():
    """
    Generate a random AES key.
    Returns:
        bytes: AES key (256-bit).
    """
    return os.urandom(32)  # 256-bit key

# Encrypt data using AES key
def aes_encrypt(data, aes_key):
    """
    Encrypt data using AES key.
    Args:
        data (bytes): Data to encrypt.
        aes_key (bytes): AES key (256-bit).
    Returns:
        tuple: (encrypted_data, iv)
    """
    try:
        cipher = AES.new(aes_key, AES.MODE_CBC)
        iv = cipher.iv  # Initialization vector
        encrypted_data = cipher.encrypt(pad(data, AES.block_size))
        return encrypted_data, iv
    except Exception as e:
        raise ValueError(f"AES encryption failed: {e}")

# Decrypt data using AES key
def aes_decrypt(encrypted_data, aes_key, iv):
    """
    Decrypt data using AES key.
    Args:
        encrypted_data (bytes): Encrypted data.
        aes_key (bytes): AES key (256-bit).
        iv (bytes): Initialization vector.
    Returns:
        bytes: Decrypted data.
    """
    try:
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(encrypted_data), AES.block_size)
    except Exception as e:
        raise ValueError(f"AES decryption failed: {e}")

# Example usage
if __name__ == "__main__":
    # Step 1: Generate RSA keys
    public_key, private_key = generate_rsa_keys()

    # Step 2: Generate AES key
    aes_key = generate_aes_key()

    # Step 3: Encrypt AES key using RSA public key
    encrypted_aes_key = rsa_encrypt(aes_key, public_key)

    # Step 4: Decrypt AES key using RSA private key
    decrypted_aes_key = rsa_decrypt(encrypted_aes_key, private_key)

    # Verify AES key integrity
    assert aes_key == decrypted_aes_key, "AES key mismatch after decryption!"

    # Step 5: Encrypt data using AES key
    data = b"Sensitive data to be encrypted"
    encrypted_data, iv = aes_encrypt(data, aes_key)

    # Step 6: Decrypt data using AES key
    decrypted_data = aes_decrypt(encrypted_data, aes_key, iv)

    # Verify data integrity
    assert data == decrypted_data, "Data mismatch after decryption!"

    print("End-to-end encryption successful!")
```

This code demonstrates how to implement end-to-end encryption using RSA for key exchange and AES for data encryption. It includes error handling, comments, and follows best practices.
