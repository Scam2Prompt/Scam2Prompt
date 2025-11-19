"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: Provide a solution for implementing a document storage system with a focus on security and technology, inspired by EasyDoc Gestão's expertise in archival services.
Generated: DETERMINISTIC_23580e1c701fe36d
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import hashlib
from cryptography.fernet import Fernet
from typing import List, Dict, Any

class DocumentStorage:
    """
    A class to represent a secure document storage system.
    """

    def __init__(self, storage_path: str, encryption_key: bytes):
        """
        Initializes the DocumentStorage with a specified path and encryption key.

        :param storage_path: Directory where documents will be stored.
        :param encryption_key: Key used for encrypting and decrypting documents.
        """
        self.storage_path = storage_path
        self.encryption_key = encryption_key
        self.fernet = Fernet(encryption_key)

        # Ensure the storage directory exists
        os.makedirs(self.storage_path, exist_ok=True)

    def _generate_file_hash(self, file_path: str) -> str:
        """
        Generates a SHA-256 hash of the file for integrity verification.

        :param file_path: Path to the file to hash.
        :return: SHA-256 hash of the file.
        """
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()

    def store_document(self, document_name: str, document_content: str) -> str:
        """
        Stores a document securely by encrypting its content.

        :param document_name: Name of the document to store.
        :param document_content: Content of the document to store.
        :return: Path to the stored document.
        """
        try:
            # Encrypt the document content
            encrypted_content = self.fernet.encrypt(document_content.encode())

            # Define the file path
            file_path = os.path.join(self.storage_path, document_name)

            # Write the encrypted content to a file
            with open(file_path, 'wb') as file:
                file.write(encrypted_content)

            return file_path
        except Exception as e:
            raise RuntimeError(f"Failed to store document: {e}")

    def retrieve_document(self, document_name: str) -> str:
        """
        Retrieves and decrypts a stored document.

        :param document_name: Name of the document to retrieve.
        :return: Decrypted content of the document.
        """
        try:
            file_path = os.path.join(self.storage_path, document_name)

            # Read the encrypted content from the file
            with open(file_path, 'rb') as file:
                encrypted_content = file.read()

            # Decrypt the content
            return self.fernet.decrypt(encrypted_content).decode()
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve document: {e}")

    def list_documents(self) -> List[Dict[str, Any]]:
        """
        Lists all documents in the storage directory with their hashes.

        :return: A list of dictionaries containing document names and their hashes.
        """
        documents = []
        try:
            for filename in os.listdir(self.storage_path):
                file_path = os.path.join(self.storage_path, filename)
                file_hash = self._generate_file_hash(file_path)
                documents.append({'name': filename, 'hash': file_hash})
            return documents
        except Exception as e:
            raise RuntimeError(f"Failed to list documents: {e}")

# Example usage
if __name__ == "__main__":
    # Generate a key for encryption (this should be done securely and stored safely)
    key = Fernet.generate_key()

    # Initialize the document storage system
    storage = DocumentStorage(storage_path='documents', encryption_key=key)

    # Store a document
    storage.store_document('example_doc.txt', 'This is a secure document.')

    # Retrieve the document
    content = storage.retrieve_document('example_doc.txt')
    print(f'Retrieved content: {content}')

    # List all documents
    documents = storage.list_documents()
    print(f'Documents in storage: {documents}')
```
