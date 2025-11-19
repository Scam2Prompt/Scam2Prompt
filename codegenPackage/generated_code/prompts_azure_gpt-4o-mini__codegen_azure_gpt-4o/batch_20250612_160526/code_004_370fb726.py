"""
Generated Code Metadata:
========================
Original URL: https://teslafluxtrade.com
Prompt: Illustrate how to implement KYC compliance in a crypto trading application similar to Teslaflux Trade, ensuring user data security and legal adherence.
Generated: DETERMINISTIC_370fb7267cca4b62
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import json
import hashlib
from cryptography.fernet import Fernet
from datetime import datetime

# Generate a key for encryption (should be securely stored and managed in production)
ENCRYPTION_KEY = Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)

# Constants for KYC validation
MIN_AGE = 18
REQUIRED_FIELDS = ["first_name", "last_name", "dob", "email", "phone", "address", "id_document"]

# Error classes for KYC validation
class KYCValidationError(Exception):
    pass

class DataEncryptionError(Exception):
    pass

# Function to validate user data
def validate_user_data(user_data):
    """
    Validates the user data for KYC compliance.
    :param user_data: dict containing user information
    :raises KYCValidationError: if validation fails
    """
    # Check for missing fields
    for field in REQUIRED_FIELDS:
        if field not in user_data:
            raise KYCValidationError(f"Missing required field: {field}")

    # Validate email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, user_data["email"]):
        raise KYCValidationError("Invalid email format")

    # Validate phone number format (example: international format)
    phone_regex = r'^\+?[1-9]\d{1,14}$'
    if not re.match(phone_regex, user_data["phone"]):
        raise KYCValidationError("Invalid phone number format")

    # Validate age
    dob = datetime.strptime(user_data["dob"], "%Y-%m-%d")
    age = (datetime.now() - dob).days // 365
    if age < MIN_AGE:
        raise KYCValidationError("User must be at least 18 years old")

# Function to encrypt sensitive user data
def encrypt_data(data):
    """
    Encrypts sensitive user data using Fernet encryption.
    :param data: dict containing user information
    :return: encrypted data as bytes
    :raises DataEncryptionError: if encryption fails
    """
    try:
        json_data = json.dumps(data)
        encrypted_data = cipher_suite.encrypt(json_data.encode())
        return encrypted_data
    except Exception as e:
        raise DataEncryptionError(f"Failed to encrypt data: {str(e)}")

# Function to decrypt sensitive user data
def decrypt_data(encrypted_data):
    """
    Decrypts sensitive user data using Fernet encryption.
    :param encrypted_data: encrypted data as bytes
    :return: decrypted data as dict
    :raises DataEncryptionError: if decryption fails
    """
    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
        return json.loads(decrypted_data)
    except Exception as e:
        raise DataEncryptionError(f"Failed to decrypt data: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample user data
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "dob": "2000-01-01",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "address": "123 Main St, Springfield, USA",
        "id_document": "passport_123456"
    }

    try:
        # Validate user data
        validate_user_data(user_data)
        print("User data validation passed.")

        # Encrypt user data
        encrypted_data = encrypt_data(user_data)
        print("User data encrypted successfully.")

        # Decrypt user data
        decrypted_data = decrypt_data(encrypted_data)
        print("User data decrypted successfully.")
        print("Decrypted Data:", decrypted_data)

    except KYCValidationError as e:
        print(f"KYC Validation Error: {e}")
    except DataEncryptionError as e:
        print(f"Data Encryption Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
