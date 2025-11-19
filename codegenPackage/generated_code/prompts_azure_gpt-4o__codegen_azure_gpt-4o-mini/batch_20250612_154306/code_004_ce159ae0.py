"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: Write code to create a consulting module for document organization and archiving, leveraging methodologies similar to those used by EasyDoc Gestão.
Generated: DETERMINISTIC_ce159ae0d0e25fc2
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Document:
    """Class representing a document with metadata."""
    
    def __init__(self, title: str, content: str, tags: List[str] = None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def update_content(self, new_content: str):
        """Update the content of the document."""
        self.content = new_content
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the document to a dictionary for storage."""
        return {
            'title': self.title,
            'content': self.content,
            'tags': self.tags,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class DocumentManager:
    """Class to manage document organization and archiving."""
    
    def __init__(self, storage_path: str):
        self.storage_path = storage_path
        self.documents: List[Document] = []
        self.load_documents()

    def load_documents(self):
        """Load documents from the storage path."""
        if not os.path.exists(self.storage_path):
            logging.warning("Storage path does not exist. Creating a new one.")
            os.makedirs(self.storage_path)

        for filename in os.listdir(self.storage_path):
            if filename.endswith('.json'):
                try:
                    with open(os.path.join(self.storage_path, filename), 'r') as file:
                        doc_data = json.load(file)
                        document = Document(**doc_data)
                        self.documents.append(document)
                        logging.info(f"Loaded document: {document.title}")
                except Exception as e:
                    logging.error(f"Error loading document {filename}: {e}")

    def save_document(self, document: Document):
        """Save a document to the storage path."""
        try:
            file_path = os.path.join(self.storage_path, f"{document.title}.json")
            with open(file_path, 'w') as file:
                json.dump(document.to_dict(), file, indent=4)
            logging.info(f"Document saved: {document.title}")
        except Exception as e:
            logging.error(f"Error saving document {document.title}: {e}")

    def add_document(self, title: str, content: str, tags: List[str] = None):
        """Add a new document to the manager."""
        new_doc = Document(title, content, tags)
        self.documents.append(new_doc)
        self.save_document(new_doc)

    def find_documents_by_tag(self, tag: str) -> List[Document]:
        """Find documents by a specific tag."""
        return [doc for doc in self.documents if tag in doc.tags]

    def archive_documents(self):
        """Archive all documents by moving them to an archive folder."""
        archive_path = os.path.join(self.storage_path, 'archive')
        if not os.path.exists(archive_path):
            os.makedirs(archive_path)

        for document in self.documents:
            try:
                original_path = os.path.join(self.storage_path, f"{document.title}.json")
                archived_path = os.path.join(archive_path, f"{document.title}.json")
                os.rename(original_path, archived_path)
                logging.info(f"Document archived: {document.title}")
            except Exception as e:
                logging.error(f"Error archiving document {document.title}: {e}")

# Example usage
if __name__ == "__main__":
    manager = DocumentManager(storage_path='documents')
    manager.add_document(title='Project Plan', content='This is the project plan content.', tags=['project', 'planning'])
    manager.add_document(title='Meeting Notes', content='Notes from the last meeting.', tags=['meeting', 'notes'])
    
    # Find documents by tag
    project_docs = manager.find_documents_by_tag('project')
    logging.info(f"Documents with tag 'project': {[doc.title for doc in project_docs]}")

    # Archive documents
    manager.archive_documents()
```
