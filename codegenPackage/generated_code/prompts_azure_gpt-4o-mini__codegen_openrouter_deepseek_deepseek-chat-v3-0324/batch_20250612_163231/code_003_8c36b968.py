"""
Generated Code Metadata:
========================
Original URL: https://carvalhocr.com
Prompt: Provide an example of using Carvalhocr's features to organize and retrieve documents programmatically.
Generated: DETERMINISTIC_8c36b9683c289717
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import carvalhocr
from typing import List, Dict, Optional
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentManager:
    """
    A class to manage documents using CarvalhOCR's features for organization and retrieval.
    """

    def __init__(self, storage_path: str):
        """
        Initialize the DocumentManager with a storage path.

        Args:
            storage_path (str): Path to store and retrieve documents.
        """
        self.storage_path = storage_path
        self.client = carvalhocr.Client()
        
        # Ensure storage directory exists
        os.makedirs(storage_path, exist_ok=True)

    def upload_document(self, file_path: str, metadata: Dict[str, str]) -> Optional[str]:
        """
        Upload a document with metadata to the storage.

        Args:
            file_path (str): Path to the document file.
            metadata (Dict[str, str]): Metadata associated with the document.

        Returns:
            Optional[str]: Document ID if successful, None otherwise.
        """
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")

            # Upload document to CarvalhOCR
            with open(file_path, 'rb') as file:
                document_id = self.client.upload(
                    file=file,
                    metadata=metadata
                )
            
            logger.info(f"Document uploaded successfully. ID: {document_id}")
            return document_id
        except Exception as e:
            logger.error(f"Error uploading document: {e}")
            return None

    def retrieve_document(self, document_id: str) -> Optional[Dict]:
        """
        Retrieve a document and its metadata by ID.

        Args:
            document_id (str): ID of the document to retrieve.

        Returns:
            Optional[Dict]: Dictionary containing document content and metadata if found, None otherwise.
        """
        try:
            document = self.client.retrieve(document_id)
            if document:
                logger.info(f"Document retrieved successfully. ID: {document_id}")
                return {
                    'content': document.content,
                    'metadata': document.metadata
                }
            return None
        except Exception as e:
            logger.error(f"Error retrieving document: {e}")
            return None

    def search_documents(self, query: str, limit: int = 10) -> List[Dict]:
        """
        Search documents based on a query.

        Args:
            query (str): Search query.
            limit (int): Maximum number of results to return.

        Returns:
            List[Dict]: List of matching documents with metadata.
        """
        try:
            results = self.client.search(query=query, limit=limit)
            return [{
                'id': doc.id,
                'content': doc.content,
                'metadata': doc.metadata
            } for doc in results]
        except Exception as e:
            logger.error(f"Error searching documents: {e}")
            return []

    def delete_document(self, document_id: str) -> bool:
        """
        Delete a document by ID.

        Args:
            document_id (str): ID of the document to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        try:
            self.client.delete(document_id)
            logger.info(f"Document deleted successfully. ID: {document_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting document: {e}")
            return False

# Example usage
if __name__ == "__main__":
    manager = DocumentManager(storage_path="./documents")

    # Upload a document
    metadata = {
        "title": "Sample Document",
        "author": "John Doe",
        "date": "2023-10-01"
    }
    doc_id = manager.upload_document("sample.txt", metadata)
    
    if doc_id:
        # Retrieve the document
        document = manager.retrieve_document(doc_id)
        if document:
            print(f"Retrieved document: {document['metadata']['title']}")

        # Search for documents
        results = manager.search_documents("Sample")
        print(f"Found {len(results)} matching documents")

        # Delete the document
        if manager.delete_document(doc_id):
            print("Document deleted successfully")
```
