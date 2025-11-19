"""
Generated Code Metadata:
========================
Original URL: https://opsec.finance
Prompt: "Code example for encrypting financial data at rest and in transit."
Generated: DETERMINISTIC_854458c3031fab86
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64
import ssl
import socket

# Encryption at rest using AES with Fernet

def generate_key(password: bytes, salt: bytes) -> bytes:
    """
    Derive a secure encryption key from a password and salt using PBKDF2.
    
    Args:
        password: User-provided password as bytes
        salt: Random salt value as bytes
        
    Returns:
        Encryption key suitable for Fernet
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password))

def encrypt_data(data: str, key: bytes) -> bytes:
    """
    Encrypt data using Fernet symmetric encryption.
    
    Args:
        data: Plaintext string to encrypt
        key: Encryption key (must be 32 url-safe base64-encoded bytes)
        
    Returns:
        Encrypted ciphertext as bytes
    """
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(ciphertext: bytes, key: bytes) -> str:
    """
    Decrypt data using Fernet symmetric encryption.
    
    Args:
        ciphertext: Encrypted data as bytes
        key: Encryption key (must be 32 url-safe base64-encoded bytes)
        
    Returns:
        Decrypted plaintext string
    """
    fernet = Fernet(key)
    return fernet.decrypt(ciphertext).decode()

# Encryption in transit using TLS

def create_ssl_context(certfile: str, keyfile: str, cafile: str) -> ssl.SSLContext:
    """
    Create a secure SSL context for TLS encryption.
    
    Args:
        certfile: Path to server certificate
        keyfile: Path to private key
        cafile: Path to CA certificate
        
    Returns:
        Configured SSLContext object
    """
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    context.load_verify_locations(cafile=cafile)
    context.verify_mode = ssl.CERT_REQUIRED
    return context

def secure_server(host: str, port: int, certfile: str, keyfile: str, cafile: str):
    """
    Start a secure TLS server that echoes back received messages.
    
    Args:
        host: Server hostname/IP
        port: Server port
        certfile: Path to server certificate
        keyfile: Path to private key
        cafile: Path to CA certificate
    """
    context = create_ssl_context(certfile, keyfile, cafile)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(1)
        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

def secure_client(host: str, port: int, certfile: str, cafile: str):
    """
    Connect to a secure TLS server and send a test message.
    
    Args:
        host: Server hostname/IP
        port: Server port
        certfile: Path to client certificate
        cafile: Path to CA certificate
    """
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_cert_chain(certfile=certfile)
    context.load_verify_locations(cafile=cafile)
    context.verify_mode = ssl.CERT_REQUIRED
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.connect((host, port))
            ssock.sendall(b"Secure financial data")
            data = ssock.recv(1024)
            print(f"Received: {data.decode()}")

# Example usage for encryption at rest
if __name__ == "__main__":
    # Generate a key from password
    password = b"secure_password"
    salt = os.urandom(16)
    key = generate_key(password, salt)
    
    # Encrypt and decrypt financial data
    financial_data = "Sensitive account information"
    encrypted = encrypt_data(financial_data, key)
    decrypted = decrypt_data(encrypted, key)
    
    print(f"Original: {financial_data}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    # Note: For production, store salt alongside encrypted data
    # and manage passwords securely (not hardcoded as in this example)
```
