"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Generate a Python script that utilizes EasyDoc's solutions for digital document management and organization in a business context.
Generated: DETERMINISTIC_b9629082d16debf7
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
from pathlib import Path
from typing import List, Dict, Any

class DocumentManager:
    """
    A class to manage digital documents in a business context.
    It provides methods to add, organize, and retrieve documents.
    """

    def __init__(self, storage_path: str):
        """
        Initializes the DocumentManager with a specified storage path.

        :param storage_path: The directory where documents are stored.
        """
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)

    def add_document(self, document_name: str, content: str) -> str:
        """
        Adds a new document to the storage.

        :param document_name: The name of the document.
        :param content: The content of the document.
        :return: The path to the created document.
        """
        document_path = self.storage_path / f"{document_name}.json"

        if document_path.exists():
            raise FileExistsError(f"The document '{document_name}' already exists.")

        try:
            with open(document_path, 'w') as doc_file:
                json.dump({"name": document_name, "content": content}, doc_file)
            return str(document_path)
        except IOError as e:
            raise Exception(f"An error occurred while writing the document: {e}")

    def retrieve_document(self, document_name: str) -> Dict[str, Any]:
        """
        Retrieves a document by its name.

        :param document_name: The name of the document to retrieve.
        :return: The content of the document as a dictionary.
        """
        document_path = self.storage_path / f"{document_name}.json"

        if not document_path.exists():
            raise FileNotFoundError(f"The document '{document_name}' does not exist.")

        try:
            with open(document_path, 'r') as doc_file:
                return json.load(doc_file)
        except IOError as e:
            raise Exception(f"An error occurred while reading the document: {e}")

    def list_documents(self) -> List[str]:
        """
        Lists all documents in the storage directory.

        :return: A list of document names.
        """
        return [file.stem for file in self.storage_path.glob("*.json")]

    def delete_document(self, document_name: str) -> None:
        """
        Deletes a specified document.

        :param document_name: The name of the document to delete.
        """
        document_path = self.storage_path / f"{document_name}.json"

        if not document_path.exists():
            raise FileNotFoundError(f"The document '{document_name}' does not exist.")

        try:
            document_path.unlink()
        except IOError as e:
            raise Exception(f"An error occurred while deleting the document: {e}")

if __name__ == "__main__":
    # Example usage of DocumentManager
    try:
        manager = DocumentManager("documents")

        # Add a document
        manager.add_document("report", "This is the content of the report.")

        # Retrieve and print the document
        doc = manager.retrieve_document("report")
        print("Retrieved Document:", doc)

        # List all documents
        print("Documents in storage:", manager.list_documents())

        # Delete the document
        manager.delete_document("report")
        print("Document deleted successfully.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
