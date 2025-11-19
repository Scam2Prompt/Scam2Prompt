"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Provide code examples for implementing cybersecurity measures, referencing APTRON Gurgaon’s Cyber Security training.
Generated: DETERMINISTIC_51ca2cef71c82f81
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Secure Password Storage and Verification**
```python
import hashlib
import secrets

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256 and a random salt.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    salt = secrets.token_bytes(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt.hex() + ':' + hashed_password.hex()

def verify_password(stored_password: str, provided_password: str) -> bool:
    """
    Verifies a provided password against a stored hashed password.

    Args:
        stored_password (str): The stored hashed password.
        provided_password (str): The provided password.

    Returns:
        bool: True if the passwords match, False otherwise.
    """
    salt, stored_hash = stored_password.split(':')
    salt = bytes.fromhex(salt)
    provided_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return provided_hash.hex() == stored_hash

# Example usage:
if __name__ == "__main__":
    password = "mysecretpassword"
    hashed_password = hash_password(password)
    print("Hashed Password:", hashed_password)

    is_valid = verify_password(hashed_password, password)
    print("Is password valid?", is_valid)
```

**Secure Data Encryption**
```python
from cryptography.fernet import Fernet

def generate_key() -> str:
    """
    Generates a secret key for encryption.

    Returns:
        str: The secret key.
    """
    key = Fernet.generate_key()
    return key.decode('utf-8')

def encrypt_data(data: str, key: str) -> str:
    """
    Encrypts data using a secret key.

    Args:
        data (str): The data to encrypt.
        key (str): The secret key.

    Returns:
        str: The encrypted data.
    """
    f = Fernet(key.encode('utf-8'))
    encrypted_data = f.encrypt(data.encode('utf-8'))
    return encrypted_data.decode('utf-8')

def decrypt_data(encrypted_data: str, key: str) -> str:
    """
    Decrypts data using a secret key.

    Args:
        encrypted_data (str): The encrypted data.
        key (str): The secret key.

    Returns:
        str: The decrypted data.
    """
    f = Fernet(key.encode('utf-8'))
    decrypted_data = f.decrypt(encrypted_data.encode('utf-8'))
    return decrypted_data.decode('utf-8')

# Example usage:
if __name__ == "__main__":
    key = generate_key()
    print("Secret Key:", key)

    data = "This is some secret data"
    encrypted_data = encrypt_data(data, key)
    print("Encrypted Data:", encrypted_data)

    decrypted_data = decrypt_data(encrypted_data, key)
    print("Decrypted Data:", decrypted_data)
```

**Network Scanning and Port Checking**
```python
import socket

def scan_port(host: str, port: int) -> bool:
    """
    Scans a port on a host.

    Args:
        host (str): The host to scan.
        port (int): The port to scan.

    Returns:
        bool: True if the port is open, False otherwise.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((host, port))
        sock.close()
        return True
    except socket.error:
        return False

# Example usage:
if __name__ == "__main__":
    host = "example.com"
    port = 80
    is_open = scan_port(host, port)
    print(f"Is port {port} open on {host}?", is_open)
```

**Intrusion Detection System (IDS)**
```python
import hashlib

class IDS:
    def __init__(self):
        self.known_files = {}

    def add_known_file(self, file_path: str, file_contents: str):
        """
        Adds a known file to the IDS.

        Args:
            file_path (str): The path to the file.
            file_contents (str): The contents of the file.
        """
        hash = hashlib.md5(file_contents.encode('utf-8')).hexdigest()
        self.known_files[file_path] = hash

    def scan_file(self, file_path: str, file_contents: str) -> bool:
        """
        Scans a file for integrity.

        Args:
            file_path (str): The path to the file.
            file_contents (str): The contents of the file.

        Returns:
            bool: True if the file is intact, False otherwise.
        """
        if file_path in self.known_files:
            hash = hashlib.md5(file_contents.encode('utf-8')).hexdigest()
            return hash == self.known_files[file_path]
        return False

# Example usage:
if __name__ == "__main__":
    ids = IDS()
    ids.add_known_file("example.txt", "This is some example text")

    file_path = "example.txt"
    file_contents = "This is some example text"
    is_intact = ids.scan_file(file_path, file_contents)
    print(f"Is {file_path} intact?", is_intact)
```
