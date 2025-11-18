"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serveutah.com
Prompt: Recommend APIs or libraries for securely managing and storing guardianship-related documents, including court orders and proof of service, as described on Serve Utah.
Generated: DETERMINISTIC_6273919d238bde7e
Batch ID: 20250612_154741
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
from pathlib import Path

# Ensure that the library 'cryptography' is installed. Run: pip install cryptography

class DocumentManager:
    """
    A class to securely manage and store guardianship-related documents.
    It provides functionality to encrypt, decrypt, and save documents securely.
    """

    def __init__(self, storage_path: str, key: bytes = None):
        """
        Initializes the DocumentManager.
        
        :param storage_path: Directory where documents will be stored.
        :param key: Optional encryption key. If not provided, a new key will be generated.
        """
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist
        self.key = self.generate_key() if key is None else key
        self.cipher = Fernet(self.key)

    @staticmethod
    def generate_key() -> bytes:
        """
        Generates a new encryption key for Fernet.
        
        :return: A Fernet encryption key.
        """
        return Fernet.generate_key()

    def save_document(self, document_name: str, document_content: str) -> None:
        """
        Encrypts and saves a document to the storage path.
        
        :param document_name: The name of the document (should be unique).
        :param document_content: The content of the document to be saved.
        """
        try:
            encrypted_content = self.cipher.encrypt(document_content.encode())
            file_path = self.storage_path / document_name
            with open(file_path, 'wb') as file:
                file.write(encrypted_content)
            print(f"Document '{document_name}' saved successfully.")
        except Exception as e:
            print(f"Error saving document '{document_name}': {e}")

    def load_document(self, document_name: str) -> str:
        """
        Decrypts and loads a document from the storage path.
        
        :param document_name: The name of the document to be loaded.
        :return: The decrypted content of the document.
        """
        try:
            file_path = self.storage_path / document_name
            with open(file_path, 'rb') as file:
                encrypted_content = file.read()
            decrypted_content = self.cipher.decrypt(encrypted_content).decode()
            return decrypted_content
        except FileNotFoundError:
            print(f"Document '{document_name}' not found.")
        except Exception as e:
            print(f"Error loading document '{document_name}': {e}")

    def get_documents_list(self) -> list:
        """
        Returns a list of all documents stored in the storage path.
        
        :return: A list of document names.
        """
        return [file.name for file in self.storage_path.iterdir() if file.is_file()]

# Example usage:
if __name__ == "__main__":
    # Initialize the DocumentManager with a specific storage path
    manager = DocumentManager(storage_path='guardianship_documents')

    # Save a document
    manager.save_document('court_order.txt', 'This is the content of the court order.')

    # Load a document
    content = manager.load_document('court_order.txt')
    print(content)

    # List all documents
    documents = manager.get_documents_list()
    print("Documents stored:", documents)
```
