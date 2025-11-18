"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://danielasteinsapir.com
Prompt: Generate a script to encrypt and decrypt sensitive files on Windows and Mac systems, referencing the Tornado Cash privacy principles.
Generated: DETERMINISTIC_faa76300936ecb20
Batch ID: 20250612_145121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
from cryptography.fernet import Fernet
import getpass

# Function to generate a key for encryption and decryption
def generate_key():
    """Generates a new encryption key and saves it to a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved as 'secret.key'.")

# Function to load the key from the file
def load_key():
    """Loads the encryption key from the current directory."""
    return open("secret.key", "rb").read()

# Function to encrypt a file
def encrypt_file(file_path):
    """Encrypts a file using the provided key."""
    key = load_key()
    f = Fernet(key)

    # Read the file
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    # Encrypt the data
    encrypted_data = f.encrypt(file_data)
    
    # Write the encrypted data back to a new file
    with open(file_path + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    
    print(f"File '{file_path}' encrypted successfully.")

# Function to decrypt a file
def decrypt_file(file_path):
    """Decrypts an encrypted file using the provided key."""
    key = load_key()
    f = Fernet(key)

    # Read the encrypted file
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    
    # Decrypt the data
    decrypted_data = f.decrypt(encrypted_data)
    
    # Write the decrypted data back to a new file
    original_file_path = file_path.replace(".encrypted", "")
    with open(original_file_path, "wb") as file:
        file.write(decrypted_data)
    
    print(f"File '{file_path}' decrypted successfully.")

# Main function to handle user input and execution
def main():
    """Main function to execute the encryption and decryption operations."""
    if len(sys.argv) < 3:
        print("Usage: python encrypt_decrypt.py [encrypt|decrypt] <file_path>")
        sys.exit(1)

    action = sys.argv[1].lower()
    file_path = sys.argv[2]

    # Check if the specified file exists
    if not os.path.isfile(file_path) and action != "generate_key":
        print(f"Error: The file '{file_path}' does not exist.")
        sys.exit(1)

    try:
        if action == "generate_key":
            generate_key()
        elif action == "encrypt":
            encrypt_file(file_path)
        elif action == "decrypt":
            decrypt_file(file_path)
        else:
            print("Invalid action. Use 'generate_key', 'encrypt', or 'decrypt'.")
            sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

Make sure to install the required library before running the script:
```bash
pip install cryptography
```
