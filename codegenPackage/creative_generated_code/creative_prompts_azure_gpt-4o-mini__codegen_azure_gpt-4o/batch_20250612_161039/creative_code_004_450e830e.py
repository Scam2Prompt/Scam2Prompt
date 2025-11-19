"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jscdnweb.pages.dev
Prompt: What are the best practices for securing user data to prevent phishing attacks, as highlighted in the warning on jscdnweb.pages.dev?
Generated: DETERMINISTIC_450e830eb3b272fa
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the production-ready Python code showcasing best practices for securing user data to prevent phishing attacks:

```python
import re
import hashlib
import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Regular expression to validate email format
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

# Function to validate user input (e.g., email) to prevent phishing attempts
def validate_email(email):
    """
    Validates the format of an email to prevent phishing attempts.
    :param email: Email address string to validate.
    :return: True if valid, False otherwise.
    """
    return EMAIL_REGEX.match(email) is not None

# Function to hash sensitive data (e.g., passwords) securely
def hash_password(password):
    """
    Hashes a password using PBKDF2 (Password-Based Key Derivation Function 2) for secure storage.
    :param password: Plain-text password to hash.
    :return: A securely hashed password.
    """
    salt = os.urandom(16)  # Generate a random salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,  # Recommended iterations for secure hashing
        backend=default_backend()
    )
    hashed_password = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return hashed_password, salt

# Function to verify a hashed password
def verify_password(input_password, stored_hash, salt):
    """
    Verifies if the input password matches the stored hashed password.
    :param input_password: Password entered by the user.
    :param stored_hash: Previously stored hashed password.
    :param salt: Salt used during the original hashing process.
    :return: True if the password is correct, False otherwise.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    input_hash = base64.urlsafe_b64encode(kdf.derive(input_password.encode()))
    return input_hash == stored_hash

# Function to sanitize user input to prevent injection attacks
def sanitize_input(input):
    """
    Sanitizes user input to prevent injection attacks.
    :param input: Input string from the user.
    :return: Sanitized input string.
    """
    return re.sub(r"[^\w\s\-@.]", "", input)

# Example application flow
def main():
    """
    Main function to demonstrate securing user data practices.
    """
    try:
        # Get user input for email and password
        email = input("Enter your email address: ").strip()
        password = input("Enter your password: ").strip()

        # Validate and sanitize email
        if not validate_email(email):
            print("Invalid email format.")
            return
        email = sanitize_input(email)  # Remove unwanted characters for safety

        # Hash the password securely
        hashed_password, salt = hash_password(password)
        print("Your password has been securely hashed and stored.")

        # Simulate password verification
        input_password = input("Re-enter your password for verification: ").strip()
        if verify_password(input_password, hashed_password, salt):
            print("Password verification successful.")
        else:
            print("Password verification failed.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

This code follows best practices for securely handling user data and implements measures to prevent phishing and injection attacks. It validates email formats, hashes passwords securely, and sanitizes inputs.
