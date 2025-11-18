"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundation.ru
Prompt: Suggest tools or frameworks for creating and updating geotechnical normative and technical documents, as described by the services of the Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_a612a38578d3304d
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# geotechnical_document_manager.py

"""
This module provides functionalities to manage geotechnical normative and technical documents.
It includes a DocumentManager class for creating, updating, and retrieving document information.
"""

import os
import json
from typing import List, Dict, Any

class DocumentManager:
    """
    A class to manage geotechnical documents.
    It handles creation, updating, and listing of documents in a specified directory.
    """

    def __init__(self, storage_dir: str):
        """
        Initializes the DocumentManager with a directory to store documents.

        :param storage_dir: The directory where documents will be stored.
        """
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def _get_document_path(self, doc_name: str) -> str:
        """
        Returns the full file path for a document.

        :param doc_name: The name of the document.
        :return: Full path to the document file.
        """
        return os.path.join(self.storage_dir, f"{doc_name}.json")

    def create_document(self, doc_name: str, content: Dict[str, Any]) -> None:
        """
        Creates a new document with the given name and content.

        :param doc_name: The name of the document to create.
        :param content: A dictionary containing the document's content.
        :raises FileExistsError: If a document with the same name already exists.
        """
        doc_path = self._get_document_path(doc_name)
        if os.path.exists(doc_path):
            raise FileExistsError(f"Document '{doc_name}' already exists.")
        
        with open(doc_path, 'w') as doc_file:
            json.dump(content, doc_file)
        print(f"Document '{doc_name}' created successfully.")

    def update_document(self, doc_name: str, new_content: Dict[str, Any]) -> None:
        """
        Updates an existing document with new content.

        :param doc_name: The name of the document to update.
        :param new_content: A dictionary with the new content for the document.
        :raises FileNotFoundError: If the document does not exist.
        """
        doc_path = self._get_document_path(doc_name)
        if not os.path.exists(doc_path):
            raise FileNotFoundError(f"Document '{doc_name}' not found.")
        
        with open(doc_path, 'r+') as doc_file:
            content = json.load(doc_file)
            content.update(new_content)
            doc_file.seek(0)  # Move to the beginning of the file
            json.dump(content, doc_file)
            doc_file.truncate()  # Remove any leftover data

        print(f"Document '{doc_name}' updated successfully.")

    def list_documents(self) -> List[str]:
        """
        Lists all documents in the storage directory.

        :return: A list of document names (without extension).
        """
        return [f[:-5] for f in os.listdir(self.storage_dir) if f.endswith('.json')]

# Example usage
if __name__ == "__main__":
    try:
        manager = DocumentManager(storage_dir="geotechnical_documents")
        manager.create_document("geotechnical_standards", {"version": "1.0", "content": "Geotechnical standards content."})
        manager.update_document("geotechnical_standards", {"last_updated": "2023-10-01"})
        print("Documents in storage:", manager.list_documents())
    except Exception as e:
        print(f"An error occurred: {e}")
```
