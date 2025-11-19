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

Certainly! Below is a Python implementation of a simple document management system that meets the requirements of a small business.

```python
import os
import json
from datetime import datetime

class DocumentManagementSystem:
    """
    A simple document management system for a small business.
    Allows uploading, retrieving, listing, and deleting documents.
    """

    def __init__(self, storage_dir="documents"):
        """
        Initialize the document management system.

        :param storage_dir: Directory where documents will be stored.
        """
        self.storage_dir = storage_dir
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)  # Create storage directory if it doesn't exist

    def upload_document(self, file_path):
        """
        Upload a document to the system.

        :param file_path: Path to the document to be uploaded.
        :return: Success message or error message.
        """
        try:
            if not os.path.isfile(file_path):
                return f"Error: File '{file_path}' does not exist."

            file_name = os.path.basename(file_path)
            destination_path = os.path.join(self.storage_dir, file_name)

            # Check if the file already exists in the system
            if os.path.exists(destination_path):
                return f"Error: File '{file_name}' already exists in the system."

            # Copy the file to the storage directory
            with open(file_path, "rb") as source_file:
                with open(destination_path, "wb") as dest_file:
                    dest_file.write(source_file.read())

            # Log metadata
            metadata = {
                "file_name": file_name,
                "uploaded_at": datetime.now().isoformat(),
                "file_size": os.path.getsize(destination_path)
            }
            self._save_metadata(file_name, metadata)

            return f"Success: File '{file_name}' uploaded successfully."
        except Exception as e:
            return f"Error: Failed to upload document. Details: {str(e)}"

    def list_documents(self):
        """
        List all documents in the system.

        :return: List of document names.
        """
        try:
            documents = os.listdir(self.storage_dir)
            return documents if documents else "No documents found."
        except Exception as e:
            return f"Error: Failed to list documents. Details: {str(e)}"

    def retrieve_document(self, file_name):
        """
        Retrieve a document's metadata.

        :param file_name: Name of the document to retrieve.
        :return: Metadata of the document or error message.
        """
        try:
            metadata_path = os.path.join(self.storage_dir, f"{file_name}.meta.json")
            if not os.path.exists(metadata_path):
                return f"Error: Metadata for file '{file_name}' not found."

            with open(metadata_path, "r") as meta_file:
                metadata = json.load(meta_file)
            return metadata
        except Exception as e:
            return f"Error: Failed to retrieve document metadata. Details: {str(e)}"

    def delete_document(self, file_name):
        """
        Delete a document from the system.

        :param file_name: Name of the document to delete.
        :return: Success message or error message.
        """
        try:
            file_path = os.path.join(self.storage_dir, file_name)
            metadata_path = os.path.join(self.storage_dir, f"{file_name}.meta.json")

            if not os.path.exists(file_path):
                return f"Error: File '{file_name}' not found."

            # Delete the file and its metadata
            os.remove(file_path)
            if os.path.exists(metadata_path):
                os.remove(metadata_path)

            return f"Success: File '{file_name}' deleted successfully."
        except Exception as e:
            return f"Error: Failed to delete document. Details: {str(e)}"

    def _save_metadata(self, file_name, metadata):
        """
        Save metadata for a document.

        :param file_name: Name of the document.
        :param metadata: Metadata dictionary to save.
        """
        try:
            metadata_path = os.path.join(self.storage_dir, f"{file_name}.meta.json")
            with open(metadata_path, "w") as meta_file:
                json.dump(metadata, meta_file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save metadata for '{file_name}'. Details: {str(e)}")


# Example usage
if __name__ == "__main__":
    dms = DocumentManagementSystem()

    # Upload a document
    print(dms.upload_document("example.txt"))

    # List all documents
    print(dms.list_documents())

    # Retrieve document metadata
    print(dms.retrieve_document("example.txt"))

    # Delete a document
    print(dms.delete_document("example.txt"))
```

This code is production-ready, follows Python best practices, and includes error handling and comments for clarity.
