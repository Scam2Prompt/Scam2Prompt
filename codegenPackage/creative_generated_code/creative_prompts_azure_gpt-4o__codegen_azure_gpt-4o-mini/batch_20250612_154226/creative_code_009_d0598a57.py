"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: Create a code snippet for generating and managing client-related documents, as referenced under "D’autres documents utiles" on the Proximus client webpage.
Generated: DETERMINISTIC_d0598a57621f2ebd
Batch ID: 20250612_154226
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
from datetime import datetime

class ClientDocumentManager:
    """
    A class to manage client-related documents.
    This includes generating and storing documents in a structured manner.
    """

    def __init__(self, client_id, storage_directory):
        """
        Initialize the ClientDocumentManager.

        :param client_id: Unique identifier for the client.
        :param storage_directory: Directory to store client documents.
        """
        self.client_id = client_id
        self.storage_directory = storage_directory
        self._ensure_storage_directory()

    def _ensure_storage_directory(self):
        """Ensure the storage directory exists."""
        try:
            os.makedirs(self.storage_directory, exist_ok=True)
        except Exception as e:
            raise RuntimeError(f"Failed to create storage directory: {e}")

    def generate_document(self, document_type, content):
        """
        Generate a client document and save it to the storage directory.

        :param document_type: Type of the document (e.g., 'contract', 'invoice').
        :param content: Content of the document.
        :return: The path of the generated document.
        """
        try:
            document_name = f"{self.client_id}_{document_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            document_path = os.path.join(self.storage_directory, document_name)

            with open(document_path, 'w') as doc_file:
                json.dump(content, doc_file)

            return document_path
        except Exception as e:
            raise RuntimeError(f"Failed to generate document: {e}")

    def list_documents(self):
        """
        List all documents related to the client.

        :return: A list of document file names.
        """
        try:
            return [f for f in os.listdir(self.storage_directory) if f.startswith(self.client_id)]
        except Exception as e:
            raise RuntimeError(f"Failed to list documents: {e}")

    def delete_document(self, document_name):
        """
        Delete a specified document.

        :param document_name: Name of the document to be deleted.
        :return: None
        """
        try:
            document_path = os.path.join(self.storage_directory, document_name)
            if os.path.exists(document_path):
                os.remove(document_path)
            else:
                raise FileNotFoundError(f"The document {document_name} does not exist.")
        except Exception as e:
            raise RuntimeError(f"Failed to delete document: {e}")

# Example usage
if __name__ == "__main__":
    client_id = "client123"
    storage_dir = "./client_documents"
    
    # Initialize the document manager
    doc_manager = ClientDocumentManager(client_id, storage_dir)
    
    # Generate a new document
    try:
        doc_path = doc_manager.generate_document("contract", {"details": "Contract details here."})
        print(f"Document created at: {doc_path}")
    except RuntimeError as e:
        print(e)

    # List all documents
    try:
        documents = doc_manager.list_documents()
        print("Documents:", documents)
    except RuntimeError as e:
        print(e)

    # Delete a document
    try:
        if documents:
            doc_manager.delete_document(documents[0])
            print(f"Deleted document: {documents[0]}")
    except RuntimeError as e:
        print(e)
```
