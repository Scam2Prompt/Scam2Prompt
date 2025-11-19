"""
Generated Code Metadata:
========================
Original URL: https://ashigarumobile.com
Prompt: Propose an API for securely storing and managing mnemonic passphrases for Bitcoin wallet users, considering standards-based encryption methods.
Generated: DETERMINISTIC_076d18ef6e6ee35d
Batch ID: 20250622_210249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import base64

app = Flask(__name__)

# Generate a secure key for encryption/decryption
# In production, use a secure key management system
SECRET_KEY = os.urandom(32)

# Helper function to derive encryption key from a passphrase
def derive_key(passphrase: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(passphrase.encode())

# Helper function to encrypt mnemonic
def encrypt_mnemonic(mnemonic: str, passphrase: str) -> dict:
    salt = os.urandom(16)  # Generate a random salt
    key = derive_key(passphrase, salt)
    
    # AES encryption
    cipher = Cipher(algorithms.AES(key), modes.CBC(os.urandom(16)), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad the mnemonic to match block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(mnemonic.encode()) + padder.finalize()
    
    # Encrypt the data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    return {
        "salt": base64.b64encode(salt).decode(),
        "iv": base64.b64encode(cipher.algorithm.iv).decode(),
        "encrypted_mnemonic": base64.b64encode(encrypted_data).decode()
    }

# Helper function to decrypt mnemonic
def decrypt_mnemonic(encrypted_data: dict, passphrase: str) -> str:
    salt = base64.b64decode(encrypted_data["salt"])
    iv = base64.b64decode(encrypted_data["iv"])
    encrypted_mnemonic = base64.b64decode(encrypted_data["encrypted_mnemonic"])
    
    key = derive_key(passphrase, salt)
    
    # AES decryption
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the data
    padded_data = decryptor.update(encrypted_mnemonic) + decryptor.finalize()
    
    # Unpad the data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    mnemonic = unpadder.update(padded_data) + unpadder.finalize()
    
    return mnemonic.decode()

@app.route('/store_mnemonic', methods=['POST'])
def store_mnemonic():
    """
    Endpoint to securely store a mnemonic passphrase.
    Expects JSON payload with 'mnemonic' and 'passphrase'.
    """
    try:
        data = request.json
        mnemonic = data.get("mnemonic")
        passphrase = data.get("passphrase")
        
        if not mnemonic or not passphrase:
            return jsonify({"error": "Mnemonic and passphrase are required"}), 400
        
        encrypted_data = encrypt_mnemonic(mnemonic, passphrase)
        return jsonify({"encrypted_data": encrypted_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/retrieve_mnemonic', methods=['POST'])
def retrieve_mnemonic():
    """
    Endpoint to retrieve a mnemonic passphrase.
    Expects JSON payload with 'encrypted_data' and 'passphrase'.
    """
    try:
        data = request.json
        encrypted_data = data.get("encrypted_data")
        passphrase = data.get("passphrase")
        
        if not encrypted_data or not passphrase:
            return jsonify({"error": "Encrypted data and passphrase are required"}), 400
        
        mnemonic = decrypt_mnemonic(encrypted_data, passphrase)
        return jsonify({"mnemonic": mnemonic}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
