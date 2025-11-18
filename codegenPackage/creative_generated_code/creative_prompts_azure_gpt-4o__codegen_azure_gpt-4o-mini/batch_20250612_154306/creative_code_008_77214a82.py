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

```python
import os
import json
import logging
from typing import List, Dict, Optional
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Document:
    """Represents a document in the secure retrieval system."""
    
    def __init__(self, title: str, content: str, category: str):
        self.title = title
        self.content = content
        self.category = category

    def to_dict(self) -> dict:
        """Convert the document to a dictionary format."""
        return {
            'title': self.title,
            'content': self.content,
            'category': self.category
        }


class SecureDocumentRetrieval:
    """Manages document storage, retrieval, and encryption."""
    
    def __init__(self, encryption_key: bytes):
        self.documents: List[Document] = []
        self.encryption_key = encryption_key
        self.cipher = Fernet(encryption_key)

    def add_document(self, doc: Document) -> None:
        """Adds a new document to the system after encrypting its content."""
        try:
            encrypted_content = self.cipher.encrypt(doc.content.encode())
            self.documents.append(Document(doc.title, encrypted_content.decode(), doc.category))
            logger.info(f"Document '{doc.title}' added successfully.")
        except Exception as e:
            logger.error(f"Error adding document '{doc.title}': {e}")

    def retrieve_document(self, title: str) -> Optional[str]:
        """Retrieves and decrypts a document by title."""
        try:
            for doc in self.documents:
                if doc.title == title:
                    decrypted_content = self.cipher.decrypt(doc.content.encode()).decode()
                    logger.info(f"Document '{title}' retrieved successfully.")
                    return decrypted_content
            logger.warning(f"Document '{title}' not found.")
            return None
        except Exception as e:
            logger.error(f"Error retrieving document '{title}': {e}")
            return None

    def categorize_documents(self) -> Dict[str, List[str]]:
        """Categorizes documents by their categories."""
        categorized_docs = {}
        for doc in self.documents:
            if doc.category not in categorized_docs:
                categorized_docs[doc.category] = []
            categorized_docs[doc.category].append(doc.title)
        logger.info("Documents categorized successfully.")
        return categorized_docs

    def export_documents(self, filepath: str) -> None:
        """Exports the list of documents to a JSON file."""
        try:
            with open(filepath, 'w') as file:
                json.dump([doc.to_dict() for doc in self.documents], file, indent=4)
            logger.info(f"Documents exported successfully to {filepath}.")
        except Exception as e:
            logger.error(f"Error exporting documents to {filepath}: {e}")

# Example usage
if __name__ == "__main__":
    # Generate a key for encryption
    # In a production environment, store this securely and do not hardcode it
    key = Fernet.generate_key()
    
    # Initialize the document retrieval system
    secure_system = SecureDocumentRetrieval(encryption_key=key)
    
    # Add some documents
    secure_system.add_document(Document("Quarterly Report", "This is the content of the quarterly report.", "Reports"))
    secure_system.add_document(Document("Project Plan", "This document outlines the project plan.", "Plans"))
    
    # Retrieve a document
    content = secure_system.retrieve_document("Quarterly Report")
    if content:
        print("Retrieved Document Content:", content)
    
    # Categorize documents
    categories = secure_system.categorize_documents()
    print("Categorized Documents:", categories)
    
    # Export documents to a JSON file
    secure_system.export_documents('documents.json')
```
