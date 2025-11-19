"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: "Provide a list of steps and a corresponding Python code to implement a system for tracking and managing the documentation required for insolvency proceedings in the Czech Republic."
Generated: DETERMINISTIC_fb048b85e03e2bdd
Batch ID: 20250622_205206
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
from datetime import datetime

class DocumentManager:
    """
    A class to manage the documentation required for insolvency proceedings.
    """

    def __init__(self, storage_path):
        """
        Initializes the DocumentManager with a specified storage path.

        :param storage_path: Path to the directory where documents will be stored.
        """
        self.storage_path = storage_path
        self.documents = self.load_documents()

    def load_documents(self):
        """
        Loads existing documents from a JSON file.

        :return: A dictionary of documents if the file exists, otherwise an empty dictionary.
        """
        documents_file = os.path.join(self.storage_path, 'documents.json')
        if os.path.exists(documents_file):
            with open(documents_file, 'r') as file:
                return json.load(file)
        return {}

    def save_documents(self):
        """
        Saves the current documents to a JSON file.
        """
        documents_file = os.path.join(self.storage_path, 'documents.json')
        with open(documents_file, 'w') as file:
            json.dump(self.documents, file, indent=4)

    def add_document(self, doc_name, doc_type, due_date):
        """
        Adds a new document to the tracking system.

        :param doc_name: Name of the document.
        :param doc_type: Type of the document (e.g., 'application', 'report').
        :param due_date: Due date for the document submission.
        """
        if doc_name in self.documents:
            raise ValueError(f"Document '{doc_name}' already exists.")
        
        self.documents[doc_name] = {
            'type': doc_type,
            'due_date': due_date,
            'created_at': datetime.now().isoformat()
        }
        self.save_documents()

    def remove_document(self, doc_name):
        """
        Removes a document from the tracking system.

        :param doc_name: Name of the document to remove.
        """
        if doc_name not in self.documents:
            raise ValueError(f"Document '{doc_name}' does not exist.")
        
        del self.documents[doc_name]
        self.save_documents()

    def list_documents(self):
        """
        Lists all documents currently tracked.

        :return: A list of documents with their details.
        """
        return self.documents

    def get_document(self, doc_name):
        """
        Retrieves details of a specific document.

        :param doc_name: Name of the document to retrieve.
        :return: Document details if found, otherwise raises an error.
        """
        if doc_name not in self.documents:
            raise ValueError(f"Document '{doc_name}' does not exist.")
        
        return self.documents[doc_name]

def main():
    """
    Main function to demonstrate the DocumentManager functionality.
    """
    # Define the storage path for documents
    storage_path = './documents'
    os.makedirs(storage_path, exist_ok=True)

    # Initialize the DocumentManager
    doc_manager = DocumentManager(storage_path)

    # Example usage
    try:
        # Adding documents
        doc_manager.add_document('Insolvency Application', 'application', '2023-12-01')
        doc_manager.add_document('Financial Report', 'report', '2023-11-15')

        # Listing documents
        print("Current Documents:")
        print(doc_manager.list_documents())

        # Retrieving a specific document
        print("Details of 'Insolvency Application':")
        print(doc_manager.get_document('Insolvency Application'))

        # Removing a document
        doc_manager.remove_document('Financial Report')
        print("Documents after removal:")
        print(doc_manager.list_documents())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
