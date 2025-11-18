"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Write Python code to integrate a document management system for organizing, digitalizing, and securely storing files, referencing solutions similar to those provided by EasyDoc Gestão.
Generated: DETERMINISTIC_cba3854421668a18
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
import shutil
import json
from typing import List, Dict, Any

class DocumentManager:
    """
    A class to manage documents, providing functionality for organizing, digitalizing,
    and securely storing files in a structured manner.
    """

    def __init__(self, storage_path: str):
        """
        Initializes the DocumentManager with a specified storage path.
        
        Args:
            storage_path (str): The path where the documents will be stored.
        """
        self.storage_path = storage_path
        self.ensure_storage_directory()

    def ensure_storage_directory(self):
        """Ensures that the storage directory exists."""
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

    def save_document(self, file_path: str, document_id: str):
        """
        Saves a document to the designated storage path.

        Args:
            file_path (str): The path of the document to be saved.
            document_id (str): A unique identifier for the document.
        
        Raises:
            ValueError: If the document ID already exists.
            FileNotFoundError: If the provided file path does not exist.
        """
        if self.document_exists(document_id):
            raise ValueError(f"Document with ID '{document_id}' already exists.")
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        destination_path = os.path.join(self.storage_path, document_id)
        shutil.copy(file_path, destination_path)

    def document_exists(self, document_id: str) -> bool:
        """
        Checks if a document already exists in the storage.

        Args:
            document_id (str): The unique identifier for the document.

        Returns:
            bool: True if the document exists, False otherwise.
        """
        return os.path.exists(os.path.join(self.storage_path, document_id))

    def list_documents(self) -> List[str]:
        """Lists all document IDs stored in the system.

        Returns:
            List[str]: A list of document IDs.
        """
        return os.listdir(self.storage_path)

    def delete_document(self, document_id: str):
        """
        Deletes a document based on its ID.

        Args:
            document_id (str): The unique identifier for the document.
        
        Raises:
            FileNotFoundError: If the document does not exist.
        """
        document_path = os.path.join(self.storage_path, document_id)
        if not os.path.exists(document_path):
            raise FileNotFoundError(f"No document found with ID '{document_id}'.")

        os.remove(document_path)

    def export_documents(self, export_path: str):
        """
        Exports all documents to a specified directory.

        Args:
            export_path (str): The directory where documents will be exported.
        
        Raises:
            Exception: If the export path provided is invalid or not writable.
        """
        if not os.path.exists(export_path):
            raise Exception(f"Export path '{export_path}' does not exist.")

        for document_id in self.list_documents():
            doc_source = os.path.join(self.storage_path, document_id)
            doc_destination = os.path.join(export_path, document_id)
            shutil.copy(doc_source, doc_destination)

    def save_metadata(self, metadata: Dict[str, Any], metadata_file: str):
        """
        Saves metadata related to documents in JSON format.

        Args:
            metadata (Dict[str, Any]): A dictionary containing metadata information.
            metadata_file (str): The path to the file where metadata will be saved.
        
        Raises:
            IOError: If there is an issue writing to the metadata file.
        """
        try:
            with open(metadata_file, 'w') as f:
                json.dump(metadata, f, indent=4)
        except IOError as e:
            raise IOError("An error occurred while saving metadata.") from e


# Example usage:
if __name__ == '__main__':
    try:
        doc_manager = DocumentManager(storage_path='documents')
        
        # Save a document
        doc_manager.save_document(file_path='example.txt', document_id='doc_001')

        # List saved documents
        print("Saved documents:", doc_manager.list_documents())

        # Export documents
        doc_manager.export_documents(export_path='exported_documents')

        # Save metadata
        metadata = {
            "doc_001": {
                "title": "Example Document",
                "author": "Author Name",
                "date_created": "2023-10-01"
            }
        }
        doc_manager.save_metadata(metadata=metadata, metadata_file='metadata.json')

        # Delete a document
        doc_manager.delete_document(document_id='doc_001')

    except Exception as e:
        print(f"An error occurred: {e}")
```
