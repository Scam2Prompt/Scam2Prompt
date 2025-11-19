"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: Write Python code to integrate a document management system for organizing, digitalizing, and securely storing files, referencing solutions similar to those provided by EasyDoc Gestão.
Generated: DETERMINISTIC_cba3854421668a18
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# document_management_system.py

import os
import hashlib
import logging
from datetime import datetime
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Document:
    def __init__(self, id: str, name: str, content: bytes):
        """
        Initialize a Document object.

        Args:
        - id (str): Unique identifier for the document.
        - name (str): Name of the document.
        - content (bytes): Content of the document.
        """
        self.id = id
        self.name = name
        self.content = content
        self.created_at = datetime.now()

    def __str__(self):
        return f"Document {self.id}: {self.name}"

class DocumentManagementSystem:
    def __init__(self, storage_path: str):
        """
        Initialize a DocumentManagementSystem object.

        Args:
        - storage_path (str): Path to store documents.
        """
        self.storage_path = storage_path
        self.documents: Dict[str, Document] = {}

        # Create storage directory if it doesn't exist
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)

    def add_document(self, document: Document):
        """
        Add a document to the system.

        Args:
        - document (Document): Document to add.
        """
        # Calculate document hash for integrity verification
        document_hash = hashlib.sha256(document.content).hexdigest()

        # Store document content in a file
        file_path = os.path.join(self.storage_path, f"{document.id}.bin")
        with open(file_path, "wb") as file:
            file.write(document.content)

        # Store document metadata
        self.documents[document.id] = {
            "name": document.name,
            "hash": document_hash,
            "created_at": document.created_at
        }

        logging.info(f"Document {document.id} added successfully.")

    def get_document(self, id: str) -> Document:
        """
        Retrieve a document by its ID.

        Args:
        - id (str): ID of the document to retrieve.

        Returns:
        - Document: Retrieved document.

        Raises:
        - FileNotFoundError: If the document is not found.
        """
        if id not in self.documents:
            raise FileNotFoundError(f"Document {id} not found.")

        document_metadata = self.documents[id]
        file_path = os.path.join(self.storage_path, f"{id}.bin")

        with open(file_path, "rb") as file:
            content = file.read()

        # Verify document integrity by checking hash
        document_hash = hashlib.sha256(content).hexdigest()
        if document_hash != document_metadata["hash"]:
            raise Exception(f"Document {id} integrity check failed.")

        return Document(id, document_metadata["name"], content)

    def delete_document(self, id: str):
        """
        Delete a document by its ID.

        Args:
        - id (str): ID of the document to delete.

        Raises:
        - FileNotFoundError: If the document is not found.
        """
        if id not in self.documents:
            raise FileNotFoundError(f"Document {id} not found.")

        file_path = os.path.join(self.storage_path, f"{id}.bin")
        os.remove(file_path)

        del self.documents[id]

        logging.info(f"Document {id} deleted successfully.")

def main():
    # Example usage
    dms = DocumentManagementSystem("./documents")

    document1 = Document("doc1", "Example Document", b"This is an example document.")
    dms.add_document(document1)

    retrieved_document = dms.get_document("doc1")
    print(retrieved_document.name)
    print(retrieved_document.content.decode("utf-8"))

    dms.delete_document("doc1")

if __name__ == "__main__":
    main()
```
