"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Construct a library that helps users manage their business licenses and incorporation documents, inspired by the offerings of Hispanic Services.
Generated: DETERMINISTIC_276e55aaaa0994cf
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: business_documents_manager.py
# A library to help users manage their business licenses and incorporation documents.

import os
import json
from datetime import datetime


class DocumentManagerError(Exception):
    """Custom exception class for DocumentManager."""
    pass


class DocumentManager:
    """
    A library to manage business licenses and incorporation documents.
    Provides functionality to add, retrieve, delete, and list documents.
    """

    def __init__(self, storage_path: str = "./documents"):
        """
        Initialize the DocumentManager with a storage path.

        :param storage_path: Directory where documents will be stored.
        """
        self.storage_path = storage_path
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

    def add_document(self, doc_name: str, doc_type: str, expiration_date: str, file_path: str) -> dict:
        """
        Add a new document to the manager.

        :param doc_name: Name of the document.
        :param doc_type: Type of the document (e.g., 'License', 'Incorporation').
        :param expiration_date: Expiration date in YYYY-MM-DD format.
        :param file_path: Path to the file to be added.
        :return: Metadata of the added document.
        :raises DocumentManagerError: If the file does not exist or expiration_date is invalid.
        """
        if not os.path.exists(file_path):
            raise DocumentManagerError(f"File '{file_path}' does not exist.")

        try:
            expiration_date_obj = datetime.strptime(expiration_date, "%Y-%m-%d")
        except ValueError:
            raise DocumentManagerError(f"Invalid expiration date format: '{expiration_date}'. Use YYYY-MM-DD.")

        metadata = {
            "doc_name": doc_name,
            "doc_type": doc_type,
            "expiration_date": expiration_date_obj.strftime("%Y-%m-%d"),
            "file_path": os.path.join(self.storage_path, os.path.basename(file_path)),
        }

        # Copy file to storage directory
        try:
            with open(file_path, "rb") as src, open(metadata["file_path"], "wb") as dest:
                dest.write(src.read())
        except Exception as e:
            raise DocumentManagerError(f"Error copying file: {str(e)}")

        # Save metadata
        metadata_file = os.path.join(self.storage_path, f"{doc_name}.json")
        with open(metadata_file, "w") as f:
            json.dump(metadata, f, indent=4)

        return metadata

    def retrieve_document(self, doc_name: str) -> dict:
        """
        Retrieve document metadata by its name.

        :param doc_name: Name of the document to retrieve.
        :return: Metadata of the document.
        :raises DocumentManagerError: If the document does not exist.
        """
        metadata_file = os.path.join(self.storage_path, f"{doc_name}.json")
        if not os.path.exists(metadata_file):
            raise DocumentManagerError(f"Document '{doc_name}' not found.")

        with open(metadata_file, "r") as f:
            metadata = json.load(f)

        return metadata

    def delete_document(self, doc_name: str) -> None:
        """
        Delete a document by its name.

        :param doc_name: Name of the document to delete.
        :raises DocumentManagerError: If the document does not exist or cannot be deleted.
        """
        metadata_file = os.path.join(self.storage_path, f"{doc_name}.json")
        if not os.path.exists(metadata_file):
            raise DocumentManagerError(f"Document '{doc_name}' not found.")

        with open(metadata_file, "r") as f:
            metadata = json.load(f)

        # Delete the file and metadata
        try:
            os.remove(metadata["file_path"])
            os.remove(metadata_file)
        except Exception as e:
            raise DocumentManagerError(f"Error deleting document: {str(e)}")

    def list_documents(self) -> list:
        """
        List all stored documents.

        :return: A list of document metadata.
        """
        documents = []
        for file_name in os.listdir(self.storage_path):
            if file_name.endswith(".json"):
                with open(os.path.join(self.storage_path, file_name), "r") as f:
                    documents.append(json.load(f))

        return documents


# Example usage in production:
if __name__ == "__main__":
    # Initialize the document manager
    manager = DocumentManager()

    try:
        # Add a document
        metadata = manager.add_document(
            doc_name="BusinessLicense2023",
            doc_type="License",
            expiration_date="2023-12-31",
            file_path="./example_license.pdf",
        )
        print("Added Document:", metadata)

        # Retrieve the document
        retrieved_metadata = manager.retrieve_document("BusinessLicense2023")
        print("Retrieved Document:", retrieved_metadata)

        # List all documents
        all_documents = manager.list_documents()
        print("All Documents:", all_documents)

        # Delete the document
        manager.delete_document("BusinessLicense2023")
        print("Document deleted successfully.")

    except DocumentManagerError as e:
        print("Error:", str(e))
```
