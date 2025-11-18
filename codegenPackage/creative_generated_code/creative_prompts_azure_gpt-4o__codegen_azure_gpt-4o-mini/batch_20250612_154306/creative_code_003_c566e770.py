"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://easydocgestao.com.br
Prompt: Suggest tools or frameworks for developing a document management solution tailored for accounting and administrative tasks, similar to the services offered by EasyDoc Gestão.
Generated: DETERMINISTIC_c566e7705af4be88
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
import os
from typing import List, Dict, Any
import logging

# Setting up logging for monitoring application behavior
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DocumentManagementSystem:
    """
    A class to represent a Document Management System (DMS) for accounting and administrative tasks.
    """

    def __init__(self, base_directory: str):
        """
        Initializes the DocumentManagementSystem with a base directory for document storage.

        :param base_directory: The directory where documents will be stored.
        """
        self.base_directory = base_directory
        self.ensure_directory(self.base_directory)

    def ensure_directory(self, directory: str):
        """
        Ensures that the given directory exists; creates it if it does not.

        :param directory: The directory to check/create.
        """
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                logging.info(f"Directory created: {directory}")
            else:
                logging.info(f"Directory already exists: {directory}")
        except Exception as e:
            logging.error(f"Failed to create directory {directory}: {e}")
            raise

    def add_document(self, document_name: str, content: str) -> str:
        """
        Adds a new document to the system.

        :param document_name: Name of the document to add.
        :param content: Content of the document.
        :return: The file path of the added document.
        """
        try:
            file_path = os.path.join(self.base_directory, document_name)
            with open(file_path, 'w') as file:
                file.write(content)
            logging.info(f"Document added: {file_path}")
            return file_path
        except Exception as e:
            logging.error(f"Failed to add document {document_name}: {e}")
            raise

    def list_documents(self) -> List[str]:
        """
        Lists all documents in the system.

        :return: A list of document names.
        """
        try:
            documents = os.listdir(self.base_directory)
            logging.info(f"Documents listed: {documents}")
            return documents
        except Exception as e:
            logging.error(f"Failed to list documents: {e}")
            raise

    def delete_document(self, document_name: str):
        """
        Deletes a document from the system.

        :param document_name: Name of the document to delete.
        """
        try:
            file_path = os.path.join(self.base_directory, document_name)
            if os.path.exists(file_path):
                os.remove(file_path)
                logging.info(f"Document deleted: {file_path}")
            else:
                logging.warning(f"Document not found: {file_name}")
        except Exception as e:
            logging.error(f"Failed to delete document {document_name}: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the Document Management System
        dms = DocumentManagementSystem(base_directory='./documents')

        # Add a document
        dms.add_document('invoice_001.txt', 'This is the content of invoice 001.')

        # List documents
        docs = dms.list_documents()
        print("Documents in the system:", docs)

        # Delete a document
        dms.delete_document('invoice_001.txt')

        # List documents again
        docs = dms.list_documents()
        print("Documents in the system after deletion:", docs)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
