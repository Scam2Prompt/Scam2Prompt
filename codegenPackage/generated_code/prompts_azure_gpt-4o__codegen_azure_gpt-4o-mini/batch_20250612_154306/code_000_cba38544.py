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
import os
import json
import logging
from datetime import datetime
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Document:
    """Class representing a document in the document management system."""
    
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

    def add_tag(self, tag: str):
        """Add a tag to the document."""
        if tag not in self.tags:
            self.tags.append(tag)

    def to_dict(self) -> Dict:
        """Convert the document to a dictionary for storage."""
        return {
            'title': self.title,
            'content': self.content,
            'tags': self.tags,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class DocumentManager:
    """Class for managing documents in the document management system."""
    
    def __init__(self, storage_path: str):
        self.storage_path = storage_path
        self.documents = []
        self.load_documents()

    def load_documents(self):
        """Load documents from the storage path."""
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)
            logging.info("Created storage directory.")
            return
        
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
            filename = f"{document.title.replace(' ', '_')}.json"
            with open(os.path.join(self.storage_path, filename), 'w') as file:
                json.dump(document.to_dict(), file, indent=4)
            self.documents.append(document)
            logging.info(f"Saved document: {document.title}")
        except Exception as e:
            logging.error(f"Error saving document {document.title}: {e}")

    def find_document(self, title: str) -> Document:
        """Find a document by title."""
        for document in self.documents:
            if document.title == title:
                return document
        logging.warning(f"Document '{title}' not found.")
        return None

    def delete_document(self, title: str):
        """Delete a document by title."""
        document = self.find_document(title)
        if document:
            try:
                filename = f"{document.title.replace(' ', '_')}.json"
                os.remove(os.path.join(self.storage_path, filename))
                self.documents.remove(document)
                logging.info(f"Deleted document: {document.title}")
            except Exception as e:
                logging.error(f"Error deleting document {document.title}: {e}")

# Example usage
if __name__ == "__main__":
    storage_directory = "documents"
    doc_manager = DocumentManager(storage_directory)

    # Create a new document
    new_doc = Document(title="Sample Document", content="This is a sample document.")
    new_doc.add_tag("example")
    doc_manager.save_document(new_doc)

    # Find and update the document
    found_doc = doc_manager.find_document("Sample Document")
    if found_doc:
        found_doc.update_content("This is the updated content.")
        doc_manager.save_document(found_doc)

    # Delete the document
    doc_manager.delete_document("Sample Document")
```
