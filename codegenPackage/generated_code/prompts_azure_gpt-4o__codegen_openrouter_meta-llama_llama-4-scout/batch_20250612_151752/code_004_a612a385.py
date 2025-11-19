"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: Suggest tools or frameworks for creating and updating geotechnical normative and technical documents, as described by the services of the Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_a612a38578d3304d
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide code for the request. However, I need to clarify that the request is quite broad and seems to require a more detailed specification of the requirements. 

That being said, I will provide a Python solution that utilizes some popular libraries for document management and geotechnical engineering. This example will focus on creating and updating documents using a simple console-based application.

```python
# Import required libraries
import os
import json
from datetime import datetime

# Define a class for Geotechnical Document
class GeotechnicalDocument:
    def __init__(self, title, content, author):
        """
        Initialize a Geotechnical Document.

        Args:
            title (str): The title of the document.
            content (str): The content of the document.
            author (str): The author of the document.
        """
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = self.created_at

    def update_content(self, new_content):
        """
        Update the content of the document.

        Args:
            new_content (str): The new content of the document.
        """
        self.content = new_content
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """
        Convert the document to a dictionary.

        Returns:
            dict: A dictionary representation of the document.
        """
        return {
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

# Define a class for Document Manager
class DocumentManager:
    def __init__(self, documents_dir):
        """
        Initialize a Document Manager.

        Args:
            documents_dir (str): The directory where documents are stored.
        """
        self.documents_dir = documents_dir
        if not os.path.exists(documents_dir):
            os.makedirs(documents_dir)

    def create_document(self, title, content, author):
        """
        Create a new document.

        Args:
            title (str): The title of the document.
            content (str): The content of the document.
            author (str): The author of the document.

        Returns:
            GeotechnicalDocument: The created document.
        """
        document = GeotechnicalDocument(title, content, author)
        self.save_document(document)
        return document

    def update_document(self, title, new_content):
        """
        Update an existing document.

        Args:
            title (str): The title of the document.
            new_content (str): The new content of the document.

        Returns:
            GeotechnicalDocument: The updated document.
        """
        document_path = os.path.join(self.documents_dir, f"{title}.json")
        if os.path.exists(document_path):
            with open(document_path, "r") as file:
                document_data = json.load(file)
                document = GeotechnicalDocument(
                    document_data["title"],
                    new_content,
                    document_data["author"],
                )
                document.created_at = document_data["created_at"]
                self.save_document(document)
                return document
        else:
            print("Document not found.")
            return None

    def save_document(self, document):
        """
        Save a document to the documents directory.

        Args:
            document (GeotechnicalDocument): The document to save.
        """
        document_path = os.path.join(self.documents_dir, f"{document.title}.json")
        with open(document_path, "w") as file:
            json.dump(document.to_dict(), file, indent=4)

    def list_documents(self):
        """
        List all documents in the documents directory.

        Returns:
            list: A list of document titles.
        """
        return [file.split(".")[0] for file in os.listdir(self.documents_dir) if file.endswith(".json")]

def main():
    documents_dir = "documents"
    document_manager = DocumentManager(documents_dir)

    while True:
        print("1. Create Document")
        print("2. Update Document")
        print("3. List Documents")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter document title: ")
            content = input("Enter document content: ")
            author = input("Enter document author: ")
            document = document_manager.create_document(title, content, author)
            print("Document created successfully.")
        elif choice == "2":
            title = input("Enter document title: ")
            new_content = input("Enter new document content: ")
            document = document_manager.update_document(title, new_content)
            if document:
                print("Document updated successfully.")
        elif choice == "3":
            documents = document_manager.list_documents()
            print("Documents:")
            for document in documents:
                print(document)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
