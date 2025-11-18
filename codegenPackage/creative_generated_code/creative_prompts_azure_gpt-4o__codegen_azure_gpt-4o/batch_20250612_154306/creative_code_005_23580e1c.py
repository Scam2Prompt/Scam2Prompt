"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Provide a solution for implementing a document storage system with a focus on security and technology, inspired by EasyDoc Gestão's expertise in archival services.
Generated: DETERMINISTIC_23580e1c701fe36d
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib
import json
from cryptography.fernet import Fernet

# Constants for system settings
STORAGE_DIR = "secure_documents"  # Directory to store files
CONFIG_FILE = "config.json"  # File holding encryption key and metadata

# Ensure the storage directory exists
if not os.path.exists(STORAGE_DIR):
    os.makedirs(STORAGE_DIR)

class SecureDocumentStorage:
    """
    A class to provide a secure document storage system, utilizing encryption and metadata management.
    """

    def __init__(self):
        """
        Initialize the SecureDocumentStorage system, loading or generating encryption key.
        """
        self.key = self._load_or_generate_key()
        self.cipher = Fernet(self.key)

    def _load_or_generate_key(self):
        """
        Load the encryption key from configuration file or generate a new one if not present.
        """
        if os.path.exists(CONFIG_FILE):
            # Load key from the config file
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                return config['encryption_key']
        else:
            # Generate a new encryption key
            new_key = Fernet.generate_key()
            with open(CONFIG_FILE, 'w') as f:
                json.dump({'encryption_key': new_key.decode()}, f)
            return new_key

    def _compute_hash(self, file_path):
        """
        Compute SHA-256 hash of a file for integrity verification.
        """
        sha256 = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                while chunk := f.read(8192):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception as e:
            raise Exception(f"Error computing hash for file {file_path}: {e}")

    def store_document(self, file_path):
        """
        Store a document securely in the system.
        
        Args:
            file_path (str): Path to the file to be stored.
        """
        try:
            file_name = os.path.basename(file_path)
            with open(file_path, 'rb') as f:
                file_data = f.read()
            
            # Encrypt the file data
            encrypted_data = self.cipher.encrypt(file_data)

            # Compute file hash
            file_hash = self._compute_hash(file_path)
            
            # Write encrypted file to storage
            secure_file_path = os.path.join(STORAGE_DIR, file_name)
            with open(secure_file_path, 'wb') as f:
                f.write(encrypted_data)

            print(f"Document '{file_name}' stored securely with hash: {file_hash}")
        except Exception as e:
            print(f"An error occurred while storing the document: {e}")

    def retrieve_document(self, file_name, output_path):
        """
        Retrieve and decrypt a document from the storage.
        
        Args:
            file_name (str): Name of the file to retrieve.
            output_path (str): Destination path to save the decrypted file.
        """
        try:
            secure_file_path = os.path.join(STORAGE_DIR, file_name)
            if not os.path.exists(secure_file_path):
                raise Exception(f"File '{file_name}' does not exist in storage.")

            # Read and decrypt file data
            with open(secure_file_path, 'rb') as f:
                encrypted_data = f.read()
            
            decrypted_data = self.cipher.decrypt(encrypted_data)

            # Write decrypted data to output path
            with open(output_path, 'wb') as f:
                f.write(decrypted_data)

            print(f"Document '{file_name}' retrieved successfully and saved to '{output_path}'.")
        except Exception as e:
            print(f"An error occurred while retrieving the document: {e}")

# Example usage
if __name__ == "__main__":
    storage_system = SecureDocumentStorage()

    # Store a document
    storage_system.store_document("example_document.txt")

    # Retrieve the document
    storage_system.retrieve_document("example_document.txt", "retrieved_document.txt")
```
