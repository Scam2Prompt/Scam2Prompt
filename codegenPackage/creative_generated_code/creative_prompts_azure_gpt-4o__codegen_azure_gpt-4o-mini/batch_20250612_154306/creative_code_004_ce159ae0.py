"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Write code to create a consulting module for document organization and archiving, leveraging methodologies similar to those used by EasyDoc Gestão.
Generated: DETERMINISTIC_ce159ae0d0e25fc2
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
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Document:
    """Class to represent a document for organization and archiving."""

    def __init__(self, title: str, content: str, tags: List[str]):
        """
        Initialize a Document instance.
        
        :param title: Title of the document
        :param content: Content of the document
        :param tags: List of tags associated with the document
        """
        self.title = title
        self.content = content
        self.tags = tags
        self.created_at = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Document to a dictionary."""
        return {
            'title': self.title,
            'content': self.content,
            'tags': self.tags,
            'created_at': self.created_at
        }

class DocumentManager:
    """Class to manage document organization and archiving."""

    def __init__(self, storage_path: str):
        """
        Initialize DocumentManager with a specified storage path.
        
        :param storage_path: Path to the folder where documents will be stored
        """
        self.storage_path = storage_path
        self.documents: List[Document] = []

        # Create storage path if it does not exist
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)
            logging.info(f"Created storage directory at: {storage_path}")

    def add_document(self, document: Document) -> None:
        """
        Add a document to the manager and save it to storage.
        
        :param document: Document instance to be added
        """
        self.documents.append(document)
        self._save_document(document)

    def _save_document(self, document: Document) -> None:
        """Save a document to a JSON file."""
        try:
            file_path = os.path.join(self.storage_path, f"{document.title.replace(' ', '_')}.json")
            with open(file_path, 'w') as file:
                json.dump(document.to_dict(), file)
            logging.info(f"Document '{document.title}' saved successfully.")
        except Exception as e:
            logging.error(f"Error saving document '{document.title}': {e}")

    def list_documents(self) -> List[Dict[str, Any]]:
        """List all saved documents."""
        document_list = []
        for file_name in os.listdir(self.storage_path):
            if file_name.endswith('.json'):
                document_path = os.path.join(self.storage_path, file_name)
                with open(document_path, 'r') as file:
                    document_list.append(json.load(file))
        return document_list

def main():
    """Main function to demonstrate the DocumentManager functionality."""
    storage_dir = './documents'
    manager = DocumentManager(storage_dir)

    # Example usage
    doc1 = Document(title='Project Plan', content='Details about the project.', tags=['planning', 'project'])
    doc2 = Document(title='Meeting Notes', content='Notes from the last meeting.', tags=['notes', 'meeting'])

    manager.add_document(doc1)
    manager.add_document(doc2)

    # List all documents
    documents = manager.list_documents()
    logging.info("Documents in storage:")
    for doc in documents:
        logging.info(doc)

if __name__ == '__main__':
    main()
```
