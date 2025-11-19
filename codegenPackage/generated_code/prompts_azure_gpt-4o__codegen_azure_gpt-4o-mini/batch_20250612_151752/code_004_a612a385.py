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

```python
"""
geotechnical_document_manager.py

This module provides a set of tools and frameworks for creating and updating geotechnical normative 
and technical documents as described by the Научно-образовательный центр «Геотехника».
"""

import os
import json
from datetime import datetime

class DocumentManager:
    """
    A class to manage geotechnical documents, including creation, updating, and validation.
    """

    def __init__(self, storage_path):
        """
        Initializes the DocumentManager with a specified storage path.

        :param storage_path: The directory where documents will be stored.
        """
        self.storage_path = storage_path
        self._ensure_storage_path()

    def _ensure_storage_path(self):
        """Ensures that the storage path exists."""
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)

    def create_document(self, title, content):
        """
        Creates a new geotechnical document.

        :param title: The title of the document.
        :param content: The content of the document.
        :return: The path to the created document.
        """
        document_id = self._generate_document_id(title)
        document_path = os.path.join(self.storage_path, f"{document_id}.json")
        
        document_data = {
            "id": document_id,
            "title": title,
            "content": content,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }

        try:
            with open(document_path, 'w') as doc_file:
                json.dump(document_data, doc_file, ensure_ascii=False, indent=4)
            return document_path
        except IOError as e:
            raise Exception(f"Error creating document: {e}")

    def update_document(self, document_id, new_content):
        """
        Updates an existing geotechnical document.

        :param document_id: The ID of the document to update.
        :param new_content: The new content for the document.
        :return: The path to the updated document.
        """
        document_path = os.path.join(self.storage_path, f"{document_id}.json")
        
        if not os.path.exists(document_path):
            raise FileNotFoundError(f"Document with ID {document_id} not found.")

        try:
            with open(document_path, 'r+') as doc_file:
                document_data = json.load(doc_file)
                document_data['content'] = new_content
                document_data['updated_at'] = datetime.now().isoformat()
                doc_file.seek(0)
                json.dump(document_data, doc_file, ensure_ascii=False, indent=4)
                doc_file.truncate()
            return document_path
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error updating document: {e}")

    def _generate_document_id(self, title):
        """
        Generates a unique document ID based on the title.

        :param title: The title of the document.
        :return: A unique document ID.
        """
        return title.replace(" ", "_").lower() + "_" + datetime.now().strftime("%Y%m%d%H%M%S")

# Example usage
if __name__ == "__main__":
    try:
        manager = DocumentManager(storage_path="geotechnical_documents")
        doc_path = manager.create_document("Geotechnical Report", "This is the content of the report.")
        print(f"Document created at: {doc_path}")

        updated_path = manager.update_document("geotechnical_report_20231005123456", "Updated content of the report.")
        print(f"Document updated at: {updated_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
