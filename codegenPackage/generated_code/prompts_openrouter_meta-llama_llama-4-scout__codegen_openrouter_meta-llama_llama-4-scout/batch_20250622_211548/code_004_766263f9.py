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
# document_management_system.py

import os
import datetime
import json

class Document:
    """Represents a document in the system."""

    def __init__(self, title, content, author):
        """
        Initializes a Document object.

        Args:
            title (str): The title of the document.
            content (str): The content of the document.
            author (str): The author of the document.
        """
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = self.created_at

    def update(self, title=None, content=None, author=None):
        """
        Updates the document.

        Args:
            title (str, optional): The new title. Defaults to None.
            content (str, optional): The new content. Defaults to None.
            author (str, optional): The new author. Defaults to None.
        """
        if title:
            self.title = title
        if content:
            self.content = content
        if author:
            self.author = author
        self.updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Returns a dictionary representation of the document."""
        return {
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class DocumentManagementSystem:
    """Manages a collection of documents."""

    def __init__(self, storage_dir):
        """
        Initializes a DocumentManagementSystem object.

        Args:
            storage_dir (str): The directory to store documents.
        """
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def create_document(self, title, content, author):
        """
        Creates a new document.

        Args:
            title (str): The title of the document.
            content (str): The content of the document.
            author (str): The author of the document.

        Returns:
            Document: The created document.
        """
        document = Document(title, content, author)
        self.save_document(document)
        return document

    def get_document(self, title):
        """
        Retrieves a document by title.

        Args:
            title (str): The title of the document.

        Returns:
            Document: The retrieved document, or None if not found.
        """
        file_path = os.path.join(self.storage_dir, f"{title}.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
                document = Document(data["title"], data["content"], data["author"])
                document.created_at = data["created_at"]
                document.updated_at = data["updated_at"]
                return document
        return None

    def update_document(self, title, title_new=None, content=None, author=None):
        """
        Updates a document.

        Args:
            title (str): The title of the document to update.
            title_new (str, optional): The new title. Defaults to None.
            content (str, optional): The new content. Defaults to None.
            author (str, optional): The new author. Defaults to None.

        Returns:
            bool: True if the document was updated, False otherwise.
        """
        document = self.get_document(title)
        if document:
            document.update(title_new, content, author)
            self.save_document(document)
            return True
        return False

    def delete_document(self, title):
        """
        Deletes a document.

        Args:
            title (str): The title of the document to delete.

        Returns:
            bool: True if the document was deleted, False otherwise.
        """
        file_path = os.path.join(self.storage_dir, f"{title}.json")
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False

    def save_document(self, document):
        """
        Saves a document to storage.

        Args:
            document (Document): The document to save.
        """
        file_path = os.path.join(self.storage_dir, f"{document.title}.json")
        with open(file_path, "w") as file:
            json.dump(document.to_dict(), file, indent=4)


def main():
    storage_dir = "documents"
    dms = DocumentManagementSystem(storage_dir)

    while True:
        print("1. Create document")
        print("2. Get document")
        print("3. Update document")
        print("4. Delete document")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter title: ")
            content = input("Enter content: ")
            author = input("Enter author: ")
            document = dms.create_document(title, content, author)
            print(f"Document '{document.title}' created.")
        elif choice == "2":
            title = input("Enter title: ")
            document = dms.get_document(title)
            if document:
                print(f"Title: {document.title}")
                print(f"Content: {document.content}")
                print(f"Author: {document.author}")
                print(f"Created at: {document.created_at}")
                print(f"Updated at: {document.updated_at}")
            else:
                print("Document not found.")
        elif choice == "3":
            title = input("Enter title: ")
            title_new = input("Enter new title (optional): ")
            content = input("Enter new content (optional): ")
            author = input("Enter new author (optional): ")
            if dms.update_document(title, title_new or None, content or None, author or None):
                print("Document updated.")
            else:
                print("Document not found.")
        elif choice == "4":
            title = input("Enter title: ")
            if dms.delete_document(title):
                print("Document deleted.")
            else:
                print("Document not found.")
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
