"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Write code to implement a secure document retrieval system for enterprises, incorporating features like categorization and digitalization as highlighted by EasyDoc Gestão.
Generated: DETERMINISTIC_77214a8255533783
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation of a secure document retrieval system with categorization and digitalization functionalities:

```python
import os
import json
import hashlib
from cryptography.fernet import Fernet

# Secure Document Retrieval System
class SecureDocumentRetrievalSystem:
    def __init__(self, encryption_key=None, storage_path="documents"):
        """
        Initializes the system with encryption key and storage path.

        :param encryption_key: Optional encryption key for securing documents.
        :param storage_path: Path to store digitalized and categorized documents.
        """
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)  # Create storage directory if it doesn't exist

        # Generate a new encryption key if none is provided
        if encryption_key is None:
            encryption_key = Fernet.generate_key()

        self.cipher = Fernet(encryption_key)
        self.categories = {}  # Dictionary to store category metadata

    def add_document(self, file_path, category):
        """
        Adds a document to the system under the specified category.
        The document is encrypted and stored securely.

        :param file_path: Path of the document to add.
        :param category: Category under which the document is stored.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Document '{file_path}' not found.")

        with open(file_path, "rb") as file:
            file_data = file.read()

        # Encrypt the document
        encrypted_data = self.cipher.encrypt(file_data)

        # Hash the file name for secure storage
        file_name = os.path.basename(file_path)
        file_hash = hashlib.sha256(file_name.encode()).hexdigest()

        # Determine category path and save the document
        category_path = os.path.join(self.storage_path, category)
        os.makedirs(category_path, exist_ok=True)
        encrypted_file_path = os.path.join(category_path, file_hash)

        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        # Update category metadata
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(file_name)

        print(f"Document '{file_name}' added securely under category '{category}'.")

    def retrieve_document(self, file_name, category):
        """
        Retrieves and decrypts a document from the system.

        :param file_name: Name of the document to be retrieved.
        :param category: Category under which the document is stored.
        :return: Decrypted document data.
        """
        if category not in self.categories or file_name not in self.categories[category]:
            raise ValueError(f"Document '{file_name}' not found in category '{category}'.")

        # Hash the file name to locate stored file
        file_hash = hashlib.sha256(file_name.encode()).hexdigest()
        encrypted_file_path = os.path.join(self.storage_path, category, file_hash)

        if not os.path.exists(encrypted_file_path):
            raise FileNotFoundError(f"Encrypted file '{encrypted_file_path}' not found.")

        # Read and decrypt the file data
        with open(encrypted_file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        decrypted_data = self.cipher.decrypt(encrypted_data)
        print(f"Document '{file_name}' retrieved successfully from category '{category}'.")
        return decrypted_data

    def list_category_documents(self, category):
        """
        Lists all documents stored under the specified category.

        :param category: Category to list documents for.
        :return: List of document names.
        """
        if category not in self.categories:
            raise ValueError(f"Category '{category}' does not exist.")

        return self.categories[category]

    def save_metadata(self, metadata_file="metadata.json"):
        """
        Saves the category metadata to a JSON file.

        :param metadata_file: Path of the metadata file.
        """
        metadata_path = os.path.join(self.storage_path, metadata_file)
        with open(metadata_path, "w") as file:
            json.dump(self.categories, file, indent=4)
        print(f"Metadata saved to '{metadata_path}'.")

    def load_metadata(self, metadata_file="metadata.json"):
        """
        Loads the category metadata from a JSON file.

        :param metadata_file: Path of the metadata file.
        """
        metadata_path = os.path.join(self.storage_path, metadata_file)
        if os.path.exists(metadata_path):
            with open(metadata_path, "r") as file:
                self.categories = json.load(file)
            print(f"Metadata loaded from '{metadata_path}'.")
        else:
            print("Metadata file not found. Starting with empty categories.")

# Example Usage
if __name__ == "__main__":
    # Generate encryption key and initialize system
    encryption_key = Fernet.generate_key()
    system = SecureDocumentRetrievalSystem(encryption_key)

    # Add documents to the system
    system.add_document("example1.pdf", "Finance")
    system.add_document("example2.pdf", "HR")

    # List documents in a category
    print(system.list_category_documents("Finance"))

    # Retrieve a document
    retrieved_data = system.retrieve_document("example1.pdf", "Finance")
    with open("retrieved_example1.pdf", "wb") as output_file:
        output_file.write(retrieved_data)

    # Save metadata
    system.save_metadata()

    # Load metadata
    system.load_metadata()
```

This code implements a secure document retrieval system with encryption, categorization, and metadata management, adhering to the requirements stated above.
