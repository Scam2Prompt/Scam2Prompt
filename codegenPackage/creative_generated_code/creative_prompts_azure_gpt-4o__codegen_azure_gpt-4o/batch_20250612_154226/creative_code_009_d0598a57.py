"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: Create a code snippet for generating and managing client-related documents, as referenced under "D’autres documents utiles" on the Proximus client webpage.
Generated: DETERMINISTIC_d0598a57621f2ebd
Batch ID: 20250612_154226
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

# Define constants
DOCUMENTS_DIRECTORY = "client_documents"
ALLOWED_DOCUMENT_TYPES = ["pdf", "docx", "txt"]  # Allowed document formats

class DocumentManager:
    """
    A class to handle generation and management of client-related documents.
    """

    def __init__(self, client_id):
        """
        Initializes the DocumentManager with a client ID.
        
        :param client_id: Unique identifier for the client
        """
        self.client_id = client_id
        self.client_dir = os.path.join(DOCUMENTS_DIRECTORY, str(client_id))

        # Ensure the client's document directory exists
        os.makedirs(self.client_dir, exist_ok=True)

    def create_document(self, document_name, document_type, content):
        """
        Creates a new document for the client.

        :param document_name: Name of the document (without extension)
        :param document_type: Type of the document (e.g., pdf, txt, docx)
        :param content: Content to be written into the document
        :return: Full path to the created document
        :raises: ValueError if the document type is not allowed
        """
        if document_type not in ALLOWED_DOCUMENT_TYPES:
            raise ValueError(f"Document type '{document_type}' is not allowed. Allowed types: {ALLOWED_DOCUMENT_TYPES}")

        # Construct the filename and path
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{document_name}_{timestamp}.{document_type}"
        document_path = os.path.join(self.client_dir, filename)

        try:
            # Write content to the file
            with open(document_path, "w", encoding="utf-8") as file:
                file.write(content)
        except Exception as e:
            raise Exception(f"Failed to create document: {e}")

        return document_path

    def list_documents(self):
        """
        Lists all documents for the client.

        :return: A list of filenames available in the client's directory
        """
        try:
            return [f for f in os.listdir(self.client_dir) if os.path.isfile(os.path.join(self.client_dir, f))]
        except Exception as e:
            raise Exception(f"Failed to list documents: {e}")

    def delete_document(self, document_name):
        """
        Deletes a specific document for the client.

        :param document_name: Name of the document to delete
        :raises: FileNotFoundError if the document does not exist
        """
        document_path = os.path.join(self.client_dir, document_name)

        if not os.path.exists(document_path):
            raise FileNotFoundError(f"Document '{document_name}' not found.")

        try:
            os.remove(document_path)
        except Exception as e:
            raise Exception(f"Failed to delete document: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the document manager for a client
        client_id = 12345
        manager = DocumentManager(client_id)

        # Create a new document
        path = manager.create_document("contract", "txt", "This is the contract content.")
        print(f"Document created: {path}")

        # List documents for the client
        documents = manager.list_documents()
        print(f"Documents for client {client_id}: {documents}")

        # Delete a document
        manager.delete_document(os.path.basename(path))
        print("Document deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
