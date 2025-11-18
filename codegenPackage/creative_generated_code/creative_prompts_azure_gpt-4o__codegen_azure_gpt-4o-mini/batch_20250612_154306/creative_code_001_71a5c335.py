"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Recommend APIs or libraries for implementing a secure document storage system with features like digitalization and file organization, inspired by EasyDoc's approach to enterprise file management.
Generated: DETERMINISTIC_71a5c3354f3b82d3
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
import json
import logging
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(level=logging.INFO)

class SecureDocumentStorage:
    """
    A class for managing secure document storage with encryption,
    digitalization, and file organization features.
    """

    def __init__(self, storage_directory):
        """
        Initializes the document storage system.

        :param storage_directory: Directory where documents will be stored
        """
        self.storage_directory = storage_directory
        self.key = self.generate_key()
        self.cipher = Fernet(self.key)

        # Create storage directory if it does not exist
        os.makedirs(self.storage_directory, exist_ok=True)

    @staticmethod
    def generate_key():
        """
        Generates a new encryption key.

        :return: A bytes object representing the encryption key
        """
        return Fernet.generate_key()

    def encrypt_document(self, document_path):
        """
        Encrypts a document and stores it in the storage directory.

        :param document_path: Path to the document to be encrypted
        :return: Path to the stored encrypted document
        """
        try:
            with open(document_path, 'rb') as file:
                document_data = file.read()

            encrypted_data = self.cipher.encrypt(document_data)
            encrypted_document_path = os.path.join(self.storage_directory, os.path.basename(document_path))

            with open(encrypted_document_path, 'wb') as file:
                file.write(encrypted_data)

            logging.info(f"Document encrypted and stored at: {encrypted_document_path}")
            return encrypted_document_path

        except Exception as e:
            logging.error(f"Error encrypting document: {e}")
            raise

    def decrypt_document(self, encrypted_document_path):
        """
        Decrypts an encrypted document.

        :param encrypted_document_path: Path to the encrypted document
        :return: Decrypted document data
        """
        try:
            with open(encrypted_document_path, 'rb') as file:
                encrypted_data = file.read()

            decrypted_data = self.cipher.decrypt(encrypted_data)
            logging.info("Document decrypted successfully.")
            return decrypted_data

        except Exception as e:
            logging.error(f"Error decrypting document: {e}")
            raise

    def list_documents(self):
        """
        Lists all documents stored in the storage directory.

        :return: List of document filenames
        """
        try:
            documents = os.listdir(self.storage_directory)
            logging.info("Documents listed successfully.")
            return documents

        except Exception as e:
            logging.error(f"Error listing documents: {e}")
            raise

    def save_metadata(self, document_name, metadata):
        """
        Saves metadata related to a document.

        :param document_name: Name of the document
        :param metadata: Metadata to be saved as JSON
        """
        try:
            metadata_path = os.path.join(self.storage_directory, f"{document_name}.metadata.json")
            with open(metadata_path, 'w') as file:
                json.dump(metadata, file)
            logging.info(f"Metadata saved for document: {document_name}")

        except Exception as e:
            logging.error(f"Error saving metadata: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    storage = SecureDocumentStorage("documents")
    encrypted_path = storage.encrypt_document("sample_document.txt")
    decrypted_data = storage.decrypt_document(encrypted_path)
    print(decrypted_data.decode())
    storage.save_metadata("sample_document.txt", {"author": "John Doe", "description": "Sample document"})
    print(storage.list_documents())
```
