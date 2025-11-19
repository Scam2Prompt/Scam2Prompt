"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Generate a code snippet for a legal document management system that incorporates features discussed in the "Manual de Correspondência Jurídica" on the CAAG website.
Generated: DETERMINISTIC_e89fd619945c9fb8
Batch ID: 20250612_162051
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
from typing import List, Dict, Any

class LegalDocument:
    """A class to represent a legal document."""
    
    def __init__(self, title: str, content: str, doc_type: str):
        """
        Initializes a legal document.
        
        Args:
            title (str): Title of the document.
            content (str): Content of the document.
            doc_type (str): Type of the document (e.g., contract, brief).
        """
        self.title = title
        self.content = content
        self.doc_type = doc_type
    
    def to_dict(self) -> Dict[str, Any]:
        """Converts the document to a dictionary format."""
        return {
            'title': self.title,
            'content': self.content,
            'type': self.doc_type
        }

class DocumentManager:
    """A class to manage legal documents."""
    
    def __init__(self, storage_path: str):
        """
        Initializes the document manager.
        
        Args:
            storage_path (str): Path to the directory where documents are stored.
        """
        self.storage_path = storage_path
        self.ensure_storage()

    def ensure_storage(self):
        """Ensures the storage directory exists."""
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)
    
    def save_document(self, document: LegalDocument) -> None:
        """
        Saves a legal document to the storage.
        
        Args:
            document (LegalDocument): The document to save.
        """
        try:
            file_path = os.path.join(self.storage_path, f"{document.title}.json")
            with open(file_path, 'w') as file:
                json.dump(document.to_dict(), file)
            print(f"Document '{document.title}' saved successfully.")
        except Exception as e:
            print(f"Error saving document '{document.title}': {e}")
    
    def load_document(self, title: str) -> LegalDocument:
        """
        Loads a legal document from the storage.
        
        Args:
            title (str): The title of the document to load.
        
        Returns:
            LegalDocument: The loaded document.
        
        Raises:
            FileNotFoundError: If the document does not exist.
        """
        try:
            file_path = os.path.join(self.storage_path, f"{title}.json")
            with open(file_path, 'r') as file:
                doc_data = json.load(file)
            return LegalDocument(doc_data['title'], doc_data['content'], doc_data['type'])
        except FileNotFoundError:
            print(f"Document '{title}' not found.")
            raise
        except json.JSONDecodeError:
            print(f"Error decoding the document '{title}'.")
            raise

    def list_documents(self) -> List[str]:
        """Lists all saved documents in the storage."""
        try:
            return [f[:-5] for f in os.listdir(self.storage_path) if f.endswith('.json')]
        except Exception as e:
            print(f"Error listing documents: {e}")
            return []

# Example usage
if __name__ == "__main__":
    storage = DocumentManager('legal_documents')
    doc = LegalDocument("Contract_A", "This is the content of Contract A.", "contract")
    storage.save_document(doc)

    try:
        loaded_doc = storage.load_document("Contract_A")
        print(f"Loaded Document: {loaded_doc.title}, Type: {loaded_doc.doc_type}")
    except FileNotFoundError:
        print("Document could not be loaded.")
    
    print("All documents:", storage.list_documents())
```
