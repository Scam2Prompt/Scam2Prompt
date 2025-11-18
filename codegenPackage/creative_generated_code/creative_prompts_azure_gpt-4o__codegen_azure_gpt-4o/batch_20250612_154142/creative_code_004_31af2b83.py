"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasesupport.help
Prompt: Provide code examples for handling security questions and concerns in a cryptocurrency platform, inspired by the Coinbase Support page.
Generated: DETERMINISTIC_31af2b839a3ee945
Batch ID: 20250612_154142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# crypto_security_tools.py
import hashlib
import hmac
import os
import base64
from cryptography.fernet import Fernet

# Best Practices: Secure key and password generation & storage
def generate_secure_key():
    """
    Generates a secure encryption key for sensitive data storage and encryption.
    Returns:
        str: Secure key encoded in base64 format.
    """
    return base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')

def hash_password(password):
    """
    Hashes a password using a secure hashing algorithm (SHA-256).

    Args:
        password (str): Plain-text password.
    Returns:
        str: Hashed password.
    """
    salt = os.urandom(16)  # Generate a random salt
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return base64.b64encode(salt + hashed).decode('utf-8')

def verify_password(password, stored_hash):
    """
    Verifies a password against a stored hash.

    Args:
        password (str): Plain-text password input.
        stored_hash (str): The hash stored in the database.
    Returns:
        bool: True if the password matches, False otherwise.
    """
    decoded = base64.b64decode(stored_hash)
    salt = decoded[:16]
    stored_hashed_password = decoded[16:]
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return hmac.compare_digest(hashed, stored_hashed_password)

# Best Practices: Using symmetric encryption for sensitive data
def encrypt_data(data, key):
    """
    Encrypts sensitive data using a symmetric cipher (Fernet).

    Args:
        data (str): Plain-text data to encrypt.
        key (str): Encryption key (base64 encoded).
    Returns:
        str: Encrypted data.
    """
    cipher = Fernet(key.encode('utf-8'))
    return cipher.encrypt(data.encode('utf-8')).decode('utf-8')

def decrypt_data(encrypted_data, key):
    """
    Decrypts sensitive data using a symmetric cipher (Fernet).

    Args:
        encrypted_data (str): Encrypted data.
        key (str): Encryption key (base64 encoded).
    Returns:
        str: Decrypted plain-text data.
    """
    cipher = Fernet(key.encode('utf-8'))
    return cipher.decrypt(encrypted_data.encode('utf-8')).decode('utf-8')

# Best Practices: Rate limiting for sensitive operations
import time
from functools import wraps

def rate_limit(rate_limit_seconds):
    """
    Decorator to apply rate limiting to a function, ensuring it cannot be called more than once
    within a given time interval.

    Args:
        rate_limit_seconds (int): Number of seconds before the function can be called again.
    """
    def decorator(func):
        last_called_time = [0]  # Use a mutable object to store last-called timestamp

        @wraps(func)
        def wrapped(*args, **kwargs):
            current_time = time.time()
            if current_time - last_called_time[0] < rate_limit_seconds:
                raise Exception("Rate limit exceeded. Please try again later.")
            last_called_time[0] = current_time
            return func(*args, **kwargs)

        return wrapped
    return decorator

@rate_limit(5)
def sensitive_operation():
    """
    Example of a sensitive operation that should be rate-limited.
    """
    return "Sensitive operation performed."

# Best Practices: Logging security events
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("security.log"), logging.StreamHandler()]
)

def log_security_event(event_message):
    """
    Logs security-related events for monitoring and auditing purposes.

    Args:
        event_message (str): The event message to log.
    """
    logging.warning(event_message)

# Example Usage
if __name__ == "__main__":
    try:
        # Generate and store a key
        encryption_key = generate_secure_key()

        # Hash a password
        password = "my_secure_password"
        hashed_password = hash_password(password)

        # Verify a password
        assert verify_password(password, hashed_password)

        # Encrypt and decrypt sensitive data
        sensitive_data = "user_private_wallet_key"
        encrypted_data = encrypt_data(sensitive_data, encryption_key)
        decrypted_data = decrypt_data(encrypted_data, encryption_key)
        assert sensitive_data == decrypted_data

        # Perform rate-limited sensitive operation
        print(sensitive_operation())
        # Uncomment below to test rate limiting (will raise an exception)
        # print(sensitive_operation())

        # Log security event
        log_security_event("Unusual login attempt detected.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
