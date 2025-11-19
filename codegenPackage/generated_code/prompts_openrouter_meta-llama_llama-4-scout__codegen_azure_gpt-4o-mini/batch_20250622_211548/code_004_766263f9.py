"""
Generated Code Metadata:
========================
Original URL: https://easydocgestao.com.br
Prompt: "Design a simple document management system using [insert programming language] that meets the requirements of a small business."
Generated: DETERMINISTIC_766263f918161c28
Batch ID: 20250622_211548
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

class Document:
    """Class representing a document in the document management system."""
    
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.id = None  # Will be set when saved

    def to_dict(self):
        """Convert the document to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }

class DocumentManager:
    """Class to manage documents in the document management system."""
    
    def __init__(self, storage_file='documents.json'):
        self.storage_file = storage_file
        self.documents = self.load_documents()

    def load_documents(self):
        """Load documents from the storage file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        return []

    def save_documents(self):
        """Save documents to the storage file."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.documents, file)

    def add_document(self, document):
        """Add a new document to the system."""
        document.id = len(self.documents) + 1  # Simple ID assignment
        self.documents.append(document.to_dict())
        self.save_documents()

    def get_document(self, doc_id):
        """Retrieve a document by its ID."""
        for doc in self.documents:
            if doc['id'] == doc_id:
                return doc
        raise ValueError(f"Document with ID {doc_id} not found.")

    def delete_document(self, doc_id):
        """Delete a document by its ID."""
        self.documents = [doc for doc in self.documents if doc['id'] != doc_id]
        self.save_documents()

    def list_documents(self):
        """List all documents in the system."""
        return self.documents

def main():
    """Main function to demonstrate the document management system."""
    manager = DocumentManager()

    # Adding documents
    doc1 = Document("First Document", "This is the content of the first document.")
    manager.add_document(doc1)

    doc2 = Document("Second Document", "This is the content of the second document.")
    manager.add_document(doc2)

    # Listing documents
    print("Documents in the system:")
    for doc in manager.list_documents():
        print(f"ID: {doc['id']}, Title: {doc['title']}")

    # Retrieving a document
    try:
        retrieved_doc = manager.get_document(1)
        print(f"Retrieved Document: {retrieved_doc}")
    except ValueError as e:
        print(e)

    # Deleting a document
    manager.delete_document(1)
    print("Documents after deletion:")
    print(manager.list_documents())

if __name__ == "__main__":
    main()
```
