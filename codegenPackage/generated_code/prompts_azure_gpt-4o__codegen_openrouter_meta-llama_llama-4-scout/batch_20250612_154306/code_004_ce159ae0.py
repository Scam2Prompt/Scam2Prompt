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
# consulting_module.py

import os
import datetime
from typing import Dict, List

class Document:
    """Represents a document with its metadata."""

    def __init__(self, title: str, content: str, tags: List[str] = None):
        """
        Initializes a Document object.

        Args:
        title (str): The title of the document.
        content (str): The content of the document.
        tags (List[str], optional): A list of tags associated with the document. Defaults to None.
        """
        self.title = title
        self.content = content
        self.tags = tags if tags is not None else []
        self.created_at = datetime.datetime.now()

    def __str__(self):
        return f"{self.title} - {self.created_at}"

class ConsultingModule:
    """Provides functionality for document organization and archiving."""

    def __init__(self, storage_dir: str):
        """
        Initializes a ConsultingModule object.

        Args:
        storage_dir (str): The directory where documents will be stored.
        """
        self.storage_dir = storage_dir
        self.documents: Dict[str, Document] = {}

        # Create storage directory if it doesn't exist
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def add_document(self, document: Document):
        """
        Adds a document to the consulting module.

        Args:
        document (Document): The document to be added.
        """
        self.documents[document.title] = document
        self.save_document(document)

    def save_document(self, document: Document):
        """
        Saves a document to the storage directory.

        Args:
        document (Document): The document to be saved.
        """
        file_path = os.path.join(self.storage_dir, f"{document.title}.txt")
        with open(file_path, "w") as file:
            file.write(document.content)

    def get_document(self, title: str) -> Document:
        """
        Retrieves a document by its title.

        Args:
        title (str): The title of the document.

        Returns:
        Document: The document with the specified title, or None if not found.
        """
        return self.documents.get(title)

    def list_documents(self) -> List[Document]:
        """
        Lists all documents in the consulting module.

        Returns:
        List[Document]: A list of all documents.
        """
        return list(self.documents.values())

    def search_documents(self, query: str) -> List[Document]:
        """
        Searches for documents by title or tags.

        Args:
        query (str): The search query.

        Returns:
        List[Document]: A list of documents matching the search query.
        """
        results = []
        for document in self.documents.values():
            if query in document.title or query in document.tags:
                results.append(document)
        return results

def main():
    # Example usage
    module = ConsultingModule("documents")

    doc1 = Document("Example Document", "This is an example document.", ["example", "document"])
    doc2 = Document("Another Document", "This is another document.", ["another", "document"])

    module.add_document(doc1)
    module.add_document(doc2)

    print("All documents:")
    for document in module.list_documents():
        print(document)

    print("\nSearch results:")
    results = module.search_documents("example")
    for document in results:
        print(document)

if __name__ == "__main__":
    main()
```
