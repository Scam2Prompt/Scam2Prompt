"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: How can I implement a secure document storage system using the techniques described by EasyDoc for managing corporate files?
Generated: DETERMINISTIC_ac6c9aa9d368282d
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import hashlib
from cryptography.fernet import Fernet
from typing import Dict, Any

class SecureDocumentStorage:
    def __init__(self, storage_path: str, encryption_key: str):
        """
        Initialize the SecureDocumentStorage with the specified storage path and encryption key.

        :param storage_path: Directory where documents will be stored
        :param encryption_key: The key used for encrypting and decrypting documents
        """
        self.storage_path = storage_path
        self.encryption_key = encryption_key
        self.fernet = Fernet(encryption_key)

        # Ensure the storage directory exists
        os.makedirs(self.storage_path, exist_ok=True)

    def save_document(self, document_name: str, document_content: str) -> None:
        """
        Save an encrypted document to the storage.

        :param document_name: Name of the document (without extension)
        :param document_content: Content of the document to be saved
        """
        try:
            # Encrypt the document content
            encrypted_content = self.fernet.encrypt(document_content.encode())

            # Create the full path for the document
            document_path = os.path.join(self.storage_path, f"{document_name}.enc")

            # Write encrypted content to file
            with open(document_path, 'wb') as file:
                file.write(encrypted_content)

            print(f"Document '{document_name}' saved successfully.")
        except Exception as e:
            print(f"Error saving document '{document_name}': {e}")

    def retrieve_document(self, document_name: str) -> str:
        """
        Retrieve and decrypt a document from the storage.

        :param document_name: Name of the document to retrieve (without extension)
        :return: Decrypted document content
        """
        try:
            # Create the full path for the encrypted document
            document_path = os.path.join(self.storage_path, f"{document_name}.enc")

            # Read the encrypted content from file
            with open(document_path, 'rb') as file:
                encrypted_content = file.read()

            # Decrypt the content
            decrypted_content = self.fernet.decrypt(encrypted_content).decode()

            return decrypted_content
        except FileNotFoundError:
            print(f"Document '{document_name}' not found.")
            return ""
        except Exception as e:
            print(f"Error retrieving document '{document_name}': {e}")
            return ""

    def list_documents(self) -> Dict[str, Any]:
        """
        List all documents in the storage.

        :return: A dictionary with document names (without extension) as keys
        """
        try:
            documents = {}
            for filename in os.listdir(self.storage_path):
                if filename.endswith('.enc'):
                    # Store only the document name without the extension
                    documents[os.path.splitext(filename)[0]] = 'Encrypted Document'

            return documents
        except Exception as e:
            print(f"Error listing documents: {e}")
            return {}

# Example usage:
if __name__ == "__main__":
    # Generate a key for encryption
    key = Fernet.generate_key()

    # Initialize the SecureDocumentStorage
    storage = SecureDocumentStorage(storage_path='documents', encryption_key=key)

    # Save a document
    storage.save_document('example', 'This is a secure document.')

    # Retrieve the document
    content = storage.retrieve_document('example')
    print(f'Retrieved Content: {content}')

    # List all documents
    documents = storage.list_documents()
    print("Documents:", documents)
```
