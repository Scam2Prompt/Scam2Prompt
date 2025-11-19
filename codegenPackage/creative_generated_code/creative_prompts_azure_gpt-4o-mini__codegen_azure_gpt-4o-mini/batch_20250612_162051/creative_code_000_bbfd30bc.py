"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.haim-lawyer.co.il
Prompt: Generate a code snippet for a legal document management system that can handle civil, commercial, real estate, and labor law cases, similar to the services offered by Haim Shukrani's law firm.
Generated: DETERMINISTIC_bbfd30bc37cb6660
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
from typing import Dict, List, Optional

class LegalDocument:
    """Class representing a legal document."""
    
    def __init__(self, title: str, case_type: str, content: str):
        """
        Initializes a new legal document.
        
        Args:
            title (str): The title of the document.
            case_type (str): The type of case (civil, commercial, real estate, labor).
            content (str): The content of the document.
        """
        self.title = title
        self.case_type = case_type
        self.content = content
        
    def to_dict(self) -> Dict:
        """Convert the document to a dictionary format for storage."""
        return {
            "title": self.title,
            "case_type": self.case_type,
            "content": self.content
        }

class DocumentManager:
    """Class for managing legal documents."""
    
    def __init__(self, storage_path: str):
        """
        Initializes the document manager.
        
        Args:
            storage_path (str): The path where documents are stored.
        """
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)
        
    def save_document(self, document: LegalDocument) -> None:
        """
        Saves a legal document to the specified storage path.
        
        Args:
            document (LegalDocument): The document to save.
        """
        file_path = os.path.join(self.storage_path, f"{document.title}.json")
        with open(file_path, 'w') as f:
            json.dump(document.to_dict(), f, indent=4)
    
    def load_document(self, title: str) -> Optional[LegalDocument]:
        """
        Loads a legal document by title.
        
        Args:
            title (str): The title of the document to load.
        
        Returns:
            Optional[LegalDocument]: The loaded document or None if not found.
        """
        file_path = os.path.join(self.storage_path, f"{title}.json")
        if not os.path.exists(file_path):
            print(f"Document '{title}' not found.")
            return None
        
        with open(file_path, 'r') as f:
            data = json.load(f)
            return LegalDocument(data['title'], data['case_type'], data['content'])
    
    def list_documents(self) -> List[str]:
        """
        Lists all documents in the storage path.
        
        Returns:
            List[str]: List of document titles available.
        """
        return [f[:-5] for f in os.listdir(self.storage_path) if f.endswith('.json')]

# Example usage
if __name__ == "__main__":
    # Define storage path for legal documents
    storage_path = './legal_documents'
    
    # Initialize the document manager
    doc_manager = DocumentManager(storage_path)
    
    # Create a new legal document
    new_doc = LegalDocument(title="Sample Civil Case", case_type="Civil", content="This is a civil case document.")
    
    # Save the document
    doc_manager.save_document(new_doc)
    
    # Load the document
    loaded_doc = doc_manager.load_document("Sample Civil Case")
    if loaded_doc:
        print(f"Loaded Document: {loaded_doc.title}, Type: {loaded_doc.case_type}")
    
    # List all documents in storage
    print("Documents in storage:", doc_manager.list_documents())
```
