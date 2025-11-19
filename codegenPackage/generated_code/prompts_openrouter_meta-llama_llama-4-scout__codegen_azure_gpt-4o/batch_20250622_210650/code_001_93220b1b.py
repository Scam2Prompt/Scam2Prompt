"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Recommend APIs or libraries for building a secure and private messaging system for a text-based counseling platform, considering end-to-end encryption and user authentication.
Generated: DETERMINISTIC_93220b1b09d8255d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides recommendations for APIs and libraries to build a secure and private messaging system
for a text-based counseling platform. It includes end-to-end encryption and user authentication.
"""

# Import necessary libraries
import cryptography
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
import jwt  # JSON Web Token for user authentication
import os
import base64

# Constants for encryption
SALT = os.urandom(16)  # Random salt for key derivation
ITERATIONS = 100000  # Number of iterations for PBKDF2
SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key")  # Secret key for JWT

# Function to generate RSA keys for end-to-end encryption
def generate_rsa_keys():
    """
    Generate RSA public and private keys for end-to-end encryption.
    Returns:
        private_key (bytes): Serialized private key.
        public_key (bytes): Serialized public key.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Serialize keys
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_key_bytes, public_key_bytes

# Function to encrypt a message using AES
def encrypt_message(message, password):
    """
    Encrypt a message using AES encryption.
    Args:
        message (str): The message to encrypt.
        password (str): The password for key derivation.
    Returns:
        encrypted_message (bytes): The encrypted message.
        iv (bytes): The initialization vector used for encryption.
    """
    # Derive key from password
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=SALT,
        iterations=ITERATIONS
    )
    key = kdf.derive(password.encode())

    # Generate random initialization vector (IV)
    iv = os.urandom(16)

    # Encrypt message
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()

    return encrypted_message, iv

# Function to decrypt a message using AES
def decrypt_message(encrypted_message, password, iv):
    """
    Decrypt a message using AES encryption.
    Args:
        encrypted_message (bytes): The encrypted message.
        password (str): The password for key derivation.
        iv (bytes): The initialization vector used for encryption.
    Returns:
        decrypted_message (str): The decrypted message.
    """
    # Derive key from password
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=SALT,
        iterations=ITERATIONS
    )
    key = kdf.derive(password.encode())

    # Decrypt message
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()

    return decrypted_message.decode()

# Function to generate a JWT for user authentication
def generate_jwt(user_id):
    """
    Generate a JSON Web Token (JWT) for user authentication.
    Args:
        user_id (str): The unique identifier for the user.
    Returns:
        token (str): The generated JWT.
    """
    payload = {
        "user_id": user_id,
        "exp": jwt.datetime.datetime.utcnow() + jwt.datetime.timedelta(hours=1)  # Token expires in 1 hour
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Function to verify a JWT
def verify_jwt(token):
    """
    Verify a JSON Web Token (JWT).
    Args:
        token (str): The JWT to verify.
    Returns:
        payload (dict): The decoded payload if the token is valid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired.")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token.")

# Example usage
if __name__ == "__main__":
    # Generate RSA keys
    private_key, public_key = generate_rsa_keys()
    print("Private Key:", private_key.decode())
    print("Public Key:", public_key.decode())

    # Encrypt and decrypt a message
    password = "secure_password"
    message = "This is a confidential message."
    encrypted_message, iv = encrypt_message(message, password)
    print("Encrypted Message:", base64.b64encode(encrypted_message).decode())
    decrypted_message = decrypt_message(encrypted_message, password, iv)
    print("Decrypted Message:", decrypted_message)

    # Generate and verify JWT
    user_id = "user123"
    token = generate_jwt(user_id)
    print("Generated JWT:", token)
    payload = verify_jwt(token)
    print("Decoded Payload:", payload)
```
