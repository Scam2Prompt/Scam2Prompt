"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lexuscertifications.com
Prompt: What are the key steps to achieve ISO 13485 certification for medical devices, and how can I automate the documentation process?
Generated: DETERMINISTIC_f91036729f0cab07
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
import json
from datetime import datetime

class ISO13485Documentation:
    """
    A class to automate the documentation process for ISO 13485 certification.
    """

    def __init__(self, base_directory):
        """
        Initializes the documentation manager.

        Args:
            base_directory (str): The base directory where documents will be stored.
        """
        self.base_directory = base_directory
        os.makedirs(self.base_directory, exist_ok=True)

    def create_document(self, document_name, content):
        """
        Creates a document with the given content.

        Args:
            document_name (str): The name of the document to create.
            content (dict): The content to write to the document in JSON format.
        """
        document_path = os.path.join(self.base_directory, f"{document_name}.json")
        try:
            with open(document_path, 'w') as json_file:
                json.dump(content, json_file, indent=4)
            print(f"Document '{document_name}' created successfully.")
        except IOError as e:
            print(f"Error creating document '{document_name}': {e}")

    def list_documents(self):
        """Lists all documents in the base directory."""
        try:
            documents = os.listdir(self.base_directory)
            print("Documents in directory:")
            for doc in documents:
                print(f"- {doc}")
        except OSError as e:
            print(f"Error listing documents: {e}")

    def generate_key_steps(self):
        """
        Generates key steps for achieving ISO 13485 certification.
        
        Returns:
            dict: A dictionary containing key steps and their descriptions.
        """
        return {
            "1": "Define the scope of the Quality Management System (QMS).",
            "2": "Conduct a gap analysis against ISO 13485 requirements.",
            "3": "Develop and implement a QMS plan.",
            "4": "Document procedures and ensure compliance.",
            "5": "Train employees on QMS processes.",
            "6": "Conduct internal audits to assess compliance.",
            "7": "Address any non-conformities identified.",
            "8": "Apply for certification from an accredited body."
        }

    def automate_documentation(self):
        """
        Automates the documentation process by generating key steps and creating a document.
        """
        key_steps = self.generate_key_steps()
        timestamp = datetime.now().isoformat()
        document_content = {
            "timestamp": timestamp,
            "ISO13485_key_steps": key_steps
        }
        self.create_document("ISO13485_Key_Steps", document_content)

if __name__ == "__main__":
    # Example usage
    iso_docs = ISO13485Documentation(base_directory="ISO13485_Documents")
    iso_docs.automate_documentation()
    iso_docs.list_documents()
```
