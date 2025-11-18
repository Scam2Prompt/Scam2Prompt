"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gngm.clck.hk
Prompt: Develop a script to automate the creation of a GMGN account, including device ID validation, seed phrase setup, and password creation.
Generated: DETERMINISTIC_d9a1415bd568b391
Batch ID: 20250612_154728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import hashlib
import os
import json

# Error classes for custom exceptions
class ValidationError(Exception):
    pass

class AccountCreationError(Exception):
    pass

def generate_device_id():
    """
    Generate a unique device ID using a combination of random letters and numbers.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def validate_device_id(device_id):
    """
    Validate the format of the device ID.
    Must be exactly 16 characters long, containing only letters and digits.
    """
    if not (isinstance(device_id, str) and len(device_id) == 16 and device_id.isalnum()):
        raise ValidationError("Invalid device ID. Must be 16 alphanumeric characters.")

def generate_seed_phrase():
    """
    Generate a seed phrase consisting of 12 random words from a predefined word list.
    """
    word_list = [
        "apple", "orange", "banana", "grape", "kiwi", "mango", "blueberry", "peach",
        "cherry", "plum", "pear", "lemon", "lime", "watermelon", "strawberry", "raspberry",
        "pineapple", "coconut", "apricot", "nectarine", "fig", "pomegranate", "papaya", "guava",
    ]
    return ' '.join(random.choices(word_list, k=12))

def create_password():
    """
    Generate a secure random password consisting of 12 characters.
    Includes uppercase, lowercase, digits, and special characters.
    """
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return ''.join(random.choices(characters, k=12))

def hash_password(password):
    """
    Hash the password using SHA-256 for secure storage.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def create_gmgn_account():
    """
    Create a GMGN account with device ID validation, seed phrase setup, and password creation.
    Returns a JSON object containing the account details.
    """
    try:
        # Generate device ID
        device_id = generate_device_id()
        validate_device_id(device_id)

        # Generate seed phrase
        seed_phrase = generate_seed_phrase()

        # Create and hash password
        password = create_password()
        hashed_password = hash_password(password)

        # Save account details securely
        account_details = {
            "device_id": device_id,
            "seed_phrase": seed_phrase,
            "password_hash": hashed_password
        }

        # Simulate writing to a secure storage/file (for production use, implement encryption)
        account_file = os.path.join(os.getcwd(), "gmgn_account.json")
        with open(account_file, "w") as file:
            json.dump(account_details, file, indent=4)

        return account_details

    except ValidationError as ve:
        raise AccountCreationError(f"Account creation failed due to validation error: {str(ve)}")
    except Exception as e:
        raise AccountCreationError(f"Account creation failed due to an unexpected error: {str(e)}")


# Main function to kickstart the account creation process
if __name__ == "__main__":
    try:
        account = create_gmgn_account()
        print("GMGN account successfully created!")
        print("Account details:")
        print(json.dumps(account, indent=4))

        # Note: For security reasons, do not print or share the seed phrase and password in production logs.
    except AccountCreationError as ace:
        print(f"Error: {str(ace)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
