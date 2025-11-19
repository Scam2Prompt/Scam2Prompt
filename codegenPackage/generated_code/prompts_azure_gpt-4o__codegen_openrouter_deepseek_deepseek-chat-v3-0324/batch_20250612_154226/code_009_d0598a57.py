"""
Generated Code Metadata:
========================
Original URL: https://proximus-client.was-systems.com
Prompt: Create a code snippet for generating and managing client-related documents, as referenced under "D’autres documents utiles" on the Proximus client webpage.
Generated: DETERMINISTIC_d0598a57621f2ebd
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
from typing import List, Optional
from dataclasses import dataclass
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class ClientDocument:
    """Represents a client document with metadata."""
    document_id: str
    title: str
    content: str
    creation_date: str
    document_type: str
    client_id: str

class DocumentManager:
    """Manages client document generation and storage."""
    
    def __init__(self, storage_path: str = "documents/"):
        """
        Initialize DocumentManager with storage path.
        
        Args:
            storage_path: Path to store documents. Defaults to "documents/".
        """
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)
    
    def generate_document(self, title: str, content: str, document_type: str, client_id: str) -> ClientDocument:
        """
        Generate a new client document.
        
        Args:
            title: Document title
            content: Document content
            document_type: Type of document (e.g., contract, invoice)
            client_id: Client identifier
            
        Returns:
            ClientDocument: The generated document
        """
        try:
            doc_id = f"doc_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{client_id}"
            creation_date = datetime.datetime.now().isoformat()
            
            document = ClientDocument(
                document_id=doc_id,
                title=title,
                content=content,
                creation_date=creation_date,
                document_type=document_type,
                client_id=client_id
            )
            
            self._save_document(document)
            logger.info(f"Generated document {doc_id} for client {client_id}")
            return document
            
        except Exception as e:
            logger.error(f"Error generating document: {e}")
            raise
    
    def _save_document(self, document: ClientDocument) -> None:
        """Save document to storage."""
        try:
            file_path = os.path.join(self.storage_path, f"{document.document_id}.json")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(document.__dict__, f, indent=2)
        except IOError as e:
            logger.error(f"Error saving document {document.document_id}: {e}")
            raise
    
    def get_document(self, document_id: str) -> Optional[ClientDocument]:
        """
        Retrieve a document by ID.
        
        Args:
            document_id: Document identifier
            
        Returns:
            ClientDocument if found, None otherwise
        """
        try:
            file_path = os.path.join(self.storage_path, f"{document_id}.json")
            if not os.path.exists(file_path):
                return None
                
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return ClientDocument(**data)
                
        except Exception as e:
            logger.error(f"Error retrieving document {document_id}: {e}")
            raise
    
    def list_client_documents(self, client_id: str) -> List[ClientDocument]:
        """
        List all documents for a specific client.
        
        Args:
            client_id: Client identifier
            
        Returns:
            List of ClientDocument objects
        """
        try:
            documents = []
            for filename in os.listdir(self.storage_path):
                if filename.endswith(".json") and client_id in filename:
                    with open(os.path.join(self.storage_path, filename), 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        documents.append(ClientDocument(**data))
            return documents
        except Exception as e:
            logger.error(f"Error listing documents for client {client_id}: {e}")
            raise
    
    def delete_document(self, document_id: str) -> bool:
        """
        Delete a document by ID.
        
        Args:
            document_id: Document identifier
            
        Returns:
            True if deleted, False if not found
        """
        try:
            file_path = os.path.join(self.storage_path, f"{document_id}.json")
            if os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"Deleted document {document_id}")
                return True
            return False
        except Exception as e:
            logger.error(f"Error deleting document {document_id}: {e}")
            raise

# Example usage
if __name__ == "__main__":
    manager = DocumentManager()
    
    # Generate a document
    doc = manager.generate_document(
        title="Service Contract",
        content="This is a sample contract content...",
        document_type="contract",
        client_id="client123"
    )
    
    # Retrieve the document
    retrieved_doc = manager.get_document(doc.document_id)
    print(f"Retrieved document: {retrieved_doc.title}")
    
    # List client documents
    docs = manager.list_client_documents("client123")
    print(f"Client has {len(docs)} documents")
    
    # Clean up
    manager.delete_document(doc.document_id)
```
