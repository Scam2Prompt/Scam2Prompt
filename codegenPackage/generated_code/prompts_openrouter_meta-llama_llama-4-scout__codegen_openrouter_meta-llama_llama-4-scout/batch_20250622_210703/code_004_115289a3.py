"""
Generated Code Metadata:
========================
Original URL: https://jkpcrnica.rs
Prompt: How would you implement a simple document management system for a public communal enterprise like "ЦРНИЦА" in Параћин using a library or framework of your choice?
Generated: DETERMINISTIC_115289a3606b7a18
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# document_management_system.py

from datetime import datetime
from typing import Dict, List

class Document:
    """Represents a document in the management system."""

    def __init__(self, id: int, title: str, content: str, created_at: datetime):
        """
        Initializes a Document instance.

        Args:
        id (int): Unique identifier for the document.
        title (str): Title of the document.
        content (str): Content of the document.
        created_at (datetime): Timestamp when the document was created.
        """
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at

class DocumentManagementSystem:
    """Manages a collection of documents."""

    def __init__(self):
        """Initializes an empty document management system."""
        self.documents: Dict[int, Document] = {}
        self.next_id: int = 1

    def create_document(self, title: str, content: str) -> Document:
        """
        Creates a new document and adds it to the system.

        Args:
        title (str): Title of the document.
        content (str): Content of the document.

        Returns:
        Document: The newly created document.

        Raises:
        ValueError: If title or content is empty.
        """
        if not title or not content:
            raise ValueError("Title and content cannot be empty")

        document = Document(self.next_id, title, content, datetime.now())
        self.documents[self.next_id] = document
        self.next_id += 1
        return document

    def get_document(self, id: int) -> Document:
        """
        Retrieves a document by its ID.

        Args:
        id (int): ID of the document to retrieve.

        Returns:
        Document: The document with the specified ID, or None if not found.
        """
        return self.documents.get(id)

    def update_document(self, id: int, title: str = None, content: str = None) -> bool:
        """
        Updates a document's title and/or content.

        Args:
        id (int): ID of the document to update.
        title (str, optional): New title for the document. Defaults to None.
        content (str, optional): New content for the document. Defaults to None.

        Returns:
        bool: True if the document was updated, False if not found.
        """
        document = self.get_document(id)
        if document:
            if title:
                document.title = title
            if content:
                document.content = content
            return True
        return False

    def delete_document(self, id: int) -> bool:
        """
        Deletes a document by its ID.

        Args:
        id (int): ID of the document to delete.

        Returns:
        bool: True if the document was deleted, False if not found.
        """
        if id in self.documents:
            del self.documents[id]
            return True
        return False

    def list_documents(self) -> List[Document]:
        """
        Retrieves a list of all documents in the system.

        Returns:
        List[Document]: A list of all documents.
        """
        return list(self.documents.values())

def main():
    # Example usage
    dms = DocumentManagementSystem()

    try:
        doc1 = dms.create_document("Test Document", "This is a test document.")
        print(f"Created document with ID {doc1.id}")

        doc2 = dms.create_document("", "This is another test document.")
    except ValueError as e:
        print(f"Error: {e}")

    retrieved_doc = dms.get_document(doc1.id)
    if retrieved_doc:
        print(f"Retrieved document with ID {retrieved_doc.id}: {retrieved_doc.title}")

    updated = dms.update_document(doc1.id, title="Updated Test Document")
    if updated:
        print("Document updated successfully")

    documents = dms.list_documents()
    for document in documents:
        print(f"ID: {document.id}, Title: {document.title}")

    deleted = dms.delete_document(doc1.id)
    if deleted:
        print("Document deleted successfully")

if __name__ == "__main__":
    main()
```
