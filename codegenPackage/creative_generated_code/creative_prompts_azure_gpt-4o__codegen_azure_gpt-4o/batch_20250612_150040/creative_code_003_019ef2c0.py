"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: Suggest APIs for implementing secure data handling and user authentication, aligning with Fantom Internet Dienst's focus on security.
Generated: DETERMINISTIC_019ef2c05f22363c
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import bcrypt  # For hashing passwords securely
import jwt     # For generating and validating JSON Web Tokens
from cryptography.fernet import Fernet  # For symmetric encryption of sensitive data

# Constants for JWT and Encryption
SECRET_KEY = "your_jwt_secret_key"  # Replace with a strong, randomly generated secret key
ENCRYPTION_KEY = Fernet.generate_key()  # Generate a secure encryption key
fernet = Fernet(ENCRYPTION_KEY)

# Function for securely hashing passwords
def hash_password(password: str) -> str:
    """
    Hashes a plain-text password using bcrypt and returns the hashed password.
    """
    try:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')  # Decode to store as a string
    except Exception as e:
        raise RuntimeError(f"Error hashing password: {e}")

# Function to verify a hashed password
def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verifies if the given plain-text password matches with the hashed password.
    """
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    except Exception as e:
        raise RuntimeError(f"Error verifying password: {e}")

# Function for generating JWT for user authentication
def generate_jwt(payload: dict) -> str:
    """
    Generates a JSON Web Token (JWT) for the provided payload.
    """
    try:
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return token
    except Exception as e:
        raise RuntimeError(f"Error generating JWT: {e}")

# Function to decode and validate a JWT
def decode_jwt(token: str) -> dict:
    """
    Decodes and validates the provided JWT token.
    """
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        raise RuntimeError("Token has expired.")
    except jwt.InvalidTokenError:
        raise RuntimeError("Invalid token.")

# Function for encrypting sensitive data
def encrypt_data(data: str) -> str:
    """
    Encrypts the provided data using symmetric encryption (Fernet).
    """
    try:
        encrypted_data = fernet.encrypt(data.encode('utf-8'))
        return encrypted_data.decode('utf-8')  # Decode to store as a string
    except Exception as e:
        raise RuntimeError(f"Error encrypting data: {e}")

# Function for decrypting sensitive data
def decrypt_data(encrypted_data: str) -> str:
    """
    Decrypts the provided encrypted data using symmetric encryption (Fernet).
    """
    try:
        decrypted_data = fernet.decrypt(encrypted_data.encode('utf-8'))
        return decrypted_data.decode('utf-8')  # Decode to retrieve the original string
    except Exception as e:
        raise RuntimeError(f"Error decrypting data: {e}")

# Example usage
if __name__ == "__main__":
    # Password hashing and verification
    plain_password = "secure_password_123"
    hashed_pw = hash_password(plain_password)
    print(f"Hashed Password: {hashed_pw}")
    print(f"Password Verified: {verify_password(plain_password, hashed_pw)}")

    # JWT generation and validation
    user_payload = {"user_id": 123, "username": "test_user"}
    token = generate_jwt(user_payload)
    print(f"Generated JWT: {token}")
    decoded_payload = decode_jwt(token)
    print(f"Decoded Payload: {decoded_payload}")

    # Encryption and decryption
    sensitive_data = "This is very sensitive information."
    encrypted = encrypt_data(sensitive_data)
    print(f"Encrypted Data: {encrypted}")
    decrypted = decrypt_data(encrypted)
    print(f"Decrypted Data: {decrypted}")
```
