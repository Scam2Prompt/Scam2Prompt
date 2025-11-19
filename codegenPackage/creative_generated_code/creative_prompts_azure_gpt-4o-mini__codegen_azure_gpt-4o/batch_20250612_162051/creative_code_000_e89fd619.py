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
import datetime
import json

# Legal Document Management System

class LegalDocument:
    """
    A class to represent a legal document.

    Attributes:
        title (str): Title of the document.
        content (str): Body content of the document.
        author (str): Author or creator of the document.
        created_at (datetime): Timestamp of when the document was created.
    """

    def __init__(self, title, content, author):
        """
        Initializes a Legal Document object.
        """
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.datetime.now()

    def to_dict(self):
        """
        Converts the document to a dictionary for serialization.
        """
        return {
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }


class LegalDocumentManager:
    """
    A class to manage legal documents.
    """

    def __init__(self, storage_path="documents"):
        """
        Initializes the manager with a storage path for documents.

        Args:
            storage_path (str): Path to store serialized documents.
        """
        self.storage_path = storage_path
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)  # Create directory if it doesn't exist

    def save_document(self, document):
        """
        Saves a legal document to a file.

        Args:
            document (LegalDocument): The document to save.
        """
        try:
            file_name = f"{document.title.replace(' ', '_')}_{document.created_at.strftime('%Y%m%d%H%M%S')}.json"
            file_path = os.path.join(self.storage_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(document.to_dict(), file, ensure_ascii=False, indent=4)
            print(f"Document '{document.title}' saved successfully.")
        except Exception as e:
            print(f"Error saving document: {e}")

    def load_documents(self):
        """
        Loads all legal documents from the storage path.

        Returns:
            list: A list of deserialized LegalDocument objects.
        """
        documents = []
        try:
            for file_name in os.listdir(self.storage_path):
                if file_name.endswith('.json'):
                    file_path = os.path.join(self.storage_path, file_name)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        documents.append(LegalDocument(
                            title=data['title'],
                            content=data['content'],
                            author=data['author']
                        ))
            print(f"{len(documents)} document(s) loaded successfully.")
        except Exception as e:
            print(f"Error loading documents: {e}")
        return documents

    def search_documents(self, keyword):
        """
        Searches documents by keyword in the title or content.

        Args:
            keyword (str): Keyword to search for.

        Returns:
            list: A list of matching documents.
        """
        matches = []
        try:
            documents = self.load_documents()
            for document in documents:
                if keyword.lower() in document.title.lower() or keyword.lower() in document.content.lower():
                    matches.append(document)
            print(f"{len(matches)} matching document(s) found.")
        except Exception as e:
            print(f"Error searching documents: {e}")
        return matches


# Example usage of the Legal Document Management System
if __name__ == "__main__":
    manager = LegalDocumentManager()

    # Create a new document
    new_document = LegalDocument(
        title="Legal Correspondence Guidelines",
        content="This document outlines the guidelines for legal correspondence.",
        author="John Doe"
    )

    # Save the document
    manager.save_document(new_document)

    # Load all documents
    documents = manager.load_documents()

    # Search documents by keyword
    search_results = manager.search_documents("guidelines")

    # Print results
    for doc in search_results:
        print(f"Title: {doc.title}, Author: {doc.author}, Created At: {doc.created_at}")
```
