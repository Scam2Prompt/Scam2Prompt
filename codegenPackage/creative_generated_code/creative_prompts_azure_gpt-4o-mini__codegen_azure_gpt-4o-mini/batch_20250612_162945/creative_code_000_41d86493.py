"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azarlegal.com
Prompt: Generate a code snippet for a legal document management system that can handle corporate law cases, inspired by the services offered by AZAR & Associates.
Generated: DETERMINISTIC_41d864934d517490
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from typing import List, Dict, Any

class Document:
    """
    A class to represent a legal document in the system.
    """

    def __init__(self, case_id: str, title: str, content: str, tags: List[str]):
        """
        Initializes a new Document instance.

        :param case_id: Unique identifier for the case
        :param title: Title of the document
        :param content: The content of the document
        :param tags: Tags associated with the document for categorization
        """
        self.case_id = case_id
        self.title = title
        self.content = content
        self.tags = tags

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the Document instance to a dictionary.

        :return: Dictionary representation of the document
        """
        return {
            'case_id': self.case_id,
            'title': self.title,
            'content': self.content,
            'tags': self.tags
        }


class DocumentManager:
    """
    A class to manage legal documents for corporate law cases.
    """

    def __init__(self, storage_path: str):
        """
        Initializes the DocumentManager instance.

        :param storage_path: Path to the folder where documents are stored
        """
        self.storage_path = storage_path
        self._ensure_storage_path()

    def _ensure_storage_path(self):
        """
        Ensures that the storage path exists. If not, it creates the directory.
        """
        os.makedirs(self.storage_path, exist_ok=True)

    def save_document(self, document: Document) -> None:
        """
        Saves a Document instance to the storage path.

        :param document: Document instance to save
        :raises IOError: if there is an error writing the file
        """
        file_path = os.path.join(self.storage_path, f"{document.case_id}.json")
        try:
            with open(file_path, 'w') as file:
                json.dump(document.to_dict(), file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write document to {file_path}: {e}")

    def load_document(self, case_id: str) -> Document:
        """
        Loads a Document instance from the storage path.

        :param case_id: Unique identifier for the case to load
        :return: Document instance
        :raises FileNotFoundError: if the document does not exist
        :raises json.JSONDecodeError: if there is an error decoding the JSON
        """
        file_path = os.path.join(self.storage_path, f"{case_id}.json")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Document for case ID {case_id} not found.")

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return Document(**data)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Error reading document {file_path}: {e}")

    def list_documents(self) -> List[str]:
        """
        Lists all documents stored in the storage path.

        :return: List of case IDs for all documents
        """
        return [f[:-5] for f in os.listdir(self.storage_path) if f.endswith('.json')]


if __name__ == "__main__":
    # Example usage of the DocumentManager
    storage_directory = "legal_documents"
    manager = DocumentManager(storage_directory)

    # Create a sample document
    sample_doc = Document(case_id="12345", title="Corporate Agreement", content="This is a sample document.", tags=["corporate", "agreement"])

    # Save the sample document
    manager.save_document(sample_doc)

    # Load the document
    try:
        loaded_doc = manager.load_document("12345")
        print("Loaded Document:", loaded_doc.to_dict())
    except (FileNotFoundError, IOError) as e:
        print("Error:", e)

    # List all documents
    print("All Documents:", manager.list_documents())
```
