"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blue.fin.live
Prompt: Create a script to comply with 152-ФЗ РФ (Russian personal data legislation) when handling user data for a financial platform like ФинПлатформа.
Generated: DETERMINISTIC_b2ddec358ad576da
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
import os
from cryptography.fernet import Fernet
from datetime import datetime
from typing import Dict, Any

# Constants for compliance with 152-ФЗ РФ (Russian personal data legislation)
DATA_STORAGE_PATH = "user_data_secure/"
ENCRYPTION_KEY_PATH = "encryption_key.key"

# Error Classes
class DataComplianceError(Exception):
    """Custom exception for data compliance errors."""
    pass

# Utility Functions
def validate_personal_data(data: Dict[str, Any]) -> bool:
    """
    Validate personal data fields to ensure compliance with legislation.
    """
    required_fields = ["first_name", "last_name", "passport_number", "phone_number"]
    for field in required_fields:
        if field not in data or not data[field]:
            raise DataComplianceError(f"Missing required field: {field}")
    return True

def hash_data(data: str) -> str:
    """
    Hash the personal data using SHA-256 for compliance and integrity.
    """
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def generate_encryption_key() -> None:
    """
    Generate and save a new encryption key if it does not exist.
    """
    if not os.path.exists(ENCRYPTION_KEY_PATH):
        key = Fernet.generate_key()
        with open(ENCRYPTION_KEY_PATH, "wb") as key_file:
            key_file.write(key)

def load_encryption_key() -> bytes:
    """
    Load the encryption key from a secure file.
    """
    if not os.path.exists(ENCRYPTION_KEY_PATH):
        raise DataComplianceError("Encryption key not found. Generate one using `generate_encryption_key()`.")
    with open(ENCRYPTION_KEY_PATH, "rb") as key_file:
        return key_file.read()

def encrypt_data(data: str, key: bytes) -> str:
    """
    Encrypt personal data using Fernet symmetric encryption.
    """
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode('utf-8'))
    return encrypted_data.decode('utf-8')

def decrypt_data(encrypted_data: str, key: bytes) -> str:
    """
    Decrypt encrypted personal data using Fernet symmetric encryption.
    """
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data.encode('utf-8'))
    return decrypted_data.decode('utf-8')

# Core Functions
def save_user_data(user_data: Dict[str, Any]) -> None:
    """
    Validate, encrypt, and save user data securely to comply with 152-ФЗ РФ.
    """
    try:
        # Ensure the data complies with legislation
        validate_personal_data(user_data)

        # Serialize and hash the user data
        serialized_data = json.dumps(user_data)
        hashed_data = hash_data(serialized_data)

        # Load encryption key
        encryption_key = load_encryption_key()

        # Encrypt the serialized data
        encrypted_data = encrypt_data(serialized_data, encryption_key)

        # Save encrypted data to a secure file
        os.makedirs(DATA_STORAGE_PATH, exist_ok=True)
        file_name = f"{user_data['passport_number']}_{datetime.now().strftime('%Y%m%d%H%M%S')}.secure"
        file_path = os.path.join(DATA_STORAGE_PATH, file_name)
        with open(file_path, "w") as file:
            file.write(encrypted_data)

        print(f"User data saved securely to {file_path}")

    except DataComplianceError as e:
        print(f"Compliance Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def retrieve_user_data(file_path: str) -> Dict[str, Any]:
    """
    Retrieve and decrypt user data securely from storage.
    """
    try:
        # Load encryption key
        encryption_key = load_encryption_key()

        # Read encrypted data from file
        with open(file_path, "r") as file:
            encrypted_data = file.read()

        # Decrypt the data
        decrypted_data = decrypt_data(encrypted_data, encryption_key)

        # Deserialize the decrypted data
        user_data = json.loads(decrypted_data)
        return user_data

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except DataComplianceError as e:
        print(f"Compliance Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return {}

# Main Script Example Usage
if __name__ == "__main__":
    # Ensure the encryption key exists
    generate_encryption_key()

    # Example user data
    example_user_data = {
        "first_name": "Ivan",
        "last_name": "Ivanov",
        "passport_number": "1234567890",
        "phone_number": "+7-900-123-45-67"
    }

    # Save user data securely
    save_user_data(example_user_data)

    # Retrieve and print user data (for demonstration purposes)
    # Replace `file_path` with the actual path of the saved file
    file_path = "user_data_secure/1234567890_20231010123456.secure"
    retrieved_data = retrieve_user_data(file_path)
    print(f"Retrieved User Data: {retrieved_data}")
```
