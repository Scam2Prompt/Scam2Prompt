"""
Generated Code Metadata:
========================
Original URL: https://opsec.finance
Prompt: "What are the best practices for implementing operational security in financial services?"
Generated: DETERMINISTIC_751a28cd1c457749
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Operational Security Best Practices Implementation for Financial Services

This module provides a set of functions and classes to implement operational security
best practices in financial services applications.
"""

import logging
import hashlib
import os
import re
from typing import Optional
from datetime import datetime, timedelta
import secrets
import string
import ssl
import socket
from cryptography.fernet import Fernet
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class OperationalSecurity:
    """
    A class to encapsulate operational security best practices for financial services.
    """

    def __init__(self):
        self.encryption_key = self._generate_encryption_key()

    @staticmethod
    def _generate_encryption_key() -> bytes:
        """
        Generate a secure encryption key using Fernet symmetric encryption.
        
        Returns:
            bytes: Generated encryption key
        """
        return Fernet.generate_key()

    def encrypt_data(self, data: str) -> bytes:
        """
        Encrypt sensitive data using Fernet encryption.
        
        Args:
            data (str): Data to be encrypted
            
        Returns:
            bytes: Encrypted data
        """
        fernet = Fernet(self.encryption_key)
        return fernet.encrypt(data.encode())

    def decrypt_data(self, encrypted_data: bytes) -> str:
        """
        Decrypt data using Fernet encryption.
        
        Args:
            encrypted_data (bytes): Data to be decrypted
            
        Returns:
            str: Decrypted data
        """
        fernet = Fernet(self.encryption_key)
        return fernet.decrypt(encrypted_data).decode()

    @staticmethod
    def generate_strong_password(length: int = 16) -> str:
        """
        Generate a strong random password.
        
        Args:
            length (int): Length of the password (default: 16)
            
        Returns:
            str: Generated password
        """
        alphabet = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(secrets.choice(alphabet) for _ in range(length))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and any(c.isdigit() for c in password)
                    and any(c in string.punctuation for c in password)):
                return password

    @staticmethod
    def hash_sensitive_data(data: str, salt: Optional[str] = None) -> tuple:
        """
        Hash sensitive data with optional salt using PBKDF2.
        
        Args:
            data (str): Data to be hashed
            salt (str, optional): Optional salt value
            
        Returns:
            tuple: (hashed_data, salt_used)
        """
        if salt is None:
            salt = secrets.token_hex(16)
        hashed = hashlib.pbkdf2_hmac(
            'sha256',
            data.encode(),
            salt.encode(),
            100000
        )
        return hashed.hex(), salt

    @staticmethod
    def validate_password_strength(password: str) -> bool:
        """
        Validate password meets strength requirements.
        
        Args:
            password (str): Password to validate
            
        Returns:
            bool: True if password meets requirements
        """
        if len(password) < 12:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        if not re.search(r'[^A-Za-z0-9]', password):
            return False
        return True

    @staticmethod
    def secure_communication(host: str, port: int, certfile: str, keyfile: str) -> socket.socket:
        """
        Establish a secure SSL/TLS communication channel.
        
        Args:
            host (str): Host to connect to
            port (int): Port number
            certfile (str): Path to certificate file
            keyfile (str): Path to private key file
            
        Returns:
            socket.socket: Secure socket connection
        """
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # Disable older TLS versions
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        secure_sock = context.wrap_socket(sock, server_side=True)
        secure_sock.bind((host, port))
        return secure_sock

    @staticmethod
    def audit_log(action: str, user: str, details: str):
        """
        Create an audit log entry for security events.
        
        Args:
            action (str): Action being logged
            user (str): User performing the action
            details (str): Additional details
        """
        timestamp = datetime.utcnow().isoformat()
        log_entry = f"[{timestamp}] User: {user}, Action: {action}, Details: {details}"
        logger.info(log_entry)
        # In production, this would also write to a secure audit log file/database

    @staticmethod
    def enforce_session_timeout(max_minutes: int = 30):
        """
        Decorator to enforce session timeout for sensitive operations.
        
        Args:
            max_minutes (int): Maximum session duration in minutes
        """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # In a real implementation, this would check the session timestamp
                # stored in the user's session data
                session_start = kwargs.get('session_start', datetime.utcnow())
                if datetime.utcnow() - session_start > timedelta(minutes=max_minutes):
                    raise SessionTimeoutError("Session has expired")
                return func(*args, **kwargs)
            return wrapper
        return decorator


class SessionTimeoutError(Exception):
    """Exception raised when a session times out."""
    pass


# Example usage
if __name__ == "__main__":
    ops_sec = OperationalSecurity()
    
    # Example password generation and validation
    password = ops_sec.generate_strong_password()
    print(f"Generated password: {password}")
    print(f"Password valid: {ops_sec.validate_password_strength(password)}")
    
    # Example data encryption
    sensitive_data = "Credit Card: 4111-1111-1111-1111"
    encrypted = ops_sec.encrypt_data(sensitive_data)
    decrypted = ops_sec.decrypt_data(encrypted)
    print(f"Original: {sensitive_data}")
    print(f"Decrypted: {decrypted}")
    
    # Example hashing
    hashed, salt = ops_sec.hash_sensitive_data("user_password")
    print(f"Hashed: {hashed}, Salt: {salt}")
    
    # Example audit logging
    ops_sec.audit_log("LOGIN_ATTEMPT", "admin", "Successful login from 192.168.1.1")
```
